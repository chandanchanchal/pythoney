# 🚀 Hands-On Lab (HOL): Google Gemini Document AI (Advanced)

## Duration: 3–4 Hours  
## Audience: Java (Spring Boot) & .NET Developers  

---

# 🎯 Lab Goal
Build a **production-style Document AI system** using Google Gemini with:
- File Upload API
- Document Processing
- Structured JSON Extraction
- Validation Layer
- Async Pipeline Simulation

---

# 🧩 Lab Breakdown

## ⏱️ Phase 1 (30 mins): Setup & Project Initialization

### Tasks
- [ ] Create Spring Boot project (Java)
- [ ] Create .NET Web API project
- [ ] Setup folder structure:
  - controller/
  - service/
  - model/
  - util/
- [ ] Generate Gemini API Key
- [ ] Store API key in config

---

## ⏱️ Phase 2 (45 mins): File Upload API

### Tasks
- [ ] Create REST endpoint:
  - POST /upload
- [ ] Accept:
  - PDF / Image
- [ ] Save file locally or memory
- [ ] Return file ID

### Bonus
- [ ] Add file size validation
- [ ] Restrict file types

---

## ⏱️ Phase 3 (45 mins): Gemini Integration

### Tasks
- [ ] Create GeminiService
- [ ] Call Gemini REST API
- [ ] Send:
  - File content
  - Prompt

### Prompt Template
```
Extract:
- Name
- Policy Number
- Date

Return JSON format
```

### Output
- [ ] Parse response
- [ ] Convert to JSON object

---

## ⏱️ Phase 4 (30 mins): Validation Layer

### Tasks
- [ ] Validate required fields
- [ ] Validate:
  - Date format
  - Numeric values
- [ ] Handle missing fields

### Bonus
- [ ] Add confidence score field

---

## ⏱️ Phase 5 (45 mins): Async Processing

### Tasks
- [ ] Implement async job:
  - Java: @Async / ExecutorService
  - .NET: async/await + Task
- [ ] Return Job ID
- [ ] Create endpoint:
  - GET /status/{jobId}

---

## ⏱️ Phase 6 (30 mins): Multi-Document Support

### Tasks
- [ ] Accept multiple files
- [ ] Identify document type
- [ ] Use different prompts

---

## ⏱️ Phase 7 (30 mins): Final Integration

### Tasks
- [ ] Combine:
  - Upload → Process → Validate → Output
- [ ] Return final JSON
- [ ] Log processing steps

---

# 🧪 Final Challenge

Build:
- Upload API
- Gemini extraction
- Validation
- Async pipeline
- Multi-document support

---

# 📦 Expected Output

```json
{
  "name": "Priya Sharma",
  "policy_number": "ABC123",
  "date": "2024-01-10",
  "confidence": 0.92
}
```

---

# 💡 Bonus Challenges
- [ ] Add UI (React / simple HTML)
- [ ] Store results in DB
- [ ] Add retry logic
- [ ] Add logging

---

# 🏁 Outcome
By end of lab, learners will:
- Build real-world AI pipeline
- Integrate Gemini API
- Handle documents at scale
- Apply backend best practices
