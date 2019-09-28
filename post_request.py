# import requests
#
# dictToSend = {'email_list':["test.email+spam@gmail.com", "testemail@gmail.com", "test.email@gmail.com", "ramya_12@gmail.com"]}
# res = requests.post('http://localhost:5000/verify_email', json=dictToSend)
# print('response from server:', res.text)
# dictFromServer = res.json()
#


def check():
    s = "ramya<,'pos"
    invalid_chars = "&=_'-+,<>"
    for chr in s:
        if chr in invalid_chars:
            print(chr)
            print("has invalid char")
    return


check()