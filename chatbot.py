import random

# Define a list of predefined responses
responses = {
    "hello": ["Hi there!", "Hello!", "Greetings!"],
    "how are you": ["I'm just a computer program, but I'm here to help.", "I'm doing well, thank you."],
    "bye": ["Goodbye!", "Have a great day!", "See you later!"],
    "help": ["I can assist you with general inquiries. Just ask me a question."]
}

def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert user input to lowercase for case insensitivity

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I'm sorry, I don't understand that. You can ask for help if you're unsure."

if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you today? Type 'bye' to exit.")
    
    # Open a file for writing responses
    with open("chatbot_responses.txt", "w") as file:
        while True:
            user_input = input("You: ")
            if user_input.lower() == "bye":
                print("Chatbot: Goodbye!")
                break
            
            response = chatbot_response(user_input)
            print("Chatbot:", response)
            
            # Write the user input and chatbot response to the file
            file.write(f"You: {user_input}\n")
            file.write(f"Chatbot: {response}\n")
