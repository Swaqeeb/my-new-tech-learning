# Python Day 19 | 05 November 2026
#Exercise 3 - Append to existing report
report_path="01_Basics/Day_19/report.txt"
new_entry="Total Open Tickets: 8"
with open(report_path,"r") as file:
    content=file.read()
if new_entry in content:
    print("Entry already exists")
else:
    with open (report_path,"a") as file:
        file.write("\n"+new_entry)   
    print("Entry Added")