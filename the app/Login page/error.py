from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html', error_code=404, error_message='Page not found'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html', error_code=500, error_message='Internal server error'), 500

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('403.html', error_code=403, error_message='Forbidden access'), 403

@app.errorhandler(401)
def unauthorized_error(error):
    return render_template('401.html', error_code=401, error_message='Unauthorized access'), 401

@app.errorhandler(400)
def bad_request_error(error):
    return render_template('400.html', error_code=400, error_message='Bad request'), 400

@app.errorhandler(405)
def method_not_allowed_error(error):
    return render_template('405.html', error_code=405, error_message='Method not allowed'), 405
