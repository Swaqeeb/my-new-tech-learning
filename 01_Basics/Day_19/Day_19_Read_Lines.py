#Pyhtn Day 19 | 05 November
#exercise 4 - Reading a file line by line
report_path="01_Basics/Day_19/report.txt"
with open(report_path,"r") as file:
    for line in file:
        print(line.strip())
#exercise 5- Count report lines
count= 0
with open(report_path,"r") as file:
    for line in file:
        count=count+1
print("Total reprot lines:", count)
# exercise 6- Count ticket-related lines
count= 0
with open(report_path,"r") as file:
    for line in file:
        if "tickets" in line.lower():
         count =count+1
print("Total tickets related lines:",count)        
#execise 7
Search_text="Resolved Tickets: 8"
with open(report_path,"r") as file:
    for line in file:
        if Search_text.lower() in line.lower():
            print("Entry found")
            break
    else:
         print("Entry not found")
