import pandas as pd

def clean_job_data(file_path):
    job_data = pd.read_csv(file_path)

    # Handle missing values
    job_data['Salary'] = pd.to_numeric(job_data['Salary'], errors='coerce')
    job_data['Company Rating'] = pd.to_numeric(job_data['Company Rating'], errors='coerce')
    
    # Fill missing numeric data with median
    job_data['Salary'].fillna(job_data['Salary'].median(), inplace=True)
    job_data['Company Rating'].fillna(job_data['Company Rating'].median(), inplace=True)
    
    # Fill missing text data with a placeholder
    job_data.fillna('Not Listed', inplace=True)
    
    # Save cleaned data
    job_data.to_csv('cleaned_job_data.csv', index=False)

# Example usage
clean_job_data('job_data.csv')
