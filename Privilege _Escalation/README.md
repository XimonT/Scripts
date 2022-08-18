# Privilege Escalation

These tools and methods were used in [Hack The Box](https://www.hackthebox.com/) challenges:

## [`pspy`](https://github.com/DominicBreuker/pspy)

pspy is a command line tool designed to snoop on processes without need for root permissions.
It allows you to see commands run by other users, cron jobs, etc. as they execute. Great for enumeration of Linux systems in CTFs

> [`source`](https://github.com/DominicBreuker/pspy)
> [`tutorial`](https://jayden-lind.github.io/posts/htb-opensource/)

---

## [`linpeas`](linpeas.sh)

LinPEAS is a script that search for possible paths to escalate privileges on Linux/Unix*/MacOS hosts

> [`source`](https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS)

---

## [`mysql_as_root`](mysql_as_root.c)

when mysql is run with root privileges we can use it to read files that we wouldn't be able to

> [`source`](https://www.exploit-db.com/exploits/1518)
