# Python TCP & UDP Client-Server Communication

This folder contains Python implementations of **TCP** and **UDP** client-server communication using the built-in `socket` module.

## Contents

```
Python/
├── tcp_server.py
├── tcp_client.py
├── udp_server.py
└── udp_client.py
```

## Prerequisites

- Python 3.8 or later
- Any terminal (PowerShell, Command Prompt, Bash, Terminal)
- No external Python libraries are required.

Verify your Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

# Running the TCP Program

## Step 1: Open two terminals

You need **two separate terminals**.

- Terminal 1 → Server
- Terminal 2 → Client

---

## Step 2: Start the TCP server

```bash
python tcp_server.py
```

Output:

```
Waiting for client...
```

Do **not** close this terminal.

---

## Step 3: Start the TCP client

Open another terminal in the same directory.

Run:

```bash
python tcp_client.py
```

Enter a message when prompted.

The server will receive the message and can send a reply.

---

# Running the UDP Program

Again, open **two terminals**.

---

## Terminal 1

```bash
python udp_server.py
```

---

## Terminal 2

```bash
python udp_client.py
```

The client sends a message to the server, and the server responds.

---

# Project Workflow

TCP:

```
Client
   │
connect()
   │
   ▼
Server
   │
accept()
   │
send()/recv()
```

UDP:

```
Client
   │
sendto()
   │
   ▼
Server
   │
recvfrom()
   │
sendto()
```

---

# Important Notes

✔ Run the **server first**.

✔ Then run the **client**.

✔ Keep the server terminal open while the client is running.

✔ The default IP address is:

```
127.0.0.1
```

which represents **localhost** (your own computer).

✔ Make sure both programs use the **same port number**.

---

# Common Errors

## Address already in use

```
OSError: [Errno 10048]
```

Reason:

Another program is already using the port.

Solution:

- Close the previous server.
- Or change the port number in both client and server.

---

## Connection Refused

```
ConnectionRefusedError
```

Reason:

The client was started before the server.

Solution:

Start the server first.

---

## Timeout / No Response (UDP)

Reason:

The UDP server is not running or the port numbers do not match.

---

## Firewall Blocking Connection

Windows Firewall may ask for permission when running the server for the first time.

Allow access on **Private Networks** if prompted.

---

# Modifying the Programs

You can safely change:

- IP Address
- Port Number
- Messages exchanged

If you change the port or IP, update **both** the client and server files.

---

# Learning Outcomes

After completing this project, you will understand:

- Socket Programming
- Client-Server Architecture
- TCP Communication
- UDP Communication
- Connection-Oriented vs Connectionless Protocols
- Sending and Receiving Data using Python

---

# Disclaimer

This project is intended for educational purposes and should be executed only on systems and networks where you have authorization.