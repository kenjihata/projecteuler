projecteuler
============

Solving Project Euler problems: projecteuler.net

**Retrospective Problem Optimization Ideas for the Future**

- Problem 17: Instead of computing each of the words individually, calculate the number of times each phrase (e.g 'twenty' or 'hundred') is used between the lower and upper bounds. Spends less time redundantly computing the same phrases ('twenty-two', 'twenty-three').
