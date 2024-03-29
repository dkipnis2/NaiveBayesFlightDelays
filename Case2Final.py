#Case Study 2
#Group Steven, Danny, Misha, Huayang

import csv

#this function generates a list of every attribute, its column number, and
#its respective number of nos and yeses from a given data set
def genArr(ex):
    atr = []
    ind = len(ex[0])-1
    for i in range(0,ind):
        for row in ex:
            add=True
            for ent in atr:
                if(ent[1]==row[i] and ent[0]==i):
                    add=False
                    if(row[ind]==0):
                         ent[2]+=1
                    if(row[ind]==1):
                         ent[3]+=1
            if(add):
                atr.append([i,row[i],0,0])
                if(row[ind]==0):
                     atr[len(atr)-1][2]+=1
                if(row[ind]==1):
                     atr[len(atr)-1][3]+=1
    return atr

#This function returns the total number of Yeses and Nos
#in a list generated by the gen Arr function
def YNNum(ex):
    numYes = 0
    numNo = 0
    #makes sure it only gets number of nos and yeses for one column
    #such that it does not double count
    check = ex[0][0]
    for row in ex:
        if(check == row[0]):
            numYes += int(row[3])
            numNo += int(row[2])

    return [numYes,numNo]
######################
#                    #
#     Example 1      #
#                    #
######################

#this was just used to test that our method worked

ex0 = [[1,'DFW','ORD','Delta',1],
       [2,'DFW','ORD','Delta',0],
       [3,'DFW','ORD','Delta',1],
       [4,'LAX','ORD','Delta',0],
       [5,'LAX','ORD','United',1],
       [6,'LAX','LGA','United',0],
       [7,'LAX','LGA','United',1],
       [8,'LAX','LGA','Delta',0],
       [9,'DFW','LGA','United',0],
       [10,'DFW','ORD','United',1]]

print('\n\nExample 1\n')
l = genArr(ex0)
#for row in l:
#    print(row)
    
m = 3
p = 0.5
numArr = YNNum(l)
numYes = numArr[0]
numNo = numArr[1]

probD = numYes/(numYes+numNo)
probND = numNo/(numYes+numNo)
for row in l:
    if row[1] == 'DFW':
        probD *= (row[3]+m*p)/(numYes+m)
        probND *= (row[2]+m*p)/(numNo+m)
    elif row[1] == 'LGA':
        probD *= (row[3]+m*p)/(numYes+m)
        probND *= (row[2]+m*p)/(numNo+m)
    elif row[1] == 'Delta':
        probD *= (row[3]+m*p)/(numYes+m)
        probND *= (row[2]+m*p)/(numNo+m)

if(probD > probND):
    print('Delayed')
else:
    print('Not Delayed')
print(probD)
print(probND)

######################
#                    #
#     Exercise 1     #
#                    #
######################

ex1 = [[1,'SEA','ATL','Southwest','Poor',0],
       [2,'SEA','BOS','American','Good',1],
       [3,'SEA','ATL','United','Poor',1],
       [4,'SFO','BOS','Southwest','Poor',1],
       [5,'SFO','ATL','American','Good',0],
       [6,'SFO','BOS','United','Poor',1],
       [7,'SFO','BOS','United','Good',0],
       [8,'SEA','BOS','Southwest','Poor',1]]

print('\n\nExercise 1\n')
l = genArr(ex1)
    
m = 4
p = 0.5
numArr = YNNum(l)
numYes = numArr[0]
numNo = numArr[1]

#probD starts as P(Y) and probND starts as P(N), and then the
#this number is multiplied by the probabilities of the needed
#attributes
probD = numYes/(numYes+numNo)
probND = numNo/(numYes+numNo)

#goes through the list which contains each attribute and the number of nos
#and yeses of that attribute, calculating the naive bayes probability if
#it is an attribute in the problem
for row in l:
    if row[1] == 'SEA':
        probD *= (row[3]+m*p)/(numYes+m)
        probND *= (row[2]+m*p)/(numNo+m)
        probT = (row[3]+row[2])/(numYes+numNo)
    elif row[1] == 'ATL':
        probD *= (row[3]+m*p)/(numYes+m)
        probND *= (row[2]+m*p)/(numNo+m)
    elif row[1] == 'Southwest':
        probD *= (row[3]+m*p)/(numYes+m)
        probND *= (row[2]+m*p)/(numNo+m)
    elif row[1] == 'Good':
        probD *= (row[3]+m*p)/(numYes+m)
        probND *= (row[2]+m*p)/(numNo+m)

print('Flight SEA-ATL on Southwest in good weather')
print('P(Delayed|SEA,ATL,Southwest,Good) ∝ ' + str(probD))
print('P(Not Delayed|SEA,ATL,Southwest,Good) ∝ ' + str(probND))
if(probD > probND):
    print('Delayed')
else:
    print('Not Delayed')
    

##################
##  Exercise 2  ##
##################
    
print('\n\nExercise 2\n')

with open('\\\\ad.uillinois.edu\\engr\\Instructional\\dkipnis2\\documents\\Case2\\FlightDelay.csv', 'rt') as f:
    reader = csv.reader(f)
    ex2 = list(reader)

exf = []
#gets rid of column headings
ex2.pop(0)


#determines whether or not a flight is delayed by summing its
#delays and then creating a new list which includes the resulting
#delay value, 0 means not delayed and 1 means delayed
for row in ex2:
    if(int(row[3])+int(row[4]) > 15):
        exf.append([row[0],row[1],row[2],1])
    else:
        exf.append([row[0],row[1],row[2],0])

print('Example lines from exercise 2')
print('0 means not delayed, 1 means delayed')
print(exf[0])
print(exf[11])
print(exf[1122])
print(exf[2233])
print(exf[844])
print(exf[555])
print(exf[2266])
print(exf[277])
print(exf[188])

##################
##  Exercise 3  ##
##################

print('\n\nExercise 3\n')

l = genArr(exf)

m = 3
p = 0.5
numArr = YNNum(l)
numYes = numArr[0]
numNo = numArr[1]

#array of origins, destinations, and carriers
p2 = [['JFK','LAS','AA'],
      ['JFK','LAS','B6'],
      ['SFO','ORD','VX'],
      ['SFO','ORD','WN']]

#loop to compute needed probabilities in the question
for row in p2:
    ori = row[0]
    dest = row[1]
    carr = row[2]

    probD = numYes/(numYes+numNo)
    probND = numNo/(numYes+numNo)

    #goes through the list which contains each attribute and the number of nos
    #and yeses of that attribute, calculating the naive bayes probability if
    #it is an attribute in the problem
    for ent in l:
        if ent[1] == ori:
            probD *= (ent[3]+m*p)/(numYes+m)
            probND *= (ent[2]+m*p)/(numNo+m)
        elif ent[1] == dest:
            probD *= (ent[3]+m*p)/(numYes+m)
            probND *= (ent[2]+m*p)/(numNo+m)
        elif ent[1] == carr:
            probD *= (ent[3]+m*p)/(numYes+m)
            probND *= (ent[2]+m*p)/(numNo+m)

    print('Flight ' + ori + '-' + dest + ' on ' + carr)
    print('P(Delayed|'+ori+','+dest+','+carr+') ∝ '+ str(probD))
    print('P(Not Delayed|'+ori+','+dest+','+carr+') ∝ '+ str(probND))
    if(probD > probND):
        print('Delayed')
    else:
        print('Not Delayed')

    print('\n')

