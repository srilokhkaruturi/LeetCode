​# The problem

Find the largest substring that only contains unique characters

# Initial Approach

Go through the array with one loop O(n) ... did not find certain substrings, must use O(n^2) solution

# Correct approach

- Use two pointer method, exhaustive approach to finding substrings
- Second pointer starts off at initial element (case: length 1 string)
- Utilize a set to keep track of existing characters
- Append to list of unique substrings in two situations, you have made it to the end or there is a repeating character
