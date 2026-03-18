# Hands-On Lab (HOL): Google Gemini Document AI

## Audience
Developers familiar with **Java / .NET**

---

## Lab Overview
In this hands-on lab, you will build a **Document AI system using Google Gemini** that:
- Uploads PDF documents
- Extracts structured data
- Outputs JSON
- Handles multiple document types

---

# Module 1: Setup

## Step 1: Get API Key
1. Go to https://ai.google.dev
2. Generate API Key

---

## Step 2: Install SDKs

### Python (reference implementation)
```bash
pip install google-generativeai
```

### Java (REST approach)
Use WebClient / RestTemplate

### .NET
Use HttpClient

---

# Module 2: Basic Document Extractor

## Use Case: Insurance Claim Processing

### Step 1: Upload File

### Step 2: Prompt Design
Extract:
- Name
- Policy Number
- Date

### Example Prompt
```
Extract the following fields:
- Full Name
- Policy Number
- Date

Return JSON format.
```

---

## Step 3: API Call (Python Example)

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")

response = model.generate_content(
    ["Extract structured data from this document", file]
)

print(response.text)
```

---

## Step 4: Expected Output

```json
{
  "name": "Priya Sharma",
  "policy_number": "ABC123",
  "date": "2024-01-10"
}
```

---

# Module 3: Enhanced Processor

## Multi-document Support
- Claims
- Invoices
- IDs

## Add Validation
- Required fields
- Date format
- Numeric checks

---

# Module 4: Pipelines

## Key Concepts
- Batch processing
- Async processing
- Error handling
- Retry logic

---

## Example Flow
1. Upload
2. Validate
3. Process
4. Store

---

# Module 5: Confidence Scoring

## Example Output
```json
{
  "name": "Priya Sharma",
  "confidence": 0.94
}
```

---

# Bonus: .NET Sample

```csharp
var client = new HttpClient();
```

---

# Bonus: Java Sample

```java
HttpClient client = HttpClient.newHttpClient();
```

---

# Final Exercise

Build:
- Upload UI
- Gemini integration
- JSON output
- Validation

---

# Reference
Based on training content: Google Gemini Document AI
