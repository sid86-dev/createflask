@echo off

color a
set /p f_name=Enter folder name:

mkdir  %f_name%
cd %f_name%
mkdir static
cd static
mkdir css
mkdir images
mkdir js
cd ..
mkdir templates
cd templates

setlocal EnableDelayedExpansion
set LF=^


rem Two empty lines are required
set data_flask=from flask import Flask, render_template!LF!app=Flask(__name__)!LF!@app.route('/')!LF!def index():!LF!     return render_template('index.html')!LF!if __name__=='__main__':!LF!    app.run(port=4000)
set data_index=Hello world!LF!this is %f_name% flask app
set data_req=click==8.0.1!LF!Flask==2.0.1!LF!importlib-metadata==4.8.1!LF!itsdangerous==2.0.1!LF!Jinja2==3.0.1!LF!MarkupSafe==2.0.1!LF!typing-extensions==3.10.0.2!LF!Werkzeug==2.0.1!LF!zipp==3.5.0!LF!colorama==0.4.4
echo !data_index! > "index.html"
cd ..
echo !data_flask! > "app.py"
echo !data_req! > "requirements.txt"
@REM pause
start chrome http://127.0.0.1:4000/
python app.py
clear

