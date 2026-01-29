import streamlit as st
import pandas as pd

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Spotify Music Recommender",
    page_icon="🎵",
    layout="wide"
)

# -------------------- CUSTOM CSS --------------------
st.markdown("""
<style>
.song-card {
    background-color: #121212;
    padding: 15px;
    border-radius: 14px;
    margin-bottom: 15px;
    display: flex;
    gap: 15px;
    align-items: center;
    border-left: 6px solid #1DB954;
}
.song-img {
    width: 90px;
    border-radius: 10px;
}
.song-title {
    font-size: 18px;
    font-weight: bold;
    color: #1DB954;
}
.song-artist {
    font-size: 14px;
    color: #B3B3B3;
}
.song-meta {
    font-size: 13px;
    color: #9E9E9E;
}
</style>
""", unsafe_allow_html=True)
# -------------------- MODERN BUTTON CSS --------------------
st.markdown("""
<style>
/* Spotify-style Recommend button */
div.stButton > button {
    background: linear-gradient(90deg, #1DB954, #1ED760);
    color: #000000;
    font-weight: 700;
    font-size: 16px;
    padding: 0.6rem 1.8rem;
    border-radius: 999px;
    border: none;
    transition: all 0.25s ease-in-out;
    box-shadow: 0 8px 20px rgba(30, 215, 96, 0.35);
}

/* Hover effect */
div.stButton > button:hover {
    transform: scale(1.05);
    background: linear-gradient(90deg, #1ED760, #1DB954);
    box-shadow: 0 12px 25px rgba(30, 215, 96, 0.6);
}

/* Click effect */
div.stButton > button:active {
    transform: scale(0.97);
}
</style>
""", unsafe_allow_html=True)

# -------------------- LOAD DATA --------------------
@st.cache_data
def load_data():
    df = pd.read_csv("data/spotify_dataset.csv")
    df = df.dropna().reset_index(drop=True)
    return df

df = load_data()

# -------------------- CLEAN ARTIST NAMES --------------------
def extract_artists(series):
    artist_set = set()

    for entry in series:
        entry = str(entry)
        entry = entry.replace("[", "").replace("]", "")
        entry = entry.replace("'", "").replace('"', "")

        for artist in entry.split(","):
            artist_set.add(artist.strip().title())

    return sorted(artist_set)

genres = sorted(df["Genre"].unique())
artists = extract_artists(df["Artist(s)"])
artists.insert(0, "All Artists")

# -------------------- SIDEBAR --------------------
st.sidebar.title("🎧 Music Preferences")

genre = st.sidebar.selectbox("Select Genre", genres)
artist = st.sidebar.selectbox("Select Artist", artists)

min_popularity = st.sidebar.slider(
    "Minimum Popularity", 0, 100, 50
)

num_recs = st.sidebar.slider(
    "Number of Recommendations", 5, 20, 10
)

# -------------------- INITIALIZE STATE --------------------
if "recs" not in st.session_state:
    st.session_state.recs = None

if "selected_song" not in st.session_state:
    st.session_state.selected_song = None

# -------------------- TITLE --------------------
st.title("🎵 Spotify Song Recommender System")
st.write("Discover songs based on **genre, artist & popularity**")

# -------------------- RECOMMENDER LOGIC --------------------
def recommend_songs(genre, artist, min_pop, n):
    filtered = df[df["Genre"] == genre]
    filtered = filtered[filtered["Popularity"] >= min_pop]

    if artist != "All Artists":
        filtered = filtered[
            filtered["Artist(s)"]
            .str.replace(r"[\[\]'\"]", "", regex=True)
            .str.contains(artist, case=False)
        ]

    filtered = filtered.sort_values(
        by="Popularity", ascending=False
    )

    return filtered.head(n)

# -------------------- BUTTON --------------------
if st.button("🎯 Recommend Songs"):
    st.session_state.recs = recommend_songs(
        genre, artist, min_popularity, num_recs
    )
    st.session_state.selected_song = None
if "selected_index" not in st.session_state:
    st.session_state.selected_index = None


# -------------------- SHOW RECOMMENDATIONS --------------------
if st.session_state.recs is not None and not st.session_state.recs.empty:

    st.subheader("🔥 Recommended Songs")

    for i, (_, row) in enumerate(st.session_state.recs.iterrows()):

        st.markdown(
            f"""
            <div class="song-card">
                <img src="{row['Cover Image']}" class="song-img"/>
                <div>
                    <div class="song-title">🎶 {row['Track Name']}</div>
                    <div class="song-artist">👤 {row['Artist(s)']}</div>
                    <div class="song-meta">
                        🎧 {row['Genre']} · 🔥 Popularity: {row['Popularity']}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button("View Details", key=f"view_{i}"):
            st.session_state.selected_index = i
            st.session_state.selected_song = row.to_dict()

        # 🔽 INLINE DETAILS (THIS IS THE MAGIC)
        if st.session_state.selected_index == i:
            song = st.session_state.selected_song

            st.markdown("### 🎼 Song Details")

            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(song["Cover Image"], width=180)

            with col2:
                st.write(f"🎵 **Track:** {song['Track Name']}")
                st.write(f"👤 **Artist(s):** {song['Artist(s)']}")
                st.write(f"💿 **Album:** {song['Album']}")
                st.write(f"📅 **Release Date:** {song['Release Date']}")
                st.write(f"🔥 **Popularity:** {song['Popularity']}")
                st.write(f"🎧 **Genre:** {song['Genre']}")

            st.divider()
