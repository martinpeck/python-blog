from flask import render_template, got_request_exception
from app import app, db
import os
import rollbar
import rollbar.contrib.flask

@app.before_first_request
def init_rollbar():
  if not app.debug:
    if os.environ.get('ROLLBAR_ACCESS_TOKEN'):
      rollbar.init(
            os.environ.get('ROLLBAR_ACCESS_TOKEN'),
            'python-blog-dev',
            root=os.path.dirname(os.path.realpath(__file__)),
            allow_logging_basic_config=False)
      got_request_exception.connect(rollbar.contrib.flask.report_exception, app)
      rollbar.report_message('Rollbar configured for python-blog')

@app.errorhandler(404)
def not_found_error(error):
  return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
  db.session.rollback()
  return render_template('500.html'), 500