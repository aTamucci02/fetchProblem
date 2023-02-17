import csv
import sys
def spendPoints(toSpend:int,fileName): 
    with open(fileName, 'r') as file:
        transList=[]
        csvreader = csv.reader(file)
        for row in csvreader:
            transList.append(row)
    del transList[0]
    points = 0
   


    for transaction in transList:
        points+=int(transaction[1])
    if points<toSpend:
        return "ERROR: NOT ENOUGH POINTS TO SPEND"
    
    mergeSort(transList)
    i=0 
    while toSpend>0:
        int(transList[i][1])
        if int(transList[i][1])>toSpend:
            transList[i][1]=f"{int(transList[i][1])-toSpend}"
            toSpend=0
            break
        
        toSpend-=int(transList[i][1])
        transList[i][1]="0"
        i+=1
        
    
    payerList={}
    for transaction in transList:
        if(not(transaction[0]in payerList)):
            payerList.update({transaction[0]:transaction[1]})
        else:
            points = int(payerList.get(transaction[0]))
            points += int(transaction[1])
            payerList.update({transaction[0]:f"{points}"})
            #print(payerList)  
        
            
    return payerList

def mergeSort(transList):
    if len(transList) > 1:
        mid = len(transList)//2
        left = transList[:mid]
        right = transList[mid:]
        mergeSort(left)
        mergeSort(right) 
        i = 0 
        j = 0 
        k = 0
        while i < len(left) and j < len(right):
            if left[i][2] <= right[j][2]:
                transList[k] = left[i]
                i += 1
            else:
                transList[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            transList[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            transList[k] = right[j]
            j += 1
            k += 1
            
    return transList
#TODO need to move the payerList method up. Need to make list of payers ealier. 
# Otherwise you check points and you return error. I think I need to return a list of the values as 0
#change
print(spendPoints(int(sys.argv[1]),sys.argv[2]))
