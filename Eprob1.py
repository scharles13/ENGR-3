#have to start by making a varible sum
sum = 0
#the problem says under 1000 so the range is between 3 and 1000
for x in range (3,1000):
    #if then statement describing how each number must be divisable by either 3 or 5
    if x%3 == 0 or x%5 == 0:
        #then you have to add up all the multiples you got from the line above to get the sum of the question
        sum += x
print sum
