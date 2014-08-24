projecteuler
============

Solving Project Euler problems: projecteuler.net

**Retrospective Problem Optimization Ideas and Challenges for the Future**

- Problem 13: Instead of using python bigint, develop a method for addition by strings to handle integer overflow

- Problem 17: Instead of computing each of the words individually, calculate the number of times each phrase (e.g 'twenty' or 'hundred') is used between the lower and upper bounds. Spends less time redundantly computing the same phrases ('twenty-two', 'twenty-three').

- Problem 20: Instead of using python bigint, develop a method for multiplication by strings to handle integer overflow

- Problem 25: Again, instead of using python bigint, use the limit on Fibonacci numbers

- For greatest common factor, use the Euler algorithm instead of brute force

- Problem 34: Find a smarter approach than brute-force. Most likely, you can use the fact that if the greatest digit's factorial is far smaller or greater than the number, you can immediately consider it false; this way, you don't have to check all possible numbers from 10 to 9!*7.
