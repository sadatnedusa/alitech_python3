## Q201 - Bitwise AND of Numbers Range

- Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.

Example 1:

  Input: left = 5, right = 7
  Output: 4
  
Example 2:

  Input: left = 0, right = 0
  Output: 0

Example 3:

  Input: left = 1, right = 2147483647
  Output: 0

Constraints:
  0 <= left <= right <= 231 - 1
  
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

---
## Solution 4

```python3
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= right-1
        return left & right

```
