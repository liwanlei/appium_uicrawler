# encoding: utf-8
"""
@author: lileilei
"""


def title(titles):
    title = '''<!DOCTYPE html>
<html>
<head>
	<title>%s</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- 引入 Bootstrap -->
    <link href="https://cdn.bootcss.com/bootstrap/3.3.6/css/bootstrap.min.css" rel="stylesheet">
    <!-- HTML5 Shim 和 Respond.js 用于让 IE8 支持 HTML5元素和媒体查询 -->
    <!-- 注意： 如果通过 file://  引入 Respond.js 文件，则该文件无法起效果 -->
    <!--[if lt IE 9]>
     <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
     <script src="https://oss.maxcdn.com/libs/respond.js/1.3.0/respond.min.js"></script>
    <![endif]-->
    <style type="text/css">
        .hidden-detail,.hidden-tr{
            display:none;
        }
    </style>
</head>
<body>
	''' % (titles)
    connent = '''<div  class='col-md-8 col-md-offset-4' style='margin-left: 10%;margin-top: 2%;'>
    <h1 style="text-align: center;">{}测试的结果</h1>'''.format(
        titles)
    title += connent
    return title
