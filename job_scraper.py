import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_job_listings(city, num_pages=5):
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
            summary = job.find('div', class_='summary').text.strip()
            
            job_listings.append([title, company, location, summary])
    
    return pd.DataFrame(job_listings, columns=['Title', 'Company', 'Location', 'Summary'])

# Example usage
cities = ['Philadelphia', 'New York', 'San Francisco']
job_data = pd.concat([get_job_listings(city) for city in cities], ignore_index=True)
