import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string
import random # For choosing random greetings/farewells
import sys # Import sys to potentially help with output issues

print("--- DEBUG: Script started! ---") # ADD THIS LINE HERE

# --- Initialize NLTK components ---
lemmatizer = WordNetLemmatizer()

# --- Knowledge Base and Responses ---
# Define greetings, farewells, and general responses
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey")
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

FAREWELL_INPUTS = ("bye", "goodbye", "see ya", "cya", "exit", "quit")
FAREWELL_RESPONSES = ["Goodbye!", "See you later!", "Bye!", "Have a great day!"]

# Main knowledge base for specific queries
# You can expand this significantly!
KNOWLEDGE_BASE = {
    # General queries
    "how are you": "I am a bot, so I don't have feelings, but I'm functioning perfectly and ready to assist you!",
    "what is your name": "I am a simple chatbot created to help you. You can call me Bot.",
    "what can you do": "I can answer basic questions based on my knowledge base. Try asking about our services or products!",
    "who created you": "I was created by a human programmer.",
    "thank you": "You're welcome! Happy to help.",
    "thanks": "You're welcome!",

    # Product/Service related queries (expand these with real info)
    "services": "We offer product information, order tracking, and customer support. What are you looking for?",
    "products": "We have a range of electronic gadgets like laptops, mice, keyboards, and monitors. Which one interests you?",
    "laptop": "Our laptops are powerful and versatile. Do you have a specific model in mind?",
    "order status": "To check your order status, please provide your order number.",
    "support": "For technical support, please visit our support page or describe your issue.",

    # Fallback/Default
    "default": "I'm sorry, I don't understand that. Could you please rephrase or ask something else?"
}

# --- Preprocessing Functions ---
# --- Preprocessing Functions ---
def preprocess_text(text):
    """Tokenizes, lowercases, removes punctuation, and lemmatizes text."""
    # Debug print to check the type and value of 'text'
    print(f"--- DEBUG: preprocess_text received type: {type(text)}, value: '{text}'")

    if not isinstance(text, str):
        # This guard should prevent the split error if text is not a string,
        # but it means something upstream is passing a non-string.
        print("--- DEBUG: Non-string input to preprocess_text. Returning empty list.")
        return []

    text = text.lower()
    # Remove punctuation
    text = ''.join([char for char in text if char not in string.punctuation])
    
    # word_tokenize expects a string
    tokens = word_tokenize(text)
    
    # Lemmatize tokens
    lemmas = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmas

# --- Chatbot Logic ---
def respond_to_greeting(sentence):
    """Checks if the user input is a greeting and returns a random greeting response."""
    for word in sentence.split(): # Tokenize by space for simple check
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return None

def respond_to_farewell(sentence):
    """Checks if the user input is a farewell and returns a random farewell response."""
    for word in sentence.split():
        if word.lower() in FAREWELL_INPUTS:
            return random.choice(FAREWELL_RESPONSES)
    return None

def get_chatbot_response(user_input):
    """
    Processes user input and returns a relevant response.
    """
    # 1. Check for greetings
    greeting_response = respond_to_greeting(user_input)
    if greeting_response:
        return greeting_response, False # Return response and no exit flag
    
    # 2. Check for farewells (handles exit condition)
    farewell_response = respond_to_farewell(user_input)
    if farewell_response:
        return farewell_response, True # Return response and exit flag

    # 3. Process user input for knowledge base matching
    processed_input_lemmas = preprocess_text(user_input)

    # 4. Keyword/Intent Matching (simple rule-based)
    best_match_response = KNOWLEDGE_BASE["default"]
    max_matches = 0

    # Iterate through knowledge base keywords and find the best match
    for key, response_text in KNOWLEDGE_BASE.items():
        if key == "default": # Skip default for keyword matching
            continue
        
        key_lemmas = preprocess_text(key)
        
        # Count how many words from the knowledge base key are in the user's input
        current_matches = sum(1 for lemma in key_lemmas if lemma in processed_input_lemmas)
        
        # If we find more matches, update the best match
        if current_matches > max_matches:
            max_matches = current_matches
            best_match_response = response_text
        # If same number of matches, but the key is longer (more specific), prefer it
        elif current_matches == max_matches and current_matches > 0 and len(key_lemmas) > len(preprocess_text(best_match_response)):
             best_match_response = response_text

    return best_match_response, False # Return response and no exit flag

# --- Main Chatbot Interaction Loop ---
if __name__ == "__main__":
    try: # ADD THIS TRY BLOCK
        print("--- Simple Chatbot ---")
        print("Chatbot: Hello! I'm here to help. Type 'bye' or 'quit' to exit.")
        
        chatting = True
        while chatting:
            user_message = input("You: ")
            
            response, should_exit = get_chatbot_response(user_message)
            
            print(f"Chatbot: {response}")
            
            if should_exit:
                chatting = False
    except Exception as e: # ADD THIS EXCEPT BLOCK
        print(f"--- DEBUG: An error occurred: {e}")
        # You can add more detailed error logging here if needed
        sys.exit(1) # Exit with an error code