from imports import *

def upload(sock):
    client_id = input("    client id > ")
    filepath = input("    file path > ")
    key = input("    key > ")
    file = open(filepath, "rb").read()
    encrypted_file = Crypto.encrypt(file, Crypto.hash(key.encode()))
    request = {
        "method": "upload",
        "client_id": Crypto.hash_hex(client_id.encode()),
        "key": Crypto.hash_hex(key.encode()),
        "data": base64.b64encode(encrypted_file).decode()
    }
    with open("debug.txt", "w") as d:
        d.write(json.dumps(request))
    Websocket.send(sock, request)
    response = Websocket.revieve(sock)
    print("    The file id: " + response["file_id"])

def download(sock):
    client_id = input("    client id > ")
    file_id = input("    file id > ")
    key = input("    key > ")
    output_path = input("    output path > ")
    request = {
        "method": "download",
        "client_id": Crypto.hash_hex(client_id.encode()),
        "key": Crypto.hash_hex(key.encode()),
        "file_id": file_id
    }
    Websocket.send(sock, request)
    response = Websocket.revieve(sock)
    decrypted_data = Crypto.decrypt(base64.b64decode(response["data"]), Crypto.hash(key.encode()))
    with open(output_path, "wb") as output:
        output.write(decrypted_data)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    sock.connect(("127.0.0.1", 1337))
    sock.send(Crypto.save_rsa(rsa_keys.public))
    rsa_keys.server_public = Crypto.load_rsa_public(sock.recv(int(1e+6)).decode())

    menu = """
    [1] Upload [2] Download
"""
    print(menu)
    choice = input("    > ")
    if choice == "1":
        upload(sock)
    elif choice == "2":
        download(sock)

main()