# Research Ai-Agent

An AI-powered research assistant agent built with LangChain and Google's Gemini models. It can autonomously search the web, query Wikipedia, and save compiled research directly to a text file.

## Features

- **Powered by Gemini:** Uses `gemini-3-flash-preview` for high-speed reasoning and tool-calling capabilities.
- **Integrated Tools:** Equipped with DuckDuckGo Search and Wikipedia for gathering real-time, factual information.
- **Structured Output:** Enforces structured JSON responses using Pydantic (extracting Topic, Summary, Sources, and Tools Used).
- **File Saving:** Automatically saves compiled research output to a local `research_paper.txt` file.

## Prerequisites

- Python 3.9+
- A Google Gemini API Key

## Setup

1. **Install the dependencies:**
   Make sure you have all the required LangChain packages and tool dependencies installed in your environment:

   ```bash
   pip install langchain-core langchain-google-genai langchain-classic langchain-community pydantic python-dotenv ddgs wikipedia
   ```

2. **Configure Environment Variables:**
   Create a `.env` file in the root directory of the project and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_google_api_key_here
   ```

## Usage

Run the main script:

```bash
python main.py
```

When prompted with `What do you want to research?`, enter your topic and let the agent do the work!
