import os
from flask import Flask, jsonify, render_template, url_for, request, redirect
# url_for : 해당 지점으로 향하는 url을 만들어주는 함수?
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from crawling import search
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from tensorflow import keras
import numpy as np
import pickle

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # /// 세개는 상대적 path, //// 네개는 절대 path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)

model = keras.models.load_model(basedir+'/my_model.h5')
with open(basedir+'/tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


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

@app.route('/', methods=['GET'])
def test():
    return "It worked properly"


@app.route('/search/<string:keyword>/<int:page>', methods=['GET'])
def process(keyword, page):
    try:
        if request.method == "GET":
            # print("start searching")
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
            # try:
            #     result = processing(original, new_model)
            # except:
            #     return "deeplearning error!"
            # print('put data')
            x_data = []
            for datum in original:
                if datum['content']:
                    # print((' '.join(datum['content']))[:100].replace(' ', ''))
                    x_data.append(' '.join(datum['content']))
                else:
                    x_data.append(datum['title'])

            # print('MAKE SEQUENCE')
            sequences = tokenizer.texts_to_sequences(x_data)
            x_data = sequences
            # print('data processing')
            data = np.array(pad_sequences(x_data, maxlen = 16899))
            # print('predict')
            result = model.predict(data)
            resultlist = result.tolist()
            
            for idx in range(len((original))):
                original[idx]['isTrader'] = resultlist[idx][0] 
            return jsonify(original)
    except Exception as e:
        print(str(e))
    return "OMG, Something Wrong"

if __name__ == "__main__":

    app.run(debug=False, host="0.0.0.0", port=5000)
    # app.run(debug=False)