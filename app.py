import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load job data

try:
    job_data = pd.read_csv('job_data.csv')
    if 'Skills' in job_data.columns:
        all_skills = [skill for sublist in job_data['Skills'] for skill in sublist]
        st.write("Skills processed successfully.")
    else:
        st.warning("The 'Skills' column is not present in the data.")
except Exception as e:
    st.error(f"An error occurred: {e}")
  

# Sidebar filters
city = st.sidebar.selectbox('Select City', job_data['Location'].unique())
industry = st.sidebar.text_input('Industry (optional)')

# Filter data
filtered_data = job_data[job_data['Location'] == city]
if industry:
    filtered_data = filtered_data[filtered_data['Summary'].str.contains(industry.lower())]

# Display top skills
st.header(f"Top Skills in {city} {'for ' + industry if industry else ''}")
all_skills = [skill for sublist in filtered_data['Skills'] for skill in sublist]
skill_counts = pd.Series(all_skills).value_counts().head(20)

st.bar_chart(skill_counts)

# WordCloud of skills
st.header("WordCloud of Skills")
wordcloud = WordCloud(width=800, height=400).generate(' '.join(all_skills))

fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
