# Extra

Extra tool and other i've found:

### [`flask route to add for reverse shell`](flask_reverse_shell.py)

what to add in a configuration file on a flask server to open a reverse shell, just go to:
`http://<target>/rev?cmd=id`

we used this in a LFI exploit, we build a [`script`](upload_script.py) to upload a file that overwrites a configuration file that has all the directories of the webapplication
the filename that had the reverse shell and later overwrites the original file was called: `/app/app/views.py`
the location of the configuration file was in: `/source/app/app/views.py`
the location of the upload folder was in `/source/app/public/uploads/<new_file>`
> [`source`](https://ToDo)

---

### [`ToDo`](ToDo)
