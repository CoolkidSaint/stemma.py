import streamlit as st

# Title and description
st.title("Twi Word Stemmatizer")
st.markdown("Enter a Twi word to find its stem. Only works for specific words in the system.")

# Sample stem dictionary with 300 Twi words
stem_dict = {
    'abofra': 'bofra', 'aberewa': 'berewa', 'akyire': 'kyire', 'ɛyɛ': 'yɛ', 'yɛreko': 'ko',
    'ɔbarima': 'barima', 'ɔbaa': 'baa', 'ɔpanyin': 'panyin', 'ɔyɛ': 'yɛ', 'ɛka': 'ka',
    'mekɔ': 'kɔ', 'wobɛkɔ': 'kɔ', 'rekɔ': 'kɔ', 'aba': 'ba', 'maba': 'ba',
    'ɔba': 'ba', 'ɛbɛba': 'ba', 'cɔ': 'cɔ', 'acɔ': 'cɔ', 'bɛcɔ': 'cɔ',
    'bɛyɛ': 'yɛ', 'yɛɛ': 'yɛ', 'ayɛ': 'yɛ', 'bɔ': 'bɔ', 'abɔ': 'bɔ',
    'rebɔ': 'bɔ', 'wɔbɔ': 'bɔ', 'wɔyɛ': 'yɛ', 'cɛ': 'cɛ', 'ɛcɛ': 'cɛ',
    'mekae': 'kae', 'kaeɛ': 'kae', 'rekasa': 'kasa', 'kasaa': 'kasa', 'nkasa': 'kasa',
    'dwom': 'dwom', 'to': 'to', 'ato': 'to', 'reto': 'to', 'nato': 'to',
    'didi': 'didi', 'edidi': 'didi', 'redi': 'didi', 'adidi': 'didi', 'nadi': 'didi',
    'di': 'di', 'adi': 'di', 'redi': 'di', 'midi': 'di', 'wodi': 'di',
    'ware': 'ware', 'aware': 'ware', 'reware': 'ware', 'yɛware': 'ware', 'bɛware': 'ware',
    'da': 'da', 'ada': 'da', 'bɛda': 'da', 'reada': 'da', 'daɛ': 'da',
    'c': 'c', 'ac': 'c', 'bɛc': 'c', 'rekɔɔ': 'kɔ', 'kɔɔ': 'kɔ',
    'cɔɔ': 'cɔ', 'bɔɔ': 'bɔ', 'diɛ': 'di', 'cɛɛ': 'cɛ', 'yɛɛɛ': 'yɛ',
    # Add the rest of your 300 words here...
}

# User input
user_input = st.text_input("Type a Twi word")

# Display result
if user_input:
    stem = stem_dict.get(user_input.lower(), "Word not found in stemmer.")
    st.markdown(f"### Stemmed Word: `{stem}`")

# Sidebar: Display all available words
st.sidebar.markdown("### Available Words")
word_list = sorted(list(stem_dict.keys()))
st.sidebar.text_area("All 300 Words (Scroll ↓)", "\n".join(word_list), height=400)
