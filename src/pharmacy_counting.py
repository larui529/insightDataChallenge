#################################################################
# Author: Rui La
# University of California, San Diego
# Email: larui529@gmail.com
# insight data engineering data challenge
#################################################################
import sys
import StringIO
import csv

# function to loaddata line by line
def loaddata(filename):
    f = open(filename, "rb")
    dataset = list(f.readlines())[1:]
    for i in range(len(dataset)):
        #dataset[i] = [x.strip() for x in dataset[i].split(',')]
        s = StringIO.StringIO(dataset[i])
        dataset[i] = list(csv.reader(s, skipinitialspace=True))[0]
    return dataset

# function to process data
def processData(dataset):
    names = {} # store user name of each drug
    total_cost = {} # store total cost of each drup
    
    # 0: id, 1: last_name, 2: first_name, 3: drug_name, 4: drug_cost
    for i in xrange(len(dataset)):
        #print dataset[i][3]
        if dataset[i][3] not in names: # if names doesn't contain drup
            names[str(dataset[i][3])] = [dataset[i][1]+dataset[i][2]]
        else:
            names[str(dataset[i][3])] += [dataset[i][1]+dataset[i][2]]
        if dataset[i][3] not in total_cost:
            total_cost[str(dataset[i][3])] = float(dataset[i][4])
            #print float(dataset[i][4])
        else:
            total_cost[str(dataset[i][3])] += float(dataset[i][4])
            #print float(dataset[i][4])
    output = []
    for key, _ in names.iteritems():
        if total_cost[key]%1 == 0: # convert float to int if there is no decimal part
            total_cost[key] = int(total_cost[key])
        output.append([key, len(set(names[key])), total_cost[key]])
    output = sorted(output, key = lambda x: (-x[2], x[0]))
    return output

# output result
def outputData(filename):
    outF = open(filename, "w")
    outF.write('drug_name,num_prescriber,total_cost')
    outF.write("\n")
    for line in output:
        print line
        outF.write(",".join(map(str, line)))
        outF.write("\n")
    outF.close()
    
filename = sys.argv[1]
dataset = loaddata(filename)
output = processData(dataset)
outputData(sys.argv[2])