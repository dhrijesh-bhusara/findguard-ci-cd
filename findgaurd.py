def process_report(name, age, location, is_verified):
   
    if name == "" or location == "":
        return "Error: Missing required details"
    
    if age <= 0 or age > 120:
        return "Error: Invalid age"

    if not is_verified:
        return "Report Pending Verification"

    if age < 12:
        priority = "HIGH"
    elif age <= 60:
        priority = "MEDIUM"
    else:
        priority = "HIGH"

    return f"Report Approved | Priority: {priority} | Location: {location}"

print(process_report("Rahul", 10, "Mumbai", True))
