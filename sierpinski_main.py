from math import factorial

"""Program works by creating a Pascal's Triangle, and assigning each odd number a
triangle that would be printed out in various 'stages' """


#the NCR operation in mathematics used in the binomial expansion
def NCR(n,r):
    n_factorial = 1

    for i in range(r):
        n_factorial *= (n-i)
        
    value = n_factorial//(factorial(r))

    return value


#function to create a row of the pascal triangle
def pascal(n):
    row = []

    i = -1
    while i < n:
        i += 1
        row.append(NCR(n,i))
        
    return row

#the triangle itself separated in various 'stages'
def triangle(dimension,currentStage,blank=False,first=False):

    """if the size of the overall sierpinski triangle isn't too large, then we can have a triangle which
    is separated in three """
    
    if dimension == 3:
        stages= ['    /\\','  /  \\','/____\\']

    #if it's too big, then it's a triangle separated in two
    else:
        stages = ['  /\\','/__\\']
    
    #if there's no triangle, the blank equivalent of the 'stage' is returned
    if blank:
        
        return ' '*(len(stages[currentStage]))

    #if it's the first triangle then the spacing is different
    if first:
        return stages[currentStage].strip()
        
    return stages[currentStage]

#the function assigning the triangle 'stages' to the pascal odd numbers
def pascal_triangulator(dimension,stage,n):

    row = pascal(n)
    triangleRow = ''

    for x in row:
        if not x%2:
            #setting even numbers to False
            row[row.index(x)] = 0

    #to identify the first triangle in each row
    k = 0
    
    for e in row:
        k += 1
       
        if k == 1:
            triangleRow += triangle(dimension,stage,False,True)
        elif e:
            triangleRow += triangle(dimension,stage)
        else:
            triangleRow += triangle(dimension,stage,True)

    return triangleRow


#main function
def sierpinski(size):

    totalIterations = 2**size
    dimension = 3

    #if too big, then the dimension of each triangle is 2
    if size >= 5:
        dimension = 2

    for sierpinskiRow in range(totalIterations):
        for subRow in range(dimension):

            #the spacing before the triangles is determined by this operation
            subRowStages = ' '*(int(totalIterations/2)*dimension*2 - sierpinskiRow*dimension - subRow - 1)

            subRowStages += pascal_triangulator(dimension,subRow, sierpinskiRow)

            print(subRowStages)

#######################################################################################################################################

""" Program designed and made by Gabriele Trotta
Start: 17/02/20 22:01
End: 17/02/20 22:57

To enhance the effect of the Sierpinski triangle, you could modify the font size of
the editor, through this and changing the font_size to 1 in configDialog.py,
I managed to create a Sierpinski triangle of size 8, or-else a triangle with a base of 1024 characters.
If using font 1, preferbly use fonts such as Courier New Baltic or Forte."""

