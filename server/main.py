import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware

# summarizer.py
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

client = OpenAI()


class URLCheckRequest(BaseModel):
    url: str

@app.post("/scrape_url")
async def scrape_url(request: URLCheckRequest):
    """
    Scrape the page at the given URL and extract the text content.
    Returns the scraped text.
    """
    response = requests.get(request.url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    prompt = f"""
    --------
    {text}
    --------
    Using the above information and write a summary -- \
    The report should be well structured, informative, \
    in depth, with facts and numbers if available and a maximum of 500 words.
    Please do your best, this is very important to my career."""

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a research scholar whose expertise lies in analyzing text and summarizing it within 250 words."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"result": completion.choices[0].message.content}


