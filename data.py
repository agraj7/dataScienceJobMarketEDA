import pandas as pd

# Sample data
data = {
    'Title': ['Data Scientist', 'Data Analyst', 'Machine Learning Engineer', 
              'Business Intelligence Analyst', 'Data Scientist', 'Data Engineer'],
    'Company': ['Tech Innovators', 'Data Solutions Inc', 'AI Labs', 
                'Analytics Group', 'Analytics Co', 'DataWorks'],
    'Location': ['Philadelphia', 'New York', 'San Francisco', 
                 'Philadelphia', 'New York', 'San Francisco'],
    'Summary': [
        'Analyzing large datasets to provide actionable insights.',
        'Interpreting data to support business decisions.',
        'Building and optimizing machine learning models.',
        'Creating reports and dashboards to track business performance.',
        'Developing algorithms to improve data accuracy and usability.',
        'Designing and maintaining data pipelines.'
    ],
    'Skills': [
        'Python;Machine Learning;Data Analysis',
        'SQL;Excel;Data Visualization',
        'Python;TensorFlow;Deep Learning',
        'Power BI;SQL;Data Modeling',
        'Python;R;Statistics',
        'SQL;Python;ETL'
    ]
}

# Create DataFrame
job_data = pd.DataFrame(data)

# Save DataFrame to CSV
job_data.to_csv('job_data.csv', index=False)
