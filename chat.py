import openai

# Set your OpenAI API key here
openai.api_key = "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"

# Define a global variable to store the response
response = None

def get_response(animal):
    global response  # Declare 'response' as a global variable
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(animal),
        temperature=0.6,
    )
    return response.choices[0].text

def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.
Animal: {}
Names:""".format(
        animal.capitalize()
    )

if __name__ == "__main__":
    animal_input = input("Enter an animal: ")
    result = get_response(animal_input)
    print(f"Bot: {result}")
