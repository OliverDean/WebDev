from flask import render_template
from flask_login import current_user, logout_user
from . import app, db

def init_app_error(app):
    app.register_error_handler(404, not_found_error)
    app.register_error_handler(500, lambda e: internal_error(e, app))
    app.register_error_handler(403, forbidden_error)
    app.register_error_handler(401, unauthorized_error)
    app.register_error_handler(400, bad_request_error)
    app.register_error_handler(405, method_not_allowed_error)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html', error_code=404, error_message='Page not found\n I thought it was right here...'), 404

@app.errorhandler(500)
def internal_error(error, _):
    if current_user.is_authenticated:
        logout_user()  # Log out the current user
    db.session.rollback()
    return render_template('error.html', error_code=500, error_message='Internal server error\n Thats an oops'), 500

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('error.html', error_code=403, error_message='Forbidden access\n You shall not pass!'), 403

@app.errorhandler(401)
def unauthorized_error(error):
    return render_template('error.html', error_code=401, error_message='Unauthorized access\n You shall not pass!'), 401

@app.errorhandler(400)
def bad_request_error(error):
    return render_template('error.html', error_code=400, error_message='Bad request\n Computer says no'), 400

@app.errorhandler(405)
def method_not_allowed_error(error):
    return render_template('error.html', error_code=405, error_message='Method not allowed\n Computer says no'), 405


