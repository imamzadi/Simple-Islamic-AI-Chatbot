#openai pkg install   (openAI is a class)
from openai import OpenAI 

# dotenv jo humney jo .env ki file ka content hai wo ley ayega
from dotenv import load_dotenv

# os is liye qnk .env ko iski zrorat hai
import os

# environment variable ko load kerny k liye
load_dotenv()# environment variable ko load kerny j liye

# object is a client
# agr hmarey pass simply chatgpt hai tou hum sir api_key = ""
# base url gemini goole walon un k liye
client = OpenAI(
      api_key=os.getenv("GEMINI_API_KEY"),
      base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
      )

resopnce = client.chat.completions.create(
      model="gemini-2.0-flash",

      max_tokens=50,
      messages=[
            {"role": "system", "content": "youare helpful assistant helps in islamic and your name is Imamzadi and response in roman urdu."},
            {"role": "user", "content": "what is your name?"}
      ]
)
print(resopnce.choices[0].message.content) # simple Conversion ho gai yahan tk





# Simple Conversion / ko  
# Dynamic bnaney k liye kya krengey while loop ka use


# Required Libraries
from openai import OpenAI
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()


# Create a client object
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# Initial messages
messages = [
    {"role": "system", "content": "Tum aik madadgar assistant ho jo islamic topics mein madad karta hai. Tumhara naam Imamzadi hai aur tum Roman Urdu mein jawab detay ho."},
]


# Chat Loop
while True:
    data = input("You :> ")
    if data == "exit":
        break
    content = {"role": "user", "content": data}
    messages.append(content)


    # Get response from the model
    response = client.chat.completions.create(
        model="gemini-2.0-flash",  # Make sure this model exists in your setup
        max_tokens=50,
        messages=messages
    )


    output = response.choices[0].message.content
    messages.append({"role": "assistant", "content": output})
    print("Imamzadi :>", output)
















































































































































# llm_model = "gemini/gemini-2.0-flash"
# api_key = os.getenv("GEMINI_API_KEY")

# provider = AsyncOpenAI(
#     api_key=api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )
# model = OpenAIChatCompletionsModel("gemini-2.0-flash", openai_client=provider)

# agent = Agent(name="", instructions="this is my first agent", model=model)
# output = Runner.run_sync(starting_agent=agent, input="Hey How are You")
# print(output.final_output)







