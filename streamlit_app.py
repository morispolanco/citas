python
import streamlit as st
import random

# Dictionary of quotes grouped by topics
quote_database = {
    "Wisdom": [
        "The only true wisdom is in knowing you know nothing. - Socrates",
        "Knowing yourself is the beginning of all wisdom. - Aristotle",
        "The unexamined life is not worth living. - Socrates"
    ],
    "Happiness": [
        "Happiness is the highest good. - Aristotle",
        "Happiness is the meaning and purpose of life. - Albert Camus"
    ],
    "Knowledge": [
        "Knowledge is power. - Francis Bacon",
        "The fool doth think he is wise, but the wise man knows himself to be a fool. - William Shakespeare"
    ]
}

def get_quotes(topic):
    if topic in quote_database:
        return quote_database[topic]
    else:
        return []

# Streamlit app
def main():
    st.title("Philosopher Quotes")
    
    topics = list(quote_database.keys())
    selected_topic = st.selectbox("Select a topic", topics)
    
    if st.button("Generate Quotes"):
        quotes = get_quotes(selected_topic)
        if len(quotes) > 0:
            selected_quotes = random.sample(quotes, 10)
            for quote in selected_quotes:
                st.write("- " + quote)
        else:
            st.write("No quotes found for the selected topic.")

if __name__ == "__main__":
    main()
