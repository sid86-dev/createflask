# create a working directory  
echo "Enter a folder name: ";
read folder_name
mkdir $folder_name

cd $folder_name
# build templates
mkdir templates
cd templates
touch index.html
echo '<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Flask app</title>
</head>

<body>
    <h1>Hello World</h1>
</body>

</html>' > index.html;
cd ..
# build static files
mkdir static
cd static
mkdir css
mkdir js
mkdir images
cd ..
# build app.py file
touch app.py
echo 'from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=="__main__":
    app.run()

' > app.py;
# installs modules
pip install flask;
pip freeze > requirements.txt;
echo 'click==8.0.1
colorama==0.4.4
Flask==2.0.1
importlib-metadata==4.8.1
itsdangerous==2.0.1
Jinja2==3.0.1
MarkupSafe==2.0.1
typing-extensions==3.10.0.2
Werkzeug==2.0.1
zipp==3.5.0
' > requirements.txt;
python app.py;
