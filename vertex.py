# Before you start run this command:
# pip install --upgrade --user --quiet google-cloud-aiplatform
# after running pip install make sure you restart your kernel
import vertexai
from vertexai.language_models import TextGenerationModel
from vertexai.preview.generative_models import GenerationConfig,GenerativeModel
# Set values as per your requirements
PROJECT_ID = 1 # set to your project_id
vertexai.init(project=1, location=us-central1)
PROMPT=´What is a LLM?´ # set your prompt here
model = GenerativeModel(‘gemini-1.5-pro-002’)
# call the Gemini API
response = model.generate_content(PROMPT)
print(response.text)
# google AI Studio SDK
import google.generativeai as genai
import os
# update with your API key
genai.configure(api_key=os.environ[“GOOGLE_API_KEY”])
# choose the model
model = genai.GenerativeModel(‘gemini-pro’)
response = model.generate_content(‘What is a LLM?’) # set your prompt here
print(response.text)