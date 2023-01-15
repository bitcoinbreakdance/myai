import openai

# Replace YOUR_API_KEY with your actual API key
openai.api_key = "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"

# Define the prompt
prompt = "Write a short story about a robot who is programmed to love humans"

# Use the OpenAI API to generate text
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024
)

# Print the generated text
print(response["choices"][0]["text"])
