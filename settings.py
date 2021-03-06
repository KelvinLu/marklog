import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

MARKLOG_POST_DIR = os.path.join(basedir, 'marklog/assets/posts')

MARKLOG_BLOG_TITLE = 'My Awesome Marklog Blog'

MARKLOG_BLOG_DESC = 'I am very cool'

MARKLOG_BLOG_POST_COLORS = ['#DE0D6C', '#0F92B1', '#FFDF0F']