# Academic Research Assistant Agent

This project is an example implementation of an AgentPro-style ReAct agent that assists with academic literature reviews. It searches Semantic Scholar, downloads open access PDFs, extracts their text, summarizes them with OpenAI, and generates a PowerPoint presentation.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenAI API key in the environment:
   ```bash
   export OPENAI_API_KEY=your-key-here
   ```

## Usage

Run the agent with a research query:

```bash
python main.py "transformers in NLP" --limit 3
```

This will produce `summary.pptx` in the working directory summarizing the papers.
