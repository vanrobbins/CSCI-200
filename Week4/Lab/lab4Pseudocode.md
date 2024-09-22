# Lab 4 Pseudocode

## Van Robbins 9/21/2024

### Executable File

~~~[python]
    import utility file
    Create a function that asks for the user to select a shape
    print("What shape would you like to draw?");
    shape=int(input("1| Square\n2| Rectangle\n 3| Equilateral Triangle 4| Circle"));
    if shape=!1 or shape=!2 or shape=!3 or shape!=4:
        print("Please pick a valid shape by entering a number 1-4");
        recall function for user to try again
    elif shape==1
        sizeEq= call sizeEqualWL function from utility file shape will have same length and width
        call square function with sizeEq;
    elif shape==3
        sizeEq= call sizeEqualWL function
        call triangle function with sizeEq;
    elif shape==4
        sizeEq= call sizeEqualWL function
        call circle function with sizeEq;
    else
        sizeDiff= call sizeDiffWL function from utility file shape has different length and width results in array
        width= sizeDiff[0];
        length= sizeDiff[1];
        call rectangle function with width and length
~~~

### Utility File

~~~[python]
def sizeEqualWL()
    wl=int(input("Please enter the size of a side or radius of the shape (2-10)"));
    return wl;

def sizeDiffWL()
    print("Please enter the width and length of the shape of the shape (2-10)")
    w=int(input("Width: "))
    l=int(input("Length: "))
    else:
     return w,l;
def size
def square(size)
    Use loop to print out * the number of times of the size for first line
    Use loop to print out *, spaces in the amount of size-2 and another *
    Use loop to print out * the number of times of the size for final line of shape
def triangle(size)
    mid=int(size/2)
    spaceBetween=0
    spaceOutside=mid
    Use loop to print out spaces to equal mid then *
    Use loop that each time is run adds 1 to spaceBetween:
        print out spaces to equal spaceOutside=spaceOutside-1 
        then *
        then spaces equal to spaceBetween then another * 
        until spaceBetween = mid
    Use loop to print out * the number of times of the size for final line of shape
def rectangle(sizeW,sizeL)
    Use loop to print out * the number of times of the sizeW for first line
    Use loop to print out *, spaces in the amount of sizeW-2 and another * until as long as sizeL-2
    Use loop to print out * the number of times of the sizeW for final line

~~~
