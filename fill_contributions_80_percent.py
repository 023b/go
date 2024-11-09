import os
import datetime
import subprocess
import random

# Configuration
repo_path = "/path/to/your/repo"  # Change to your local repository path
commit_message = "Backdated commit for contribution graph"
start_date = datetime.datetime(2023, 4, 1)  # Start from April 1, 2023
end_date = datetime.datetime.now()  # Until today
fill_percentage = 0.8  # 80% of the days to be filled

# Function to execute shell commands
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error: {stderr.decode().strip()}")
    return stdout.decode().strip()

# Change to the repository directory
os.chdir(repo_path)

# Generate a list of dates from start_date to end_date
total_days = (end_date - start_date).days + 1
all_dates = [(start_date + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(total_days)]

# Calculate the number of days to fill based on the percentage
days_to_fill = int(total_days * fill_percentage)
selected_dates = random.sample(all_dates, days_to_fill)

# Create commits on the selected dates
for commit_date in sorted(selected_dates):
    # Create or update a file
    with open("contribution_file.txt", "a") as file:
        file.write(f"Commit made on {commit_date}\n")

    # Stage the file
    run_command("git add contribution_file.txt")
    
    # Commit with a specific date
    run_command(f'git commit -m "{commit_message} on {commit_date}" --date="{commit_date}T12:00:00"')

    print(f"Commit created for date: {commit_date}")

# Push all changes to GitHub
run_command("git push origin main")  # Change 'main' to 'master' if using 'master' branch

print(f"Your contribution graph has been updated from April 2023 to now with approximately 80% green boxes!")
