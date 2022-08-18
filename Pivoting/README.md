# Pivoting

These tools were used in [Hack The Box](https://www.hackthebox.com/) challenges:

## [`chisel`](ssti_payload_generator_java_springboot.py)

Chisel is a fast TCP/UDP tunnel, transported over HTTP, secured via SSH.
Single executable including both client and server. Written in Go (golang).
Chisel is mainly useful for passing through firewalls, though it can also be used to provide a secure endpoint into your network.

> [`source`](https://github.com/jpillora/chisel)
> [`tutorial`](https://ap3x.github.io/posts/pivoting-with-chisel/)
> [`download`](https://github.com/jpillora/chisel/releases/download/v1.7.7/chisel_1.7.7_linux_amd64.gz)

---

## [`dembe`](https://github.com/BloodhoundAllfather/dembe.git)

Dembe is a TCP tunnel application written in C.
It makes two TCP connections (either via listening or connecting) and sends out the data received from one end to another with its muti-threaded design.
It will automatically connect/listen if connection gets terminated.

> [`source`](https://github.com/BloodhoundAllfather/dembe)
