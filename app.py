import streamlit as st
import string
import re
from collections import Counter

st.set_page_config(page_title="Advanced Text Analyzer", layout="wide")

st.title("🔍 Advanced Word & Text Analyzer")

st.write(
    "Paste or type text below to get detailed statistics: words, sentences, "
    "paragraphs, characters, reading time, lexical diversity, and more."
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

        # Sentences and paragraphs
        sentences = re.split(r'[.!?]+', text.strip())
        sentence_count = len([s for s in sentences if s.strip()])
        paragraphs = [p for p in text.split("\n") if p.strip()]
        paragraph_count = len(paragraphs)

        # Averages
        avg_word_length = round(sum(len(w) for w in text.split() if w.isalpha()) / total_words, 2) if total_words else 0
        avg_sentence_length = round(total_words / sentence_count, 2) if sentence_count else 0

        # Most common words
        words_clean = [w.strip(string.punctuation).lower() for w in text.split()]
        word_freq = Counter([w for w in words_clean if w])
        most_common = word_freq.most_common(10)

        # Longest and shortest words
        longest_word = max(words_clean, key=len) if words_clean else ""
        shortest_word = min(words_clean, key=len) if words_clean else ""

        # Reading time estimate (200 wpm)
        reading_time = round(total_words / 200, 2)

        # Lexical diversity
        lexical_diversity = round(len(set(words_clean)) / total_words, 2) if total_words else 0

        # Vowels vs consonants
        vowels = sum(c.lower() in "aeiou" for c in text if c.isalpha())
        consonants = alphabets - vowels

        # Punctuation count
        punctuation_count = sum(c in string.punctuation for c in text)

        # Show results
        st.subheader("📊 Text Statistics")
        st.write(f"**Total Characters:** {total_chars}")
        st.write(f"**Total Words:** {total_words}")
        st.write(f"**Total Sentences:** {sentence_count}")
        st.write(f"**Total Paragraphs:** {paragraph_count}")
        st.write(f"**Alphabets:** {alphabets}")
        st.write(f"**Digits:** {digits}")
        st.write(f"**Spaces:** {spaces}")
        st.write(f"**Special Characters:** {specials}")
        st.write(f"**Punctuation Marks:** {punctuation_count}")
        st.write(f"**Average Word Length:** {avg_word_length}")
        st.write(f"**Average Sentence Length (words):** {avg_sentence_length}")
        st.write(f"**Reading Time (minutes):** {reading_time}")
        st.write(f"**Lexical Diversity (unique/total words):** {lexical_diversity}")
        st.write(f"**Longest Word:** {longest_word}")
        st.write(f"**Shortest Word:** {shortest_word}")
        st.write(f"**Vowels:** {vowels}")
        st.write(f"**Consonants:** {consonants}")

        # Most common words
        st.subheader("🔠 Most Common Words")
        if most_common:
            for word, freq in most_common:
                st.write(f"{word} : {freq}")
        else:
            st.write("No words found.")
    else:
        st.warning("Please enter some text to analyze.")
