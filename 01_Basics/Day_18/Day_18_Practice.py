employee={
    "name":"Karim",
    "department": "IT",
    "location":"Dhaka",
    "designation": "System Analyst"
}
for key,value in employee.items():
    print(key ,":", value)
  
employee["location"]="Chattogram"
print(employee["location"])
print(employee["designation"])
employee["employee_id"]=105
employee["status"]= "Active"
print(employee["status"])
#exercise 6
del employee["designation"]
print(employee)
removed_id=employee.pop("employee_id")
print("Removed employee id:", removed_id)
#Exercise 8
device={
    "asset_id":501,
    "type":"Laptop",
    "status":"Active"
}
print(device.get("location","Device location: Unknown"))
device["location"]="Dhaka"
device["location"]="Dhaka"
print(device.get("location","Device location: Unknown"))
#exercise 10
laptop={
    "asset_id":510,
    "owner":{
        "name":"Karim",
        "department": "Finance",
        "location":"Dhaka"
    },
    "status":"Active"}

print("Employee Name:",laptop["owner"]["name"])
print("Department:",laptop["owner"]["department"])
print("Laptop Status:",laptop["status"])
#exercise 11
laptop={
    "asset_id":510,
    "owner":{
        "name":"Karim",
        "department": "Finance",
        "location":"Dhaka"
    },
    "status":"Active"
}
laptop["owner"]["department"]= "IT" 
laptop["owner"]["location"]= "Chattogram" 
print("Updated Deperatment:",laptop["owner"]["department"])
print("Updated Location:",laptop["owner"]["location"])
#excercise 12
ticket={
    "ticket_id":105,
    "employee":{
        "name":"Rahim",
        "department":"Finance",
    },
    "status" : "open",
    "priority": "High"
}
ticket["status"]="Resolved"
ticket["resolved_by"]= "Swaqeeb"
del ticket["priority"]
print(ticket)
#exercise
tickets=[
    {"id": 101,"status": "open"},
    {"id": 102,"status": "Resolved"},
    {"id": 103,"status": "open"},
]
print(tickets[1]["status"])
#exercise
tickets=[
    {"id": 1001,"status":"open"},
    {"id": 2005,"status":"Resloved"},
    {"id": 5656,"status":"Pending"},
    {"id": 3002,"status":"closed"},
]
for ticket in tickets:
    if ticket["id"]==5656:
        print("Ticket 5656 Status:", ticket["status"])
        break
 #exercise 17
found=False
for ticket in tickets:
    
    if ticket["id"]==5656:
        found = True
        break
else:
        print("Ticket not found") 
#final challenge
tickets = [
    {"id": 101, "status": "Open"},
    {"id": 102, "status": "Pending"},
    {"id": 103, "status": "Resolved"}
]

for ticket in tickets:
     if ticket["id"]==102:
          ticket["status"]= "Resolved"
          print("Ticket 102 updated successfully")
          break
else:
 print("Ticket not found")

print(tickets[1])