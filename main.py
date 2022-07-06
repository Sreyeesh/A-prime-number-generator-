# In the last lecture we learned how to construct a generator function.
# Recall the code in an earlier lecture Two loop key words + finding prime numbers, where we learned how to find prime numbers:
# 1 for n in range(2,20):
# 2     for x in range(2, n):
# 3         if n % x == 0:
# 4             print('{} equals {} * {}.'.format(n, x, n//x))
# 5             break
# 6     else:
# 7         print('{} is a prime number.'.format(n))

# We used some nested for loops as well as for - else statements to determine primality of a number in a certain range (from 2  to 20  in the above code).
# In this exercise, we ask you to define a generator function which takes bound as input and generates prime numbers up to, but not including, the bound parameter.
# Happy coding!
# — Jose and the Teclado team
# Remember, as you progress through the course and tackle increasingly complicated challenges, joining the Discord server can be an excellent idea. It's included in the course and you can chat with other students and the Teclado team. Join at https://discord.gg/BBWwyMq.

"""
Take a look at the code in the problem description where we test if a number is prime.
Refactor the code and put it into the function below to turn the prime_generator() function into a generator.

Implement your generator so that others can get a prime number generator like this:

g = prime_generator(100)    # g can generate prime numbers under 100
next(g) # get next prime like this

Reminder: you don't need to change the function name nor the argument
"""
def prime_generator(bound):
   x = 0
   for n in range(2,20):
           for x in range(2, x):
            if n % x == 0:
                 break
            else:
              yield x

              

  