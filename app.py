import streamlit as st
import pandas as pd

# Load the job data
try:
    job_data = pd.read_csv('job_data.csv')
except Exception as e:
    st.error(f"Error loading data: {e}")
    job_data = pd.DataFrame()

st.title("Data Science Job Market EDA")

# Display the DataFrame in a table format
st.write("### Job Listings Overview", job_data)

# Filter by Location (optional)
location = st.selectbox("Select Location", options=job_data['Location'].unique())
filtered_data = job_data[job_data['Location'] == location]

# Display selected job listings
st.write(f"### Job Listings in {location}", filtered_data)

# Detailed view of a selected job
selected_job = st.selectbox("Select a Job Title", options=filtered_data['Job Title'])

# Show detailed information about the selected job
job_details = filtered_data[filtered_data['Job Title'] == selected_job].iloc[0]

st.write(f"**Job Title:** {job_details['Job Title']}")
st.write(f"**Company Name:** {job_details['Company Name']}")
st.write(f"**Location:** {job_details['Location']}")
st.write(f"**Salary:** {job_details['Salary']}")
st.write(f"**Date Posted:** {job_details['Date']}")
st.write(f"**Company Rating:** {job_details['Company Rating']}")

# Display the company logo
if pd.notna(job_details['Logo']):
    st.image(job_details['Logo'], caption=f"Logo of {job_details['Company Name']}")

# Link to the job posting
if pd.notna(job_details['Job Link']):
    st.write(f"[Job Link]({job_details['Job Link']})")

# Summary statistics
st.write("### Summary Statistics")

# Average Company Rating
average_rating = job_data['Company Rating'].mean()
st.write(f"**Average Company Rating:** {average_rating:.2f}")

# Average Salary
job_data['Salary'] = pd.to_numeric(job_data['Salary'], errors='coerce')
average_salary = job_data['Salary'].mean()
st.write(f"**Average Salary:** ${average_salary:,.2f}")

# Job Count by Location
st.write("**Job Count by Location:**")
st.bar_chart(job_data['Location'].value_counts())
