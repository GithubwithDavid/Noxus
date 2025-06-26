from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message);
