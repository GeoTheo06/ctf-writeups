```

/* WARNING: Function: _guard_dispatch_icall replaced with injection: guard_dispatch_icall */

undefined8 FUN_140018ee0(int param_1,undefined8 *param_2)

{
  byte bVar1;
  undefined8 uVar2;
  size_t sVar3;
  byte local_28;
  int hasToBe1188;
  int local_20;
  int local_18;
  
  if (param_1 < 2) {
    printf(s_Usage:_%s_<flag>_140094668,*param_2);
    uVar2 = 1;
  }
  else {
    sVar3 = strlen((char *)param_2[1]);
    if (sVar3 == 0x15) {
      hasToBe1188 = 0x24;
      for (local_20 = 0; local_20 < 0x15; local_20 = local_20 + 1) {
        local_28 = *(byte *)(param_2[1] + (longlong)local_20) ^ (&DAT_140092000)[local_20];
        for (local_18 = 0; local_18 < 4; local_18 = local_18 + 1) {
          bVar1 = local_28 & 3;
          if ((local_28 & 3) == 0) {
            hasToBe1188 = hasToBe1188 + -0x23;
          }
          else if (bVar1 == 1) {
            hasToBe1188 = hasToBe1188 + 1;
          }
          else if (bVar1 == 2) {
            hasToBe1188 = hasToBe1188 + 0x23;
          }
          else if (bVar1 == 3) {
            hasToBe1188 = hasToBe1188 + -1;
          }
          (*(code *)(&PTR_LAB_140092020)[hasToBe1188])();
          local_28 = local_28 >> 2;
        }
      }
      if (hasToBe1188 == 0x4a4) {
        printf(s_Successfully_escaped!_140094698);
        uVar2 = 0;
      }
      else {
        printf(s_You_got_caught..._1400946b0);
        uVar2 = 1;
      }
    }
    else {
      printf(s_You_got_caught..._140094680);
      uVar2 = 1;
    }
  }
  return uVar2;
}
```