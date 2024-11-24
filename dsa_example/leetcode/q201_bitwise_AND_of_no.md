## Q201 - Bitwise AND of Numbers Range

- Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

  - Example 1:
    - Input: left = 5, right = 7
    - Output: 4
  
  - Example 2:
    - Input: left = 0, right = 0
    - Output: 0

  - Example 3:
    - Input: left = 1, right = 2147483647
    - Output: 0

- Constraints:
  - 0 <= left <= right <= 231 - 1
  
---

- To solve the problem of finding the **bitwise AND** of all numbers in a given range `[left, right]`, we can use a straightforward bit-shifting approach. 
- The key observation is that the result of the bitwise AND operation depends on the common prefix (most significant bits) of the binary representations of `left` and `right`.
- As the range grows, lower bits turn to zero.

## Solution 1

### Algorithm Explanation:
1. If `left != right`, any differing bits in the binary representation between `left` and `right` will result in zeros in the lower positions of the result.
2. Keep shifting both numbers to the right until they are equal. This effectively trims the differing bits.
3. The remaining bits represent the common prefix. Shift it back to its original position.


### Python Implementation:

```python
def range_bitwise_and(left: int, right: int) -> int:
    shift = 0
    # Find the common prefix by right-shifting
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
    
    # Shift back to the original position
    return left << shift

# Examples
print(range_bitwise_and(5, 7))          # Output: 4
print(range_bitwise_and(0, 0))          # Output: 0
print(range_bitwise_and(1, 2147483647)) # Output: 0
```

### Explanation of Examples:
1. **Example 1**:
   - Binary representations:
     - `5 -> 101`
     - `6 -> 110`
     - `7 -> 111`
   - The common prefix is `100` (decimal 4).

2. **Example 2**:
   - `left = 0`, `right = 0`: Result is `0` because there's only one number.

3. **Example 3**:
   - `left = 1`, `right = 2147483647`:
     - The entire range spans numbers with differing higher bits. 
     - Result is `0` because no bits are common across the range.

### Complexity:
- **Time Complexity**: \(O(\log(\text{right}))\) due to bit-shifting.
- **Space Complexity**: \(O(1)\), as no additional space is used. 

---

## Solution 2:

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left < right:
            left >>=1
            right >>=1
            count+=1
        return left << count
```

---
## Solution 3

```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return -1 << (left ^ right).bit_length() & left
```

### Why it is an efficient solution for finding the bitwise AND of numbers in the range `[left, right]`.


### **Code Breakdown**
```python
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return -1 << (left ^ right).bit_length() & left
```

#### **Step-by-step Explanation**:
1. **XOR Operation (`left ^ right`)**:
   - The XOR (`^`) of `left` and `right` identifies the positions of bits where `left` and `right` differ.
   - For example:
     - `left = 5 (101)` and `right = 7 (111)`.
     - `left ^ right = 2 (010)` (difference in the 2nd position from the right).
   - The positions of differing bits tell us how far apart the numbers are.

2. **Find the Most Significant Differing Bit (`.bit_length()`)**:
   - The `bit_length()` method gives the position (1-based) of the most significant bit in the XOR result.
   - This indicates the highest bit position where `left` and `right` differ.
   - Example:
     - For `left = 5` and `right = 7`, `left ^ right = 2 (010)`.
     - `.bit_length()` is `2` (2nd bit).

3. **Create a Mask to Zero Out Differing Bits (`-1 << ...`)**:
   - `-1` in binary is represented as all `1`s.
   - Left-shifting `-1` by the number of differing bits zeros out all bits below the most significant differing bit.
   - Example:
     - Left-shifting `-1` by `2`: `-1 << 2 = 11111100 (binary)`.
     - This mask retains only the common prefix of `left` and `right`.

4. **Apply the Mask (`& left`)**:
   - The bitwise AND (`&`) operation between the mask and `left` extracts only the common bits in the positions above the most significant differing bit.
   - This gives the result for the bitwise AND of all numbers in the range `[left, right]`.

### **Efficiency**
This method is extremely efficient for several reasons:

1. **Avoids Iteration**:
   - The naive solution would iterate through all numbers between `left` and `right`, performing a bitwise AND for each pair. This is computationally expensive for large ranges.
   - Instead, this approach computes the result in \(O(1)\) time complexity, relying on bit manipulations.

2. **Bitwise Operations Are Fast**:
   - XOR, bit-length calculation, left-shifting, and AND operations are low-level bitwise operations, which are very fast compared to iterative or arithmetic operations.

3. **Focuses Only on Differing Bits**:
   - By identifying the most significant differing bit, the solution effectively zeros out all bits that vary within the range, which is the essence of the problem.


### **Why is it the Most Efficient?**
- **Time Complexity**: O(1), because all operations (`^`, `.bit_length()`, `<<`, `&`) run in constant time.
- **Space Complexity**: O(1), as no extra memory is used.
- This is more efficient than approaches involving loops, which would take \(O(n)\) time for a range of size (n).


### **Examples**
#### Example 1:
Input: `left = 5`, `right = 7`
- `left ^ right = 2 (010)`.
- `.bit_length() = 2`.
- `-1 << 2 = 11111100`.
- `11111100 & 5 = 4`.

Output: `4`.

#### Example 2:
Input: `left = 1`, `right = 2147483647`
- `left ^ right = 2147483646`.
- `.bit_length() = 31`.
- `-1 << 31 = 10000000000000000000000000000000`.
- `10000000000000000000000000000000 & 1 = 0`.

Output: `0`.

This approach is optimal for large ranges due to its constant-time complexity and reliance on efficient bitwise operations.

---
## Solution 4

```python3
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= right-1
        return left & right

```
