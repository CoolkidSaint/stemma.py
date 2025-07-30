
import streamlit as st
import pandas as pd

# Define prefixes to remove
prefixes = ["me", "wo", "ɔ", "yɛ", "bɛ", "re", "a", "mo", "wɔn"]

# Define 100 Twi words
words = [
    "mekɔ", "rekɔ", "bɛkɔ", "wokɔ", "ɔkɔ", "yɛkɔ",
    "mecom", "rekom", "bɛkom", "wokom", "ɔkom", "yɛkom",
    "mepɛ", "repɛ", "bɛpɛ", "wopɛ", "ɔpɛ", "yepɛ",
    "medidi", "redidi", "bedidi", "wodidi", "ɔdidi", "yedidi",
    "mɛkɔ", "mɛba", "rebɔ", "bɛbɔ", "bɛyɛ", "yɛbɔ",
    "mema", "bɛma", "rebɔ", "yɛma", "bɛdi", "medi",
    "ɔdi", "redi", "woahu", "ɔahu", "mehu", "rehu",
    "mehunu", "rehunu", "mehwe", "yehwe", "woama", "ɔama",
    "meyɛ", "yɛyɛ", "yɛyɛɛ", "rebɔ", "mebɔ", "yɛbɔ",
    "bɛfa", "mefa", "reba", "rewu", "wɔda", "yɛda",
    "meware", "bɛware", "reware", "ɔware", "wɔbɔ", "yɛkyerɛ",
    "ɔkyerɛ", "wokyerɛ", "mekyerɛ", "rekyerɛ", "wokɔda", "ɔkɔda",
    "wokɔso", "ɔkɔso", "rekɔso", "yɛda", "wɔreba", "ɔreba",
    "bɛreba", "wɔkɔ", "ɔkɔ", "wokɔ", "wokɔɔ", "ɔbɛkɔ",
    "wobɛkɔ", "mobɛkɔ", "wɔbɛkɔ", "yɛbɛkɔ", "wɔbɛfa", "yɛbɛfa",
    "mobɛfa", "ɔbɛfa", "meyɛ", "yɛyɛ", "meba", "woba"
]

# Define stemmer function
def stem_twi(word):
    for prefix in sorted(prefixes, key=len, reverse=True):
        if word.startswith(prefix):
            return word[len(prefix):]
    return word

# Apply stemming
stemmed_words = [(word, stem_twi(word)) for word in words]
df = pd.DataFrame(stemmed_words, columns=["Original Word", "Stemmed"])

# Streamlit UI
st.title("Twi Word Stemmatization App")
st.write("This app demonstrates simple stemming by removing common Twi prefixes.")
st.dataframe(df)

# Allow user to enter their own word
st.write("## Try it yourself")
user_input = st.text_input("Enter a Twi word:")
if user_input:
    stemmed = stem_twi(user_input)
    st.write(f"**Stemmed version:** `{stemmed}`")
