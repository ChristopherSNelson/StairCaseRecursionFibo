Certainly! Here's the code with a hashbang, __init__.py, and main function, incorporating the previous improvements:
Python

#!/usr/bin/env python3

from typing import Optional, Union

def staircase(n: int,whichFxn:str) -> int:
  """
  Calculates the number of ways to climb a staircase with n steps.

  Args:
      n: The number of steps in the staircase (must be a non-negative integer).
      whichFxn: Which function to use. "memo", "plain" or "fib"
      
  Returns:
      The number of ways to climb the staircase.

  Raises:
      ValueError: If n is negative.
  """

  if n < 0:# belt and suspenders. redundant vs main.
    raise ValueError("n must be a non-negative integer.")

  assert(whichFxn in {"memo", "plain", "fib"},f"wonky {whichFxn} input.") # belt and suspenders. redundant vs main.

  # Use memoization for efficiency (avoiding redundant calculations)
  memo = {0: 1, 1: 1, 2: 2}  # Base cases for 0, 1, and 2 steps

  if whichFxn.lower() =="memo":
       # Recursive approach with memoization
       def recursiveWithMemo(n):
         if n in memo:
           return memo[n]
         memo[n] = helper(n - 1) + helper(n - 2)
         return memo[n]

 elif whichFxn.lower() =="memo":
     def recursive_plain(n):
         for i in range(n):
         if n==1:
              return 1
         elif n==2:
              return 2
         elif n==0:
              return 1 # There is one way to go zero steps. n is supposed to be a positive integer...
         elif n<0:
              raise ValueError("Negative steps does not make much sense in the context of climbing. n is supposed to be a positive integer...")
         else:
              ways=staircase(n-1)+staircase(n-2) #recursion!
              return(ways)

elif whichFxn.lower() =="fib":
       def fibo_stairs:
         sqrt_5 = 5 ** 0.5
         fib_n = (((1 + sqrt_5)/2) ** (n+1) - ((1-sqrt_5)/2) ** (n + 1))/sqrt_5
         return int(fib_n)

else:
  raise ValueError(f"Something strange happened with whichFxn: {str(whichFxn)}")


# Unit tests (use 'test_staircase.py')
def test_staircase():
  assert staircase(0) == 1
  assert staircase(1) == 1
  assert staircase(2) == 2
  assert staircase(3) == 3
  assert staircase(4) == 5

def main():
  """
  Entry point for the program. Takes user input for n and prints the result.
  """
  while True:
    try:
      n = int(input("Enter the number of stairs (non-negative integer): "))
      if n < 0:
        raise ValueError("n must be a non-negative integer.")
      break
    except ValueError as e:
      print(f"Error: {e}")

    try:
      whichFxn = str(input("Enter the number of stairs (non-negative integer): "))
      if whichFxn not in {"memo", "plain", "fib"}: #},f"wonky {whichFxn} input."
        raise ValueError(f"wonky {whichFxn} input. Expects memo plain or fib.")
      break
    except ValueError as e:
      print(f"Error: {e}")

  print(f"Number of ways to climb {n} stairs: {staircase(n,whichFxn)}")

if __name__ == "__main__":
  main()

