# Get user input
task = input("Enter the task: ")
priority = input("Enter the priority (high, medium, low): ").lower()
time_bound = input("Is the time-bound? (yes or no): ").lower()
match priority:
    case "high":
        message = (f"is a high priority task. ")
    case "medium":
        message = (f"is a MEDIUM priority task." )
    case "low":
        message = (f"is a low priority task.")
    
# Check if the task is time-bound and modify the message
if time_bound == "yes":
    message += " This task requires immediate attention today!"
else:
    message += " This task can be scheduled for later."
# Print the customized reminder
print(message)
