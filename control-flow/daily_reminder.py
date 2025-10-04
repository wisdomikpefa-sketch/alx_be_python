# Get user input
task = input("Enter the task description: ")
priority = input("Enter the task priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority using match-case
match priority:
    case "high":
        message = f"REMINDER: '{task}' is a high priority task"
    case "medium":
        message = f"REMINDER: '{task}' is a medium priority task."
    case "low":
        message = f"REMINDER: '{task}' is a low priority task. "
    case _:
        message = f"REMINDER: '{task}' has an UNKNOWN priority."

# Check if the task is time-bound and modify the message
if time_bound == "yes":
    message += "that requires immediate attention today!"
else:
    message += "Consider completing it when you have free time."

# Print the customized reminder
print(message)
