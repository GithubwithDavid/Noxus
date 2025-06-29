import google.generativeai as genai

genai.configure(api_key="AIzaSyD7LcmmY8eK16iIZwkH_1joN4uPvxjYcMI")
model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("What is the best free api model of gemini i can use?")
print(response.text)