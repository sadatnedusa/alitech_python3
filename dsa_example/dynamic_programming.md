# What is dp array in programming

A **`dp` array** in programming typically refers to an array used in **Dynamic Programming**, a technique for solving problems by breaking them down into smaller overlapping subproblems and solving each subproblem only once.
The `dp` array is used to store the results of these subproblems, so they don’t need to be recomputed, saving time and reducing redundant calculations.

### Key Features of a `dp` Array:
1. **Memoization**: In **top-down dynamic programming** (recursive approach with memoization), the `dp` array stores solutions to subproblems as they are computed.
2. **Tabulation**: In **bottom-up dynamic programming** (iterative approach), the `dp` array is built up from smaller subproblem solutions to larger ones.
3. **Optimization**: It helps optimize the solution by preventing recalculations.

### Structure and Use:
- **1D `dp` Array**: For problems where a single variable tracks the state.
  - Example: Fibonacci numbers.
    ```c
    int dp[100]; // Array to store Fibonacci numbers
    dp[0] = 0;
    dp[1] = 1;
    for (int i = 2; i < 100; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }
    ```

- **2D `dp` Array**: For problems with two variables defining the state.
  - Example: Longest Common Subsequence (LCS).
    ```c
    int dp[m+1][n+1];
    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= n; j++) {
            if (i == 0 || j == 0) dp[i][j] = 0; // Base case
            else if (str1[i-1] == str2[j-1])
                dp[i][j] = dp[i-1][j-1] + 1; // Characters match
            else
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]); // Take max of two options
        }
    }
    ```

- **3D or Higher Dimensional `dp` Arrays**: For problems with more complex state variables.

### Common Applications:
- **Fibonacci Sequence**: Using a 1D array to store intermediate results.
- **Knapsack Problem**: Using a 2D array to store results based on item index and weight capacity.
- **Shortest Paths (e.g., Floyd-Warshall Algorithm)**: Using a 2D array for distance computation.
- **String Problems**: LCS, Edit Distance, etc., use 2D `dp` arrays.

By leveraging `dp` arrays effectively, dynamic programming simplifies complex problems and ensures efficient computation.
