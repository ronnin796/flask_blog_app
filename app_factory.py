from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from extensions import db, login_manager, ckeditor
from views.blog_views import blog_bp
from views.user_views import user_bp
from decouple import config


def create_app():

    app = Flask(__name__)

    app.config["SECRET_KEY"] = config("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///posts.db"

    Bootstrap5(app)
    ckeditor.init_app(app)
    app.register_blueprint(blog_bp)
    app.register_blueprint(user_bp)
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    return app
