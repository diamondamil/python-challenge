## Import Modules

import os

import csv



## Use the os module to read file path

csv_Path = os.path.join("Resources", "budget_data.csv")

#print(csv_Path)



## Open the CSV

with open(csv_Path, newline = "") as csv_File:



    # Initiate csv reader

    csv_Reader = csv.reader(csv_File, delimiter = ",")

    #print(csv_Reader)



    # Read the Header row 

    csv_Header = next(csv_File)

    print(f'\nHeader: {csv_Header}')



    # Create lists to store Date and Revenue columns

    DateCol = []

    RevenueCol = []

    



    # Read each row x in data

    for x in csv_Reader:

 

        # Store all Date records in a list

        DateCol.append(x[0])



        # Store all Revenue records in a list

        RevenueCol.append(int(x[1]))





    # Print the count of Months    

    TotalMonths = len(DateCol)

    print(f'Total months in dataset: {TotalMonths}')



    # Total net amount of "Profi/Losses" over the entire period

    NetTotal = sum(RevenueCol)

    print(f'Total: ${NetTotal}')



    # The average change in "Profit/Losses" between months over the entire period

    AverageChange = round(float(NetTotal/TotalMonths) , 2)

    print(f'Average Change: $ {AverageChange}')



    # Greatest Increase in Profits

    GreatestIncrease = max(RevenueCol)

    print(f'Greatest INCREASE in revenue: ${GreatestIncrease}') #how do i pull in date



    # Greatest Decrease in Profits

    GreatestDecrease = min(RevenueCol) 

    print(f'Greatest DECREASE in revenue: ${GreatestDecrease}') #how do i pull in date



# Use os module to specify output file to WRITE to

csv_Output_Path = os.path.join("budgetdata.txt")



# Open the output file using WRITE mode

with open(csv_Output_Path, "w", newline = "") as csv_File_Out:



    # Initialize csv.writer

    csv_Writer = csv.writer(csv_File_Out)



    # Write results to text file

    csv_Writer.writerow(["Results"])

    csv_Writer.writerow(["----------"])

    csv_Writer.writerow(["Total months in dataset: " + str(TotalMonths)])

    csv_Writer.writerow(["Total: $" + str(NetTotal)])

    csv_Writer.writerow(["Average Change: $" + str(AverageChange)])

    csv_Writer.writerow(["Greatest INCREASE in revenue: $" + str(GreatestInc)]) #how do i pull in date

    csv_Writer.writerow(["Greatest DECREASE in revenue: $" + str(GreatestDec)]) #how do i pull in date

    

