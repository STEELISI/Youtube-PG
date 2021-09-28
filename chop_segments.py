#=============================================================================================================#
#  HOW TO RUN?                                                                                                #
#  python3 chop_segments.py                                                                                   #
#  Please provide LABEL, SEGMENT_LENGTH, OUTPUT_PATH, INPUT_FILE_TO_CHOP.                                     #
#=============================================================================================================#
import csv
import sys
import nltk
from nltk import tokenize
#=============================================================================================================#
LABEL = 1
SEGMENT_LENGTH = 100
OUTPUT_PATH = "APPROPRIATE.CSV"
INPUT_FILE_TO_CHOP = "SAMPLE_INPUT_FILE.txt"
#=============================================================================================================#
#When we run the script for appropriate channels, we set the LABEL as 1 else we set it as 0 for inappropriate #
#=============================================================================================================#
visited = set()
## To ensure there are no duplicate video IDs
s = ""
cur = ""
prev = []
flag = 0
identifier = 0

#=============================================================================================================#
f = open(INPUT_FILE_TO_CHOP)
with open(OUTPUT_PATH, 'w') as csvfile:
    fieldnames = ['','Unnamed: 0','Unnamed: 0.1','Transcript','ID','Label']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'': '', 'Unnamed: 0': 'Unnamed: 0', 'Unnamed: 0.1': 'Unnamed: 0.1', 'Transcript' : 'Transcript', 'ID' : 'VIDEO ID', 'Label' : 'Label'})
    for line in f:
        # Channel IDs are present in lines containing ||||
        if("||||" in line):
            continue
        # Video IDs are present in lines containing ####
        if("####" in line):
            cur = line.strip()
            if(flag == 1):
                identifier  +=1
                text = s.strip()
                groups = nltk.word_tokenize(text)
                n_split_groups = []
                while len(groups):
                    n_split_groups.append(' '.join(groups[:SEGMENT_LENGTH]))
                    groups = groups[SEGMENT_LENGTH:]
                for part in n_split_groups:
                    writer.writerow({'': identifier, 'Unnamed: 0': identifier, 'Unnamed: 0.1': identifier, 'Transcript' : part, 'ID' : prev[1], 'Label' : LABEL })
                print("PROCESSED VIDEO ID",str(prev[1]))
                flag = 0
     
        if("####" in line  and (line.strip() not in visited)):
            s = ""
            flag = 1
            visited.add(line.strip())
            prev = cur.split("####")
        if("####" not in line and flag == 1):
            s += line.strip() + " "
    if(flag == 1):
        identifier +=1
        text = s.strip()
        groups = nltk.word_tokenize(text)
        n_split_groups = []
        while len(groups):
            n_split_groups.append(' '.join(groups[:SEGMENT_LENGTH]))
            groups = groups[SEGMENT_LENGTH:]
        for part in n_split_groups:
            writer.writerow({'': identifier, 'Unnamed: 0': identifier, 'Unnamed: 0.1': identifier, 'Transcript' : part, 'ID' : prev[1], 'Label' : LABEL })
#=============================================================================================================#



