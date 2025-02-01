from litellm import completion
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the API key securely
api_key = os.getenv("GEMINI_API_KEY")
api_key = os.getenv("ANTHROPIC_API_KEY")
api_key = os.getenv("GROQ_API_KE")


# os.environ['GEMINI_API_KEY'] = 'AIzaSyDoNF1SOBdEQhNJqQ9M-xlE'

def gemini():
    response = completion(
        model="gemini/gemini-1.5-flash",
        messages=[{ "content": "WHo is the founder of Pakistan?","role": "user"}]
    )

    print(response.choices[0].message.content)


def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{ "content": "Hello, how are you?","role": "user"}],
    )

    print(response.choices[0].message.content)    


def anthropic():
    response = completion(
        model="claude-3-opus-20240229",
        messages=[{ "content": "Hello, how are you?","role": "user"}],
        
    )

    print(response.choices[0].message.content)    



def llama():
    response = completion(
        model="llama3-8b-8192",  
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        api_base="https://api.groq.com/openai/v1",  
    )
    print(response["choices"][0]["message"]["content"])  

