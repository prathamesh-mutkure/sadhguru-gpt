import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="tunedModels/sadhguru-mini-h8iq4ay0q80e",
    generation_config=generation_config,
)

chat_session = model.start_chat(
    history=[
    ]
)


def main():
    print("Welcome to the SadhguruGPT -")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        bot_response = chat_session.send_message(
            f"Answer as sadhguru in short - {user_input}")
        print(f"Bot: {bot_response}")


if __name__ == "__main__":
    main()
