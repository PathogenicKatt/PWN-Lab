from pwn import *

#print(cyclic(100))
# The output of this code will be a pattern of 100 characters that can be used to identify the offset in a buffer overflow attack.

print(cyclic_find(0x61616174)) #this will give us the offset