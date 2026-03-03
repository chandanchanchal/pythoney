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
