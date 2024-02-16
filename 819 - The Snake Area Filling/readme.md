# Challenge 819 - The Snake — Area Filling

This challenge is based on the classic videogame "Snake".

Assume the game screen is an `n * n` square, and the snake starts the game with length 1 (i.e. just the head) positioned on the top left corner.

In this version of the game, the length of the snake doubles each time it eats food (e.g. if the length is 4, after eating it becomes 8).

Create a function that takes the side length of the game screen and returns the number of times the snake can eat before it runs out of space on the game screen.

## Examples
```python
snake_fill(3) ➞ 3

snake_fill(6) ➞ 5

snake_fill(24) ➞ 9
```
