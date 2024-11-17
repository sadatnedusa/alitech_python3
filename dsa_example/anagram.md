**Anagram Checker**

When we take the characters from a word, phrase, or string and rearrange them, we may end up with a scrambled version of the original text that contains the same letters.

For example, the letters in the string `"Silent Night"` can be rearranged to form `"Listen Thing"`. To identify if two strings are valid scrambled versions of each other, they must follow these rules:
- Both strings must contain the **same number of the same letters**, regardless of order.
- The comparison ignores **spaces, punctuation, and capitalization**.

**Task**: Write a function `is_anagram()`, which takes two strings and checks if they contain the exact same characters (ignoring spaces, punctuation, and capitalization).
The function should return `True` if the strings match this criterion; otherwise, return `False`.

#### **Parameters**
- `string1`: A string input.
- `string2`: Another string input.

#### **Result**
- `bool`: Returns `True` if the strings are scrambled versions of each other, otherwise `False`.

#### **Constraints**
- Both input strings will contain at least one character.

#### **Example 1**
Input:  
`"Dormitory"`, `"Dirty Room"`  
Result:  
`True`

#### **Example 2**
Input:  
`"Code Newbie"`, `"Decode Vine"`  
Result:  
`False`

---

### **Python Code **

```python
def is_anagram(string1, string2):
    # Custom function to clean a string and count characters
    def clean_and_count(s):
        char_count = {}
        for char in s:
            # Consider only alphabetic characters and convert to lowercase
            if char.isalpha():
                char = char.lower()
                # Increment character count
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
        return char_count

    # Clean both strings and count their characters
    count1 = clean_and_count(string1)
    count2 = clean_and_count(string2)

    # Compare the character dictionaries
    return count1 == count2

# Example Usage
print(is_scrambled("Dormitory", "Dirty Room"))  # Output: True
print(is_scrambled("Code Newbie", "Decode Vine"))  # Output: False
print(is_scrambled("Silent Night", "Listen Thing"))  # Output: True
```

---

### **Explanation**
1. **Custom Cleaning**:
   - The `clean_and_count` function processes the string to:
     - Remove non-alphabetic characters.
     - Convert characters to lowercase.
     - Count occurrences of each letter in a dictionary.

2. **Validation**:
   - Both strings are cleaned and converted to character dictionaries.
   - The dictionaries are compared. If they match, the strings are scrambled versions of each other.

3. **Modified Example**:
   - Replaced previous examples with `Dormitory` → `Dirty Room` and others.
