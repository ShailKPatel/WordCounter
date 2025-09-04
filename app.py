import streamlit as st
import string

st.set_page_config(page_title="Word & Character Counter", layout="centered")

st.title("🔍 Word & Character Counter")

st.write(
    "Paste or type text below to get quick statistics: words, letters, digits, "
    "spaces, and special characters."
)

# Input box
text = st.text_area("Enter your text here:", height=200)

if st.button("Analyze Text"):
    if text.strip():
        # Basic counts
        total_chars = len(text)
        total_words = len(text.split())
        alphabets = sum(c.isalpha() for c in text)
        digits = sum(c.isdigit() for c in text)
        spaces = sum(c.isspace() for c in text)
        specials = total_chars - (alphabets + digits + spaces)

        # Show results
        st.subheader("📊 Text Statistics")
        st.write(f"**Total Characters:** {total_chars}")
        st.write(f"**Total Words:** {total_words}")
        st.write(f"**Alphabets:** {alphabets}")
        st.write(f"**Digits:** {digits}")
        st.write(f"**Spaces:** {spaces}")
        st.write(f"**Special Characters:** {specials}")
    else:
        st.warning("Please enter some text to analyze.")
