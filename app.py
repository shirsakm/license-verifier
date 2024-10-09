from flask import Flask, jsonify, request
from auth import auth
from main import main
from lify import verify_license

app = Flask(__name__)
app.secret_key = 'secret'
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(main, url_prefix='/')

@app.route('/verify/<license_id>')
def verify(license_id):
    status = verify_license(license_id)

    return jsonify(status)

if __name__ == '__main__':  
    app.run()