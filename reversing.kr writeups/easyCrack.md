![[Pasted image 20250322225834.png]]
![[Pasted image 20250322225839.png]]

## **Analysis**

The executable contains a function `FUN_00401080` that handles password validation. Here's the breakdown of the decompiled code:

### **Key Variables**

1. `hasToBe'E'`: A character variable that must be set to `'E'`.
    
2. `local_63`: Represents the second character of the input, which must be `'a'`.
    
3. `cStack_62`: Represents the third and fourth characters, which are compared to the string `"5y"`.
    
4. `97ElementsArray`: An array that stores the remaining characters of the input, which are compared to `"R3versing"`.
    

### **Password Validation Logic**

1. **First Character (`'E'`):**
    
    - The code explicitly checks if the first character of the input is `'E'` by comparing `hasToBe'E'` to `'E'`.
2. **Second Character (`'a'`):**

    - The code explicitly checks if the second character (`local_63`) is `'a'`:
        if (local_63 == 'a')
        
3. **Third and Fourth Characters (`'5'` and `'y'`):**
    
    - The code uses `strncmp` to compare the third and fourth characters (`cStack_62`) with the string `"5y"` stored at `DAT_00406078`:
        hasToBe0 = _strncmp(&cStack_62, &DAT_00406078, 2);
        
4. **Remaining Characters (`'R3versing'`):**
    
    - A loop compares the input starting from the fifth character against the string `"AGR3versing"` found inside `s_AGR3versing_0040606a`. However, the first two characters (`"AG"`) are skipped due to an initial pointer increment in the loop. Thus, the input must match `"R3versing"` starting from the fifth character.

Thus, the password is: **`Ea5yR3versing`**.