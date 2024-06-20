# webscraper_LLM_Chain
This project is a Python script that scrapes text from a specified website and processes it using a language model to answer questions based on the scraped content.. It's useful to obtain specific information from a website faster rather than scrolling, or to avoid hallucinations from LLM.

# Installation
Use the package manager pip to install the required dependencies.

```bash
pip install -r requirements.txt
```

# Requirements
The project requires the following Python packages:

```plaintext
beautifulsoup4==4.12.3
docx==0.2.4
dotenv-python==0.0.1
langchain==0.2.3
langchain-community==0.0.37
langchain-core==0.2.5
langchain-openai==0.1.8
langchainhub==0.1.15
openai==1.26.0
python-docx==1.1.2
python-dotenv==1.0.1
requests==2.31.0
```

These are listed in the requirements.txt file.

# Usage

### 1. Set up environment variables:
Create a .env file in the root directory of your project and add the necessary environment variables for your OpenAI API key.

```bash
OPENAI_API_KEY=your_openai_api_key
```
### 2. Modify the base URL:
In the script, change the base_url variable to the URL of the website you want to scrape.

```bash
base_url = "Paste the URL of the website you want to scrape here"
```

### 3. Run the script:
Execute the script to scrape the website and process the text.

```bash
python script_name.py
````

### 4. Query the model:
The script will process the text and allow you to ask questions based on the scraped content.

# Example
Here is a brief overview of what the script does:

Sends a GET request to the specified website.

Parses the HTML content using BeautifulSoup.

Finds all the links on the page and scrapes the text from each linked page.

Saves the scraped text into a Word document.

Splits the text into two parts and uses a language model to answer questions based on the context.

# Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.
