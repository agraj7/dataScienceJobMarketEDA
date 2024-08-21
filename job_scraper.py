import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_job_listings(city, num_pages=5):
    job_listings = []
    base_url = f"https://www.indeed.com/jobs?q=data+scientist&l={city}"
    
    for page in range(num_pages):
        url = f"{base_url}&start={page * 10}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for job in soup.find_all('div', class_='jobsearch-SerpJobCard'):
            title = job.find('a', class_='jobtitle').text.strip()
            company = job.find('span', class_='company').text.strip()
            location = job.find('div', class_='location').text.strip() if job.find('div', class_='location') else city
            salary = job.find('span', class_='salary').text.strip() if job.find('span', class_='salary') else 'Not Listed'
            date_posted = job.find('span', class_='date').text.strip()
            job_link = job.find('a')['href']
            company_rating = job.find('span', class_='ratingsContent').text.strip() if job.find('span', class_='ratingsContent') else 'Not Rated'
            logo = job.find('img')['src'] if job.find('img') else None
            
            job_listings.append([title, company, location, salary, date_posted, logo, job_link, company_rating])
    
    return pd.DataFrame(job_listings, columns=['Job Title', 'Company Name', 'Location', 'Salary', 'Date', 'Logo', 'Job Link', 'Company Rating'])

# Save to CSV
def save_jobs_to_csv(cities):
    all_jobs = pd.concat([scrape_job_listings(city) for city in cities], ignore_index=True)
    all_jobs.to_csv('job_data.csv', index=False)

# Example usage
cities = ['Philadelphia', 'New York', 'San Francisco']
save_jobs_to_csv(cities)
