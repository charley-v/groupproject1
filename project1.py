import time
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox as m_box

#algorithms
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

def graph(arr):
    
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
    plt.bar(algo, rtime, color ='red', width = 0.3)

    plt.xlabel("Algorithms", fontweight = "bold", fontsize = 15)
    plt.ylabel("Runtime(ms)", fontweight = "bold", fontsize = 15)
    plt.title("Sorting Algorithms")
    def addlabels(x,y):
        for i in range(len(x)):
            plt.text(i, y[i], y[i], ha = 'center')
    
    addlabels(algo,rtime)

    plt.show()

def gui():
    root = tk.Tk()
    root.title("Sorting Algorithms")
    root.geometry('600x400')

    lbl = tk.Label(root, text = "Enter an Array", justify='center')
    txt = tk.Entry(root, justify='center')
    lbl.pack()
    txt.pack()

    #clear button
    def clear_txt():
        txt.delete(0,'end')

    #submit button
    def clicked():
        try:
            n = txt.get()
            arr = [int(item) for item in n.split()]
            graph(arr)
        except ValueError:
            m_box.showerror('Error', 'Only digits seperated by space, Try again')
            graph(arr)
    
    btn1 = tk.Button(root, text = "Submit", bg = 'white',command =clicked,justify='center')
    btn2 = tk.Button(root, text = "Cancel", bg = 'white',command = root.destroy,
                 justify='center', highlightcolor='red')
    btn3 = tk.Button(root, text = "Clear",  bg = 'white', command=clear_txt, justify='center')
    btn1.pack()
    btn2.pack()
    btn3.pack()
    root.mainloop()
    
def main():
    gui()


main()


