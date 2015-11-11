# -*- coding: utf-8 -*-
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app,Bottle,route,run,debug,request,template

from datetime import datetime
import sys

@route('/',method='GET')
@route('/<user_name>')
def diary(user_name='小小游侠'):

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

<h1>小小游侠的聊天室</h1>
<p>欢迎小小游侠来到聊天室小憩一会。
<br />如果想用自己的名字加入交谈，
<br />可以用 “zoejane.pythonanywhere.com/YOURNAME”进行登录，
<br />名字可以是字母和数字和下划线的组合。
<br />
<br />想搭建一个相似的网页，可以看这里的教程。
<br />这个网页的具体的代码也可以在这里看到。
<br />
<br />我是<a href='mailto:dadac123@gmail.com'>Zoe Jane</a>，欢迎一起分享你的心得和感悟。
<br />我的<a href='mailto:dadac123@gmail.com'>Email</a>
<br />我的<a href='http://zoejane.github.com'>GitHub</a>
<br />我的<a href='http://zoejane.github.com'>GitBook</a>
<br /></p>

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

    if request.GET.get('save_diary','').strip():

        today=datetime.now()
        newDiary=request.GET.get('newdiary', '').strip()

        diaryFile = open('diary.txt')
        diaryContent = diaryFile.read()
        diaryFile.close()

        with open('diary.txt', 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            newDiaryLine=today.strftime("%Y/%m/%d/ %T")+ '  ['+user_name+'] '+newDiary
            f.write(newDiaryLine.rstrip('\r\n') + '\n' + content)

        diaryFile = open('diary.txt')
        diaryContent = diaryFile.read()
        diaryFile.close()
        diaryContent=diaryContent.replace('\n', '<br />')

        return output_start+user_name+output_middle+diaryContent+output_end
    return output_start+user_name+output_middle+diaryContent+output_end


application = default_app()

run(host='localhost', port=1234, debug=True)
