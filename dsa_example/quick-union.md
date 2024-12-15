## **Quick-Union** data structure:

```python
class QuickUnion:
    def __init__(self, n):
        # Initialize the id array where each element is its own root
        self.id = list(range(n))

    def root(self, i):
        # Find the root of the element i
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        # Check if p and q are connected (i.e., have the same root)
        return self.root(p) == self.root(q)

    def union(self, p, q):
        # Connect p and q by linking the root of p to the root of q
        rootP = self.root(p)
        rootQ = self.root(q)
        
        # If they are not already connected, perform the union
        if rootP != rootQ:
            self.id[rootP] = rootQ
            print(f"Union of {p} and {q}: {self.id}")

# Example usage
if __name__ == "__main__":
    quick_union = QuickUnion(10)  # Create a quick-union structure with 10 elements

    # Perform union operations
    quick_union.union(3, 4)
    quick_union.union(4, 9)
    quick_union.union(8, 0)
    quick_union.union(2, 3)
    quick_union.union(5, 6)

    # Check if two elements are connected
    print(f"Are 3 and 9 connected? {quick_union.connected(3, 9)}")
    print(f"Are 8 and 0 connected? {quick_union.connected(8, 0)}")
```

### Explanation:
1. **Initialization**: In the `__init__` method, the `id` array is initialized such that each element is its own root. This means each element points to itself initially.

2. **Root Function**: The `root` function traces through the array until it finds the root (the element that points to itself). This is done by following the chain of pointers starting from the given element.

3. **Connected Function**: The `connected` function checks if two elements are in the same component by comparing their roots.

4. **Union Function**: The `union` function connects two components by linking the root of one component to the root of the other. This operation modifies the `id[]` array to perform the union.

### Example Usage:
- In this example, we perform multiple `union` operations to connect different elements, and then check if certain pairs of elements are connected using the `connected` method.


---

In a **quick-union** data structure, each element points to another element in the `id[]` array. The root of an element is the one whose index points to itself.
To find the roots of two elements, we need to trace their indices recursively until we find the element that points to itself.

Given the `id[]` array for 10 elements as:

| i  | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
|----|----|----|----|----|----|----|----|----|----|----|
| id[i] | 0  | 9  | 6  | 5  | 4  | 2  | 6  | 1  | 0  | 5  |

Let's trace the roots of elements **3** and **7**:

### Root of 3:
1. Start at index 3: `id[3] = 5`
2. Now, follow the pointer at index 5: `id[5] = 2`
3. Follow the pointer at index 2: `id[2] = 6`
4. Follow the pointer at index 6: `id[6] = 6` (6 is the root, as `id[6]` points to itself)

So, the root of element 3 is **6**.

### Root of 7:
1. Start at index 7: `id[7] = 1`
2. Now, follow the pointer at index 1: `id[1] = 9`
3. Follow the pointer at index 9: `id[9] = 5`
4. Follow the pointer at index 5: `id[5] = 2`
5. Follow the pointer at index 2: `id[2] = 6`
6. Follow the pointer at index 6: `id[6] = 6` (6 is the root, as `id[6]` points to itself)

So, the root of element 7 is also **6**.

### Answer:
The roots of elements **3** and **7** are **6** and **6**, respectively.

Thus, the correct answer is:
**6 and 6**.
