def staircase(n):
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

for i in range(11)[1:]:
     print(staircase(i))
