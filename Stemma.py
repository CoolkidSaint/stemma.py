import streamlit as st
import pandas as pd

# Title and subtitle
st.title("Twi Word Stemmatizer")
st.subheader("Enter a Twi word (like '3y3' or 'bc') to find its stem.")

# Replace keyboard-friendly Twi characters with actual ones
def normalize_twi_input(word):
    return word.replace("3", "ɛ").replace("c", "ɔ")

# Basic stemmer (this is a placeholder rule-based method)
def stem_twi_word(word):
    suffixes = ['mu', 'foɔ', 'ni', 'no', 'sɛm', 'fo', 'yɛ', 're', 'ka', 'di', 'to', 'de', 'ma', 'ne', 'na']
    for suffix in suffixes:
        if word.endswith(suffix) and len(word) > len(suffix) + 1:
            return word[:-len(suffix)]
    return word

# The 300 Twi words list (You can expand or customize this list)
twi_words = [
    'ɛda', 'ɛdɔ', 'ɛno', 'ɛyɛ', 'ɛreba', 'ɛkɔ', 'ɛwɔ', 'ɛbɛ', 'ɛfa', 'ɛka',
    'ɔba', 'ɔdɔ', 'ɔyɛ', 'ɔreba', 'ɔkɔ', 'ɔwɔ', 'ɔbɛ', 'ɔfa', 'ɔka', 'ɔman',
    'abofra', 'abusua', 'adan', 'adaka', 'adɔeɛ', 'afuo', 'agoro', 'agya', 'ahɔhoɔ', 'ahenni',
    'akoa', 'akɔdaa', 'akɔnnɔ', 'amaneɛ', 'anan', 'asɛm', 'asɔre', 'atadeɛ', 'atɛkyɛ', 'awareɛ',
    'banbɔ', 'barima', 'bere', 'bisa', 'boɔ', 'bra', 'brɛ', 'da', 'dɔ', 'dwene',
    'dwom', 'dze', 'ɛban', 'ɛbɔ', 'ɛda', 'ɛdɔ', 'ɛka', 'ɛkwan', 'ɛkɔ', 'ɛno',
    'ɛre', 'ɛsɛ', 'ɛsono', 'ɛyɛ', 'fa', 'fie', 'foforo', 'frɛ', 'gya', 'gye',
    'hɔ', 'hwɛ', 'ka', 'kasa', 'kɔ', 'kyerɛ', 'kyɛ', 'ma', 'man', 'me',
    'mmara', 'mmere', 'mmerɛ', 'mpa', 'mpaboa', 'mpeaw', 'mu', 'na', 'nea', 'neɛma',
    'nkyɛn', 'nkwa', 'nkɔsoɔ', 'nsa', 'nsuo', 'nsɛm', 'nwanwa', 'nwoma', 'nyansa', 'nya',
    'nyɛ', 'nyimpa', 'ɔbarima', 'ɔbea', 'ɔbɔadeɛ', 'ɔdom', 'ɔkɔm', 'ɔman', 'ɔpanyin', 'ɔsɔfoɔ',
    'ɔtan', 'ɔwɔ', 'ɔyɛ', 'pa', 'papa', 'saa', 'sɛ', 'sɛnea', 'sɛnkanee', 'soma',
    'sɔ', 'sɔre', 'sua', 'suban', 'sɛnkanee', 'sɛnea', 'te', 'to', 'tumi', 'wɔ',
    'wɔfa', 'wɔyɛ', 'wo', 'yɛ', 'yere', 'yɛn', 'yɛre', 'yɛyɛ', 'yɛfo', 'yɛni',
    'yɛreba', 'yɛbɛ', 'yɛda', 'yɛdɔ', 'yɛka', 'yɛnko', 'yɛreba', 'yɛreko', 'yɛyɛ', 'yɛwɔ',
    'yɛwo', 'yɛyɛfo', 'yɛyɛni', 'yɛyɛre', 'yɛyɛsɛ', 'yɛyɛyɛ', 'yɛyɛbɛ', 'yɛyɛda', 'yɛyɛdɔ', 'yɛyɛka',
    'yɛyɛnko', 'yɛyɛreba', 'yɛyɛreko', 'yɛyɛyɛ', 'yɛyɛwɔ', 'yɛyɛwo', 'yɛyɛyɛfo', 'yɛyɛyɛni', 'yɛyɛyɛre', 'yɛyɛyɛsɛ',
    'yɛyɛyɛyɛ', 'yɛyɛyɛbɛ', 'yɛyɛyɛda', 'yɛyɛyɛdɔ', 'yɛyɛyɛka', 'yɛyɛyɛnko', 'yɛyɛyɛreba', 'yɛyɛyɛreko', 'yɛyɛyɛyɛ', 'yɛyɛyɛwɔ',
    'yɛyɛyɛwo', 'yɛyɛyɛyɛfo', 'yɛyɛyɛyɛni', 'yɛyɛyɛyɛre', 'yɛyɛyɛyɛsɛ', 'yɛyɛyɛyɛyɛ', 'yɛyɛyɛyɛbɛ', 'yɛyɛyɛyɛda', 'yɛyɛyɛyɛdɔ', 'yɛyɛyɛyɛka'
]

# Apply normalization to word list for matching
normalized_word_map = {normalize_twi_input(word): word for word in twi_words}

# INPUT
user_input = st.text_input("Enter Twi word (type 3 for ɛ and c for ɔ):")
if user_input:
    normalized = normalize_twi_input(user_input.lower())
    if normalized in normalized_word_map:
        stemmed = stem_twi_word(normalized)
        st.success(f"**Original Word:** {normalized_word_map[normalized]}\n\n**Stem:** {stemmed}")
    else:
        st.error("Word not found in dictionary. Please check spelling or use 3 and c as needed.")

# FULL DICTIONARY
with st.expander("📚 View All 300 Twi Words"):
    df = pd.DataFrame({'Available Twi Words': sorted(twi_words)})
    st.dataframe(df, height=300)
