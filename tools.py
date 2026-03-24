from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.tools import Tool
from datetime import datetime

def save_to_txt(data: str, filename: str = "research_paper.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    formatted_text = f"--- Research Output ---\nTImestamp: {timestamp}\n\n{data}\n---"

    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_text)
    
    return f"Data saved to {filename}"  

save_tool = Tool(
    name="save_text_to_file",
    description="Saves structured research data to text file",
    func=save_to_txt,    
)


search = DuckDuckGoSearchRun()

search_tool = Tool(
    name="search",
    description="Search the web for information",
    func=search.run,
)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=100)
wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)
