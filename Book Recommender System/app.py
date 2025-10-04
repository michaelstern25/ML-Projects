from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model files
similarity = pickle.load(open("similarity.pkl", "rb"))
pivot_table = pickle.load(open("books_list.pkl", "rb"))
books = pickle.load(open("books.pkl", "rb"))   # <-- add this (your books dataframe)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/recommend', methods=['POST'])
def recommend():
    book_name = request.form['book']
    try:
        index = np.where(pivot_table.index == book_name)[0][0]
        similar_items = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:6]
        
        recommendations = []
        for i in similar_items:
            book_title = pivot_table.index[i[0]]
            
            # Get book info from books dataframe
            book_info = books[books['book-title'] == book_title].drop_duplicates('book-title').iloc[0]
            img_url = book_info['image-url-m']
            
            recommendations.append({"title": book_title, "image": img_url})
        
        return render_template("index.html", book=book_name, recommendations=recommendations)
    except Exception as e:
        print("Error:", e)   # helpful for debugging
        return render_template("index.html", error="Book not found. Try another!")
# ✅ Server Start
# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)


# @app.route('/')
# def home():
#     return render_template("index.html")

# @app.route('/recommend', methods=['POST'])
# def recommend():
#     book_name = request.form['book']
#     try:
#         index = np.where(pivot_table.index == book_name)[0][0]
#         similar_items = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:6]
#         recommendations = [pivot_table.index[i[0]] for i in similar_items]
#         return render_template("index.html", book=book_name, recommendations=recommendations)
#     except:
#         return render_template("index.html", error="Book not found. Try another!")

# if __name__ == "__main__":
#     app.run(debug=True)