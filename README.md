# AI-CHATBOT-WITH-NLP
COMPANY: CODETECH IT SOLUTIONS NAME : N.SAI KIRAN REDDY INTERN ID: CT06DN318 DOMAIN : PYTHON DURATION: 6 WEEKS MENTOR: NEELA SANTOSH

# DESCRIPTION
This Python-based chatbot project is a rule-based conversational agent designed to simulate human-like interactions. It utilizes Natural Language Processing (NLP) techniques to interpret user inputs and respond with relevant information from a predefined knowledge base. The chatbot's core functionality lies in its ability to handle greetings, farewells, and common queries, making it suitable for basic customer support or informational roles.

The chatbot is implemented using the nltk (Natural Language Toolkit) library, which powers the preprocessing pipeline. Specifically, it employs tokenization and lemmatization to standardize user inputs. The WordNetLemmatizer from NLTK helps convert words to their root form, which improves the accuracy of keyword matching and ensures that different forms of a word (e.g., "running", "ran", "runs") are treated the same.

The system begins by initializing several sets of known phrases:

Greetings (e.g., "hello", "hi", "what's up") and corresponding responses.

Farewells (e.g., "bye", "exit") that signal the end of a conversation.

A knowledge base that maps common queries (like “what is your name” or “order status”) to predefined answers.

The chatbot starts with a welcoming message and then enters an interactive loop where it continuously waits for user input. When a message is received, it first checks if the message matches any greetings or farewells. If a match is found, an appropriate response is selected randomly from the list, giving the illusion of varied and natural responses.

If no greeting or farewell is detected, the chatbot proceeds to process the message using the preprocess_text() function. This function lowercases the input, removes punctuation, tokenizes the sentence, and lemmatizes the tokens. The cleaned tokens are then compared against the lemmatized forms of keys in the knowledge base.

The chatbot uses a keyword matching strategy to identify the most relevant response. It calculates how many lemmatized words from each knowledge base key are present in the user's input. The response with the highest number of matches is chosen. If no meaningful match is found, a default response is returned to prompt the user to rephrase their query.

The script also includes debugging features, such as print statements and try-except blocks. These assist in identifying errors, particularly in the preprocessing and input stages, making the chatbot robust against unexpected inputs or system errors.

This chatbot is a practical starting point for students or developers looking to build intelligent assistants. It’s modular and extensible—developers can easily add more domain-specific queries, integrate APIs, or incorporate machine learning models for more dynamic interactions. Moreover, it provides a clean example of how to use NLP libraries like NLTK for conversational applications.

In conclusion, this chatbot exemplifies the foundational principles of conversational AI using Python and rule-based logic. It’s lightweight, easy to maintain, and a perfect base for developing into a more complex virtual assistant.

#OUTPUT

![Image](https://github.com/user-attachments/assets/ba1601dd-4568-4013-b43a-ff42c4de1a3f)
