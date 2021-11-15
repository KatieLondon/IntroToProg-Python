# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# KLondon, 11/10/2021 Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt" # Data Storage File
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task": lstRow[0], "Priority": lstRow[1]}
    lstTable.append(dicRow)
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(""""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice == '1'):
        for row in lstTable:
            print(row["Task"] + " , " + row["Priority"].strip()) #Use strip to remove the carriage return so as not to have an empty line seperating each row
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice == '2'):
        strTask = input("Enter a to-do list task: ")
        strPriority = input("Enter the priority for this task: ")
        dicRow = {'Task': strTask, 'Priority': strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice == '3'):
        strRemove= input("Which item would you like to remove? ")
        for row in lstTable:
            if row["Task"].lower() == strRemove.lower():
                lstTable.remove(row)
        print("The task has been removed from the To-Do List")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice == '4'):
         objFile = open(strFile,"w")
         for row in lstTable:
            objFile.write("\n" + row["Task"] + ", " + row["Priority"])
         objFile.close()
         print("The data has been saved to the" + strFile)
         continue
    # Step 7 - Exit program
    elif (strChoice == '5'):
        print("Exiting the program")
        break  # and Exit the program