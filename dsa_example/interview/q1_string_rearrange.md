
## String given below 

- Input: `"SoftwareEngineeringInTesting"`
- Output: `"TestingEngineeringInSoftware"`

- Rearranged in reverse order: `"Software"`, `"Engineering"`, and `"InTesting"`.

### Steps:
1. Identify the parts in the string.
2. Rearrange the parts as required.
3. Join them back together to form the desired output.

### Python Code:

```python
# Input string
str1 = "SoftwareEngineeringInTesting"

# Break the string into parts
# Assuming the parts are separated based on capitalization:
import re
parts = re.findall(r'[A-Z][a-z]*', str1)

# Rearrange the parts
reordered_str = ''.join(parts[::-1])

# Print the result
print(reordered_str)
```

### Explanation:
1. **Breaking the string into parts**: 
   - The regular expression `r'[A-Z][a-z]*'` helps break the input string into parts that start with an uppercase letter followed by any number of lowercase letters. This way, we can split `"SoftwareEngineeringInTesting"` into `["Software", "Engineering", "In", "Testing"]`.
   
2. **Reversing the parts**: 
   - The list `parts[::-1]` reverses the order of the list. So, the order becomes `["Testing", "In", "Engineering", "Software"]`.

3. **Joining the parts**: 
   - `''.join()` is used to combine the parts into a single string.

### Output:
```
TestingInEngineeringSoftware
```
