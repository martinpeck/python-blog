from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  user = {'username': 'Martin'}
  posts = [
    {
      'author': {'username': 'Martin'},
      'body': 'My first blog post!'
    },
    {
      'author': {'username': 'Jessica'},
      'body': 'Getting a better understanding of Python'
    }
  ]
  return render_template('index.html', title='Home', user=user, posts=posts)