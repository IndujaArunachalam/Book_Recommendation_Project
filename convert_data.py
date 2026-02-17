import pandas as pd

# Define the columns for the CMU dataset
cols = ['wiki_id', 'freebase_id', 'title', 'author', 'pub_date', 'genres', 'summary']

try:
    # Read the text file using 'tab' as the separator
    df = pd.read_csv('booksummaries.txt', sep='\t', names=cols, header=None)
    
    # Keep only the columns needed for your ML model
    df = df[['title', 'summary']]
    
    # Drop any rows that are missing a summary or title
    df.dropna(inplace=True)
    
    # Save as CSV
    df.to_csv('books.csv', index=False)
    print("Successfully created books.csv with", len(df), "entries!")

except FileNotFoundError:
    print("Error: 'booksummaries.txt' not found in this folder.")