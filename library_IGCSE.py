def counting(array):
    global counter 
    counter = 0
    for i in array:
        counter+=1
    print(f"The array has {counter} elements.")
    return counter

def totalling(array):
    global total 
    total = 0
    for i in array:
        total+=i
    print(f"The total of the elements array is {total}.")
    return total

def linearsearch(array):
    value=float(input("What number do you want to search for in your array?"))
    found=False
    index=0
    while not found and index<len(array):
        if array[index]==value:
            found=True
        else:
            index+=1
        if found == True:
            print(f"Your number has been found at position {index}")
        else:
            print("Your value has not been found in the array.")
        
def bubblesort(array):
    lengtharray = len(array)
    for i in range(lengtharray):
        swapped = False
        for j in range(0, lengtharray-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
            print(array)
        if not swapped:
            break

def minimum(array):
    minimum=array[0]
    for i in array[1:]:
        if i < minimum :
            minimum=i
            print(minimum)
    print(f"The minimum value from {array} is {minimum}")  

def maximum(array):
    maximum=array[0]
    for i in array[1:]:
        if i > maximum :
            maximum=i
            print(maximum)
    print(f"The maximum value from {array} is {maximum}")
    
def average(array):
    totalling(array)
    counting(array)
    average=total/counter
    print(f"The averega of this array {array} is {average}")
    