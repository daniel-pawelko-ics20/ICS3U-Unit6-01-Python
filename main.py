#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Array

from random import randint


def main():
    # main function for array

    # define average variable
    average = 0

    # create array with 10 random numbers/process
    arr = [randint(1, 100) for rand in range(10)]

    # add up arr/process
    for num in arr:
        print(f"The random number is: {num}")
        average += num

    # output
    print(f"\nThe average is {average/10}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
