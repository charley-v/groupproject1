import time
import ast
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import numpy as np
import sys

print(sys.getrecursionlimit)
sys.setrecursionlimit(10000)

#algorithms

#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
#quick sort
def quick_sort(arr, key = lambda x: x):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if key(x) <= key(pivot)]
        greater = [x for x in arr[1:] if key(x) > key(pivot)]
        return quick_sort(less, key) + [pivot] + quick_sort(greater, key)
#merge sort
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

#gui application
def graph():
    #create instance of tkinter
    root = tk.Tk()
    #title of the window
    root.title("Sorting Algorithms")
    
    #title and input dialog box for elements
    index_label = tk.Label(root, text="Enter the number of\n elements in the array")
    index_label.grid(row=2, column=0, sticky = "W")  
    user_index = tk.Entry(root, width = 10)
    user_index.grid(row=2, column=0, padx = 150, sticky= "W")  
    
    #title and input dialog box for array
    label = tk.Label(root, text="Array")
    label.grid(row=2, column=0, padx = 250, sticky = "W")    
    array_text = tk.Entry(root, width= 70)
    array_text.grid(row=2, column=0, padx = 300,sticky= "W")

        
    #clear button
    def clear_txt():
        array_text.delete(0,'end')
        user_index.delete(0,'end')
        fig = plt.figure(figsize=(8,7), dpi = 100)
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=3)

    #generate array button
    def generate():
        try:
            # Get user input 
            user_input = int(user_index.get())
            # Generate a random array with user input length
            random_array = [random.randint(1, 1000) for x in range(user_input)]

        # Display the random array in the result entry widget
            array_text.delete(0, tk.END)
            #turn it into a string so user can add more to the array if they want
            array_text.insert(0, str(random_array)) 
          
        except ValueError:
            # Handle the case where the user input is not a valid integer
            array_text.delete(0, tk.END)
            array_text.insert(0, "Invalid input. Please enter a valid integer.")
    
    #run comparison button
    def run():
        gen_array = array_text.get()
        new_arr = ast.literal_eval(gen_array)
        new_arr = [int(element) for element in new_arr]
        
        #list of different sorts
        sorts = {'Bubble Sort': bubble_sort, 
                'Merge Sort' : mergeSort, 
                'Quick Sort' : quick_sort}
        
        #array for times
        run_times = []
        #measures execution time for each sort
        for sort in sorts.values():
            start_time = time.time()
            sort(new_arr)
            end_time = time.time()
            elapsed_time = end_time - start_time
            run_times.append(elapsed_time*1000)
        for i in range(len(run_times)):
            print(run_times[i])
        
        #create bar graph
        fig = plt.figure(figsize=(8,7), dpi = 100)
        labels = ("Bubble Sort", "Merge Sort", "Quick Sort")
        #arrange labels equidistant from each other
        label_position = np.arange(len(labels))
        times = [run_times[0], run_times[1], run_times[2]]
        color = ['red', 'blue', 'purple']
        
        #what information goes in each bar 
        plt.bar(label_position, times, align='center', alpha=1.0, color = color)
        plt.xticks(label_position, labels)
        plt.ylabel('Time (ms)')
        plt.xlabel("Sorting Algorithms")
        plt.tight_layout(pad = 2.2, w_pad = 0.5, h_pad = 0.1)
        plt.title('Comparing Sorting Algorithms')
        
        #adds text to axes
        for index, datapoints in enumerate(times):
            plt.text(x = index, y = datapoints, s = f"{datapoints}", fontdict = dict(fontsize = 10), ha='center', va = 'bottom')
        
        #show the bar graph in tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0, columnspan=3)  # Adjust columnspan as needed
        
    #generate array button
    btn0 = tk.Button(root, text = "Generate", bg = 'white', command = generate).grid(row = 3, column = 0, padx = 150, sticky= "W")
    #submit and run code button
    btn1 = tk.Button(root, text = "Run", bg = 'white', command = run, justify='center').grid(row = 3, column = 0)
    #end program button
    btn2 = tk.Button(root, text = "Exit", bg = 'white',command = root.destroy, justify='center', highlightcolor='red').grid(row = 4, column = 0)
    #clear fields button
    btn3 = tk.Button(root, text = "Clear",  bg = 'white', command=clear_txt, justify='center').grid(row = 5, column = 0)

    #frame = tk.Frame(root)    

    root.mainloop()
    
def main():
    graph()


main()
