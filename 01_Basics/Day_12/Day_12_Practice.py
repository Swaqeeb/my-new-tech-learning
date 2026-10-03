# Python — Day 12 Practice
# Date: 03 Oct 2026
# Topic: Built-in Functions & Useful String Methods

name = "Swaqeeb"
print(len(name))
print(name.upper())
print(name.lower())

message = "   Hello Python   "
print(message.strip())

message = "I am learning Python"
print(message.replace("Python", "SQL"))

tools = "Excel, Word, PowerPoint, Outlook"
tool_list = tools.split(",")
for tool in tool_list:
    print(tool.strip())

job = "I work as a system analyst"
print(job.find("system"))
print(job.find("Python"))

skills = "Python SQL Python Git Python"
print(skills.count("Python"))

filename = "monthly_report.pdf"
print(filename.startswith("monthly"))
print(filename.endswith(".pdf"))

servers = ["Server01", "Server02", "Server03"]
print(" | ".join(servers))

age = 30
salary = "50000"
print(isinstance(age, int))
print(isinstance(salary, int))

# Final challenge
report = "  Python, SQL, Git, Python  "
clean_report = report.strip()
print(clean_report)
print(clean_report.count("Python"))

items = clean_report.split(",")
print(items)

for item in items:
    print(item.strip())

print(clean_report.startswith("Python"))
