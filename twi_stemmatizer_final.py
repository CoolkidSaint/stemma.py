
import streamlit as st
import pandas as pd

# Replace this list with the actual 300 cleaned Twi words (ɛ, ɔ included)
twi_words = [
    "kɔ", "bɛkɔ", "ɛkɔ", "rekɔ", "bɔ", "ɛbɔ", "rebɔ", "bɛbɔ", "yɛ", "bɛyɛ", 
    "ɛyɛ", "reyɛ", "di", "ɛdi", "redi", "bɛdi", "ka", "ɛka", "reka", "bɛka", 
    "tɔ", "ɛtɔ", "retɔ", "bɛtɔ", "fa", "ɛfa", "refa", "bɛfa", "gye", "ɛgye", 
    "regye", "bɛgye", "hwe", "ɛhwe", "rehwe", "bɛhwe", "yɛn", "ɛyɛn", "reyɛn", 
    "bɛyɛn", "kɔɔ", "baa", "bɔɔ", "yɛɛ", "mee", "wɔɔ", "yɛnko", "mmra", "bra",
    "yɛyɛ", "reba", "rebɛyɛ", "bɛyɛɛ", "firi", "frɛ", "yɛfrɛ", "kae", "da", "te", 
    "ɛte", "wote", "tumi", "nsa", "abɔ", "abɛ", "de", "ma", "yɛyɛɛ", "yɛnfa", 
    "mpa", "nkyerɛ", "nkyia", "bɔne", "adeɛ", "nnam", "nsuo", "kɔkɔɔ", "kɔkɔ", 
    "ɔkɔ", "yɛre", "yɛpɛ", "yɛsrɛ", "bɛyɛre", "bɛpɛ", "bɛsrɛ",
]

# Function to "stem" the word: match to base form
def stem_word(word):
    matches = [w for w in twi_words if word in w or w in word]
    return matches if matches else ["No match found"]

# Streamlit app
st.set_page_config(page_title="Twi Stemmatizer", layout="centered")
st.title("Twi Stemmatizer")
st.write("Enter a Twi word below to find its stem/root word.")

# User input
user_input = st.text_input("Enter a Twi word (use ɛ and ɔ):", "")

# Process input
if user_input:
    stemmed = stem_word(user_input)
    df = pd.DataFrame({
        "Input Word": [user_input] * len(stemmed),
        "Stemmed Match": stemmed
    })
    st.table(df)
else:
    st.info("Type a Twi word above to get started.")
