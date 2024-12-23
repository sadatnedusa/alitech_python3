## Q213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 
### Example 1:

- Input: nums = [2,3,2]
- Output: 3
     - Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

### Example 2:

- Input: nums = [1,2,3,1]
- Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

### Example 3:

Input: nums = [1,2,3]
Output: 3

---

### Brute force approach 

To solve the problem efficiently, we need to use a dynamic programming approach.
Since the houses are arranged in a circle, the problem becomes a bit more complex than the linear House Robber problem. 

Here’s the approach:

1. **Circular Arrangement**: The circular arrangement means the first and last house cannot both be robbed. To handle this:
   - Solve the problem twice:
     - Exclude the first house.
     - Exclude the last house.
   - Return the maximum of the two results.

2. **Dynamic Programming**: For a linear arrangement of houses (helper function):
   - Use two variables, `prev1` and `prev2`, to keep track of the maximum money that can be robbed up to the current house without alerting the police.
   - For each house:
     - Compute `current` as the maximum of robbing this house (`prev2 + nums[i]`) or skipping it (`prev1`).
     - Update `prev2` to `prev1` and `prev1` to `current`.

3. **Implementation**:

```python
def rob(nums):
    if len(nums) == 1:
        return nums[0]
    
    def rob_linear(nums):
        prev1, prev2 = 0, 0
        for num in nums:
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
        return prev1
    
    # Rob excluding the first house or the last house
    return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))

# Example usage
nums1 = [2, 3, 2]
nums2 = [1, 2, 3, 1]
nums3 = [1, 2, 3]

print(rob(nums1))  # Output: 3
print(rob(nums2))  # Output: 4
print(rob(nums3))  # Output: 3
```

### Explanation:
1. For `nums = [2,3,2]`:
   - Excluding the first house: `[3,2]`, maximum = 3.
   - Excluding the last house: `[2,3]`, maximum = 3.
   - Result: `max(3, 3) = 3`.

2. For `nums = [1,2,3,1]`:
   - Excluding the first house: `[2,3,1]`, maximum = 4.
   - Excluding the last house: `[1,2,3]`, maximum = 4.
   - Result: `max(4, 4) = 4`.

3. For `nums = [1,2,3]`:
   - Excluding the first house: `[2,3]`, maximum = 3.
   - Excluding the last house: `[1,2]`, maximum = 2.
   - Result: `max(3, 2) = 3`.

This approach ensures O(n) time complexity and O(1) space complexity.
