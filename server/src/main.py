from imports import *

def client_thread(sock):
    rsa_keys.client_public = Crypto.load_rsa_public(sock.recv(int(1e+6)).decode())
    sock.send(Crypto.save_rsa(rsa_keys.public))
    request = Websocket.revieve(sock)
    if request["method"] == "upload":
        file_id = Utility.generate_id()
        Db.add(request, file_id)
        Websocket.send(sock, {"file_id": file_id})
    if request["method"] == "download":
        data = Db.find(request)
        Websocket.send(sock, data)

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server.bind(("", 1337))
    server.listen()
    print("started")

    while True:
        client, address = server.accept()
        threading.Thread(target=client_thread, args=(client, )).start()

main()