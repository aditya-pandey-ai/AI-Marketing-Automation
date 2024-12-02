import os
from groq import Groq

def generate_llm_insights(campaign_summary):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a marketing strategy expert analyzing campaign performance."
                },
                {
                    "role": "user",
                    "content": f"""
                    Analyze these campaigns:
                    {campaign_summary}
                    """
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
