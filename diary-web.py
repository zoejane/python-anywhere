
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app

# @route('/')
# def hello_world():
#    return 'Hello from Bottle!'

# -*- coding: utf-8 -*-
from bottle import Bottle,route,run,debug,request,template

from datetime import datetime
import sys



@route('/')
@route('/diary')
def greeting():
    diaryFile = open('diary.txt')
    diaryContent = diaryFile.read()
    diaryFile.close()
    diaryContent=diaryContent.replace('\n', '<br />')
    return '''
    <head>
  <meta charset="utf-8">
  <title>Zoe's Diary</title>
  <!-- Bootstrap core CSS -->
  <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Custom styles for this template -->
  <link href="css/cover.css" rel="stylesheet">
</head>
<body>

    <h3 class="masthead-brand">Diary of Yours</h3>
    <p>Hello, I am your diary.
      <br />Do you wanna share something with me?</p>
    <p class="lead">
      <a href="/writing" class="btn btn-lg btn-default">Writing diary</a>
      <a href="/reading" class="btn btn-lg btn-default">Reading diary</a>
    </p>

    <p>Share your feeling:</p>
<form action="/writing" method="GET">
<input type="text" size="70" maxlength="100" name="newdiary">
<input type="submit" name="save" value="Save">
</form>

<p>====Diary====</p>'''+diaryContent+'''<br /><br /><a href='/writing'>Writing Diary<a><br /><a href='/'>Back Home<a>

  <div class="inner">
    <p>life is wonderful</p>
  </div>

</body>'''


@route('/reading')
def reading():
    diaryFile = open('diary.txt')
    diaryContent = diaryFile.read()
    diaryFile.close()
    diaryContent=diaryContent.replace('\n', '<br />')
    output='<p>====Diary====</p>'+diaryContent+"<br /><br /><a href='/writing'>Writing Diary<a><br /><a href='/'>Back Home<a>"
    return output

@route('/writing',method='GET')
def writing():
    if request.GET.get('save','').strip():

        today=datetime.now()
        newDiary=request.GET.get('newdiary', '').strip()

        diaryFile = open('diary.txt','a')
        diaryFile.write('\n'+today.strftime("%y/%m/%d")+ ' '+newDiary)
        diaryFile.close()

        diaryFile = open('diary.txt')
        diaryContent = diaryFile.read()
        diaryFile.close()
        diaryContent=diaryContent.replace('\n', '<br />')

#        return '''
#<p>The new diary was saved.</p>
#<a href='/writing'>Writing Diary<a>
#<a href='/reading'>Reading Diary<a>
#<a href='/'>Back Home<a>
#'''

        return '''
  <head>
  <meta charset="utf-8">
  <title>Zoe's Diary</title>
  <!-- Bootstrap core CSS -->
  <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Custom styles for this template -->
  <link href="css/cover.css" rel="stylesheet">
</head>
<body>

    <h3 class="masthead-brand">Diary of Yours</h3>
    <p>Hello, I am your diary.
      <br />Do you wanna share something with me?</p>
    <p class="lead">
      <a href="/writing" class="btn btn-lg btn-default">Writing diary</a>
      <a href="/reading" class="btn btn-lg btn-default">Reading diary</a>
    </p>

    <p>Share your feeling:</p>
<form action="/writing" method="GET">
<input type="text" size="70" maxlength="100" name="newdiary">
<input type="submit" name="save" value="Save">
</form>

<p>====Diary====</p>'''+diaryContent+'''<br /><br /><a href='/writing'>Writing Diary<a><br /><a href='/'>Back Home<a>

  <div class="inner">
    <p>life is wonderful</p>
  </div>

</body>'''
    else:
        return '''
<p>Share your feeling:</p>
<form action="/writing" method="GET">
<input type="text" size="70" maxlength="100" name="newdiary">
<input type="submit" name="save" value="Save">
</form>
<a href='/'>Back Home<a>
'''

# run(diary,host='localhost', port=1234, debug=True)'''


application = default_app()