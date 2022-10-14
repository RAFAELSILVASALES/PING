import socket

respostar = "S"
while respostar == "S":
    url = input("\n Digite o enderço do Site:")
    ip = socket.gethostbyname(url)
    print("O endereço ip da url é:", ip)
    respostar = input("\n Digite |S| para continuar:").upper()
