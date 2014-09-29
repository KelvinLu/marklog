import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

MARKLOG_POST_DIR = os.path.join(basedir, 'marklog/assets/posts')