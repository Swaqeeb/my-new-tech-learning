from pathlib import Path

# Find the folder containing this script
script_folder = Path(__file__).resolve().parent
print("Script folder:", script_folder)

# Build the report file's location
report_path = script_folder / "report.txt"
print("Report path:", report_path)

# Write the heading, replacing any previous content
with open(report_path, "w") as file:
    file.write("Day 20 IT Support Report")

# Append a second line
with open(report_path, "a") as file:
    file.write("\nOpen tickets: 15")

# Exercise 1: Handle a missing file
try:
    with open(script_folder / "missing_report.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Report file not found.")

print("Missing-file exercise finished.")

# Exercise 2: Read the existing report
try:
    with open(report_path, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Please check the report location.")

print("Check completed.")
