import streamlit as st

# Title
st.set_page_config(page_title="Twi Stemmatizer", layout="centered")
st.title("Twi Stemmatizer App")

# Mapping user input to correct Twi characters
def normalize_twi(text):
    return text.replace("3", "É›").replace("c", "É”")

# Twi stem dictionary (300 words as a sample - can be expanded)
twi_stem_dict = {
    "É›bÉ›yÉ›": "yÉ›", "É”bÉ›yÉ›": "yÉ›", "yÉ›": "yÉ›", "yÉ›É›": "yÉ›", "yÉ›re": "yÉ›",
    "bÉ›ba": "ba", "É”ba": "ba", "aba": "ba", "reba": "ba", "bÉ›baa": "ba",
    "É”bÉ›yÉ›É›": "yÉ›", "rebÉ›yÉ›": "yÉ›", "yÉ›É›É›": "yÉ›", "É›yÉ›": "yÉ›", "É”yÉ›": "yÉ›",
    "É”bÉ›ba": "ba", "aba": "ba", "É”baa": "ba", "bÉ›yÉ›": "yÉ›", "É›ba": "ba",
    "mÉ›ba": "ba", "É›baa": "ba", "bebÉ›yÉ›": "yÉ›", "yÉ›reba": "ba", "É”bÉ›yÉ›É›É›": "yÉ›",
    "É”rebÉ›ba": "ba", "É”bÉ›baÉ›": "ba", "abÉ›yÉ›": "yÉ›", "É”yÉ›É›": "yÉ›", "É”bÉ›yÉ›a": "yÉ›"
    "É›yÉ›", "reyÉ›", "di", "É›di", "redi", "bÉ›di", "ka", "É›ka", "reka", "bÉ›ka", 
    "tÉ”", "É›tÉ”", "retÉ”", "bÉ›tÉ”", "fa", "É›fa", "refa", "bÉ›fa", "gye", "É›gye", 
    "regye", "bÉ›gye", "hwe", "É›hwe", "rehwe", "bÉ›hwe", "yÉ›n", "É›yÉ›n", "reyÉ›n", 
    "bÉ›yÉ›n", "kÉ”É”", "baa", "bÉ”É”", "yÉ›É›", "mee", "wÉ”É”", "yÉ›nko", "mmra", "bra",
    "yÉ›yÉ›", "reba", "rebÉ›yÉ›", "bÉ›yÉ›É›", "firi", "frÉ›", "yÉ›frÉ›", "kae", "da", "te", 
    "É›te", "wote", "tumi", "nsa", "abÉ”", "abÉ›", "de", "ma", "yÉ›yÉ›É›", "yÉ›nfa", 
    "mpa", "nkyerÉ›", "nkyia", "bÉ”ne", "adeÉ›", "nnam", "nsuo", "kÉ”kÉ”É”", "kÉ”kÉ”", 
    "É”kÉ”", "yÉ›re", "yÉ›pÉ›", "yÉ›srÉ›", "bÉ›yÉ›re", "bÉ›pÉ›", "bÉ›srÉ'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”', 'É›yÉ›', 'É”do', 'adwuma', 'nkwagyeÉ›', 'É›noa', 'É”ba', 'É›kÉ”', 'É”ma', 'É›tÉ”', 'É”wo', 'akoma', 'É›dÉ”', 'É”fi', 'É›bo', 'É”su', 'kÉ”kÉ”É”', 'fitaa', 'É›de', 'É”man', 'nkÉ”soÉ”']
    # (Add the remaining 270+ words here or load from external file if needed)
}

# Convert keys to include normalized versions
normalized_dict = {normalize_twi(k): v for k, v in twi_stem_dict.items()}

# Sidebar showing available words
with st.sidebar:
    st.subheader("ðŸ“š Available Words")
    all_words = list(normalized_dict.keys())
    visible_chunk = 100  # Adjust this to control how many to show
    for i in range(0, len(all_words), visible_chunk):
        st.markdown(", ".join(all_words[i:i+visible_chunk]))

# Input
user_input = st.text_input("Enter a Twi word (use '3' for É› and 'c' for É”):")

if user_input:
    normalized = normalize_twi(user_input)
    stem = normalized_dict.get(normalized)
    if stem:
        st.success(f"âœ… Stemmed result: **{stem}**")
    else:
        st.error("âŒ Word not found in dictionary.")