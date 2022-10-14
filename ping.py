import scapy.all as scapy
import requests
ip = "192.168.10.60"

resposta = scapy.sr1(scapy.IP(dst=ip) / scapy.ICMP(), timeout=3)

if resposta is not None:
    print(resposta)
    print(resposta.src)
    print(resposta.dst)

else:
    print("Host inacessível")
    token = ""
    id_chat = ""
    message = ""
    url = f"https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={message}"

    requests.get(url)
