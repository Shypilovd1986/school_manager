import unittest
from app.models import User


class UserModelTestCase(unittest.TestCase):
    def test_password_setter(self):
        u = User(first_name='Bon', last_name='aaf', email='sfsf@kad.com', password='234241245')
        self.assertTrue(u.password_hash is not None)

    def test_no_password_getter(self):
        u = User(first_name='Bon', last_name='aaf', email='sfsf@kad.com', password='234241245')

        with self.assertRaises(AttributeError):
            u.password

    def test_password_verification(self):
        u = User(first_name='Bon', last_name='aaf', email='sfsf@kad.com', password='234241245')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))

    def test_password_salts_are_random(self):
        u = User(first_name='Bon', last_name='aaf', email='sfsf@kad.com', password='234241245')
        u2 = User(first_name='Bon', last_name='aaf', email='sfsf@kad.com', password='234241245')
        self.assertTrue(u.password_hash != u2.password_hash)
