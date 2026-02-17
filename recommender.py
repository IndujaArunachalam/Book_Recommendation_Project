import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class BookRecommender:
    def __init__(self, csv_path):
        # Load the dataset
        self.df = pd.read_csv(csv_path)
        
        # Fill missing summaries to prevent vectorizer errors
        self.df['summary'] = self.df['summary'].fillna('')
        
        # Initialize the TF-IDF Vectorizer to convert text to numbers
        # We use 'english' stop words to ignore common words like 'the' or 'and'
        self.tfidf = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = self.tfidf.fit_transform(self.df['summary'])
        
        # Pre-compute the Cosine Similarity matrix
        self.cosine_sim = cosine_similarity(self.tfidf_matrix, self.tfidf_matrix)

    def recommend(self, title_input, num_results=5):
        """
        Finds a book title using fuzzy matching and returns top similar books.
        """
        # 1. Fuzzy Search: Find books that contain the input string
        matches = self.df[self.df['title'].str.contains(title_input, case=False, na=False)]
        
        if matches.empty:
            return None
            
        # 2. Get the index of the first match found
        idx = matches.index[0]
        actual_title = self.df.iloc[idx]['title']
        
        # 3. Get similarity scores for all books compared to this one
        sim_scores = list(enumerate(self.cosine_sim[idx]))
        
        # 4. Sort books based on similarity scores in descending order
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        
        # 5. Get indices of top results (skipping index 0 because that is the book itself)
        top_indices = [i[0] for i in sim_scores[1:num_results+1]]
        
        # 6. Return the titles and summaries as a list of dictionaries
        return self.df.iloc[top_indices][['title', 'summary']].to_dict('records')