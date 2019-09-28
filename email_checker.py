#!flask/bin/python
from flask import Flask, request, jsonify, abort
import socket
from validity_check import *

app = Flask(__name__)


# this function serves as 
@app.route('/')
def index():
    return "call ~/verify_email with a list of emails which are to be verified in JSON, FORM or ARGS request"


@app.route('/verify_email', methods=['POST'])
def verify_email():
    var_name = 'email_list'
    if request.json and var_name in request.json:
        email_list = request.json.get('email_list')
    elif request.form and var_name in request.form:
        email_list = eval(request.form['email_list'])
    elif request.args and var_name in request.args:
        email_list = eval(request.args['email_list'])
    else:
        abort(400)

    unique_mails = {}

    known_email_dns = {'gmail.com': 0, 'yahoo.com': 0, 'hotmail.com': 0}
    
    for e in email_list:
        if isinstance(e, str):
            e = e.lower()
            first, second, is_valid = check_domain(e, known_email_dns)
            if is_valid:
                user_valid, modified_username = check_username(first)
                if user_valid and modified_username not in unique_mails:
                    unique_mails[modified_username] = 0

    ret = {
        'number_emails_input' : str(len(email_list)),
        'num_valid_unique_emails': str(len(unique_mails))
    }

    return jsonify({'ret': ret}), 201


if __name__ == '__main__':
    app.run(debug=True)
