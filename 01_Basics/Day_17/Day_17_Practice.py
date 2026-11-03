open_tickets=[5,12,3,18,7,15]
count=0
for ticket in open_tickets:
    if ticket>10:
        count=count+1
print("Employee with high workload:",count)
        #Exercise 2
open_tickets=[8,15,4,22,11,6]
count=0
for ticket in open_tickets:
    if ticket>10:
        count=count+1
        print("High Workload:", ticket)
print("Total employee with high workload:",count) 
         #exercise 3
open_tickets=[8,15,4,22,11,6]
count=0  
for ticket in open_tickets:
          if ticket >10:
               count=count+ticket
print("Total high-workload tickets:",count)    
open_tickets=[7,14,3,21,12,5,18]
total_tickets=0
count=0
for ticket in open_tickets:
     if ticket>10:
          total_tickets=total_tickets+ticket
          count= count+1
print("Employee with high workload:",count)
print("Total high-workload tickets",total_tickets)          
 #exercise 5

def count_hugh_workload(Open_tickets):
     count=0
     for ticket in Open_tickets:
          if ticket>10:
               count =count+1
     return count 
team_a=[5,12,18,3,20]
result= count_hugh_workload(team_a)
print("High workload employee:",result)
#new 
def calculate_high_workload(open_tickets):
     total=0
     for ticket in open_tickets:
          if ticket>10:
               total=total+ticket
     return total
         
team_b=[6,14,9,25,12]
result=calculate_high_workload(team_b)
print("Total high-worload tickets:",result)      
#next 
def calculate_high_workload(open_tickets,threshold):
     total=0
     for ticket in open_tickets:
          if ticket >threshold:
               total=total+ticket
     return total
team_b=[6,14,9,25,12]
result =calculate_high_workload(team_b,15)
print("Total high-workload tickets:",result)
result =calculate_high_workload(team_b,10)
print("Total high-workload tickets:",result)                          
result =calculate_high_workload(team_b,20)
print("Total high-workload tickets:",result)                
#exercise 7

def analyze_workload(open_tickets):
     count =0
     total=0
     for ticket in open_tickets:
          if ticket>10:
               count=count+1
               total=total+ticket
               
     return count,total
team_c=[8,16,4,23,12,7]
count,result= analyze_workload(team_c)
print("Employees with high workload:",count)
print("Total high-workload tickets:",result)
                          