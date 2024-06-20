import os
from dotenv import load_dotenv
load_dotenv('')
import requests
from bs4 import BeautifulSoup
from docx import Document
from urllib.parse import urljoin
import pprint
from langchain.chains import StuffDocumentsChain, LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain.chat_models import ChatOpenAI

# Define the URL of the website you want to scrape
base_url = "Paste the URL of the website you want to scrape here"

# Send a GET request to the website
response = requests.get(base_url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the links on the page
links = soup.find_all("a")

# Create a new Word document
doc = Document()
txt = ""
i = 0

# For each link, send a GET request to the linked page and scrape the text
for link in links:
    i += 1
    url = urljoin(base_url, link.get("href"))
    if url.startswith("mailto:") or url.startswith("tel:"):
        continue
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    for paragraph in paragraphs:
        doc.add_paragraph(paragraph.text)
        txt += paragraph.text

print(i)
#Save the document
doc.save("scraped_text.docx")

#Split the text into two parts
part_1=txt[:500000]
part_2=txt[500000:-1]

# This controls how each document will be formatted. Specifically,
# it will be passed to `format_document` - see that function for more
# details.

template = """ Answer the question based only on the following context:

{context}

Question: {question}
"""

prompt = PromptTemplate(
    input_variables=["context","question"],
    template=template
)

llm = ChatOpenAI(model="gpt-4-1106-preview",temperature=0)

# The prompt here should take as an input variable the
# `document_variable_name`

llm_chain = LLMChain(llm=llm, prompt=prompt)

# Ask a question based on the context
query = "Write your question here."

# Run the model
# The `context` variable is passed to the `format_document` function
res1 = llm_chain.run(context=part_1, question=query)
res2 = llm_chain.run(context=part_2, question=query)
pprint.pprint(res1)
pprint.pprint(res2)