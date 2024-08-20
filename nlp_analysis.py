from job_scraper import job_data
import pandas as pd
import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nlp = spacy.load('en_core_web_sm')

def extract_skills(text):
    doc = nlp(text)
    return [ent.text for ent in doc.ents if ent.label_ == "ORG" or ent.label_ == "SKILL"]

job_data['Skills'] = job_data['Summary'].apply(extract_skills)

# Combine all skills for visualization
all_skills = [skill for sublist in job_data['Skills'] for skill in sublist]

# Visualize with WordCloud
wordcloud = WordCloud(width=800, height=400).generate(' '.join(all_skills))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
# Frequency of top skills
skill_counts = pd.Series(all_skills).value_counts().head(20)

# Bar plot of top skills
skill_counts.plot(kind='barh', figsize=(10, 6))
plt.xlabel('Frequency')
plt.title('Top 20 Skills in Data Science Job Listings')
plt.show()
