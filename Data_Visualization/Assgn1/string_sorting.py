import random
import string
import matplotlib.pyplot as plot

"""Function to sort the strings with respect to first character."""
def sortListOfStrings(list_of_strings, list_index):
    print("\n" + "List" + str(list_index) + " before sorting", list_of_strings)
    list_size = len(list_of_strings)
    for i in range(list_size):
        for j in range (i, list_size):
            if (list_of_strings[i]>=list_of_strings[j]):
                list_of_strings[i],list_of_strings[j] = list_of_strings[j],list_of_strings[i]
    print("\n" + "List" + str(list_index) + " after sorting", list_of_strings)

"""Function to plot the strings with respect to their lengths"""
def scatterPlotOfStringLengths(list_of_strings, figure_index):
    xaxis = []
    for i in range(len(list_of_strings)):
        xaxis.append(i)
    yaxis = []
    for i in list_of_strings:
        yaxis.append(len(i))
     
    plot.scatter(xaxis,yaxis)
    plot.xlabel('string indexes in the list')
    plot.ylabel('lengths of strings')
    plot.suptitle('Figure_' + str(figure_index) + ': string order after sorting versus their lengths')
    plot.show(block="false")

"""Function to generate a random string of random length """
def randomStringGenerator():  
    choice_of_chars = string.printable
    strLen = random.randint(1,5)
    return ''.join(random.choice(choice_of_chars) for i in range(strLen))

"""generating five lists of strings using randomStringGenerator function"""

""" Test case 1"""
list1 = []
for n in range(1, 501, 1):
     list1.append(randomStringGenerator())
sortListOfStrings(list1, 1)
scatterPlotOfStringLengths(list1, 1)

""" Test case 2"""
list2 = []
for n in range(1, 501, 1):
     list2.append(randomStringGenerator())
sortListOfStrings(list2, 2)
scatterPlotOfStringLengths(list2, 2)

""" Test case 3"""
list3 = []
for n in range(1, 501, 1):
     list3.append(randomStringGenerator())
sortListOfStrings(list3, 3)
scatterPlotOfStringLengths(list3, 3)

""" Test case 4"""
list4 = []
for n in range(1, 501, 1):
     list4.append(randomStringGenerator())
sortListOfStrings(list4, 4)
scatterPlotOfStringLengths(list4, 4)

""" Test case 5"""
list5 = []
for n in range(1, 501, 1):
     list5.append(randomStringGenerator())
sortListOfStrings(list5, 5)
scatterPlotOfStringLengths(list5, 5)
