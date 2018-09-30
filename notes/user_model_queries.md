# User Model Queries

## Importing the database and models

``` python
>>> from app import db
>>> from app.models import User, Post
```

## Adding two users to the database

```python
>>> u = User(username='Martin', email='martin@example.com')
>>> db.session.add(u)
>>> db.session.commit()
>>> u = User(username='Jessica', email='jessica@example.com')
>>> db.session.add(u)
>>> db.session.commit()
```

## Retrieve all users

```python
>>> users = User.query.all()
>>> users
[<User Martin>, <User Jessica>]
>>> for u in users:
...     print(u.id, u.username)
...
1 Martin
2 Jessica

```

## Get User by ID

```python
>>> u = User.query.get(1)
>>> u
<User Martin>
>>> u = User.query.get(2)
>>> u
<User Jessica>
>>> u = User.query.get(3)
>>> u
>>> u == None
True
```

## Filter users by e-mail

```python
>>> users = User.query.filter_by(email='martin@example.com')
>>> users[0]
<User Martin>
>>> users.count()
1
>>> users.all()
[<User Martin>]
```

## Find users with e-mails that end with a particular pattern

```python
>>> users = User.query.filter(User.email.endswith('example.com'))
>>> users.all()
[<User Martin>, <User Jessica>]
```