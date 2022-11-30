from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = True


db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Tests for model for Users."""

    def setUp(self):
        '''Clean up any existing users:'''

        User.query.delete()
        db.session.commit()

    def tearDown(self):
        '''Clean up any fouled transactions.'''

        db.session.rollback()

    def test_user_name(self):
        test = User(first_name='Test', last_name='User')
        self.assertEqual(test.first_name, "Test")

        test1 = User(first_name='Test', last_name='Userx')
        self.assertEqual(test1.last_name, "Userx")

    # Does not work... why?
    def test_url_link(self):
        test2 = User(first_name='Test', last_name='User')
        self.assertEqual(test2.image_url, "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png")


    
# question to ask tomorrow-- do i need to be connected to my test DB when doing these?

        

