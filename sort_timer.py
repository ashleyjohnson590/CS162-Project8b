#Author: Ashley Johnson
#Date: 5/20/2021
#Description: Program uses time module and decorator function to time the number of seconds it
#takes the decorator function to run and the wrapper function returns the elapsed time. The
#compare sorts function generates a list of 1000 numbers and makes a separate copy of the list.
# Function times how long it takes bubble sort to sort the copy of the list of numbers. Function
# does the same for a list of 2000, 3000, and up to 10,000 numbers. Program generates a graph using
# matlib that plots number of elements being sorted on the x axis, and time in seconds to sort on
# the y axis.
import random
from functools import wraps
import time
import matplotlib.pyplot as plt
import matplotlib as mat

def list_generator(size, low=1, high=10000):
    """generates a list of random numbers from 1 to 10,000"""

    print("\n\nGenerating list of size {}".format(size))
    randomlist = [random.randint(low, high) for x in range(size)]
    return randomlist

def sort_timer(sort_function):
    """decorator function that times how many seconds it takes the function to run. The
     wrapper function returns the elapsed time."""
    @wraps(sort_function)
    def wrapper(list):
        begin = time.perf_counter()
        sort_function(list)
        end = time.perf_counter()
        runtime = end-begin
        return runtime
    return wrapper

def compare_sorts(b_sort,i_sort):
    """generates a list of 1000 numbers using list_generator helper function and makes a separate
    copy of the list. Function times how long it takes for insertion sort to sort the copy and how
    long it takes bubble sort to sort the copy. Function repeats the same procedure for 2000, 3000
    and up to 10,000 random numbers. """
    #config = mat.get_configdir()
    #print(config)
    x_vals = []
    y_vals_bubble = []
    y_vals_insert = []

    i = 1000
    while i <= 10000:
        my_list = list_generator(i)
        my_list2 = list(my_list)
        x_vals.append(i)
        print("Getting time for bubble_sort...")
        y_vals_bubble.append(b_sort(my_list))
        print("Getting time for insert_sort...")
        y_vals_insert.append(i_sort(my_list2))
        i += 1000
    plt.plot(x_vals, y_vals_bubble,'go--',label='Bubble Sort')
    plt.plot(x_vals, y_vals_insert, 'ro--', label='Insertion Sort')
    plt.legend(loc="upper left")
    plt.show()


@sort_timer
def bubbleSort(a_list):
    """
    Sorts a_list in ascending order
    """
    for pass_num in range(len(a_list) - 1):
        for index in range(len(a_list) - 1 - pass_num):
            if a_list[index] > a_list[index + 1]:
                temp = a_list[index]
                a_list[index] = a_list[index + 1]
                a_list[index + 1] = temp

# Function to do insertion sort
@sort_timer
def insertion_sort(a_list):
  """
  Sorts a_list in ascending order
  """
  for index in range(1, len(a_list)):
    value = a_list[index]
    pos = index - 1
    while pos >= 0 and a_list[pos] > value:
      a_list[pos + 1] = a_list[pos]
      pos -= 1
    a_list[pos + 1] = value

def main():
    compare_sorts(bubbleSort,insertion_sort)

if __name__ == "__main__":


    main()