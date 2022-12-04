"""Blogly application."""

from flask import Flask, request, render_template, session, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] ='idk123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

connect_db(app)

db.create_all()

@app.route('/')
def home_page():
    '''this current takes the users to the users list page'''
    return redirect('/users')



@app.route('/users')
def user_page():
    '''This shows a list of all current users'''
    users = User.query.all()
    return render_template('home.html', users=users)



@app.route('/users/<int:user_id>')
def load_details(user_id):
    '''this shows the profile's details'''
    user = User.query.get_or_404(user_id)
    posts = Post.query.filter_by(user_id=user_id).all()
    return render_template('detail.html', user=user, posts=posts)



@app.route('/users/new', methods=['GET'])
def present_new_user_form():
    '''this presents the user with the form to add a new user'''
    return render_template('new_user.html')


@app.route('/users/new', methods=['POST'])
def collect_form_data():
    """This gathers what the client entered and makes a new user on the DB. Then takes them back to the users list page."""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    url_link = request.form['url']

    new_user = User(first_name=first_name, last_name=last_name, image_url=url_link)
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


@app.route('/users/<int:user_id>/edit', methods=['GET'])
def present_edit_page(user_id):
    """This just presents the page and form where the user can enter the info for the edit"""
    user = User.query.get_or_404(user_id)

    return render_template('edit_profile.html', user=user)


@app.route('/users/<int:user_id>/edit', methods=['POST'])
def gather_edit_data(user_id):
    """This gathers what the client entered and then proceeds to update that user on the DB. Then takes them back to the users list page."""
    new_first_name = request.form['first_name']
    new_last_name = request.form['last_name']
    new_url_link = request.form['url']

    current_user = User.query.get_or_404(user_id)
    current_user.first_name = str(new_first_name)
    current_user.last_name = str(new_last_name)
    current_user.image_url = str(new_url_link)

    db.session.add(current_user)
    db.session.commit()

    return redirect('/users')



@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """This will delete a user from the DB and then take the client back to the users list page"""
    current_user = User.query.get_or_404(user_id)
    db.session.delete(current_user)
    db.session.commit()

    return redirect('/users')


# Part TWO routes


@app.route('/users/<int:user_id>/posts/new', methods=['GET'])
def present_new_post_form(user_id):
    """This will present the form for a user to add a new post."""
    current_user = User.query.get_or_404(user_id)

    return render_template('new_post.html', user=current_user)


@app.route('/users/<int:user_id>/posts/new', methods=['POST'])
def add_new_post(user_id):
    """This will collect the form data nad make a new post."""
    new_post_title= request.form['title']
    new_post_content= request.form['content']

    new_post = Post(title=new_post_title, content=new_post_content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()

    return redirect(f"/users/{user_id}")


@app.route('/posts/<int:post_id>')
def get_post_content(post_id):
    """This will get the post and its corresponding content"""
    current_post = Post.query.get_or_404(post_id)
    return render_template('posts.html', post=current_post)



@app.route('/posts/<int:post_id>/edit', methods=['GET'])
def show_edit_form(post_id):
    """This will prompt the user with a form to edit their post."""
    current_post = Post.query.get_or_404(post_id)

    return render_template('edit_post.html', post=current_post)


@app.route('/posts/<int:post_id>/edit', methods=['POST'])
def make_post_edit(post_id):
    """This will make the edits to the post from the form data."""
    current_post = Post.query.get_or_404(post_id)

    new_post_title= request.form['title']
    new_post_content= request.form['content']

    current_post.title= str(new_post_title)
    current_post.content= str(new_post_content)

    db.session.add(current_post)
    db.session.commit()

    return redirect(f'/posts/{post_id}')


@app.route('/posts/<int:post_id>/delete')
def delete_post(post_id):
    """This will delete the currently selected post."""
    current_post = Post.query.get_or_404(post_id)
    user_id = current_post.user.id
    db.session.delete(current_post)
    db.session.commit()

    return redirect(f'/users/{user_id}')




