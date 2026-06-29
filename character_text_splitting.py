from langchain_text_splitters import CharacterTextSplitter
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import SimpleDirectoryReader
from llama_index.core import Document

text = """LangChain is a powerful framework for developing applications powered by language models.
It enables developers to chain together components like LLMs, prompts, and memory to create advanced conversational AI systems.
Text splitters in LangChain help break large documents into smaller pieces for processing."""

def character_splitter():
    splitter = CharacterTextSplitter(
        chunk_size=40,
        chunk_overlap=10,
        separator=" "
    )

    chunks = splitter.split_text(text.replace("\n", " "))

    print("📄 Number of Chunks:", len(chunks))
    for i, chunk in enumerate(chunks):
        print(f"\nChunk {i+1}:\n{chunk}")

def doc_character_splitter():
    splitter = CharacterTextSplitter(
        chunk_size=40,
        chunk_overlap=10,
        separator=" "
    )
    docs=splitter.create_documents([text])
    for doc in docs:
        print(f"\n Document Details: {doc.page_content} \n Metadata : {doc.metadata}")

def llama_character_splitter():
    splitter=SentenceSplitter(
        chunk_size=200,
        chunk_overlap=15,
    )
    documents=SimpleDirectoryReader(
        input_files=["test_files\Git Cheat Sheat.pdf"]
    ).load_data()

    nodes=splitter.get_nodes_from_documents(documents)
    for node in nodes:
        print(node)
        print("------------------------------------------------------")


if __name__ == "__main__":  
    llama_character_splitter()