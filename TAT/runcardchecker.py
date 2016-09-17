import re

file = raw_input("Enter file name: ")
if len(file) < 1: file = "Runcards.txt"
fhand = open(file)
numlist = list()

print "\nSearching for invalid times...\n"

for line in fhand:
    pieces = line.split()
    for i in pieces:
        if re.search('57973:13', i):    #using regex
        #if i == "57973:13" or i == '"57973:13' or i == '57973:13"':
            print "Station cannot reach boxpoly: " + pieces[0]
    else:
        continue

print "DONE."

#KEVIN WAS HERE
#DAVID WAS HERE