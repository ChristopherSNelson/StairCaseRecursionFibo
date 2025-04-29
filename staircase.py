#!/usr/bin/env python3

def staircase(n: int, whichFxn: str = "fib") -> int:
  """
  Calculates the number of ways to climb a staircase with n steps.
  You can climb one or two stes at a time.
  This follows the Fibonacci sequence.

  Args:
      n: The number of steps in the staircase (must be a non-negative integer).
      whichFxn: Which function to use. "memo", "plain" or "fib"
      
  Returns:
      The number of ways to climb the staircase. (

  Raises:
      ValueError: If n is negative.
  """

  if n < 0:
    raise ValueError("n must be a non-negative integer.")
  
  if whichFxn.lower() =="memo":
       # Recursive approach with memoization for efficiency
       def recursiveWithMemo(n):
         memo = {0: 1, 1: 1, 2: 2}  # Base cases for 0, 1, and 2 steps
         if n in memo:
           return memo[n]
         memo[n] = recursiveWithMemo(n - 1) + recursiveWithMemo(n - 2)
         return memo[n]

 elif whichFxn.lower() =="plain":
     def recursive_plain(n):
         for i in range(n):
         if n==1:
              return 1
         elif n==2:
              return 2
         elif n<=0:
              raise ValueError("n should be a positive integer.")
         else:
              ways=staircase(n-1)+staircase(n-2) 
              return(ways)

elif whichFxn.lower() =="fib":
       def fibo_stairs(n):
         sqrt_5 = 5 ** 0.5
         fib_n = (((1 + sqrt_5)/2) ** (n+1) - ((1-sqrt_5)/2) ** (n + 1))/sqrt_5
         # alternative with golden ratio: fib_n = round(((1.618034)**n-(1-1.618034)**n)/sqrt_5)
         return int(fib_n)

def test_staircase():
  assert staircase(0) == 1
  assert staircase(1) == 1
  assert staircase(2) == 2
  assert staircase(3) == 3
  assert staircase(4) == 5
  assert staircase(4) == 8
  

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
      whichFxn = str(input("Choose a function. Expects 'memo', 'plain', or 'fib': "))
      if whichFxn not in {"memo", "plain", "fib"}: 
        raise ValueError(f"Bad function input. Expects 'memo', 'plain', or 'fib'.")
      break
    except ValueError as e:
      print(f"Error: {e}")

  print(f"Number of ways to climb {n} stairs: {staircase(n,whichFxn)}")

if __name__ == "__main__":
  test_staircase()
  main()

