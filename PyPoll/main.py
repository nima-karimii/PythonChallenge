import os

import  csv
os.system('cls')

csvpath = os.path.join('Resources','election_data.csv')

with open (csvpath) as csvfile :
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)


    TotalVote=0
    Candidate=[]
    CandidateVote=[]
    K=0

    print (csv_header)
  

    for row in csvreader:
      if row[2] not in Candidate:
        Candidate.append(row[2])
        CandidateVote.append(1)
      else:
          x = Candidate.index(row[2])
          CandidateVote[x]=1+int(CandidateVote[x])
      TotalVote=TotalVote+1


print(Candidate)
print(CandidateVote)

