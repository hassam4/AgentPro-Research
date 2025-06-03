import os
from tools.semantic_scholar import search_papers
from tools.pdf_downloader import download_pdfs
from tools.pdf_reader import read_pdf
from tools.summarizer import summarize_text
from tools.ppt_generator import create_ppt


class ResearchAgent:
    """Simple ReAct-style agent for academic research."""

    def __init__(self, query: str, limit: int = 3):
        self.query = query
        self.limit = limit
        self.openai_api_key = os.getenv("OPENAI_API_KEY")

    def run(self) -> str:
        print(f"Thought: I need to search papers for '{self.query}'.")
        papers = search_papers(self.query, limit=self.limit)
        print(f"Observation: found {len(papers)} papers.")

        print("Thought: I should download open access PDFs.")
        pdf_paths = download_pdfs(papers)
        print(f"Observation: downloaded {len(pdf_paths)} PDFs.")

        summaries = []
        for paper, path in zip(papers, pdf_paths):
            print(f"Thought: reading and summarizing '{paper['title']}'.")
            text = read_pdf(path)
            summary = summarize_text(text, self.openai_api_key)
            summaries.append({"title": paper["title"], "summary": summary})
            print(f"Observation: summarized '{paper['title']}'.")

        print("Thought: generating presentation.")
        ppt_path = create_ppt(summaries)
        print("Observation: presentation created.")
        return ppt_path
