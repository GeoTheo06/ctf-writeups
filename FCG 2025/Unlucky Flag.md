

```
┌──(gio㉿kali)-[~/Desktop] └─$ file main main: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), BuildID[sha1]=17af4099afd1010aca2cf3b0f2445ca91810c7b9, for GNU/Linux 4.4.0, dynamically linked, interpreter /lib/ld-linux.so.2, no section header 
```

by decompiling the program in ghidra, we see
assembly view:
```
                             **************************************************************
                             *                          FUNCTION                          *
                             **************************************************************
                             undefined FUN_00011070()
             undefined         <UNASSIGNED>   <RETURN>
             undefined4        Stack[0x0]:4   local_res0                              XREF[1]:     00011077(R)  
             undefined1        Stack[-0x18]:1 local_18                                XREF[1]:     0001118e(*)  
             undefined4        Stack[-0x24]:4 local_24                                XREF[2]:     000110a1(W), 
                                                                                                   00011182(R)  
             undefined1        Stack[-0x3f]:1 local_3f                                XREF[2]:     000110eb(*), 
                                                                                                   0001110a(*)  
             undefined1        Stack[-0x44]:1 local_44                                XREF[1]:     000110a4(*)  
             undefined4        Stack[-0x54]:4 local_54                                XREF[2]:     000110f5(W), 
                                                                                                   00011100(R)  
             undefined4        Stack[-0x58]:4 local_58                                XREF[2]:     000110ee(W), 
                                                                                                   0001113f(R)  
             undefined4        Stack[-0x5c]:4 local_5c                                XREF[4]:     0001108f(W), 
                                                                                                   00011156(R), 
                                                                                                   0001116d(R), 
                                                                                                   0001119c(R)  
             undefined4        Stack[-0x70]:4 local_70                                XREF[1]:     000110ae(*)  
                             FUN_00011070                                    XREF[2]:     entry:000111dc(*), 00013fec(*)  
        00011070 8d 4c 24 04     LEA        ECX=>Stack[0x4],[ESP + 0x4]
        00011074 83 e4 f0        AND        ESP,0xfffffff0
        00011077 ff 71 fc        PUSH       dword ptr [ECX + local_res0]
        0001107a 55              PUSH       EBP
        0001107b 89 e5           MOV        EBP,ESP
        0001107d 57              PUSH       EDI
        0001107e e8 41 03        CALL       FUN_000113c4                                     undefined FUN_000113c4()
                 00 00
        00011083 81 c7 71        ADD        EDI,0x2f71
                 2f 00 00
        00011089 56              PUSH       ESI
        0001108a 53              PUSH       EBX
        0001108b 51              PUSH       ECX
        0001108c 83 ec 50        SUB        ESP,0x50
        0001108f 89 7d ac        MOV        dword ptr [EBP + local_5c],EDI
        00011092 8d 87 14        LEA        EAX,[EDI + 0xffffe014]
                 e0 ff ff
        00011098 89 fb           MOV        EBX,EDI
        0001109a 65 8b 35        MOV        ESI,dword ptr GS:[0x14]
                 14 00 00 00
        000110a1 89 75 e4        MOV        dword ptr [EBP + local_24],ESI
        000110a4 8d 75 c4        LEA        ESI=>local_44,[EBP + -0x3c]
        000110a7 56              PUSH       ESI
        000110a8 50              PUSH       EAX
        000110a9 e8 b2 ff        CALL       FUN_00011060                                     undefined FUN_00011060()
                 ff ff
        000110ae 89 34 24        MOV        dword ptr [ESP]=>local_70,ESI
        000110b1 e8 9a ff        CALL       FUN_00011050                                     undefined FUN_00011050()
                 ff ff
        000110b6 83 c4 10        ADD        ESP,0x10
        000110b9 8d 58 fa        LEA        EBX,[EAX + -0x6]
        000110bc b8 56 55        MOV        EAX,0x55555556
                 55 55
        000110c1 f7 eb           IMUL       EBX
        000110c3 89 d8           MOV        EAX,EBX
        000110c5 c1 f8 1f        SAR        EAX,0x1f
        000110c8 29 c2           SUB        EDX,EAX
        000110ca 89 d8           MOV        EAX,EBX
        000110cc 8d 14 52        LEA        EDX,[EDX + EDX*0x2]
        000110cf 29 d0           SUB        EAX,EDX
        000110d1 89 da           MOV        EDX,EBX
        000110d3 83 e2 01        AND        EDX,0x1
        000110d6 09 d0           OR         EAX,EDX
        000110d8 0f 85 8f        JNZ        LAB_0001116d
                 00 00 00
        000110de 83 fb 0b        CMP        EBX,0xb
        000110e1 0f 8f 86        JG         LAB_0001116d
                 00 00 00
        000110e7 85 db           TEST       EBX,EBX
        000110e9 7e 6b           JLE        LAB_00011156
        000110eb 8d 45 c9        LEA        EAX=>local_3f,[EBP + -0x37]
        000110ee 89 5d b0        MOV        dword ptr [EBP + local_58],EBX
        000110f1 31 ff           XOR        EDI,EDI
        000110f3 31 f6           XOR        ESI,ESI
        000110f5 89 45 b4        MOV        dword ptr [EBP + local_54],EAX
        000110f8 2e 8d b4        LEA        ESI,[ESI]
                 26 00 00 
                 00 00
                             LAB_00011100                                    XREF[1]:     00011142(j)  
        00011100 8b 45 b4        MOV        EAX,dword ptr [EBP + local_54]
        00011103 89 f1           MOV        ECX,ESI
        00011105 ba 0d 00        MOV        EDX,0xd
                 00 00
        0001110a 0f be 1c 30     MOVSX      EBX,byte ptr [EAX + ESI*0x1]=>local_3f
        0001110e 89 f0           MOV        EAX,ESI
        00011110 83 e1 01        AND        ECX,0x1
        00011113 75 1b           JNZ        LAB_00011130
        00011115 d1 f8           SAR        EAX,0x1
        00011117 b9 01 00        MOV        ECX,0x1
                 00 00
        0001111c 74 19           JZ         LAB_00011137
        0001111e 66 90           NOP
                             LAB_00011120                                    XREF[1]:     00011135(j)  
        00011120 0f af d2        IMUL       EDX,EDX
        00011123 a8 01           TEST       AL,0x1
        00011125 75 09           JNZ        LAB_00011130
                             LAB_00011127                                    XREF[1]:     0001112e(j)  
        00011127 d1 f8           SAR        EAX,0x1
        00011129 0f af d2        IMUL       EDX,EDX
        0001112c a8 01           TEST       AL,0x1
        0001112e 74 f7           JZ         LAB_00011127
                             LAB_00011130                                    XREF[2]:     00011113(j), 00011125(j)  
        00011130 0f af ca        IMUL       ECX,EDX
        00011133 d1 f8           SAR        EAX,0x1
        00011135 75 e9           JNZ        LAB_00011120
                             LAB_00011137                                    XREF[1]:     0001111c(j)  
        00011137 0f af d9        IMUL       EBX,ECX
        0001113a 83 c6 01        ADD        ESI,0x1
        0001113d 01 df           ADD        EDI,EBX
        0001113f 39 75 b0        CMP        dword ptr [EBP + local_58],ESI
        00011142 75 bc           JNZ        LAB_00011100
        00011144 89 f8           MOV        EAX,EDI
        00011146 b9 ff ff        MOV        ECX,0x7fffffff
                 ff 7f
        0001114b 99              CDQ
        0001114c f7 f9           IDIV       ECX
        0001114e 81 fa b8        CMP        EDX,0x1f717b8
                 17 f7 01
        00011154 74 46           JZ         LAB_0001119c
                             LAB_00011156                                    XREF[1]:     000110e9(j)  
        00011156 8b 5d ac        MOV        EBX,dword ptr [EBP + local_5c]
        00011159 83 ec 0c        SUB        ESP,0xc
        0001115c 8d 83 29        LEA        EAX,[EBX + 0xffffe029]
                 e0 ff ff
        00011162 50              PUSH       EAX
        00011163 e8 d8 fe        CALL       FUN_00011040                                     undefined FUN_00011040()
                 ff ff
        00011168 83 c4 10        ADD        ESP,0x10
        0001116b eb 15           JMP        LAB_00011182
                             LAB_0001116d                                    XREF[2]:     000110d8(j), 000110e1(j)  
        0001116d 8b 5d ac        MOV        EBX,dword ptr [EBP + local_5c]
        00011170 83 ec 0c        SUB        ESP,0xc
        00011173 8d 83 17        LEA        EAX,[EBX + 0xffffe017]
                 e0 ff ff
        00011179 50              PUSH       EAX
        0001117a e8 c1 fe        CALL       FUN_00011040                                     undefined FUN_00011040()
                 ff ff
        0001117f 83 c4 10        ADD        ESP,0x10
                             LAB_00011182                                    XREF[2]:     0001116b(j), 000111b1(j)  
        00011182 8b 45 e4        MOV        EAX,dword ptr [EBP + local_24]
        00011185 65 2b 05        SUB        EAX,dword ptr GS:[0x14]
                 14 00 00 00
        0001118c 75 25           JNZ        LAB_000111b3
        0001118e 8d 65 f0        LEA        ESP=>local_18,[EBP + -0x10]
        00011191 31 c0           XOR        EAX,EAX
        00011193 59              POP        ECX
        00011194 5b              POP        EBX
        00011195 5e              POP        ESI
        00011196 5f              POP        EDI
        00011197 5d              POP        EBP
        00011198 8d 61 fc        LEA        ESP,[ECX + -0x4]
        0001119b c3              RET
                             LAB_0001119c                                    XREF[1]:     00011154(j)  
        0001119c 8b 5d ac        MOV        EBX,dword ptr [EBP + local_5c]
        0001119f 83 ec 0c        SUB        ESP,0xc
        000111a2 8d 83 3a        LEA        EAX,[EBX + 0xffffe03a]
                 e0 ff ff
        000111a8 50              PUSH       EAX
        000111a9 e8 92 fe        CALL       FUN_00011040                                     undefined FUN_00011040()
                 ff ff
        000111ae 83 c4 10        ADD        ESP,0x10
        000111b1 eb cf           JMP        LAB_00011182
                             LAB_000111b3                                    XREF[1]:     0001118c(j)  
        000111b3 e8 18 02        CALL       FUN_000113d0                                     undefined FUN_000113d0()
                 00 00
        000111b8 66 90           NOP
        000111ba 66 90           NOP
        000111bc 66 90           NOP
        000111be 66 90           NOP

```
decompiled view in c:
```
/* WARNING: Function: __i686.get_pc_thunk.bx replaced with injection: get_pc_thunk_bx */

undefined4 FUN_00011070(void)

{
  uint uVar1;
  char *pcVar2;
  int iVar3;
  uint uVar4;
  uint uVar5;
  int iVar6;
  uint uVar7;
  int unaff_EDI;
  int in_GS_OFFSET;
  undefined8 uVar8;
  undefined4 uStack_64;
  undefined4 uStack_60;
  int local_5c;
  uint local_58;
  char *local_54;
  undefined1 local_44 [5];
  char local_3f [27];
  int local_24;
  
  FUN_000113c4();
  local_5c = unaff_EDI + 0x2f71;
  local_24 = *(int *)(in_GS_OFFSET + 0x14);
  FUN_00011060(unaff_EDI + 0xf85,local_44);
  iVar3 = FUN_00011050(local_44);
  uVar1 = iVar3 - 6;
  if ((uVar1 == ((int)uVar1 / 3) * 3 && (uVar1 & 1) == 0) && ((int)uVar1 < 0xc)) {
    if (0 < (int)uVar1) {
      local_54 = local_3f;
      iVar3 = 0;
      uVar7 = 0;
      do {
        iVar6 = 0xd;
        pcVar2 = local_54 + uVar7;
        uVar5 = uVar7 & 1;
        uVar4 = uVar7;
        if (uVar5 != 0) goto LAB_00011130;
        uVar5 = 1;
        while (uVar4 = (int)uVar4 >> 1, uVar4 != 0) {
          iVar6 = iVar6 * iVar6;
          for (; (uVar4 & 1) == 0; uVar4 = (int)uVar4 >> 1) {
            iVar6 = iVar6 * iVar6;
          }
LAB_00011130:
          uVar5 = uVar5 * iVar6;
        }
        uVar7 = uVar7 + 1;
        iVar3 = iVar3 + (int)*pcVar2 * uVar5;
      } while (uVar1 != uVar7);
      local_58 = uVar1;
      if (iVar3 % 0x7fffffff == 0x1f717b8) {
        FUN_00011040(local_5c + -0x1fc6);
        goto LAB_00011182;
      }
    }
    FUN_00011040(local_5c + -0x1fd7);
  }
  else {
    FUN_00011040(local_5c + -0x1fe9);
  }
LAB_00011182:
  if (local_24 != *(int *)(in_GS_OFFSET + 0x14)) {
    uStack_64 = 0x111b8;
    uVar8 = FUN_000113d0();
    uStack_64 = (undefined4)uVar8;
    FUN_00011030(PTR_FUN_00013fec,uStack_60,&local_5c,0,0,(int)((ulonglong)uVar8 >> 0x20),&uStack_64
                );
    do {
                    /* WARNING: Do nothing block with infinite loop */
    } while( true );
  }
  return 0;
} 

```

