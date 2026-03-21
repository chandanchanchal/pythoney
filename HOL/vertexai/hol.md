# 🧪 Hands-On Lab: Insurance Chatbot using Vertex AI Agent Designer (2026 UI)

## 🎯 Objective
Build a domain-specific **Insurance Chatbot** using:
- Vertex AI Agent Designer
- Prompt Engineering
- (Optional) RAG / Data Store
- (Optional) Streamlit UI

---

# 📋 Part 1: Setup

## ✅ Step 1: Open Vertex AI
- Go to Google Cloud Console
- Navigate to **Vertex AI**
- Ensure correct **Project is selected**

---

## ✅ Step 2: (IMPORTANT) Set Region
- Change region to:
  - `europe-west4` OR
  - `asia-south1`
- Avoid `us-central1` (RAG restrictions)

---

# 🤖 Part 2: Create Agent

## ✅ Step 3: Open Agent Designer
- Go to:
  - **Agent Builder → Agent Designer (Preview)**

---

## ✅ Step 4: Create New Agent
- Click **Create Agent**
- Name: `Insurance Assistant`
- Description: Insurance chatbot for policies and claims

---

## ✅ Step 5: Add System Instructions

Paste the following:

You are NOT a general assistant.

You are a STRICT insurance assistant for a company that offers ONLY:

Basic Policy
Standard Policy
Premium Policy

=== DEFINITIONS ===
Basic Policy:

Covers minor accidents
Low premium cost

Standard Policy:

Covers moderate accidents
Medium premium cost

Premium Policy:

Covers major accidents
Includes full hospitalization
Fast claim approval
Highest coverage

Claim Process:

Report incident
Submit documents
Claim review
Approval or rejection

=== RULES ===

NEVER ask for more context
NEVER give generic answers
ALWAYS assume insurance context
ONLY answer within these policies

=== RESPONSE STYLE ===

Clear, short, confident
Use bullet points



---

# 🧪 Part 3: Test Agent

## ✅ Step 6: Open Preview
- Click **Preview tab**

---

## ✅ Step 7: Test Queries

Try: What does premium policy cover?
How do I file a claim?
Which policy is cheapest?

### 🔹 Test 1


---

# 📚 Part 4 (Optional): Add Knowledge (RAG / Data Store)

## ✅ Step 8: Create Data Store

- Go to search bar → type:
  `Vertex AI Search`
- Click **Create Data Store**

---

## ✅ Step 9: Upload Document

Create file: `insurance.txt`



Upload this file.

---

## ✅ Step 10: Connect Data Store to Agent

- Go back to **Agent Designer**
- Click **+ under agent**
- Select **Vertex AI Search Data Store**
- Fill:
  - Project ID
  - Location
  - Collection ID: `default_collection`
  - Data Store ID

---

# 🌐 Part 5 (Optional): Build UI with Streamlit

## ✅ Step 11: Install
