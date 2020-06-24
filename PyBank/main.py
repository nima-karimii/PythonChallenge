
# Please First run it in your Terminal , Thanks ;)


import os
import sys
import csv
import shutil
from colorama import Fore, Back, Style 


# CLearing The ScreenTerminal
os.system('cls')

# Adreess of Source data to read and destination of genarating reports

SavingRoot='analysis/report.txt'
ReadingRootFile='Resources/budget_data.csv'

# Opening and Reading the Data from Source

csvpath = os.path.join(ReadingRootFile)

with open (csvpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
  
    # Define the Variables
    Rowcount=0               #RowCounter
    Total=0                  #Sum up the Profit/Loose
    FirstValue =0            #First Profit/Loose
    FirstDay=""              #First Day of Profit/Loose
    LastValue =0             # LAst Profit/Loose
    LastDay=""               #Last Day of Profit/Loose
    MaxValue=0               # MAx Profit/Loose
    MinValue=0               # Min Profit/Loose
    DateMax=""               # Date of Max Profit/Loose
    DateMin=""               # DAte of Min Profit/Loose
    MaxChange=0              # Maximum change in 2 Days
    MinChange=0              # Minimum Change in 2 Days
    MaxChangedate=""         # Day of Maximum Change
    MinChangedate=""         # Day of Minimum Change
    PerValue=0               # Previuse day Profit/Loose



    for row in csvreader:

       # Finding the first value and Last value for caculating the Avrage change
        if Rowcount== 0 :
            FirstValue = int(row[1])
            FirstDay = row[0]    
        else:
            LastValue = int(row[1])
            LastDay = row[0]
            
        # Finding the MAximum Profit and the date
        if int(row[1])> MaxValue :
            MaxValue= int(row[1])
            DateMax = row[0]

        #Finding the Maximum Loose and the date
        if int(row[1])< MinValue :
            MinValue= int(row[1])
            DateMin = row[0]

        # Finding the MAximum Profit change  and the date
        if int(row[1])-PerValue >MaxChange:
            MaxChange =int(row[1])-PerValue
            MaxChangedate = row[0]

        # Finding the MAximum Loose change and the date
        if int(row[1])-PerValue < MinChange:
            MinChange =int(row[1])-PerValue
            MinChangedate = row[0]    
            
        # For the Next Loop we need the The Value of the previous Profit/Loose to calculate the change 
        PerValue=int(row[1])

        # Calculating the sum of Profit/Loose
        Total= int(row[1]) + Total
        
        #Cunting the number of days
        Rowcount= Rowcount +1
    # print(row)

#Calculating the Avrage of Profit/Loose  
AvarageValue = Total/Rowcount

#Calculating the Avrage change of Profit/Loose
AvarageChange= (FirstValue-LastValue)/(1-Rowcount)

# Printing the report on Screen
print(Fore.RED+"Financial Analysis From "+ FirstDay+ ' to ' +LastDay)
print("--------------------------------------------"+Style.RESET_ALL)
print(('{:<20s}{:<10s}{:^12s}{:>1.1s}'.format('Total Months: ',str(Rowcount),'*','*')))
print(('{:<20s}{:<10s}{:^12s}{:>1.1s}'.format('Total : ',str(Total),'*','*')))
print(('{:<20s}{:<10.2f}{:^12s}{:>1.1s}'.format('Avarage : ',AvarageValue,'*','*')))
print(('{:<20s}{:<10.2f}{:^12s}{:>1.1s}'.format('Avarage Change: ',AvarageChange,'*','*')))
print(('{:<20s}{:<10s}{:^12s}{:>1.1s}'.format('MAX Profit :  ',str(DateMax) , '+'+str(MaxValue),'*')))
print(('{:<20s}{:<10s}{:^12s}{:>1.1s}'.format('MIN Looses :  ',str(DateMin) , str(MinValue),'*')))
print('\n')
print(Fore.GREEN+'Greatest Increase in Profits: '+ MaxChangedate+' : ' + str(MaxChange))
print('Greatest Decrease in Profits: '+ MinChangedate +' : ' + str(MinChange)+'\n'+Style.RESET_ALL)

# 
if (input('Do you want to save it as a TXT file? (y)es/(n)o?--->  ')=='y'):
  print ( '\nThe TXT file was genarated in  '+ str(SavingRoot)+'\n\n' )
  
  sys.stdout= open(SavingRoot,"w")
  print("Financial Analysis From "+ FirstDay+ ' to ' +LastDay)
  print("----------------------------")
  print(('{:<20s}{:<10s}{:^12s}{:>1.1s}'.format('Total Months: ',str(Rowcount),'*','*')))
  print(('{:<20s}{:<10s}{:^12s}{:>1.1s}'.format('Total : ',str(Total),'*','*')))
  print(('{:<20s}{:<10.2f}{:^12s}{:>1.1s}'.format('Avarage : ',AvarageValue,'*','*')))
  print(('{:<20s}{:<10.2f}{:^12s}{:>1.1s}'.format('Avarage Change: ',AvarageChange,'*','*')))
  print(('{:<20s}{:<10s}{:^12s}{:>1.1s}'.format('MAX Profit :  ',str(DateMax) , '+'+str(MaxValue),'*')))
  print(('{:<20s}{:<10s}{:^12s}{:>1.1s}'.format('MIN Looses :  ',str(DateMin) , str(MinValue),'*')))

  print('\n')
  print('Greatest Increase in Profits: '+ MaxChangedate+' : ' + str(MaxChange))
  print('Greatest Decrease in Profits: '+ MinChangedate +' : ' + str(MinChange)+'\n')

  
  
  sys.stdout.close()

