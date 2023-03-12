# In developement !

# Hidata encryption system

## Communication
RSA encryption, key exchange at the beginning of the commucation (using sockets) and then use websockets to send and recieve data
## File upload and download
### Client
* Upload
```py
data = bytes
key = str
client_id = str

encrypted_data = encrypt(data, key)

request = {
	"client_id": hash(client_id),
	"key": hash(key),
	"data": encrypted_data
}

response = {
	"file_id": file_id
}
```
* Download
```py
client_id = str
file_id = str
key = str

request = {
	"client_id": hash(client_id),
	"key": hash(key),
	"file_id" = file_id
}

response = {
	"data": encrypted_data
}

data = decrypt(response["data"], key)
```
### Server
* Upload (get)
```py
response = {
	"client_id" = hash
	"key" = hash
	"data" = data
}

file_id = generate_id()
db.add(requested["client_id"], requested["data"], requested["key"], file_id)

request = {
	"file_id": file_id
}
```
* Download
```py
response = {
	"client_id" = hash,
	"key" = hash,
	"file_id" = file_id
}

request = {
	"data" = db.find(response["client_id"], response["key"], response["file_id"])
}
```
