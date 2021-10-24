# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 06:40:24 2019

@author: Arash

a script for dividing arbitrary number of integers inot different parts using 
at maximum 1GB of the RAM . ( i.e 1 Billion integers into 34 different parts )
It divides each 29826161 ( = 1024 ** 3 (the storage of ram ) / 36 (maximum 
space an integer can occupy) ) integers and sort them in the RAM then writes
them in seperate files. 
Now we have x (i.e: 34 = [ 1000000000 (1B) / 29826161 ] ) files which the integers
in them are sorted .  (i.e: in 1B example 33 of this files have 29826161 integers
and the last one has 15736687. ( 1000000000 % 29826161 ) )
Then we read first integers from each file and then finding minimum of them,
writing the minimum at the final file and then assigning the next integer to 
the place in the list which was minimum from the file which had the minimum .
"""
import time 
start_time = time.time() 
flag = True #it will become false when the program reachs the end of file
k = 0 #it shows the "k"th part
counter = 0 #for counting the number of integers the source file has.
with open("largefile.txt", 'r') as file: #reading the file which contains random integers
    while flag:
        line_list = [] #temporary list for sorting at the RAM 
        for i in range(29826161): #every 29826161 will be sorted and written in seperate files
            try :
                value = int(file.readline())
                line_list.append(value)
                counter += 1
            except ValueError: #if it reaches the end of file it will raise an exceptation
                flag = False # ... so the program will set flag to false to prevent the outer loop from another iteration
                break #... and break the inner loop .
            
        line_list.sort() #sorting list using python's library
        with open('part' + str(k) + '.txt' , 'w') as temp : #writing sorted integers in seperate files
            for line in line_list:
                temp.write(str(line) + '\n')
        k += 1 #adding one to k after writing each file 

#open files to read integers from and store them in list of file handlers
#called files . them and write the minimum at the "result.txt" file    
files = []
for i in range(k): #we have k files.
    files.append(open("part" + str(i) + ".txt", "r"))
result = open('result.txt', 'w')
         
lst = [] #the list we find minimum of it each time .
#at first we assign the first integers from each file to it .
#... so by finding the minimum of the list we find the minimum of the whole integers .
for i in range(k):
    lst.append( int( files[i].readline() ) ) 
for i in range(counter): #finding minimum of all integers and writing it at result.txt file which means writing all numbers but in sorted way from minimum to maximum. 
    index_min = lst.index( min(lst) )
    result.write(str(lst[index_min]) +'\n')
    #reading from different files and modify different place at the list due to minimum was from which file .
    value = files[index_min].readline() #read from the file the minimum was from.
    if value != '' :
        lst[index_min] = int(value) #... and assign the value we read to the that file.
    else: #if we reach the end of the file at list we assign infinite number which is greater than any integer .
        lst[index_min] = float("inf")
                
for i in range(k): #closing files we have read from and write to .
    files[i].close() 
result.close()

end_time = time.time()
print("the execution of the program was:", end=" ")
print( round(end_time - start_time, 2) )
