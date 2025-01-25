from datetime import datetime

# Get current date and time
current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Write to version.md
with open("../../version-control/docs/version.md", "w") as file:
    file.write(f"Current Time is: {current_time}")