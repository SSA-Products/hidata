from imports import *

class Utility:

    def random_bytes(length):
        rbytes = b""
        for n in range(length):
            rbytes += random.randbytes(1)
        return rbytes
    
    def generate_id():
        rbytes = b""
        for n in range(32):
            rbytes += random.randbytes(1)
        return rbytes.hex()