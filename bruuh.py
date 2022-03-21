from flask import Flask, make_response, jsonify
from flask_restful import reqparse, abort, Api, Resource
from data import db_session, news_resources


app = Flask(__name__)
api = Api(app)
app.config['SECRET KEY'] = 'ddd'
api = Api(app, catch_all_404s=True)
db_sess = db_session.create_session()
def main():
    api.add_resource(news_resources.NewsListResource, '/api/v2/news')
    api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
