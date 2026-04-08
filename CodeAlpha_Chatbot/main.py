def generate_reply(user_text):
    """
    Return a response based on simple predefined inputs.
    """

    text = user_text.lower().strip()

    if text == "hello":
        return "Hi"

    elif text == "how are you":
        return "I am fine, thanks!"

    elif text == "bye":
        return "Goodbye!"

    else:
        return "I didn't understand that."


def start_chat():

    print("Chat started. Type 'bye' to end the conversation.\n")

    while True:
        user_message = input("You: ")

        bot_reply = generate_reply(user_message)
        print("Bot:", bot_reply)

        if user_message.lower().strip() == "bye":
            break


if __name__ == "__main__":
    start_chat()