import socket
import json
import hashlib
import random
import rsa
import threading
import base64
from Crypto.Cipher import AES

class rsa_keys:
    public, private = rsa.newkeys(2048)
    server_public = b""

from crypto import Crypto
from websocket import Websocket