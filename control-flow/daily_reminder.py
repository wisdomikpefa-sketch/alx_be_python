# Get user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        message = (f"'{task}' is a high priority task")
    case "medium":
        message = (f"'{task}' is a MEDIUM priority task." )
    case "low":
        message = (f"'{task}' is a low priority task.")
    
if time_bound == "yes":
    message += " that task requires immediate attention today!"
else:
    message += " This task can be scheduled for later."
# Print the customized reminder
print(message)
