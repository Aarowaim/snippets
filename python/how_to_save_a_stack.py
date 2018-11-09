'''Description:
This is an example I hosted on repl.it on April 2, 2018 to demonstrate why all recursive calls should be optimized into iterative calls when possible
Recursion is totally valid when problem solving, but recursive *call chains* are an easy way to shoot oneself in the foot
Save stack frames by writing the recursion using an iterating "accumulator" pattern
This strategy applies to many different types of recursive calls, and in addition to preventing stack overflows, it does improve performance noticablye.
'''

# recursion
def factorial_r(n):
    if n > 1:
        return n * factorial_r(n-1)
    else:
        return 1

# iteration     
def factorial_i(n):
    accumulator = 1
    while n > 0:
        accumulator *= n
        n -= 1
    return accumulator

print('Recursion:', factorial_r(25))
print('Iteration:', factorial_i(25))

try:
    print('Recursion:', factorial_r(2500))
except:
    print('Recursion: Maximum recursion depth hit')
print('Iteration:', str(factorial_i(2500))[:50] + '...')
