import os
import numpy as np
import faiss
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Step 1: Load document
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Step 2: Split into chunks
chunks = text.split("\n\n")

# Step 3: Create embeddings
embeddings = []

for chunk in chunks:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=chunk
    )
    embeddings.append(response.data[0].embedding)

embeddings = np.array(embeddings).astype("float32")

# Step 4: Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

#####################################################
def ask_question(question):
    # Convert question into embedding
    q_embedding = client.embeddings.create(
        model="text-embedding-3-small",
        input=question
    ).data[0].embedding

    q_embedding = np.array([q_embedding]).astype("float32")

    # Search in FAISS
    distances, indices = index.search(q_embedding, k=2)

    retrieved_chunks = [chunks[i] for i in indices[0]]

    context = "\n".join(retrieved_chunks)

    # Generate answer using context
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Answer only from provided context."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion:{question}"}
        ]
    )

    return response.choices[0].message.content


while True:
    user_input = input("\nAsk: ")
    print("\nAnswer:", ask_question(user_input))