by following the offsets and the functions i found that the output function is called with the winning parameters when ran with the offset -0x1fc6.

a simplified version of the code would be:
```
  int length = strlen(input);
    int uVar1 = length - 6;
    if (uVar1 == (uVar1/3)*3 && (uVar1 & 1) == 0 && uVar1 < 12 && uVar1 > 0) {
        // i.e. uVar1 must be 6

        int sum = 0;
        for (int i = 0; i < uVar1; i++) {
            // weight = 13^i
            int weight = 1;
            int e = i;
            int base = 13;
            while (e > 0) {
                if (e & 1)   weight *= base;
                base *= base;
                e >>= 1;
            }
            sum += (int)(unsigned char)( inner[i] ) * weight;
        }

        // For the check we can skip the remainder completely because sum < 2^31−1 (2.1e9)
        if (sum == 0x01F717B8) {
            success();
        } else {
            wrong_password();
        }
    } else {
        wrong_length();
    }
```

this check 
``` 
uVar1 == (uVar1/3)*3     // i.e. "divisible by 3"
&& (uVar1 & 1) == 0       // i.e. "even"
&& uVar1 < 12
&& uVar1 > 0;
```
means that uVar1 must be 6 since its the only possible number with these restrictions. Thus we deduce that strlen(input) - 6 == 6 <=> strlen(input) == 12

