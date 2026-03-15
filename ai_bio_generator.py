import openai
import os

def generate_dynamic_bio():
    "\""Generates a dynamic professional bio using LLM."\""
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = "Write a short, engaging professional bio for a Software Engineer specializing in AI integrations and Frontend Architecture."
    
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "Software Engineer | AI-Integrated Web Specialist"

if __name__ == "__main__":
    print(generate_dynamic_bio())