"""Seed file to make sample data for db."""

from models import db, User, Post, Tag, PostTag, connect_db
from app import app


# Create all tables:
db.drop_all()
db.create_all()

# Adds some users:
John = User(first_name='John', last_name='Jamieson')
Kate = User(first_name='Kate', last_name='Ortega')
Joel = User(first_name='Joel', last_name='Miller')

# Adds some posts:
dog_post = Post(title='My New Puppy', content="I got a new puppy! Its a beagle.", user_id=1)
dog2_post = Post(title='Puppy Update', content="My beagle has zoomies all the time!", user_id=1)
cat_post = Post(title='My New Cat', content="I got a new cat! Its a tabby.", user_id=2)
snake_post = Post(title='My New Snake', content="I got a new snake! Its cool.", user_id=3)

# Adds some tags:
cute_tag = Tag(name='cute')
animal_tag = Tag(name='animal')
mammal_tag = Tag(name='mammal')
reptile_tag = Tag(name='reptile')

# Adds some post tags
dog_post_tag1 = PostTag(post_id=1, tag_id=1)
dog_post_tag2 = PostTag(post_id=1, tag_id=2)
dog_post_tag3 = PostTag(post_id=1, tag_id=3)
dog2_post_tag1 = PostTag(post_id=2, tag_id=1)
dog2_post_tag2 = PostTag(post_id=2, tag_id=2)
dog2_post_tag3 = PostTag(post_id=2, tag_id=3)
cat_post_tag1 = PostTag(post_id=3, tag_id=1)
cat_post_tag2 = PostTag(post_id=3, tag_id=2)
cat_post_tag3 = PostTag(post_id=3, tag_id=3)
snake_post_tag1 = PostTag(post_id=4, tag_id=4)


# Adds and commits everything in the proper order:
db.session.add_all([John, Kate, Joel])
db.session.commit()

db.session.add_all([dog_post, dog2_post, cat_post, snake_post])
db.session.commit()

db.session.add_all([cute_tag, animal_tag, mammal_tag, reptile_tag])
db.session.commit()

db.session.add_all([dog_post_tag1,dog_post_tag2,dog_post_tag3,dog2_post_tag1,dog2_post_tag2,dog2_post_tag3])
db.session.add_all([cat_post_tag1,cat_post_tag2,cat_post_tag3])
db.session.add(snake_post_tag1)
db.session.commit()