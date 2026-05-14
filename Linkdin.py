from dotenv import load_dotenv
import os

from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()

# Initialize Gemini LLM
llm = ChatGroq(
    model="llama3-8b-8192",
    google_api_key=os.getenv("GROKAI_API_KEY"),
    temperature=0.0
)

# Prompt Template
prompt = PromptTemplate(
    input_variables=["topic", "tone", "targeted_audiance"],
    template="""
You are an AI assistant optimized to write linkdin posts.

Write a Attractive post about {topic}.

tone: {tone}

targeted_audiance: {targeted_audiance}
"""
)

# User Input
topic = input("Topic: ")
tone = input("Tone: ")
targeted_audiance = input("Targeted Audience: ")

# Create Final Prompt
final_prompt = prompt.format(
    topic=topic,
    tone=tone,
    targeted_audiance=targeted_audiance
)

# Generate Response
response = llm.invoke(final_prompt)

# Print Output
print("\nGenerated LinkedIn Post:\n")
print(response.content)