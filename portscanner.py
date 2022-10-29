<pre style="background: rgb(238, 238, 238); border: 1px dashed rgb(153, 153, 153); line-height: 14px; outline: 0px; overflow: auto; padding: 5px; vertical-align: baseline; width: 592.016px;"><code style="background-attachment: initial; background-clip: initial; background-color: #f1f1f1; background-origin: initial; background-position: 0% 0%; background-repeat: no-repeat; background-size: initial; background: url("images/code.gif") left top no-repeat rgb(241, 241, 241); border-color: rgb(221, 221, 221); border-image: initial; border-style: dotted dotted dotted solid; border-width: 1px 1px 1px 10px; display: block; margin: 0px; outline: 0px; padding: 20px; vertical-align: baseline;">import socket

site = input("Tarancak siteyi giriniz : ")
target = socket.gethostbyname(site)

print("-" * 50)
print("Hedef taranıyor: " + target)
print("-" * 50)

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        
        if result == 0:
            print("Port {} açık.".format(port))
        s.close()
        
except Exception as e:
    print("Hata!", e)
