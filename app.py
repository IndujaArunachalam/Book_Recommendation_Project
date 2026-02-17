import os
from flask import Flask, render_template, request
from recommender import BookRecommender

# This forces Flask to look in the exact right place on your PC
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, 'templates')
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Initialize the model
model = BookRecommender('books.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    results = None
    query = ""
    
    if request.method == 'POST':
        query = request.form.get('book_title')
        results = model.recommend(query)
        # Debug print to see if it's working in the terminal
        print(f"Searching for: {query}")
        print(f"Found: {results}")
        
    return render_template('index.html', results=results, query=query)

if __name__ == '__main__':
    # Try a different port to avoid Windows system conflicts
    app.run(debug=True, port=5001)