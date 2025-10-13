'''
try:
    statement-1
    statement-2
    statement-3
except xxxx:
    statement-4

statement-5'''

# Here the first case 
#If there is no exception 
#Then normal execution 1,2,3,5

#If there is execption at statement -2 
#1,4,3,5 NT-->Normal Termination

#If there is exception at 2 and no handling
#1,AT-->Abnormal Termination

