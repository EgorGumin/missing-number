## Missing Number Problem

### Given
A list which contains n-1 numbers from range 1 to n.
The list contains each number only once, except the one which is missing.<br>

### Problem
Find the missing number.

### Constraints
* n >= 2
* each number in the list is an int

### Solution
We will use the fact that a sum of the `1..n` series is `n * (n + 1) / 2`.
The difference between a complete series sum and a sum of the given list will be the missing number.<br>
_Using XOR for this task is a common but less obvious and not more effective approach._

## Run tests
`python -m unittest discover`