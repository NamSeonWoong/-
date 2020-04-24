import os
from flask import Flask, jsonify, render_template, url_for, request, redirect
# url_for : 해당 지점으로 향하는 url을 만들어주는 함수?
from crawling import search
from DeepLearning import processing
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # /// 세개는 상대적 path, //// 네개는 절대 path
db = SQLAlchemy(app)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    user = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(30), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Post {self.id}>'

@app.route('/search/<string:keyword>/<int:page>', methods=['GET'])
def process(keyword, page):
    try:
        if request.method == "GET":
            original = search(keyword, page)
            # for item in original:
            #     new_post = Post(
            #         title=item.get('title'), 
            #         user=item.get('user'),
            #         category=item.get('category'), 
            #         price=item.get('price'), 
            #         content=item.get('content'), 
            #         date=item.get('date'), 
            #         url=item.get('url')
            #         )
            #     db.session.add(new_post)
            # db.session.commit()
            result = processing(original)
            return jsonify(result)
    except Exception as e:
        print(str(e))
    return "OMG, Something Wrong"

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0",port="5000")
    # app.run(debug=False)