from app.utils.llm import llm

response = llm.invoke(
    "Reply with exactly: Mistral connection successful."
)

print(response.content)