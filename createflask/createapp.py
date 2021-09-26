import time
import subprocess
from tqdm import tqdm
import time

class Create:
    def __init__(self, name):
        self.name = name

    start = time.time()
    
    tasks1 = ['mkdir static', 'mkdir templates', 'cd templates', 'echo from flask import Flask > app.py', 'echo app=Flask(__name__) >> app.py', 'echo @app.route("/") >> app.py', 'echo def index(): >> app.py', 'echo      return "Hello world this is flask app" >> app.py', 'echo if __name__=="__main__": >> app.py', 'echo     app.run(debug=True) >> app.py', 'echo click==8.0.1 >> requirements.txt', 'echo Flask==2.0.1 >> requirements.txt', 'echo importlib-metadata==4.8.1 >> requirements.txt', 'echo itsdangerous==2.0.1 >> requirements.txt', 'echo Jinja2==3.0.1 >> requirements.txt', 'echo MarkupSafe==2.0.1 >> requirements.txt', 'echo typing-extensions==3.10.0.2 >> requirements.txt', 'echo Werkzeug==2.0.1 >> requirements.txt', 'echo zipp==3.5.0 >> requirements.txt', 'echo colorama==0.4.4 >> requirements.txt']


    def sow(self,server):
        execution = "run"

        print('build starting...')

        for task in self.tasks1: 
            p1 = subprocess.run(task, shell=True)
            
            if p1.returncode != 0:
                execution = "dismiss"
                break 
        
        if execution == "run":
            for i in tqdm (range (len(self.tasks1)),
		        desc="Creating…",
		        ascii=False, ncols=75):
	            time.sleep(0.02)

            finish = time.time()

            final_task =  ['pip install --upgrade flask','start http://127.0.0.1:5000/', 'python app.py']

            print(f'flask app created in {round(finish-self.start, 2)} seconds')

            if server==True:
                for task in final_task:
                    p2 = subprocess.run(task, shell=True)
            


if __name__ == "__main__":
    app = Create('app')

    app.sow(server=True)