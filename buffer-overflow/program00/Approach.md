## My Approach
If i can find the address of the print_flag, then i can be able to direct the program to execute it. By using this syntax: `print print_flag`, i was able to find the address as `0x80491d5`.

Now, this is where the math comes in to be able to craft the payload. i already have my offset(through the `pattern.py` script), which will take us just before the return address.

To overwrite the return address, i have to first convert the address of `print_flag` function,
to `little-endian` bytes since i have compiled the program as a 32-bit. Which is basically x86. 

The payload is crafted as `payload.py`

### Key Terms:
- `little-endian`: a byte ordering where the least significant byte of a multi-byte data value is stored at the lowest memory address, while the most significant byte is stored at the highest memory address.