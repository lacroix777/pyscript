#!/usr/bin/python3

################################################################################
##  Project: Maillog                                                          ##
##           script to read in three arguments on the command line and        ##
##           finds their average to two decimal places.                       ##
##  Cintia Celi                                                               ##
##                                                                            ##
################################################################################

''' INSTRUCTIONS'''
''' Download the mail.log file.
This script finds all the servers that sent email (e.g. connected to this email server),
and write out a csv file named 'servers.csv' with column 1 being the server name and column 2
being the server IP.  Each server must appear just once in the CSV file. Add your script to your
git repo and let me know when you are done as firstname-maillog.py, '''

import re
import csv
import sys

'''contex manager to open the file'''
with open('mail.log', 'r') as file_in:
    servers = {}                       #because this is a text file and Im working with DictWriter, I need a dict output file
    file_reader = file_in.readlines()  #to read the text file using a dialog,

    '''contex manager to write the file'''
    with open('servers.csv', 'w', newline = '') as fout:

        '''loop over each line to select the groups identifiers'''
        for line in file_reader:
            match = re.search('connect from (.*)\[(.*)\]', line)
            
            if match:               
                server = match.group(1)
                ip = match.group(2)

                if server in servers.keys():
                    continue
                else:
                    servers[server] = ip       
                
        fieldnames = ['server', 'ip']
                
        csv_writer = csv.writer(fout, delimiter=',')

        '''writting out the output file'''        
        csv_writer.writerow(fieldnames)
        for key,value in servers.items():
            row = [key, value]
            csv_writer.writerow(row)
                    
                
            
