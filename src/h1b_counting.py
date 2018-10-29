
# Author: Shaily Parikh
# Date: 29th October 2018

import csv
import sys

occupation_dictionary={}
state_dictionary={}
is_header=True
input_file=sys.argv[1]
occupation_output=sys.argv[2]
state_output=sys.argv[3]
# Read file and maintain dictionary to count occupation occurences and dictionary to count state occurences
with open(input_file, 'r') as f:
    reader = csv.DictReader(f, delimiter=';', quoting=csv.QUOTE_ALL)
    for row in reader:
        if is_header:
            is_header=False
            for i in row.keys():
                # identify column name with SOC_NAME that has occupation name information.
                if i.lower().find("soc_name")!=-1:
                    column_name_occupation=i
                    break
            for i in row.keys():
                # identify column name with STATE but not EMPLOYER that has state information.
                if i.lower().find("state")!=-1:
                    if i.lower().find("employer")==-1:
                        column_name_state=i
                        break
        # Maintain occupation occurences count        
        if row[column_name_occupation] in occupation_dictionary:
            occupation_dictionary[row[column_name_occupation]]+=1
        else:
            occupation_dictionary[row[column_name_occupation]]=1
          
        # Maintain state occurences count     
        if row[column_name_state] in state_dictionary:
            state_dictionary[row[column_name_state]]+=1
        else:
            state_dictionary[row[column_name_state]]=1
     



# Calculate total occupation counts
total_occupation=sum(occupation_dictionary.values())
# Calculate total state counts
total_state=sum(state_dictionary.values())



occupation_count=list(((key,value) for key,value in occupation_dictionary.items()))
# Sort occupation-count pair in descending order by count
occupation_count.sort(key=lambda x: (-x[1],x[0]))

state_count=list(((key,value) for key,value in state_dictionary.items()))
# Sort state-count pair in descending order by count
state_count.sort(key=lambda x: (-x[1],x[0]))

def write_output(file_name,counts,header):
    output_file = open(file_name,"w")
    output_file.write(header)
    for i in counts[0:10]:
        output_file.write(str(i[0])+";"+str(i[1])+";"+str(round((i[1]*100/total_occupation)+0.0,1))+"%\n")
    output_file.close()


# Take 10 most common occupation-count pair and write them to the output file.
write_output(occupation_output,occupation_count,"TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")


# Take 10 most common state-count pair and write them to the output file.
write_output(state_output,state_count,"TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")






