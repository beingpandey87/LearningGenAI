from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

# Step 1: Define a sample text corpus
raw_corpus = [
    "The quick brown fox jumps over the lazy dog.",
    "I love deep learning and natural language processing.",
    "Artificial intelligence and machine learning are transforming industries.",
    "The dog and the fox are running in the forest."
]

def word2vec_embedding_operations():
    """
    This function demonstrates the use of Word2Vec embeddings on a sample text corpus.
    It includes training the model, extracting word vectors, finding similar words,
    and calculating cosine similarity between words.
    """
    # Step 2: Preprocess and tokenize the text
    # simple_preprocess lowercases, tokenizes, and removes punctuation
    tokenized_corpus = [simple_preprocess(sentence) for sentence in raw_corpus]

    # Step 3: Initialize and train the Word2Vec model
    model = Word2Vec(
        sentences=tokenized_corpus,
        vector_size=100,  # Dimensionality of the word vectors
        window=5,         # Maximum distance between current and predicted word
        min_count=1,      # Ignores words with total frequency lower than this
        workers=4,        # Use 4 threads for training
        sg=0              # 0 for CBOW architecture, 1 for Skip-gram
    )

    # Step 4: Access and use the trained embeddings
    print("--- Word2Vec Embedding Operations ---\n")

    # A. Extract the raw vector for a specific word
    fox_vector = model.wv['fox']
    print(f"Vector representation for 'fox' (showing first 5 of {len(fox_vector)} dimensions):")
    print(fox_vector[:5], "\n")

    # B. Find the most semantically similar words
    similar_words = model.wv.most_similar('fox', topn=2)
    print("Words most similar to 'fox':")
    print(similar_words, "\n")

    # C. Calculate the cosine similarity score between two words
    similarity_score = model.wv.similarity('learning', 'intelligence')
    print(f"Cosine similarity between 'learning' and 'intelligence': {similarity_score:.4f}")

if __name__ == "__main__":
    word2vec_embedding_operations()
    