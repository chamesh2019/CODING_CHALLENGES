# Challenge 822 - Is This a Right Angled Triangle?

Given three numbers, determine whether they are the edges of a right-angled triangle.

## Examples
```python
right_triangle(3, 4, 5) ➞ True
# This is the classic example of a "nice" right angled triangle.

right_triangle(145, 105, 100) ➞ True
# This is a less famous example.

right_triangle(70, 130, 110) ➞ False
# This isn't a right angled triangle.
```
## Notes

- Notice the largest side of the triangle might not be the last one passed to the function
- All numbers will be integers