the format of the flag is FCTF{} which is 6 characters so we need to find the remaining inner 6 characters.

after the length check, the program does:
```
weight = 13^i
sum += (int)(inner[i]) * weight;

if ( (sum % 0x7FFFFFFF) == 0x01F717B8 ) print flag
else wrong
```

thus to find the inner 6 characters we need to find inner[i] for i {0...6} such that
 $inner[0]*13^0 + inner[1]*13^1 + inner[2]*13^2  + inner[3]*13^3 + inner[4]*13^4 + inner[5]*13^5 = 0x01F717B8  (= 32 970 680).$
 so I created a python script that uses meet-in-the-middle approach to cut the 26^6 search down to 2×26^3

```
import itertools

# 1) Define the target sum from the binary (hex 0x01F717B8).
target = 0x01F717B8

# 2) Precompute powers of 13^i for i=0..5 so we can multiply quickly.
powers = [13 ** i for i in range(6)]  # [1, 13, 169, 2197, 28561, 371293]

# 3) Choose the character set for each position.  Here we restrict to uppercase A–Z.
chars = [chr(c) for c in range(ord('A'), ord('Z') + 1)]  # ['A', 'B', ..., 'Z']

# 4) Build a dictionary for the "first half" (positions 0,1,2):
#    key = (ord(c0)*13^0 + ord(c1)*13^1 + ord(c2)*13^2)
#    value = list of all 3-letter prefixes that produce that partial sum.
first_half = {}
for c0, c1, c2 in itertools.product(chars, repeat=3):
    partial_sum = (ord(c0) * powers[0]
                 + ord(c1) * powers[1]
                 + ord(c2) * powers[2])
    first_half.setdefault(partial_sum, []).append(c0 + c1 + c2)

# 5) Now iterate over all 3-letter triples for positions 3,4,5:
solutions = []
for c3, c4, c5 in itertools.product(chars, repeat=3):
    partial_sum_high = (ord(c3) * powers[3]
                      + ord(c4) * powers[4]
                      + ord(c5) * powers[5])
    needed = target - partial_sum_high
    
    # If 'needed' is in our first_half dictionary, each prefix there
    # combines with (c3,c4,c5) to form a full 6-byte solution.
    if needed in first_half:
        for prefix in first_half[needed]:
            solutions.append(prefix + c3 + c4 + c5)

# 6) Print out any 6-letter "inner" strings that work.
print(solutions)
```
and the results were:
```
['CFWLES', 'CSVLES', 'PEWLES', 'PRVLES', 'CFWLRR', 'CSVLRR', 'PEWLRR', 'PRVLRR', 'CFJMES', 'CSIMES', 'PEJMES', 'PRIMES', 'CFJMRR', 'CSIMRR', 'PEJMRR', 'PRIMRR', 'CFWYDS', 'CSVYDS', 'PEWYDS', 'PRVYDS', 'CFWYQR', 'CSVYQR', 'PEWYQR', 'PRVYQR', 'CFJZDS', 'CSIZDS', 'PEJZDS', 'PRIZDS', 'CFJZQR', 'CSIZQR', 'PEJZQR', 'PRIZQR']
```

where obviously PRIMES is the correct one.

As a result the flag FCTF{PRIMES} satisfies all requirements