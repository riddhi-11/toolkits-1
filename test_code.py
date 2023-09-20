import csv

# Specify the path to the CSV file
csv_file_path = "job_data.csv"

# Define the job titles for which we want to compute the average
job_titles = ["Data Architect", "Senior Business Analyst", "Data Scientist", "Machine Learning Engineer"]

try:
    # Open the CSV file for reading
    with open(csv_file_path, 'r', newline='') as csvfile:
        # Create a CSV reader
        csvreader = csv.DictReader(csvfile)
        
        # Initialize variables to calculate the average
        total_salaries = 0
        num_jobs = 0

        # Iterate through each row in the CSV file
        for row in csvreader:
            job_title = row['job_title']
            num_of_salaries = int(row['num_of_salaries'])

            # Check if the job title is in the list of specified titles
            if job_title in job_titles:
                total_salaries += num_of_salaries
                num_jobs += 1

        # Calculate the average                                                           
        if num_jobs > 0:
            average_salary = total_salaries / num_jobs
        else:
            average_salary = 0

        # Display the average salary
        print("Average Salary for Specified Job Titles:")
        print(average_salary)

except FileNotFoundError:
    print(f"CSV file not found: {csv_file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

