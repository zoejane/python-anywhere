# -*- coding: utf-8 -*-
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app
from bottle import Bottle,route,run,debug,request,template

from datetime import datetime
import sys



@route('/',method='GET')
def diary():
    diaryFile = open('diary.txt')
    diaryContent = diaryFile.read()
    diaryFile.close()
    diaryContent=diaryContent.replace('\n', '<br />')
    output_start ='''
    <head>
  <meta charset="utf-8">
  <title>Diary of Yours</title>
  <!-- Bootstrap core CSS -->
  <link href="http://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">
  <!-- Custom styles for this template -->
  <link href="css/cover.css" rel="stylesheet">
</head>
<body>

    <h3 class="masthead-brand">Diary of Yours</h3>
    <p>Hello, I am your diary.你好
      <br />Do you wanna share something with me?</p>

      <form action="/" method="GET">
<input type="text" size="70" maxlength="100" name="user_name">
<input type="submit" name="save_name" value="保存">
</form>

    <p><b>Share your feeling:</b></p>
<form action="/" method="GET">
<input type="text" size="70" maxlength="100" name="newdiary">
<input type="submit" name="save_diary" value="Save">
</form>

<p>====Diary====</p>'''
    
    output_end='''<br /><br />

  <div class="inner">
    <p><i>life is wonderful</i></p>
  </div>

</body>'''

    user_name='guest'
    if request.GET.get('save_name','').strip():
        user_name=request.GET.get('user_name', '').strip()
        print user_name
    if request.GET.get('save_diary','').strip():

        today=datetime.now()
        newDiary=request.GET.get('newdiary', '').strip()

        diaryFile = open('diary.txt','a')
        print user_name+'now'
        diaryFile.write('\n'+today.strftime("%y/%m/%d")+ '  ['+user_name+'] '+newDiary)
        diaryFile.close()

        diaryFile = open('diary.txt')
        diaryContent = diaryFile.read()
        diaryFile.close()
        diaryContent=diaryContent.replace('\n', '<br />')

        return output_start+diaryContent+output_end
    return output_start+diaryContent+output_end


application = default_app()

run(host='localhost', port=1234, debug=True)
