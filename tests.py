from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):

  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_password_hashing_works_for_matching_password(self):
    u = User(username='martin')
    u.set_password('123')
    self.assertTrue(u.check_password('123'))

  def test_password_hashing_fails_for_different_password(self):
    u = User(username='martin')
    u.set_password('123')
    self.assertFalse(u.check_password('234'))

  def test_avatar_url_generation(self):
    u = User(username='jessica', email="jess@example.com")
    expectedUrl = 'https://www.gravatar.com/avatar/4f0dc70323496e4a44bb8fa12fb900b1?d=identicon&s=128'
    self.assertEqual(u.avatar(128), expectedUrl)

  def test_user_follows_user(self):
    # create two users
    u1 = User(username='user1', email='user1@example.com')
    u2 = User(username='user2', email='user2@example.com')
    db.session.add(u1)
    db.session.add(u2)
    db.session.commit()

    # assert that they're not following anyone
    self.assertEqual(u1.followed.all(), [])
    self.assertEqual(u2.followed.all(), [])

    # user1 follows user2
    u1.follow(u2)
    db.session.commit()

    self.assertTrue(u1.is_following(u2))
    self.assertEqual(u1.followed.count(), 1)
    self.assertEqual(u1.followed.first().username, 'user2')
    self.assertEqual(u2.followers.count(), 1)
    self.assertEqual(u2.followers.first().username, 'user1')

    u1.unfollow(u2)
    db.session.commit()

    self.assertFalse(u1.is_following(u2))
    self.assertEqual(u1.followed.count(), 0)
    self.assertEqual(u2.followers.count(), 0)

  def test_follow_posts(self):
    # create four users
    u1 = User(username='john', email='john@example.com')
    u2 = User(username='susan', email='susan@example.com')
    u3 = User(username='mary', email='mary@example.com')
    u4 = User(username='david', email='david@example.com')
    db.session.add_all([u1, u2, u3, u4])

    # create four posts
    now = datetime.utcnow()
    p1 = Post(body="post from john", author=u1, timestamp=now + timedelta(seconds=1))
    p2 = Post(body="post from susan", author=u2, timestamp=now + timedelta(seconds=4))
    p3 = Post(body="post from mary", author=u3, timestamp=now + timedelta(seconds=3))
    p4 = Post(body="post from david", author=u4,timestamp=now + timedelta(seconds=2))
    db.session.add_all([p1, p2, p3, p4])
    db.session.commit()

    # setup the followers
    u1.follow(u2)  # john follows susan
    u1.follow(u4)  # john follows david
    u2.follow(u3)  # susan follows mary
    u3.follow(u4)  # mary follows david
    db.session.commit()

    # check the followed posts of each user
    f1 = u1.followed_posts().all()
    f2 = u2.followed_posts().all()
    f3 = u3.followed_posts().all()
    f4 = u4.followed_posts().all()
    self.assertEqual(f1, [p2, p4, p1])
    self.assertEqual(f2, [p2, p3])
    self.assertEqual(f3, [p3, p4])
    self.assertEqual(f4, [p4])

if __name__ == '__main__':
  unittest.main(verbosity=2)