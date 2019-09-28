import requests


"Citation: Code from stack overflow : https://stackoverflow.com/questions/10313001/is-it-possible-to-make-post-request-in-flask"

dictToSend = {'email_list':["test.email+spam@gmail.com", "testemail@gmail.com", "test.email@gmail.com", "ramya_12@gmail.com"]}
# ******* change this localhost url if necessary while testing ***************
res = requests.post('http://localhost:5000/unique_email', json=dictToSend)
print('response from server:', res.text)
dictFromServer = res.json()

