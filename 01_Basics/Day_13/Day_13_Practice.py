# Python — Day 13 | 06 Oct 2026
# String Validation Methods

# 1. isdigit()
age = "35"
print(age.isdigit())

# 2. isalpha()
name = "Swaqeeb"
print(name.isalpha())

# Full-name example using replace()
name = "Tarin Islam"
clean_name = name.replace(" ", "")
print(clean_name.isalpha())

# 3. isalnum()
username = "Swaqeeb123"
print(username.isalnum())

# 4. isspace()
text = "   "
print(text.isspace())

# Better empty-input validation using strip()
message = "   "
if message.strip() == "":
    print("Empty message")
else:
    print("Message received")

# 5. islower()
code = "python"
print(code.islower())

# 6. isupper()
code = "PYTHON"
print(code.isupper())

# 7. title() and istitle()
name = "swaqeeb islam"
new_name = name.title()
print(new_name)
print(new_name.istitle())

# Final challenge
username = "  Swaqeeb123 "
clean_username = username.strip()

if clean_username.isalnum():
    print("Valid username")
else:
    print("Invalid username")
