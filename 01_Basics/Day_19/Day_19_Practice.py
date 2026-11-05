device={
    "asset_id":501,
    "status": "Active",
    "location": "Dhaka"
}
device["status"]="Inactive"
device["assigned_to"]="Karim"
del device["location"]
# Python Day 19 | 05 November 2026
# Exercise 1 - Writing to a text file
with open("01_Basics/Day_19/report.txt","w") as file:
    file.write("IT Support Report")
    import os
    print("File saved in:", os.getcwd())
# Exercise 2 - Reading a text file
with open("01_Basics/Day_19/report.txt","r") as file:
    content=file.read()
print(content)    
with open("01_Basics/Day_19/report.txt","a") as file:
    file.write("\n Total open Tickets:15")