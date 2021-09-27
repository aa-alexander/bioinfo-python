#to get the best hit form the blast results output

#read the blast result file
fh = open("resultfile", "r").readlines()

#creating an empty dictionary
Hit_dict = {}

#loop to take the hit id and the score and make them as dictionary
#it creates a dict with unique key and the multiple hits of the same key values are made into a list
for line in fh:
    Id,score = line.split("\t",11)[0],float(line.split("\t",11)[-1])
    Hit_dict.setdefault(Id,[]).append(score)

#create new dictionary for the best max score
BH_dict = {}
for Id,score in Hit_dict.items():
    max_score = max(score)
    BH_dict[Id] = max_score

#comparing to the intial file and printing the entire line
for line in fh:
    Hits = line.split("\t",11)
    for k,v in BH_dict.items():
        if k == Hits[0]:
            if v == float(Hits[-1]):
                print(line, end ='')
