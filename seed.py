"""Seed file to make sample data for db."""

from models import db, User, Post, connect_db
from app import app


# Create all tables:
db.drop_all()
db.create_all()


John = User(first_name='John', last_name='Jamieson')
Kate = User(first_name='Kate', last_name='Ortega')
Joel = User(first_name='Joel', last_name='Miller')

dog_post = Post(title='My New Puppy', content="I got a new puppy! Its a beagle.", user_id=1)
dog2_post = Post(title='Puppy Update', content="My beagle has zoomies all the time!", user_id=1)
cat_post = Post(title='My New Cat', content="I got a new cat! Its a tabby.", user_id=2)
snake_post = Post(title='My New Snake', content="I got a new snake! Its cool.", user_id=3)

db.session.add_all([John, Kate, Joel])

db.session.commit()

db.session.add_all([dog_post, dog2_post, cat_post, snake_post])

db.session.commit()