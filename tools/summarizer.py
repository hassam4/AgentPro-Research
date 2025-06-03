import openai


PROMPT = (
    "Summarize the following academic paper text in a concise paragraph "
    "highlighting the main contributions, methods, and conclusions."
)


def summarize_text(text: str, api_key: str, model: str = "gpt-3.5-turbo") -> str:
    """Summarize text using OpenAI ChatCompletion."""
    if not api_key:
        raise ValueError("OpenAI API key is required")
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": PROMPT + "\n" + text}]
    )
    return response.choices[0].message["content"].strip()
