def create_ticket():
    print("=== IT Helpdesk Ticket ===")
    
    student_name = input("Student Name : ")
    student_id = input("Student ID   : ")
    issue = input("Issue        : ")
    location = input("Location     : ")
    priority = input("Priority (High/Medium/Low): ")

    # Assign technician based on priority level
    if priority.strip().capitalize() == "High":
        technician = "Ahmad"
    elif priority.strip().capitalize() == "Medium":
        technician = "Siti"
    elif priority.strip().capitalize() == "Low":
        technician = "Ali"
    else:
        technician = "Unassigned"

    status = "Pending"

    # Return ticket details as a dictionary
    return {
        "student_name": student_name,
        "student_id": student_id,
        "issue": issue,
        "location": location,
        "priority": priority,
        "technician": technician,
        "status": status
    }