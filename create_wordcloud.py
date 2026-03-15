import csv
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def create_word_cloud_from_csv(csv_file, output_image, width=740, height=460):
    """Create a word cloud from category count CSV data"""
    
    # Read the CSV file and create a frequency dictionary
    frequencies = {}
    total_categories = 0
    
    print(f"Reading category data from {csv_file}...")
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row['normalized_category_name']
            count = int(row['usage_count'])
            frequencies[category] = count
            total_categories += 1
    
    print(f"Loaded {total_categories} categories")
    print(f"Most used category: {max(frequencies.items(), key=lambda x: x[1])}")
    
    # Create the word cloud
    print(f"Generating word cloud ({width}x{height})...")
    wordcloud = WordCloud(
        width=width,
        height=height,
        background_color='white',
        max_words=200,  # Limit to top 200 categories for better readability
        relative_scaling=0.5,
        colormap='viridis'
    ).generate_from_frequencies(frequencies)
    
    # Create figure and plot
    plt.figure(figsize=(width/100, height/100))  # Convert pixels to inches (approx)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    
    # Save the word cloud
    plt.tight_layout(pad=0)
    plt.savefig(output_image, dpi=100, bbox_inches='tight', facecolor='white')
    print(f"Word cloud saved as {output_image}")
    
    # Optionally display it
    plt.show()

if __name__ == '__main__':
    csv_file = 'category_count.csv'
    output_image = 'category_wordcloud.png'
    
    create_word_cloud_from_csv(csv_file, output_image, width=740, height=460)