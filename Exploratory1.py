#averages list
def average(blank):
    sum = 0
    for element in blank:
        sum += element
    average = sum/float(len(blank))
    return average
#prints the average of 4,9, and 5
print average([4,9,5])
#prints average of variable, tree
tree = [6,7,8,9]
print average(tree)

x = average([30,12,56])
print x
