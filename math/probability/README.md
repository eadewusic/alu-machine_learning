# Probability Assignment

## Project Overview

This project is focused on understanding and applying fundamental concepts of probability, probability distributions, and related mathematical functions. It includes both theoretical and practical tasks, requiring you to implement probability-based algorithms and solve mathematical approximations without the use of external Python libraries.

The project explores topics such as:

- Basic Probability Theory
- Disjoint and Independent Events
- Probability Distributions
  - Normal Distribution
  - Binomial Distribution
  - Poisson Distribution
  - Hypergeometric Distribution
- Cumulative Distribution Functions (CDFs)
- Variance, Standard Deviation, and Mean
- Mathematical Approximations for functions like the error function (`erf`)

## Learning Objectives

By the end of this project, I should be able to:

- Understand and explain probability theory fundamentals.
- Implement various probability distributions from scratch.
- Calculate statistical measures such as mean, variance, and standard deviation.
- Work with probability functions like CDFs and PMFs.
- Approximate mathematical constants like π and e for computations.
- Implement probability functions without importing external libraries.

## Usage

### Prerequisites

- Python 3.5 or higher (The project is designed for Ubuntu 16.04 LTS)
- Knowledge of basic Python syntax and probability theory.

### How to Run

1. Clone or download this repository.
2. Navigate to the project directory:
   ```bash
   cd path/to/project_directory
   ```
3. Ensure the Python scripts are executable:
   ```bash
   chmod +x *.py
   ```
4. Execute each Python file as follows:
   ```bash
   ./task_X.py
   ```

### Mathematical Approximations

For mathematical approximations of irrational numbers and special functions, the following values are used:

- π (Pi): `3.1415926536`
- e (Euler's Number): `2.7182818285`

For the error function (erf) approximation, the following equation is implemented:

\[
\text{erf}(x) = \frac{2}{\sqrt{\pi}} \left( x - \frac{x^3}{3} + \frac{x^5}{10} - \frac{x^7}{42} + \frac{x^9}{216} \right)
\]

erf(x)= 
π
​
 
2
​
 (x− 
3
x 
3
 
​
 + 
10
x 
5
 
​
 − 
42
x 
7
 
​
 + 
216
x 
9
 
​
 )

### Example Task

In Task 1, we implement the approximation for the error function using the above formula. The function takes a single input `x` and returns the approximate value of `erf(x)`.

```python
#!/usr/bin/env python3

# Task 1: Error function approximation
pi = 3.1415926536

def erf_approx(x):
    return (2 / (pi**0.5)) * (x - (x**3)/3 + (x**5)/10 - (x**7)/42 + (x**9)/216)

# Example usage
x = 1.0
print("erf({}) ≈ {}".format(x, erf_approx(x)))
```

## Requirements

- All files should end with a new line.
- All Python scripts must be executable.
- The project should adhere to `pycodestyle` (version 2.5).
- All functions and classes should have proper documentation.
