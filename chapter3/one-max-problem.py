"""
using the DEAP framework

The OneMax (or One-Max) problem is a simple optimization task that is often
used as the Hello World of genetic algorithm frameworks. We will use this problem
to demostrate how DEAP can be used to implement a genetic algorithm.

The OneMax task is to find the binary string of a given lenght that maximizes
the sum of its digits. For example, the OneMax problem of length 5 will consider
candidates such as the following:

    10010 (sum of digits=2)
    01110 (sum of digits=3)
    11111 (sum of digits=5)

Obviously (to us), the solution to this problem is always the string that comprises
all 1s. But the genetic algorithm does not have this knowledge, and needs to blindly 
look for this solutions using its genetic operators. If the algorithm does its job,
it will find the solution, or at least one close to t, within a reasonable amount of 
time.

"""



def main():
    pass


if __name__ == "__main__":
    main()
