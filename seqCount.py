#to count the number of sequence in each fasta file

#read the file as single string
fasta = open("path/to/multisequence.fasta", "r").read()

#split the string from the fastaheader
list = fasta.split('>')

#since the first line starts with the fastaheader there would be an empty element created. del that first element
del list[0]

#for loop to iterate through the list
for line in list:
    [fastaHeader,seq] = line.split("\n",1)       #splitting the title/name of the file and the seq for each fasta file
    fastaHeader = fastaHeader.split(" ",1)[0]    
    seq = [i for i in seq if i.strip() != ""]    
    print(fastaHeader, "\t", len(seq))
