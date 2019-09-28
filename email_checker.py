#!flask/bin/python
from flask import Flask, request, jsonify, abort
from validity_check import *

app = Flask(__name__)


# this function serves as
@app.route('/')
def index():
    return "call ~/unique_email with a list of emails which are to be verified in JSON, FORM or ARGS request"


@app.route('/unique_email', methods=['POST'])
def unique_email():

    # check to verify the format of request , expecting the requests to be in json, args or form format
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

    # caching known domain names to reduce time spent in lookup
    known_email_dns = {'gmail.com': 0, 'yahoo.com': 0, 'hotmail.com': 0}

    for e in email_list:
        if isinstance(e, str) and e not in unique_mails:
            e = e.lower()
            first, second, is_valid = check_domain(e, known_email_dns) # verifying domain name of the email addrss
            if is_valid:
                user_valid, modified_username = check_username(first) # Verifying username
                if user_valid:
                    modified_addr = modified_username + '@' + second
                    if modified_addr not in unique_mails:
                        unique_mails[modified_addr] = 0

    ret = {
        'number_emails_input' : str(len(email_list)),
        'num_valid_unique_emails': str(len(unique_mails))
    }

    return jsonify({'ret': ret}), 201


if __name__ == '__main__':
    app.run(debug=True)
