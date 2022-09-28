# Extra

Extra tool and other i've found:

## [`flask route to add for reverse shell`](flask_reverse_shell.py)

what to add in a configuration file on a flask server to open a reverse shell, just go to:

`http://<target>/rev?cmd=id`

we used this in a LFI exploit, we build a [`script`](upload_script.py) to upload a file that overwrites a configuration file that has all the directories of the webapplication
the filename that had the reverse shell and later overwrites the original file was called: `/app/app/views.py`
the location of the configuration file was in: `/source/app/app/views.py`
the location of the upload folder was in `/source/app/public/uploads/<new_file>`
> [`source`](https://github.com/Knocks83)

---

## [`Crack JWT with John`]()

to crack the jwt just copy/paste the token inside a text file called jwt.txt
and run john with a wordlist, we can use rockyou.txt as always:

`john jwt.txt —wordlist=wordlist.txt —format=HMAC-SHA256`

> [`source`](https://blog.pentesteracademy.com/hacking-jwt-tokens-bruteforcing-weak-signing-key-johntheripper-89f0c7e6a87)

---

## [`Crack JWT with jwt-cracker`]()

to crack a jwt hashed with only numbers we can use jwt-cracker a tool we can just install from [`github`](https://github.com/lmammino/jwt-cracker)
just crack the jwt as it is from the terminal:

`jwt-cracker "eyJhbGc.<SNAP>`

> [`source`](https://github.com/lmammino/jwt-cracker)

---
