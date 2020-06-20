
import os

import  csv
os.system('cls')

csvpath = os.path.join('Resources','budget_data.csv')

with open (csvpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter=',')
  #  print(csvreader)
    csv_header = next(csvreader)
  #  print(f"CSV Header: {csv_header}")
    Rowcount=0
    Total=0
    FirstValue =0
    LastValue =0
    MaxValue=0
    MinValue=0
    DateMax=""
    DateMin=""
    MaxChange=0
    MinChange=0
    MaxChangedate=""
    MinChangedate=""
    PerValue=0



    for row in csvreader:

        print(row)


        if Rowcount== 0 :
            FirstValue = int(row[1])
        else:
            LastValue = int(row[1])

        if int(row[1])> MaxValue :
            MaxValue= int(row[1])
            DateMax = row[0]

        if int(row[1])< MinValue :
            MinValue= int(row[1])
            DateMin = row[0]

        if int(row[1])-PerValue >MaxChange:
            MaxChange =int(row[1])-PerValue
            MaxChangedate = row[0]

        if int(row[1])-PerValue < MinChange:
            MinChange =int(row[1])-PerValue
            MinChangedate = row[0]    
            
        PerValue=int(row[1])

        Total= int(row[1]) + Total
        
        Rowcount= Rowcount +1
    # print(row)
AvarageValue = Total/Rowcount
AvarageChange= (FirstValue-LastValue)/(1-Rowcount)

print ('Total Months: ' + str(Rowcount))
print ('Total: '+ str(Total))
print('Average: '+str(AvarageValue))
#print(str(FirstValue))
#print (str(LastValue))
print('Average Change: '+ str(AvarageChange))
print('MAX: '+ str(DateMax)+':' + str(MaxValue))
print('MIN: '+ str(DateMin)+':' + str(MinValue))
print('Maximum Change: '+ MaxChangedate+':' + str(MaxChange))
print('Miinimum change: '+ MinChangedate +':' + str(MinChange))


