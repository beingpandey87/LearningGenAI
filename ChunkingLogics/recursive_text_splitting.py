from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """LangChain is a powerful framework for developing applications powered by language models.
It enables developers to chain together components like LLMs, prompts, and memory to create advanced conversational AI systems.
Text splitters in LangChain help break large documents into smaller pieces for processing."""


def recursive_spliter():
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=65,
        chunk_overlap=10,
    )

    docs=text_splitter.create_documents([text])
    print("📄 Number of Chunks:", len(docs))
    for i, doc in enumerate(docs):
        print(f"\nChunk {i+1}:\n{doc}")

if __name__ == "__main__":  
    recursive_spliter()