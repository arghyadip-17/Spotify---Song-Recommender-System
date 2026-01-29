# 🎵 Spotify Indian Song Recommender System

A **modern, interactive Spotify-style music recommender web app** built using **Streamlit** and **Machine Learning**. The app recommends songs based on **genre, artist preference, and popularity**, with a clean UI inspired by Spotify.

---

## 🚀 Features

* 🎧 Genre-based song recommendations
* 👤 Artist filtering (or explore all artists)
* 🔥 Popularity threshold control
* 🎯 Custom number of recommendations
* 🖼️ Album cover display with rich song cards
* 📊 Detailed song view (album, release date, genre, popularity)
* ⚡ Fast performance with Streamlit caching

---
<img width="1919" height="907" alt="image" src="https://github.com/user-attachments/assets/b57deaf6-1556-4ace-9d83-1eb19e443814" />


## 🧠 Machine Learning 

This project also includes a **content-based recommender pipeline** using **TF-IDF on song lyrics**:

* Text cleaning & preprocessing
* TF-IDF vectorization
* Model artifacts saved using `pickle`

> ⚠️ Note: Pickle (`.pkl`) files are **not included** in the repository and should be generated locally.

---

## 🗂️ Project Structure

```
├── app.py                 # Streamlit web application
├── recommender.py         # TF-IDF model training & pickle generation
├── requirements.txt       # Project dependencies
├── data/
│   └── spotify_dataset.csv
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit** – frontend & deployment
* **Pandas / NumPy** – data processing
* **Scikit-learn** – TF-IDF & ML utilities

---
<img width="1919" height="905" alt="image" src="https://github.com/user-attachments/assets/6da91f46-87ab-4b84-b629-578130af7dc2" />


## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/spotify-music-recommender.git
cd spotify-music-recommender
```

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit App

```bash
streamlit run app.py
```
<img width="1919" height="900" alt="image" src="https://github.com/user-attachments/assets/a1f2b44f-e845-416e-b3dc-8921ee634b6e" />

---

## 🧪 (Optional) Generate ML Pickle Files

If you want to build the TF-IDF recommender artifacts:

```bash
python recommender.py
```

This will generate:

* `songs.pkl`
* `tfidf.pkl`
* `tfidf_matrix.pkl`

⚠️ These files are **ignored in GitHub** via `.gitignore`.

---


## 📌 Notes

* `venv/` and `.pkl` files are intentionally **excluded** from version control
* The app currently uses popularity-based filtering; ML-based recommendations can be integrated easily


---

⭐ If you like this project, consider giving it a star!
