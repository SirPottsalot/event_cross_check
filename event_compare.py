#! /bin/env python3
# import librarys
import argparse

# function
def AutocraticCommonalityDectectorino(a,b,c):
    return ['Date: {} Time: {} Time_Diff: {}'.format((x[0]),(y[1][0:-1]),str(round(abs(float(x[1])-float(y[1])),9)))  for x in a for y in b  if x[0] == y[0] and round(abs(float(x[1])-float(y[1])),9) <= c]

#Get arguments from command line to get path to file
parser = argparse.ArgumentParser(description = 'This script is designed to look at the event lists times from FD and SD to find coincidence events.')
parser.add_argument('-FD',metavar='/path/to/file',default='C:/Users/Potts/github/event_cross_check/ps5_events.txt',action='store',help='Path to the FD event list (default ./ps5_events.txt)')
parser.add_argument('-SD',metavar='/path/to/file',default='C:/Users/Potts/github/event_cross_check/EVENTS.txt',action='store',help='Path to the SD event list (default ./EVENTS.TXT)')
args = parser.parse_args()

# Store all varibles into lists
sd_events = [x.split(' ')[1:3] for x in open(args.SD,'r').readlines()]
fd_events = [x.split(' ')[1:3] for x in open(args.FD,'r').readlines()]

# Call function
AutocraticCommonalityDectectorino(sd_events,fd_events,1)


# return [' '.join(x[0:]) + ' ' +' '.join(y[0:]) for x in a for y in b  if x[0] == y[0] and abs(float(x[1])-float(y[1])) <= c]
#return ['Date: ' + ''.join(x[0]) + ' Time: ' +''.join(y[1]) for x in a for y in b  if x[0] == y[0] and abs(float(x[1])-float(y[1])) <= c]
