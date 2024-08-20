from job_scraper import job_data
# Remove duplicates
job_data.drop_duplicates(inplace=True)

# Handle missing values (if any)
job_data.dropna(inplace=True)

# Normalize text
job_data['Summary'] = job_data['Summary'].str.lower().str.replace('[^\w\s]', '')
