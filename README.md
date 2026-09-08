# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built using Python, NLP techniques, and Machine Learning concepts. The system recommends movies that are similar to a movie selected by the user based on information such as **genres, keywords, movie overview, cast, and director**.

The recommendation engine uses **CountVectorizer** to convert movie descriptions into numerical feature vectors and **Cosine Similarity** to measure the similarity between movies.

---

## 📌 Project Overview

With thousands of movies available across different platforms, finding movies similar to a user's interests can be difficult.

This project solves the problem by building a **content-based recommendation system** that analyzes the characteristics of movies and recommends the most similar movies.

For example, if a user selects:

> **The Dark Knight Rises**

the system can recommend movies such as:

* The Dark Knight
* Batman Returns
* Batman
* Batman Forever
* Batman Begins

The recommendations are generated based on the similarity between the movies' content features.

---

## 🎯 Objectives

* Build a content-based movie recommendation system.
* Perform data cleaning and preprocessing.
* Extract useful movie features.
* Combine multiple movie attributes into a single text-based feature.
* Apply NLP preprocessing techniques.
* Convert text into numerical vectors.
* Calculate similarity between movies.
* Generate Top-N movie recommendations.
* Save the processed data and similarity matrix for application use.
* Deploy the recommendation system using Streamlit.

---

## 🗂️ Dataset

The project uses the **TMDB 5000 Movies and Credits datasets**.

The datasets contain information such as:

* Movie title
* Genres
* Keywords
* Movie overview
* Cast
* Crew
* Director
* Movie ID

The movie and credits datasets are merged using the movie ID before feature engineering.

---

## 🔄 Project Workflow

```text
TMDB Movies Dataset
        +
TMDB Credits Dataset
        ↓
Data Loading
        ↓
Data Cleaning
        ↓
Merge Datasets
        ↓
Feature Selection
        ↓
Extract Genres
Extract Keywords
Extract Overview
Extract Cast
Extract Director
        ↓
Feature Engineering
        ↓
Create "Tags" Feature
        ↓
Text Preprocessing
        ↓
Lowercase Text
        ↓
Porter Stemming
        ↓
CountVectorizer
        ↓
Movie Feature Vectors
        ↓
Cosine Similarity
        ↓
Recommendation Function
        ↓
Top 5 Similar Movies
        ↓
Save Model Artifacts
        ↓
Streamlit Application
```

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

### 1. Dataset Merging

The movies and credits datasets are combined using the movie ID.

### 2. Feature Selection

Only relevant features are retained for building the recommendation system:

```text
movie_id
title
genres
keywords
overview
cast
crew
```

### 3. JSON-like Data Processing

Features such as genres, keywords, cast, and crew contain structured information stored in string format.

These values are converted into usable Python lists and processed further.

### 4. Cast Extraction

The first three cast members are extracted and used as movie features.

### 5. Director Extraction

The director is extracted from the crew information.

### 6. Creating Movie Tags

The following information is combined into a single `tags` column:

```text
genres
+
overview
+
keywords
+
cast
+
director
```

This combined text representation allows the recommendation system to compare movies based on their overall content.

---

## 🧠 NLP Preprocessing

After creating the `tags` feature, NLP preprocessing is performed.

### Lowercase Conversion

All text is converted to lowercase to maintain consistency.

### Porter Stemming

The **Porter Stemmer** is used to reduce words to their root/stem form.

For example:

```text
adventure → adventur
fantasy   → fantasi
following → follow
```

This helps similar words contribute to similar features.

---

## 🔢 Feature Extraction — CountVectorizer

The processed movie tags are converted into numerical feature vectors using:

```python
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(
    max_features=5000,
    stop_words='english'
)
```

The resulting feature matrix contains **4,806 movies and 5,000 features**.

Each movie is represented as a numerical vector based on the words present in its tags.

---

## 📐 Cosine Similarity

After converting movies into numerical vectors, **Cosine Similarity** is used to calculate how similar two movies are.

```python
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vector)
```

The similarity score indicates how closely two movies are related based on their content.

A higher similarity score means that the movies have more similar feature representations.

---

## 🎯 Recommendation Algorithm

The recommendation function works as follows:

1. User selects a movie.
2. The system finds the movie's index.
3. Similarity scores for that movie are retrieved.
4. Movies are sorted by similarity score.
5. The most similar movies are selected.
6. The Top 5 recommendations are displayed.

Conceptually:

```text
Selected Movie
      ↓
Find Movie Index
      ↓
Retrieve Similarity Scores
      ↓
Sort by Similarity
      ↓
Select Top 5
      ↓
Display Recommendations
```

---

## 💻 Example

### Input

```text
The Dark Knight Rises
```

### Output

```text
The Dark Knight
Batman Returns
Batman
Batman Forever
Batman Begins
```

---

## 💾 Saved Artifacts

The processed movie information and similarity matrix are saved using Python's `pickle` module.

```python
pickle.dump(new_df, open('Artificats/movie_list.pkl', 'wb'))
pickle.dump(similarity, open('Artificats/similarity.pkl', 'wb'))
```

These files can then be loaded by the application without having to repeat the complete preprocessing and similarity calculation every time.

---

## 🖥️ Streamlit Application

The project can be deployed as an interactive **Streamlit web application**.

The application allows users to:

1. Select a movie.
2. Click the recommendation button.
3. Receive a list of similar movies.

### Application Flow

```text
User
 ↓
Select Movie
 ↓
Recommendation Function
 ↓
Similarity Matrix
 ↓
Top 5 Similar Movies
 ↓
Display Results
```

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-learn
* NLTK
* Pickle

### NLP

* Porter Stemmer
* Text preprocessing
* Stop-word removal
* CountVectorizer

### Machine Learning Concepts

* Feature Engineering
* Text Vectorization
* Cosine Similarity
* Content-Based Recommendation

### Deployment

* Streamlit

---

## 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
│
├── Movie_Recommendation_System.ipynb
│
├── Artificats/
│   ├── movie_list.pkl
│   └── similarity.pkl
│
├── data/
│   └── README.md
│
├── images/
│   └── screenshots/
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

> **Note:** The exact folder names can be changed depending on how your final project files are organized.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Movie-Recommendation-System
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux/macOS

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Key Concepts Demonstrated

This project demonstrates practical understanding of:

* Exploratory Data Analysis
* Data Cleaning
* Feature Engineering
* Text Preprocessing
* Natural Language Processing
* Stemming
* Bag-of-Words representation
* CountVectorizer
* Vector similarity
* Cosine Similarity
* Content-Based Recommendation Systems
* Model/Artifact Serialization
* Streamlit Deployment

---

## 🚀 Future Improvements

The current system is a **content-based recommender**. It can be further improved by adding:

* User rating-based recommendations
* Collaborative filtering
* Hybrid recommendation systems
* TF-IDF vectorization
* Better recommendation evaluation
* Movie posters and additional metadata
* Movie search functionality
* Top-N recommendation customization
* Personalized recommendations based on user history
* More advanced NLP embeddings

---

## 📌 Project Highlights

* Built a content-based recommendation engine using movie metadata.
* Combined multiple movie attributes into a unified feature representation.
* Applied NLP preprocessing using Porter Stemming.
* Converted text into numerical vectors using CountVectorizer.
* Used Cosine Similarity to calculate movie-to-movie similarity.
* Generated Top 5 movie recommendations.
* Saved processed data and similarity matrix for efficient application use.
* Designed for deployment through Streamlit.

---

## 👨‍💻 Author

**Siddhant Ghungarde**

Aspiring Data Scientist | Machine Learning Enthusiast
