import subprocess
import time
from rich.console import* 
from rich.theme import* 
from rich.progress import track
from rich.markdown import Markdown

custome_theme = Theme({'success': 'green', 'error': 'bold red', 'normal': 'yellow'})

console = Console(theme=custome_theme)

class Create:
    def __init__(self, name):
        self.name = name

    start = time.time()

    tasks1 = ['mkdir static', 'mkdir templates', 'cd templates', 'echo from flask import Flask > app.py', 'echo app=Flask(__name__) >> app.py', 'echo @app.route("/") >> app.py', 'echo def index(): >> app.py', 'echo      return "Hello world this is flask app" >> app.py', 'echo if __name__=="__main__": >> app.py', 'echo     app.run(debug=True) >> app.py', 'echo click==8.0.1 >> requirements.txt', 'echo Flask==2.0.1 >> requirements.txt', 'echo importlib-metadata==4.8.1 >> requirements.txt', 'echo itsdangerous==2.0.1 >> requirements.txt', 'echo Jinja2==3.0.1 >> requirements.txt', 'echo MarkupSafe==2.0.1 >> requirements.txt', 'echo typing-extensions==3.10.0.2 >> requirements.txt', 'echo Werkzeug==2.0.1 >> requirements.txt', 'echo zipp==3.5.0 >> requirements.txt', 'echo colorama==0.4.4 >> requirements.txt']

    def sow(self,server):
        execution = "run"

        console_ = Console()

        now = datetime.now()

        current_time = now.strftime("%H:%M:%S")

        MARKDOWN = f'''
        
# Flask app build starting at {current_time}

'''

        md = Markdown(MARKDOWN)

        console_.print(md)

        try:
            for task in self.tasks1: 
                p1 = subprocess.run(task, shell=True)
            
                if p1.returncode != 0:
                    execution = "dismiss"
                    break 
                    
            show_ = ['app.py', 'requirements.txt', 'static dir', 'template dir']

            with console_.status("[bold green]Working on tasks...") as status:
                while show_:
                    task_ = show_.pop(0)
                    time.sleep(1)
                    console_.log(f"Building {task_} complete")
        
        
        except:
            console.print('Build Failed :bangbang:', style='error')

        if execution == "run":

            finish = time.time()

            final_task =  ['pip install --upgrade flask','start http://127.0.0.1:5000/', 'python app.py']
            
            console.print('Build success :heavy_check_mark:', style='success')
            console.print(f'flask app created in {round(finish-self.start, 2)} seconds', style='success')
            time.sleep(1)

            if server==True:
                console.print('Installing Dependencies...', style='normal')
                for task in final_task:
                    p2 = subprocess.run(task, shell=True , stderr=subprocess.DEVNULL)
                    if final_task.index(task) == 1:
                        console.print('Running server on port 5000', style='success')
            


if __name__ == "__main__":
    app = Create('app')

    app.sow(server=False)