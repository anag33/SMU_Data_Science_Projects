import os
import csv

cereal_csv = r"Activities\01-Stu_CerealCleaner\Resources\cereal.csv"

#open and read the csv 
with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

    #read through each row of data after the header
    for row in csvreader:

        #convert row to float and compare to grams of fiber 
        if float(row[7]) >= 5:
            print(row)
