import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def generate_wordcloud(text_data):
    wordcloud = WordCloud(width=800, height=400, background_color ='white').generate(' '.join(text_data))
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

def nlp_analysis(file_path):
    job_data = pd.read_csv(file_path)

    # Generate a word cloud of job titles
    generate_wordcloud(job_data['Job Title'])

# Example usage
nlp_analysis('cleaned_job_data.csv')
