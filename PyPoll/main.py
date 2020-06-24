import os
import sys
import  csv

# CLearing The ScreenTerminal
os.system('cls')

# Adreess of Source data to read and destination of genarating reports

SavingRoot='analysis/report.txt'
ReadingRootFile='Resources/election_data.csv'

# Just a pop msg for user
input(' Warning!! Genarating report from (' +ReadingRootFile + ') may take few seconds. \n Please be patient ! \n Press ENTER To continue or Ctrl+Z to break.' )
print('\n GENERATING REPORTS . . .')

# Opening and Reading the Data from Source

csvpath = os.path.join(ReadingRootFile)

with open (csvpath) as csvfile :

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)   # Skipping the header

    # Define the Variables

    TotalVote=0           # Counters For number of Vote  
    Candidate=[]          # List of Candidate
    CandidateVote=[]      # List of Number of votes of each Candidate
    

    
    for row in csvreader:                       # Reading the file by Row

      if row[2] not in Candidate:               
        
        # If the name Candidate is not in Candidate list add it and 
        # add 1 for it's first vote in the CandidateVote List
        Candidate.append(row[2])
        CandidateVote.append(1)
      else:
          # Find the index number of the candidate and 1 to the number of thier votes
          x = Candidate.index(row[2])
          CandidateVote[x]=1+int(CandidateVote[x])
      # Adding up the Number of Voters
      TotalVote=TotalVote+1


# Desiging to print the report in the screen

print('\n\n'+'Election Results'+ '\n' + '-------------------------')
print('Total Votes: '+ str(TotalVote) + '\n' 
+'------------------------')

i=0  # counter for looping in the List of Candidate and Candidatevote

print('{:<10s}{:>4s}{:^12s}{:>1.1s}'.format('Candidate','%','Votes',''))
for i in range(len(Candidate)) :
  print('{:<10s}{:>4s}{:^12s}{:>1.1s}'.format(Candidate[i],str(int(round(CandidateVote[i]*100/TotalVote))),str(CandidateVote[i]),'*'))

print('------------------------')

# Indexing the Max Vote from CandidateVote list And them finding the Winner from Candidate list
print ('WINNER :  '+Candidate[CandidateVote.index(max(CandidateVote))])

print('------------------------\n\n')
# Confirming whit user to save the report file by pressing 'y'

if (input('Do you want to save it as a TXT file? (y)es/(n)o?  ')=='y'):
  print ( '\nThe TXT file was genarated in  '+ str(SavingRoot)+'\n\n' )

  sys.stdout= open(SavingRoot,"w")

  # Desiging to print the report in the file

  print('Election Results'+ '\n' + '-------------------------')
  print('Total Votes: '+ str(TotalVote) + '\n' +'------------------------')
  
  i=0
  print('{:<10s}{:>4s}{:^12s}{:>1.1s}'.format('Candidate','%','Votes',''))
  for i in range(len(Candidate)) :
    print('{:<10s}{:>4s}{:^12s}{:>1.1s}'.format(Candidate[i],str(int(round(CandidateVote[i]*100/TotalVote))),str(CandidateVote[i]),'*'))

  print('------------------------')

  # Indexing the Max Vote from CandidateVote list And them finding the Winner from Candidate list
  print ('WINNER :  '+Candidate[CandidateVote.index(max(CandidateVote))])

  print('------------------------')


  sys.stdout.close()
  
  
# a= input('Press any key to Exit')


