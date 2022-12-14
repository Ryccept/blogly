"""Models for Blogly."""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"

class User(db.Model):
    '''User Database.'''

    __tablename__ = 'users'

    def __repr__(self):
        """Show info about a user."""

        u = self
        return f"<User {u.id} {u.first_name} {u.last_name} {u.image_url}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.Text, nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")

class Post(db.Model):
    '''User Database.'''

    __tablename__ = 'posts'

    def __repr__(self):
        """Show info about a user."""

        u = self
        return f"<User {u.id} {u.title} {u.content} {u.created_at} {u.user_id}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    tags = db.relationship('Tag',
                               secondary='posttags',
                               backref='posts')



class Tag(db.Model):
    '''User Database.'''

    __tablename__ = 'tags'

    def __repr__(self):
        """Show info about a user."""

        u = self
        return f"<User {u.id} {u.name}>"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)



class PostTag(db.Model):
    '''User Database.'''

    __tablename__ = 'posttags'

    def __repr__(self):
        """Show info about a user."""

        u = self
        return f"<User {u.post_id} {u.tag_id}>"

    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), primary_key=True, nullable=False)
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"), primary_key=True, nullable=False)