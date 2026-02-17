📚 BookMatch AI – Semantic Recommendation Engine

BookMatch AI is a web-based book recommendation system that uses Natural Language Processing (NLP) to help users discover their next favorite read.

Unlike traditional systems that rely only on genres or categories, this engine analyzes the thematic content and plot summaries of over 16,000 books to find deep semantic connections between them.

🚀 Features
🔎 Semantic Analysis

Uses TF-IDF (Term Frequency–Inverse Document Frequency) from Scikit-Learn to understand the importance of words within book summaries.

📐 Vector Space Similarity

Computes similarity between books using Cosine Similarity, measuring the mathematical distance between summary vectors.

🔍 Fuzzy Search

Flexible search functionality that:

Handles partial titles

Ignores case sensitivity

Matches similar book names

🎨 Modern UI

Clean dark-mode interface

Built using Flask + Jinja2

Responsive design with custom CSS

🛠️ Technical Stack
Backend

Python 3.x

Flask

Machine Learning

Scikit-Learn

TF-IDF Vectorizer

Cosine Similarity

Data Processing

Pandas (Data cleaning & manipulation)

Frontend

HTML5

CSS3

Jinja2 Templating

🧠 How It Works
1️⃣ Text Vectorization

The system converts book summaries into a numerical matrix using TF-IDF.

It:

Removes common stop words (e.g., the, is, a)

Focuses on meaningful keywords

Assigns weight based on word importance

This transforms textual data into a vector space representation.

2️⃣ Similarity Calculation

When a user searches for a book, the engine calculates similarity using the Cosine Similarity formula:

          similarity=cos(θ)=A⋅B/∥A∥∥B∥​
Where:

A = Vector of selected book

B = Vector of another book

Books with higher cosine scores are considered more thematically similar.

📂 Project Structure
BookMatch-AI/
│
├── static/
│   └── style.css          # Dark-mode styling
│
├── templates/
│   └── index.html         # Main web interface
│
├── app.py                 # Flask server & routing logic
├── recommender.py         # ML Model (TF-IDF & Cosine Similarity)
├── books.csv              # Processed dataset (16k+ books)
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation

🔧 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/BookMatch-AI.git
cd BookMatch-AI

2️⃣ Create & Activate Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


Mac/Linux:

python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py


The app will be available at:

http://127.0.0.1:5001