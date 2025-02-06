from langchain_groq import ChatGroq

llm = ChatGroq(
    temperature=0,
    groq_api_key= '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',
    model="llama-3.3-70b-versatile",
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
response=llm.invoke("the first person to land on moon was")
print(response.content)