#to count the number of fasta files in a multifasta file

fastaLines = open("path/to/multisequence.fasta","r").readlines()
#print(fastaLines)

#print(fastaLines[0])
#print(fastaLines[1])

for i in range(len(fastaLines)):
    if fastaLines[i].startswith('>'):
      print(fastaLines[i], end="")
