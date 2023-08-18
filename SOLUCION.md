## Solution

We need to find pairs of integers from a list, those pairs sum them up must match witha target given

### Steps:

1. **Inizialitation `seen`**: we store number that were already visited

2. **List**: for each `n`, we get the different `target - n`

3. **Validacion**: If the different exists in Set `seen`, we hve found the target

### Worse case escenario Big O

Time complexity for this soutio is **O(n)**, we just iterate ones, and operation with the Set `seen`is **O(1)**. We got the total of **O(n)**.
