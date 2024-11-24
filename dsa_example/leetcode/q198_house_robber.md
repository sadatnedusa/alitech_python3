## Q198. House Robber

You are a professional robber planning to rob houses along a street. 

Each house has a certain amount of money stashed, the only constraint stopping you from robbing 
each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

- Example 1:
 - Input: nums = [1,2,3,1]
 - Output: 4
   - Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
- Total amount you can rob = 1 + 3 = 4.

- Example 2:
 - Input: nums = [2,7,9,3,1]

- Output: 12
 - Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
 - Total amount you can rob = 2 + 9 + 1 = 12.
 
- Constraints:
 - 1 <= nums.length <= 100
 - 0 <= nums[i] <= 40

---

### This is a classic dynamic programming problem known as the "House Robber" problem.

### Problem Breakdown

You need to decide which houses to rob to maximize the total money, but with the restriction that you cannot rob two adjacent houses. Let's use dynamic programming to solve this.

### Approach

We can define `dp[i]` as the maximum amount of money you can rob from the first `i` houses. The key observation is that for each house `i`, you have two choices:

1. **Skip house `i`**: In this case, the maximum amount of money you can rob is just the value of `dp[i-1]`, which is the optimal solution up to house `i-1`.
   
2. **Rob house `i`**: In this case, you cannot rob house `i-1`, but you can rob house `i` and then the optimal amount for the first `i-2` houses. So, the value will be `nums[i] + dp[i-2]`.

Thus, the recurrence relation is:
\[ dp[i] = \max(dp[i-1], nums[i] + dp[i-2]) \]

### Base Cases:
- `dp[0] = nums[0]` (If there's only one house, you rob it)
- `dp[1] = max(nums[0], nums[1])` (With two houses, you rob the one with the higher amount)

### Final Answer:
The final answer will be stored in `dp[n-1]`, where `n` is the number of houses.

### Solution Code (Python)

```python
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # dp array to store the maximum money we can rob up to house i
    dp = [0] * len(nums)
    
    # Base cases
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    # Fill the dp array for all houses starting from house 2
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], nums[i] + dp[i-2])
    
    # The result is the maximum money we can rob from all houses
    return dp[-1]
```

### Explanation:

1. **Base cases**: 
   - `dp[0] = nums[0]`: If there's only one house, rob it.
   - `dp[1] = max(nums[0], nums[1])`: If there are two houses, rob the one with the higher money.
   
2. **Dynamic Programming Transition**: 
   - For each house `i`, calculate the maximum money you can rob either by:
     - Not robbing house `i` and taking the value from `dp[i-1]`
     - Robbing house `i` and adding the value of `nums[i]` to the amount robbed from `dp[i-2]`.

3. **Result**: The final answer is stored in `dp[-1]`, which contains the maximum money that can be robbed from all houses.

### Time Complexity:
- **O(n)**, where `n` is the number of houses. We loop through the array once and perform constant-time operations for each house.

### Space Complexity:
- **O(n)** for the `dp` array. You could optimize space to **O(1)** by only keeping track of the last two values (`dp[i-1]` and `dp[i-2]`), but the above implementation uses an array for clarity.

### Example Walkthrough

#### Example 1:
```python
nums = [1, 2, 3, 1]
rob(nums)
```
- Initialize `dp`: `[1, 2, 0, 0]`
- For house 2: `dp[2] = max(dp[1], nums[2] + dp[0]) = max(2, 3 + 1) = 4`
- For house 3: `dp[3] = max(dp[2], nums[3] + dp[1]) = max(4, 1 + 2) = 4`
- Final result: `dp[3] = 4`

#### Example 2:
```python
nums = [2, 7, 9, 3, 1]
rob(nums)
```
- Initialize `dp`: `[2, 7, 0, 0, 0]`
- For house 2: `dp[2] = max(dp[1], nums[2] + dp[0]) = max(7, 9 + 2) = 11`
- For house 3: `dp[3] = max(dp[2], nums[3] + dp[1]) = max(11, 3 + 7) = 11`
- For house 4: `dp[4] = max(dp[3], nums[4] + dp[2]) = max(11, 1 + 11) = 12`
- Final result: `dp[4] = 12`
- 
---

![image](https://github.com/user-attachments/assets/61e627b7-58a4-4349-93be-7d8cb620c543)

![image](https://github.com/user-attachments/assets/ede79e9e-64fe-4712-8079-7d1daa26eb1e)

![image](https://github.com/user-attachments/assets/8f56822b-a1fc-496a-9c5e-782e9c63842a)

![image](https://github.com/user-attachments/assets/de88207f-c7f3-4a43-838c-8bb1473c99e0)

![image](https://github.com/user-attachments/assets/4037cebe-cff3-4db5-956e-215c357f43b0)

![image](https://github.com/user-attachments/assets/60c71404-35fd-4a08-ba0f-5daa459c0624)

![image](https://github.com/user-attachments/assets/12906c8f-eac2-4889-b643-ba496d317131)

![image](https://github.com/user-attachments/assets/5b2e1cc3-3654-4d6a-8806-4c8b79393515)

![image](https://github.com/user-attachments/assets/af2ca3a9-1019-4c1d-9cd7-75dca568eebc)

![image](https://github.com/user-attachments/assets/11ee51e5-df2a-4f12-a959-af36a0e66aa3)

![image](https://github.com/user-attachments/assets/589fc733-1ce3-48a7-a299-a6bfb4576da9)





