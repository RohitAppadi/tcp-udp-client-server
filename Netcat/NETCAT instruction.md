# TCP & UDP Client-Server Communication using Netcat (Windows)

This guide demonstrates how to establish **TCP** and **UDP** client-server communication using **Ncat (Netcat)** on **Windows**.

> **Note**
> This guide is written specifically for **Windows**, where the executable is **`ncat`**.
>
> On Linux and macOS, Netcat is usually installed as **`nc`**, and the installation process varies depending on your distribution.

---

# Prerequisites

- Windows 10 or Windows 11
- PowerShell or Command Prompt
- Ncat (comes with the Nmap package)

---

# Installing Ncat on Windows

## Step 1

Download **Nmap** from:

https://nmap.org/download.html

## Step 2

Run the installer.

During installation, ensure **Ncat** is selected (it is enabled by default).

## Step 3

Open a new PowerShell window and verify the installation.

```powershell
ncat --version
```

If installed correctly, you'll see output similar to:

```
Ncat: Version 7.xx
```

---

# Linux Users

This repository focuses on **Windows**.

Linux users typically install Netcat differently depending on the distribution.

Examples:

Ubuntu/Debian

```bash
sudo apt install netcat-openbsd
```

or

```bash
sudo apt install netcat
```

Fedora

```bash
sudo dnf install nmap-ncat
```

Arch Linux

```bash
sudo pacman -S gnu-netcat
```

After installation, Linux users generally use:

```bash
nc
```

instead of

```bash
ncat
```

---

# Checking Installation

Run

```powershell
ncat --help
```

If the help menu appears, everything is installed correctly.

---

# Basic Parameters

| Parameter | Description |
|-----------|-------------|
| `-l` | Listen for incoming connections |
| `-u` | Use UDP instead of TCP |
| `-v` | Verbose mode |
| `-p` | Specify local source port |

---

# TCP Communication

## Step 1 — Open Two Terminals

Open **two** PowerShell windows.

Terminal 1

```
Server
```

Terminal 2

```
Client
```

---

## Step 2 — Start the Server

Run

```powershell
ncat -l 2399
```

The terminal will wait for an incoming connection.

Do **not** close this terminal.

---

## Step 3 — Connect as the Client

Open the second terminal.

Run

```powershell
ncat localhost 2399
```

If everything is correct, the connection will be established.

---

## Step 4 — Exchange Messages

Simply start typing.

Anything typed on the **client** appears on the **server**.

Likewise, anything typed on the **server** appears on the **client**.

Example

Server

```
Hello!!
I am Rohit
Testing TCP connection
```

Client

```
Hello!!
I am Rohit
Testing TCP connection
```

---

# UDP Communication

Unlike TCP, UDP is **connectionless**.

The only difference is adding the `-u` parameter.

---

## Step 1 — Start the UDP Server

```powershell
ncat -u -l 2399
```

---

## Step 2 — Connect the UDP Client

Open another terminal.

Run

```powershell
ncat -u localhost 2399
```

---

## Step 3 — Send Messages

Begin typing.

Messages typed on one terminal should appear on the other.

---

## Step 4 — Verify the UDP Connection

Open a **third** PowerShell window.

Run

```powershell
netstat -an | Select-String 2399
```

If the connection exists, you should see entries similar to

```
UDP    [::]:2399
UDP    [::1]:58256
```

---

# Common Errors

## 'ncat' is not recognized

```
'ncat' is not recognized...
```

### Cause

Ncat is not installed or not added to your system PATH.

### Solution

- Install Nmap.
- Restart PowerShell.
- Verify using

```powershell
ncat --version
```

---

## Connection Refused

```
Connection refused
```

### Cause

The server is not running.

### Solution

Always start the **server first**.

---

## Port Already in Use

```
Address already in use
```

### Cause

Another application is already using port **2399**.

### Solution

- Close the previous process.
- Or choose another port.

Example

```powershell
ncat -l 3000
```

Then connect using

```powershell
ncat localhost 3000
```

---

## Firewall Prompt

The first time you run Ncat, Windows Firewall may ask for permission.

Click

```
Allow Access
```

for **Private Networks**.

---

# Project Structure

```
Netcat/
│
├── README.md
├── screenshots/
│
└── examples/
```

---

# Learning Outcomes

By completing this practical, you will understand:

- Client-Server Architecture
- TCP Communication
- UDP Communication
- Socket Listening
- Port Communication
- Localhost Networking
- Basic Network Troubleshooting
- Netcat Command Usage

---

# References

- Nmap Official Documentation: https://nmap.org/
- Netcat Documentation: https://nmap.org/ncat/

---

# Disclaimer

This project is intended for educational purposes only.

Run these commands only on systems and networks where you have authorization.