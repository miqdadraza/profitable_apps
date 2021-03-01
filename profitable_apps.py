"""
# Profitable App Profiles

## About Project:
In this project, we will be analysing data about apps from the Apple app store as well as the Android app store.

## Goal of Project:
Our goal is to help developers understand what kind of apps are more likely to be downloaded by users, and what kinda of apps are possibly profitable.
"""

from csv import reader
def open_dataset(dataset, header = True): #defining function, takes two input parameters
    opened_file = open(dataset)
    read_file = reader(opened_file)
    data = list(read_file) #converts the file into a list
    if header:
        header_dataset = data[0]
        list_dataset = data[1:]
        return header_dataset, list_dataset #if there is a header, a tuple of the header and data will be returned
    else:
        list_dataset = data[0:]
        return list_data #if there is no header, the data will be returned


#opening the Android data set
android_data = open_dataset('googleplaystore.csv')
android_data_header, an
#print(android_data)