# -*- coding: utf-8 -*-
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app
from bottle import Bottle,route,run,debug,request,template

from datetime import datetime
import sys


@route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

@route('/',method='GET')
@route('/<user_name>')
def diary(user_name='guest'):
#    print user_name
    diaryFile = open('diary.txt')
    diaryContent = diaryFile.read()
    diaryFile.close()
    diaryContent=diaryContent.replace('\n', '<br />')
    lujing="'/'+username"
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

    <p><b>Share your feeling:</b></p>
<form action="'''
    output_middle='''" method="GET">
<input type="text" size="70" maxlength="100" name="newdiary">
<input type="submit" name="save_diary" value="Save">
</form>

<p>====Diary====</p>'''
    
    output_end='''<br /><br />

  <div class="inner">
    <p><i>life is wonderful</i></p>
  </div>

</body>'''
    print user_name
    if request.GET.get('save_diary','').strip():

        today=datetime.now()
        newDiary=request.GET.get('newdiary', '').strip()

        diaryFile = open('diary.txt')
        diaryContent = diaryFile.read()
        diaryFile.close()

#        diaryFile = open('diary.txt','a')
#        diaryFile.write('\n'+today.strftime("%y/%m/%d")+ '  ['+user_name+'] '+newDiary)
#        diaryFile.close()

        with open('diary.txt', 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            newDiaryLine=today.strftime("%y/%m/%d")+ '  ['+user_name+'] '+newDiary
            f.write(newDiaryLine.rstrip('\r\n') + '\n' + content)

        diaryFile = open('diary.txt')
        diaryContent = diaryFile.read()
        diaryFile.close()
        diaryContent=diaryContent.replace('\n', '<br />')

        return output_start+user_name+output_middle+diaryContent+output_end
    return output_start+user_name+output_middle+diaryContent+output_end


application = default_app()

run(host='localhost', port=1234, debug=True)
