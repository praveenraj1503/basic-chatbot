import spacy
from random import choice

# Load the English language model from spaCy
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("spaCy language model not found. Install it using 'python -m spacy download en_core_web_sm'")
    exit()

class ChatBot:
    def __init__(self):
        self.responses = {
            "greeting": ["Hello!", "Hi there!", "Hey!", "Good to see you!"],
            "farewell": ["Goodbye!", "See you later!", "Take care!"],
            "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
            "default": ["I'm not sure I understand.", "Could you clarify that?", "Tell me more about that."],
        }

    def classify_intent(self, user_input):
        """
        Classify the user's intent based on keywords or context in the input.
        """
        doc = nlp(user_input.lower())

        if any(token.lemma_ in ["hello", "hi", "hey"] for token in doc):
            return "greeting"
        elif any(token.lemma_ in ["bye", "goodbye", "farewell"] for token in doc):
            return "farewell"
        elif any(token.lemma_ in ["thank", "thanks"] for token in doc):
            return "thanks"
        else:
            return "default"

    def get_response(self, intent):
        """
        Get a response based on the user's intent.
        """
        return choice(self.responses.get(intent, self.responses["default"]))

    def chat(self):
        print("ChatBot: Hi! I'm a chatbot. Type 'exit' to end the chat.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("ChatBot: Goodbye!")
                break
            intent = self.classify_intent(user_input)
            response = self.get_response(intent)
            print(f"ChatBot: {response}")

if __name__ == "__main__":
    chatbot = ChatBot()
    chatbot.chat()
