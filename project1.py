import time
import random
import ctypes
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np

ctypes.windll.shcore.SetProcessDpiAwareness(1)

def gen_rand_arr():
    try:
        # Get user input 
        user_input = int(entry.get())
        # Generate a random array with user input length
        random_array = [random.randint(1, 100) for x in range(user_input)]

       # Display the random array in the result entry widget
        result_box.delete(0, tk.END)
        #turn it into a string so user can add more to the array if they want
        result_box.insert(0, str(random_array)) 
        
        for i in range(0, len(random_array)):
            random_array[i] = int(random_array)
        
    except ValueError:
        # Handle the case where the user input is not a valid integer
        result_box.delete(0, tk.END)
        result_box.insert(0, "Invalid input. Please enter a valid integer.")

    
root = tk.Tk()
#root.geometry("800x500")
#scale lettering with size of frame
root.tk.call('tk', 'scaling', 2.0)
titleLabel = tk.Label(root, text = "Algorithm Comparisons")
#titleLabel.pack(padx = 5, pady = 5)

# User input box
entry = tk.Entry(root, width=10)
entry.grid(row=0, column=0, padx=10, pady=10)

# generate array button
array_button = tk.Button(root, text="Generate Array", command=gen_rand_arr)
array_button.grid(row=0, column=1, padx=5, pady=5)


# Show resulting generated array. Can be edited by user
result_box = tk.Entry(root, width=60)
result_box.grid(row=0, column=2, padx=10, pady=10)

root.mainloop()

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr, key = lambda x: x):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if key(x) <= key(pivot)]
        greater = [x for x in arr[1:] if key(x) > key(pivot)]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)
    
def mergeSort(arr):
    if len(arr) > 1: 
        mid = len(arr) // 2 
        L = arr[:mid] 
        R = arr[mid:] 
        mergeSort(L) 
        mergeSort(R)
        i = j = k = 0 
                      
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main():

    #random array, implenet user input/gui
    arr = [10,2,3,4,1,3,32,34,12,23,11,22]
    
    #list of different sorts
    sorts = {'Bubble Sort': bubble_sort, 
             'Merge Sort' : mergeSort, 
             'Quick Sort' : quick_sort}
    
    #array for times
    rtimes = []

    #measures execution time for each sort
    for sort in sorts.values():
        start_time = time.time()
        sort(arr)
        end_time = time.time()
        elapsed_time = end_time - start_time
        rtimes.append((elapsed_time * 1000)/1000)


    #graph
    algo = list(sorts.keys())
    rtime = rtimes
    fig = plt.figure(figsize = (10,5))
    plt.bar(algo, rtime, color ='green', width = 0.3)

    plt.xlabel("Algorithms", fontweight = "bold", fontsize = 15)
    plt.ylabel("Runtime(ms)", fontweight = "bold", fontsize = 15)
    plt.title("Sorting Algorithms")

    #plt.show()

main()


