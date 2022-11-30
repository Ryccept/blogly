"""Blogly application."""

from flask import Flask, request, render_template, session, jsonify, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User

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

    return render_template('detail.html', user=user)



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

    # not sure why this is not just editing the previous entry... it instead just makes a new row? It works when done in Ipython
    return redirect('/users')



@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    """This will delete a user from the DB and then take the client back to the users list page"""
    current_user = User.query.get_or_404(user_id)
    db.session.delete(current_user)
    db.session.commit()

    return redirect('/users')



















# John = User(first_name='John', last_name='Jamieson', image_url='atest.png')
# Kate = User(first_name='Kate', last_name='Ortega', image_url='atest1.png')
# Joel = User(first_name='Joel', last_name='Miller', image_url='atest2.png')

# db.session.add(John)
# db.session.add(Kate)
# db.session.add(Joel)

# db.session.commit()



