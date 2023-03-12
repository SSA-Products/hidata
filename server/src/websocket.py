from imports import *

# idk if i can call it a websocket thing but it uses json with sockets so idk...

class Websocket:

    def send(socket, data):
        data = json.dumps(data).encode()
        data = Crypto.encrypt_rsa(data, rsa_keys.client_public)
        socket.send(data)

    def revieve(socket):
        data = socket.recv(int(1e+8))
        data = Crypto.decrypt_rsa(data, rsa_keys.private)
        try:
            data = data.decode("utf-8")
        except:
            print("Can't decode data from recieve")
        data = json.loads(data)
        return data