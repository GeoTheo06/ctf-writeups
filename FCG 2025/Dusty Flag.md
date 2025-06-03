I found this old Software in my basement. I can't seem to be able to run it though and the License Key is all but washed away. Could you help your old man out ? Flag is of the form FCTF{...} 
```
┌──(gio㉿kali)-[~/Downloads] 
└─$ file LICENSE.EXE 
LICENSE.EXE: MS-DOS executable, MZ for MS-DOS
```

opening this MS-DOS file in Ghidra will only show the stub. To see the actual code i had to firsts unpack the exe with upx: 
```
upx -d LICENSE.EXE -o LICENSE_unpacked.EXE
```
when i opened that in ghidra, i found the strings:
```
       11eb:0194 45 6e 74        ds         "Enter your dusty old license: "
                 65 72 20 
                 79 6f 75 
       11eb:01b3 25              ??         25h    %
       11eb:01b4 73              ??         73h    s
       11eb:01b5 00              ??         00h
       11eb:01b6 43              ??         43h    C
       11eb:01b7 45              ??         45h    E
       11eb:01b8 53              ??         53h    S
       11eb:01b9 4e              ??         4Eh    N
       11eb:01ba 72              ??         72h    r
       11eb:01bb 5d              ??         5Dh    ]
       11eb:01bc 63              ??         63h    c
       11eb:01bd 75              ??         75h    u
       11eb:01be 5a              ??         5Ah    Z
       11eb:01bf 61              ??         61h    a
       11eb:01c0 7a              ??         7Ah    z
       11eb:01c1 7c              ??         7Ch    |
       11eb:01c2 75              ??         75h    u
       11eb:01c3 4b              ??         4Bh    K
       11eb:01c4 7c              ??         7Ch    |
       11eb:01c5 61              ??         61h    a
       11eb:01c6 51              ??         51h    Q
       11eb:01c7 79              ??         79h    y
       11eb:01c8 43              ??         43h    C
       11eb:01c9 70              ??         70h    p
       11eb:01ca 70              ??         70h    p
       11eb:01cb 69              ??         69h    i
       11eb:01cc 66              ??         66h    f
       11eb:01cd 00              ??         00h
       11eb:01ce 43 6f 72        ds         "Correct License\n"
                 72 65 63 
                 74 20 4c 
       11eb:01df 49 6e 63        ds         "Incorrect License\n"
                 6f 72 72 
                 65 63 74 

```

obviously the license is the random letters starting at 0x01b6 but xored or encrypted somehow. We will use this string later. 

Looking at the strings I noticed that there are no external references which is probably because of the dos file. Instead searching of how to configure ghidra to show them somehow, I opened Search -> Memory... and inputted the address 0x01ce to find the logic that checks if the input equals license.

with this search i found the code i need. in ghidra's pseudo c it looks like this:
```

undefined2 __cdecl16near FUN_1000_0238(void)

{
  int iVar1;
  int iVar2;
  undefined2 unaff_SS;
  byte local_24 [32];
  int local_4;
  
  if (&stack0xffd8 <= DAT_11eb_009e) {
    FUN_1000_1e42(0x1000);
  }
  local_4 = FUN_1000_01fa();
  FUN_1000_0e93(0x194);
  FUN_1000_1733(0x1b3,local_24);
  iVar1 = FUN_1000_0d38(local_24);
  for (iVar2 = 0; iVar2 < iVar1; iVar2 = iVar2 + 1) {
    local_24[iVar2] = local_24[iVar2] ^ (byte)local_4;
    local_4 = local_4 + 1;
  }
  iVar1 = FUN_1000_0d55(0x1b6,local_24);
  if (iVar1 == 0) {
    FUN_1000_0e93(0x1ce);
  }
  else {
    FUN_1000_0e93(0x1df);
  }
  return 0;
}

```
or my version:
```
undefined2 __cdecl16near FUN_1000_0238(void)
{
    // local_4 will hold our running XOR key (a single byte, extended to a word),
    // and local_24[ ] is a 32-byte buffer on the stack into which the user’s input is read.
    byte  local_24[32];
    int   local_4;        // will hold the first XOR key (16-bit, but only low byte is used)
    int   length, i;
    
	//useless
    if (&stack0xffd8 <= DAT_11eb_009e) {
        FUN_1000_1e42(0x1000);
    }

    // Step 1: Get the initial XOR key and store it in local_4.
    // FUN_1000_01fa() returns a 16-bit value; only low byte is used below.
    local_4 = FUN_1000_01fa();

    // Step 2: Print the prompt at offset 0x194
    // 0x194 points to "Enter your dusty old license: " 
    FUN_1000_0e93(0x0194);

    // Step 3: Read one line of input into stack buffer local_24
    FUN_1000_1733(0x01B3, local_24);

    // FUN_1000_0D38(local_24) returns strlen(local_24) into AX.
    length = FUN_1000_0D38(local_24);

    // Step 5: For each character of the user’s input, do: 
    // buffer[i] = buffer[i] XOR (current_key);
    // current_key++;
    for (i = 0; i < length; i++) {
        local_24[i] = local_24[i] ^ (byte)local_4;
        local_4 = local_4 + 1;
    }

    // Step 6: Compare that transformed buffer against the license key (scrambled) at offset 0x1B6.
    // If the comparison returns zero, it is a match.
    i = FUN_1000_0D55(0x01B6, local_24);
     
    if (i == 0) {
        FUN_1000_0e93(0x01CE);   // prints "Correct License\n"
    } else {
        FUN_1000_0e93(0x01DF);   // prints "Incorrect License\n"
    }

    return 0;
}
```

so the string in 0x01b6 (the scrambled license) is in hex: 0x43, 0x45, 0x53, 0x4E, 0x72, 0x5D, 0x63, 0x75, 0x5A, 0x61, 0x7A, 0x7C, 0x75, 0x4B, 0x7C, 0x61, 0x51, 0x79, 0x43, 0x70, 0x70, 0x69, 0x66

We know from the description that the flag is of the form FCTF{C0 ... Cn}
and we know from the decompiled code that:
C0  ^ (initial_key + 0)  ==  scrambled_license[0]

Since we know that the first character is F and the first element in the scrambled_license array is 0x43, we can find the initial key:
initial_key = c0 ^ scrambled_license = 0x46  ^  0x43  =  0x05

now that we have the starting initial_key value , we can easily find the rest letters of the license:
C1  ^ (initial_key + 1)  =  scrambled_license[1]
C1 = 0x45 ^ 0x06 = 0x43 = 'C'

doing this for all the elements in scrambled_license, we get the flag:
FCTF{WhyWouldYouDoThis}