import socket
"""
This file contains functions useful in checking validity of an email address
"""


"""
input :
    1. email; type: string,
    2. known_email_dns ; type: dictionary [containing already recorded dns host names]
    ex 1 : email : "ramya12.rao@gmail.com", known_email_dns : {'gmail.com': 0, 'yahoo.com': 0, 'hotmail.com': 0}
output :
    1. first half of email [type string],
    2. second half of email [type string],
    3. return valid dns host or not [boolean]

    ex 1 : ramya12.rao@gmail.com , first_half = ramya12.rao, second_half = gmail.com

"""


def check_domain(email, known_email_dns):
    # splitting the string with @ and checking the length of the split
    at_check = email.split('@')
    if len(at_check) != 2:
        return None, None, False

    # if the domain name is already know then return it
    if at_check[1] in known_email_dns:
        return at_check[0], at_check[1], True

    # use socket.gethostbyname() to check for valid domain name
    try:
        _ = socket.gethostbyname(at_check[1])
    except:
        return None, None, False

    known_email_dns[at_check[1]] = 0
    return at_check[0], at_check[1], True


"""
input :
    1. username ; type: string [first half of email],
    ex 1 : ramya12.rao+somthing
output :
    1. return valid username or not ; type boolean
    2. return the username; which maybe modified

    ex 1 : True, ramya12.rao
    used google username check rules to validate username : https://support.google.com/mail/answer/9211434?hl=en

"""


def check_username(username):
    # check presence of + and ignore all the characters after that
    plus_ind = username.find('+')
    if plus_ind != -1:
        username = username[:plus_ind]

    # Make sure username is between 6 and 30 characters in length and does not have . at the begining
    if len(username) < 6 or len(username) > 30 or username[0] == '.':
        return False, None

    # check for invalid characters
    invalid_chars = "&=_'-+,<>"
    for chr in username:
        if chr in invalid_chars:
            return False, None

    # makign sure only one period exists and ignoring it
    period_split = username.split('.')
    if len(period_split) > 2:
        return False, None

    username = username.replace('.', '')

    return True, username


