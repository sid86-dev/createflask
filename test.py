lst = []

req = ['click==8.0.1','Flask==2.0.1','importlib-metadata==4.8.1','itsdangerous==2.0.1','Jinja2==3.0.1','MarkupSafe==2.0.1','typing-extensions==3.10.0.2','Werkzeug==2.0.1','zipp==3.5.0','colorama==0.4.4']

lst2 = []
for i in req:
	lst2.append(f'echo {i} >> requirements.txt')

print(lst2)
