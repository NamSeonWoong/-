원하는 프로젝트 디렉토리 생성

pip3 install virtualenv

source env/Scripts/activate (또는 source env/bin/activate)

pip install flask flask-sqlalchemy

app.py 파일 생성

> app.py 내용

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

python app.py로 실행

app.py와 같은 폴더에 static, templates 폴더 생성

templates 폴더 내부에 base.html, index.html, !+tab(vscode 기준)으로 기본 템플릿 생성뒤 body에 

> base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
    {% block head %}
    {% endblock %}
</head>
<body>
    {% block body %}
    {% endblock %}
</body>
</html>
```

- {% %} : Jinja2 문법, 
- block~endblock : 해당 부분에 다른 html파일을 넣는 템플릿으로 쓸수 있게 해줌 

> index.html

```html
{% extends 'base.html' %}
{% block head %} 
<h1>
    Template
</h1>
{% endblock %}

{% block body %} 
{% endblock %}
```

- extends '파일' 을 원해 해당 파일 내부의 block을 가져올 수 있음

> static/css/main.css 파일

```css
body {
    margin: 0;
    font-family: sans-sariff;
}
```

- base.html에서 link를 통해 가져왔다.

- {{}} : 콧수염 문법 을 통해 python 문법을 사용가능하며 url_for는 아래 app.py에서 확인



> app.py index 함수 변화

```python
from flask import Flask, render_template, url_for 
# url_for : 해당 지점으로 향하는 url을 만들어주는 함수?
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # /// 세개는 상대적 path, //// 네개는 절대 path를 의미
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
```

> db 생성

```bash
multicampus@DESKTOP-KVCQHCD MINGW64 ~/Desktop/flask
$ python
Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import db
C:\Users\multicampus\Desktop\flask\env\lib\site-packages\flask_sqlalchemy\__init__.py:834: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  warnings.warn(FSADeprecationWarning(
>>> db.create_all()
>>> exit()
```



> 최종 결과물
>
> app.py (update와 delete 기능 추가)

```python
from flask import Flask, render_template, url_for, request, redirect
# url_for : 해당 지점으로 향하는 url을 만들어주는 함수?
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # /// 세개는 상대적 path, //// 네개는 절대 path
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = Todo(content= task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/') 
    except:
        return 'There was a probelm deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)

    if request.method == 'POST':
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue updating your task"
    else:
        return render_template('update.html', task=task)


if __name__ == "__main__":
    app.run(debug=True)
```

> index.html
```python
{% extends 'base.html' %}
{% block head %} 
<title>Task Master</title>
{% endblock %}

{% block body %} 
<div class="content">
    <h1 style="text-align: center">Task Master</h1>
    {% if tasks|length < 1 %}
    <h4>There are no tasks. create one now!</1>
    {% else %}
    <table>
        <tr>
            <th>Task</th>
            <th>Added</th>
            <th>Actions</th>
        </tr>
        {% for task in tasks %}
        <tr>
            <td>{{task.content}}</td>
            <td>{{task.date_created.date()}}</td>
            <td>
                <a href="/delete/{{task.id}}">Delete</a>
                <br>
                <a href="/update/{{task.id}}">Update</a>

            </td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}

    <form action="/" method="POST">
        <input type="text" name="content" id="content">
        <input type="submit" value="Add Task">
    </form>
</div>
{% endblock %}
```
> update.html
```python
{% extends 'base.html' %}
{% block head %} 
<title>Task Master</title>
{% endblock %}

{% block body %} 
<div class="content">
    <h1 style="text-align: center;">Update Task</h1>


    <div class="form">
        <form action="/update/{{task.id}}" method="POST">
            <input type="text" name="content" id="content" value="{{task.content}}">
            <input type="submit" value="Update">
        </form>
    </div>
</div>
{% endblock %}
```
