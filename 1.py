"""
Tailor for arcsinx
"""

import math
import matplotlib.pyplot as plt
import numpy as np

def teil_arcsin(n, x):
    """
    evaluates Teilor sum for n
    """
    sum = 0
    for i in range(n):
        sum += math.factorial(2*i)*(x**(2*i+1))/((4**i)*((math.factorial(i)**2)*(2*i+1)))
    return sum

def comparison(x):
    """
    compares the difference between limited Tailor sum and math module value
    """
    numbers = range(1, 51)
    sum_list = []
    mat_val = math.asin(x)
    milestones = [1.0e-1, 1.0e-3, 1.0e-6]
    for n in numbers:
        n_val = teil_arcsin(n, x)
        sum_list.append(n_val)
        for i in range(3):
            if milestones[i] is not True and (mat_val-n_val) <= milestones[i]:
                print(f'The difference for {n} elements is {mat_val-n_val},\
 which is lesser than {milestones[i]}')
                milestones[i]=True
    if milestones.count(True)<3:
        print("Higher level of accuracy is not reachable within the scope of 50")
    print(f'The difference for {n} elements is {mat_val-n_val}')
    return sum_list, mat_val
def visual(lists):
    """
    creates plot of velues obtained by sum and math module
    """
    num_list = range(1, 51)
    fig, ax = plt.subplots()
    ax.plot(num_list, lists[0], linewidth=2.0)
    ax.plot(num_list, [lists[1]]*50, linewidth=2.0)
    ax.set(xlabel='number of elements in sum', ylabel='value',\
        title=f"Comparison for arcsin({x})")
    ax.grid()
    plt.show()

def visual2():
    """
    creates plot of velues obtained by sum and math module
    """
    n = int(input('Enter n: '))
    num_list = np.arange(-1, 1, step = 0.05)
    actual = []
    teil = []
    for x in num_list:
        actual.append(math.asin(x))
        teil.append(teil_arcsin(n, x))
    fig, ax = plt.subplots()
    ax.plot(num_list, actual, linewidth=2.0)
    ax.plot(num_list, teil, linewidth=2.0)
    ax.axline((0,0), (1,0), linestyle = '--')
    ax.axline((0,0), (0,1), linestyle = '--')
    ax.set(xlabel='number of elements in sum', ylabel='value',\
        title=f"Comparison of arcsin(x) for n={n}")
    ax.grid()
    plt.show()

if __name__=="__main__":
    print("This is a program for comparison of Tailor calculation \
    of arcsin(x) to python math module calculation")
    choice = input('I have two options of visualisation.\
Enter 1 or 2 ')
    if choice=='1':
        try:
            x = float(input("Enter x: "))
            if -1 < x < 1:
                visual(comparison(x))
            else:
                print('We take a number within the (-1:1) scope')
        except ValueError:
            print('We take a number within the (-1:1) scope')
    elif choice == '2':
        try:
            visual2()
        except ValueError:
            print('n must be int')
    else:
        print('wrong input :_(')
