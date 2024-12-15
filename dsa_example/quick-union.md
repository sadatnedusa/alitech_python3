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
