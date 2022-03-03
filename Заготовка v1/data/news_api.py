import flask
from flask import request, jsonify
from sqlalchemy_serializer import SerializerMixin
from . import db_session
from .news import News


blueprint = flask.Blueprint(
    f'news_api',
    __name__,
    template_folder='templates'
)


@blueprint.route("/api/news")
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    return jsonify(
        {
            "news": [item.to_dict(
                only=('title', 'content', 'user.name'))
                for item in news]
        }
    )

