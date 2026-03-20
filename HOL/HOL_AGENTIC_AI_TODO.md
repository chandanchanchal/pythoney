╔═══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║                 HANDS-ON LAB (HOL) - AGENTIC AI                      ║
║                                                                       ║
║     Building a Q&A Agent with LangChain and OpenAI                   ║
║                                                                       ║
║              Module 3: LangChain Essentials & Agents                 ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝


📚 LAB OVERVIEW
===============

In this hands-on lab, you will build a complete Q&A agent system using 
LangChain and OpenAI. You'll learn the architecture, implement each layer,
and create a working agent with custom tools.

Duration: 2-3 hours
Difficulty: Intermediate
Prerequisites: Python 3.8+, Basic understanding of APIs


🎯 LEARNING OBJECTIVES
======================

By the end of this lab, you will be able to:

1. Understand LangChain Architecture (5 layers)
   □ Models - Language models and their initialization
   □ Prompts - Template engineering for deterministic outputs
   □ Chains - Sequences of operations
   □ Memory - Conversation context management
   □ Agents - Autonomous decision-making systems

2. Implement Key Components
   □ Initialize OpenAI models
   □ Create prompt templates (simple, structured, few-shot)
   □ Build LLM chains
   □ Implement conversation memory
   □ Define custom tools

3. Build a Working Q&A Agent
   □ Create an agent with multiple tools
   □ Handle multi-turn conversations
   □ Store and retrieve conversation history
   □ Route questions to appropriate tools

4. Debug and Troubleshoot
   □ Handle API errors
   □ Manage API keys securely
   □ Fix import and version conflicts
   □ Monitor costs and tokens


═══════════════════════════════════════════════════════════════════════

📋 PRE-LAB SETUP (TODO)
=======================

Before starting the lab, complete these setup steps:

TASK 1: Verify Python Installation
───────────────────────────────────
[ ] Open Command Prompt
[ ] Run: python --version
[ ] Verify: Version 3.8 or higher is installed
[ ] If not installed: Download from https://python.org

TASK 2: Create Project Folder
──────────────────────────────
[ ] Create folder: LangChainLab
[ ] Navigate to folder in Command Prompt
[ ] Create subfolder: solutions (for later)

TASK 3: Set Up Virtual Environment
──────────────────────────────────
[ ] Run: python -m venv venv
[ ] Activate: venv\Scripts\activate
[ ] Verify: (venv) appears in command prompt

TASK 4: Get OpenAI API Key
──────────────────────────
[ ] Go to: https://platform.openai.com/api-keys
[ ] Sign in with OpenAI account (create if needed)
[ ] Click: "Create new secret key"
[ ] Copy the key (you won't see it again!)
[ ] Save temporarily in notepad

TASK 5: Create .env File
────────────────────────
[ ] Create file: .env in your project folder
[ ] Add line: OPENAI_API_KEY=sk-your-actual-key-here
[ ] Replace with your actual API key
[ ] Save file

TASK 6: Install Dependencies
─────────────────────────────
[ ] Run: pip install langchain==0.1.1 openai==1.3.5 langchain-community==0.0.13 langchain-core==0.1.10 python-dotenv
[ ] Wait for installation to complete
[ ] Verify: pip list (should show all packages)

TASK 7: Download Lab Files
──────────────────────────
[ ] Download: qa_agent_demo_openai_FIXED.py
[ ] Download: requirements_openai_FIXED.txt
[ ] Place in project folder
[ ] Verify files exist


═══════════════════════════════════════════════════════════════════════

🧪 LAB EXERCISES
================

After setup, complete these exercises in order:

EXERCISE 1: Understanding Architecture
═══════════════════════════════════════

Objective: Understand the 5-layer LangChain architecture

TODO Tasks:
───────────
1. [ ] Read the architecture diagram in qa_agent_demo_openai_FIXED.py
   - Look for: "LangChain Architecture Layers"
   - Find: The ASCII diagram showing 5 layers
   - Draw: Reproduce the diagram on paper

2. [ ] Identify each layer:
   [ ] Layer 1: MODELS - What does this layer do?
       Answer: ___________________________________________
   
   [ ] Layer 2: PROMPTS - What does this layer do?
       Answer: ___________________________________________
   
   [ ] Layer 3: CHAINS - What does this layer do?
       Answer: ___________________________________________
   
   [ ] Layer 4: MEMORY - What does this layer do?
       Answer: ___________________________________________
   
   [ ] Layer 5: AGENTS - What does this layer do?
       Answer: ___________________________________________

3. [ ] Run the demo: python qa_agent_demo_openai_FIXED.py
   [ ] Observe which sections run
   [ ] Note any warnings or errors
   [ ] Document output in a text file

4. [ ] Answer: How do these 5 layers interact?
   Write a 2-3 sentence explanation:
   ________________________________________________
   ________________________________________________
   ________________________________________________


EXERCISE 2: Prompt Engineering
═══════════════════════════════

Objective: Create and test different prompt templates

TODO Tasks:
───────────
1. [ ] Find the prompt engineering section in the code
   - Look for: "SECTION 2: PROMPT ENGINEERING"
   - Find: 3 different prompt examples
   
2. [ ] Analyze each prompt type:
   
   [ ] SIMPLE PROMPT
       - What's the template? _____________________
       - What's missing? _____________________
       - When would you use it? _____________________
   
   [ ] STRUCTURED PROMPT
       - What's the system role? _____________________
       - What constraints are set? _____________________
       - How is it better than simple? _____________________
   
   [ ] FEW-SHOT PROMPT
       - How many examples are shown? _____________________
       - Why are examples useful? _____________________
       - What does this improve? _____________________

3. [ ] Create your own prompt template:
   - Topic: Your choice (not insurance)
   - Create: A structured prompt with:
     [ ] Clear system role
     [ ] Specific constraints
     [ ] Output format specification
     [ ] At least 1 example
   
   Write your prompt:
   ________________________________________
   ________________________________________
   ________________________________________

4. [ ] Test your prompt:
   - Modify the code to use your prompt
   - Run the demo with your prompt
   - Compare results: Is output better? Worse? Different?
   - Document findings


EXERCISE 3: Memory Types
════════════════════════

Objective: Understand and implement memory management

TODO Tasks:
───────────
1. [ ] Find memory implementation in code
   - Look for: "SECTION 4: MEMORY TYPES"
   - Identify: 2 memory types implemented

2. [ ] Analyze BufferMemory:
   [ ] How does it work? _____________________
   [ ] When to use it? _____________________
   [ ] Pros and cons? _____________________
   [ ] Trade-offs? _____________________

3. [ ] Analyze SummaryMemory:
   [ ] How does it work? _____________________
   [ ] When to use it? _____________________
   [ ] Pros and cons? _____________________
   [ ] Trade-offs? _____________________

4. [ ] Compare the two:
   Create a table:
   ┌──────────────┬─────────────┬─────────────┐
   │ Characteristic│BufferMemory │SummaryMemory│
   ├──────────────┼─────────────┼─────────────┤
   │ Storage      │             │             │
   ├──────────────┼─────────────┼─────────────┤
   │ Best for     │             │             │
   ├──────────────┼─────────────┼─────────────┤
   │ Token cost   │             │             │
   ├──────────────┼─────────────┼─────────────┤
   │ Use case     │             │             │
   └──────────────┴─────────────┴─────────────┘

5. [ ] Modify the code:
   - Change memory type
   - Run demo again
   - Observe any differences
   - Document changes


EXERCISE 4: Building Custom Tools
══════════════════════════════════

Objective: Create and integrate custom tools into an agent

TODO Tasks:
───────────
1. [ ] Analyze existing tools:
   - Look for: "SECTION 5: AGENTS & TOOLS"
   - Find: 3 custom tools
   
   [ ] Tool 1: policy_lookup
       - What does it do? _____________________
       - Input: _____________________
       - Output: _____________________
   
   [ ] Tool 2: calculate_premium
       - What does it do? _____________________
       - Input: _____________________
       - Output: _____________________
   
   [ ] Tool 3: get_policy_faq
       - What does it do? _____________________
       - Input: _____________________
       - Output: _____________________

2. [ ] Create a NEW custom tool:
   - Choose a domain (e.g., healthcare, banking, education)
   - Design: 2 new tools for your domain
   
   Tool A:
   [ ] Name: _____________________
   [ ] Purpose: _____________________
   [ ] Input parameters: _____________________
   [ ] Output format: _____________________
   [ ] Implementation: Write pseudocode
   
   Tool B:
   [ ] Name: _____________________
   [ ] Purpose: _____________________
   [ ] Input parameters: _____________________
   [ ] Output format: _____________________
   [ ] Implementation: Write pseudocode

3. [ ] Implement your tools in code:
   [ ] Define the function
   [ ] Add docstring
   [ ] Handle edge cases
   [ ] Test with sample inputs

4. [ ] Integrate into agent:
   [ ] Add to tools list
   [ ] Update tool descriptions
   [ ] Test the agent with your new tools


EXERCISE 5: Building the Q&A Agent
═══════════════════════════════════

Objective: Understand and modify the Q&A agent logic

TODO Tasks:
───────────
1. [ ] Find the agent demo section:
   - Look for: "SECTION 6: INTERACTIVE Q&A DEMO"
   - Find: QAAgentDemo class

2. [ ] Analyze the answer_question method:
   [ ] How does routing work? _____________________
   [ ] What determines which tool is used? _____________________
   [ ] How does context flow? _____________________

3. [ ] Trace a question through the system:
   Pick a sample question: "What is a deductible?"
   [ ] How is it processed? _____________________
   [ ] Which tool handles it? _____________________
   [ ] What's the response? _____________________
   [ ] How is it stored in memory? _____________________

4. [ ] Modify the agent:
   [ ] Add 3 new sample questions
   [ ] Change the routing logic
   [ ] Add a new branch for different question type
   [ ] Test your changes

5. [ ] Create your own agent:
   [ ] Choose a new domain
   [ ] Define 3-5 tools
   [ ] Create sample questions
   [ ] Build complete working agent
   [ ] Test with memory


EXERCISE 6: Error Handling & Debugging
═══════════════════════════════════════

Objective: Handle errors and debug common issues

TODO Tasks:
───────────
1. [ ] Identify common errors in your run:
   [ ] What errors did you see? _____________________
   [ ] What caused them? _____________________
   [ ] How were they handled? _____________________

2. [ ] Debug the API key error:
   [ ] What does 401 error mean? _____________________
   [ ] How would you fix it? _____________________
   [ ] What's the validation process? _____________________

3. [ ] Handle import errors:
   [ ] What causes import errors? _____________________
   [ ] How do you fix them? _____________________
   [ ] How do you prevent them? _____________________

4. [ ] Implement error handling:
   [ ] Add try-except blocks
   [ ] Add input validation
   [ ] Add user-friendly error messages
   [ ] Test error scenarios

5. [ ] Create a troubleshooting guide:
   - Document common issues
   - List solutions for each
   - Create flowchart for debugging


EXERCISE 7: Cost Tracking & Optimization
════════════════════════════════════════

Objective: Understand API costs and optimize usage

TODO Tasks:
───────────
1. [ ] Calculate costs:
   [ ] What's the cost per 1K tokens? _____________________
   [ ] Estimate tokens for one question: _____________________
   [ ] Estimate cost for 100 interactions: _____________________

2. [ ] Analyze token usage:
   [ ] Which operations use most tokens? _____________________
   [ ] How can you reduce token usage? _____________________
   [ ] What's the trade-off? _____________________

3. [ ] Implement cost tracking:
   [ ] Add token counter
   [ ] Track cost per interaction
   [ ] Display total cost
   [ ] Create cost report

4. [ ] Optimize for cost:
   [ ] Use shorter prompts
   [ ] Implement response caching
   [ ] Batch requests
   [ ] Set token limits
   [ ] Measure improvement

5. [ ] Document findings:
   - Original cost: _____________________
   - Optimized cost: _____________________
   - Savings: _____________________


═══════════════════════════════════════════════════════════════════════

✅ LAB DELIVERABLES
====================

Submit the following by end of lab:

DELIVERABLE 1: Code Files
──────────────────────────
[ ] Modified qa_agent_demo_openai_FIXED.py
    - With custom tools
    - With additional prompts
    - With error handling
    - With improvements

[ ] Custom agent code (agent_yourname.py)
    - Your own domain
    - Your own tools
    - Your own questions
    - Fully functional

DELIVERABLE 2: Documentation
─────────────────────────────
[ ] Lab report (3-5 pages)
    - Summary of learnings
    - Architecture explanation
    - Challenges faced
    - Solutions implemented
    - Code modifications

[ ] Architecture diagram
    - Draw the 5-layer architecture
    - Show data flow
    - Include components

[ ] Prompt engineering analysis
    - Your custom prompts
    - Effectiveness comparison
    - Best practices learned

DELIVERABLE 3: Demonstrations
──────────────────────────────
[ ] Working agent demo
    - Run with 5+ questions
    - Show memory working
    - Show tools being used
    - Capture output

[ ] Error handling demo
    - Show what happens with bad input
    - Show error messages
    - Show recovery

DELIVERABLE 4: Reflection
─────────────────────────
[ ] What you learned
   - Top 3 insights: _____________________
   - Challenges overcome: _____________________
   - Skills gained: _____________________

[ ] What you would improve
   - Architecture: _____________________
   - Tools: _____________________
   - Agent logic: _____________________

[ ] Future work
   - What's next? _____________________
   - How would you extend? _____________________
   - Real-world applications? _____________________


═══════════════════════════════════════════════════════════════════════

⏱️ LAB TIMELINE
===============

Recommended pacing:

Session 1 (45 min): Setup + Exercise 1
  - Pre-lab setup (30 min)
  - Architecture exercise (15 min)

Session 2 (60 min): Exercises 2-3
  - Prompt engineering (30 min)
  - Memory types (30 min)

Session 3 (60 min): Exercises 4-5
  - Custom tools (30 min)
  - Q&A agent (30 min)

Session 4 (30 min): Exercises 6-7
  - Error handling (15 min)
  - Cost tracking (15 min)

Session 5 (30 min): Finalization
  - Complete deliverables
  - Prepare presentation


═══════════════════════════════════════════════════════════════════════

❓ FREQUENTLY ASKED QUESTIONS
=============================

Q1: What if I get import errors?
A: Check IMPORT_ERROR_FIX.md for detailed solutions

Q2: What if my API key is invalid?
A: Generate a new key from https://platform.openai.com/api-keys

Q3: Can I modify the prompts?
A: Yes! That's part of the learning. Experiment with different prompts

Q4: How do I add my own tools?
A: Follow the pattern in Exercise 4. Define function → Add to tools list

Q5: What if the demo is slow?
A: API calls take time. Be patient. Check your internet connection

Q6: Can I use different domains?
A: Absolutely! Change the domain for all exercises

Q7: How do I know if my solution is correct?
A: Your agent should answer questions, store memory, and use tools

Q8: What's the cost of running this?
A: Usually less than $0.01 per complete run with gpt-3.5-turbo

Q9: Can I work in groups?
A: Yes, but each person should build their own agent

Q10: What happens after this lab?
A: You can deploy agents, add more tools, integrate with applications


═══════════════════════════════════════════════════════════════════════

📚 RESOURCES
============

Documentation:
  - LangChain: https://python.langchain.com/docs/
  - OpenAI: https://platform.openai.com/docs
  - GitHub: https://github.com/langchain-ai/langchain

Included Files:
  - qa_agent_demo_openai_FIXED.py - Reference implementation
  - IMPORT_ERROR_FIX.md - Troubleshooting
  - QUICK_REFERENCE.md - Code snippets
  - requirements_openai_FIXED.txt - Dependencies


═══════════════════════════════════════════════════════════════════════

📝 GRADING RUBRIC
=================

Code Implementation (40%)
  [ ] All exercises completed - 10%
  [ ] Custom tools working - 10%
  [ ] Agent functioning properly - 10%
  [ ] Error handling present - 10%

Documentation (30%)
  [ ] Architecture explanation - 10%
  [ ] Code comments and clarity - 10%
  [ ] Lab report quality - 10%

Creativity & Exploration (20%)
  [ ] Custom domain choice - 5%
  [ ] Additional features - 5%
  [ ] Improvements beyond requirements - 10%

Demonstration (10%)
  [ ] Working demo shown - 5%
  [ ] Ability to explain code - 5%


═══════════════════════════════════════════════════════════════════════

🎓 SUCCESS CRITERIA
===================

You've successfully completed this lab when you can:

✓ Explain the 5-layer LangChain architecture
✓ Create custom prompt templates
✓ Implement conversation memory
✓ Define and integrate custom tools
✓ Build a working Q&A agent
✓ Handle errors gracefully
✓ Track and optimize costs
✓ Modify and extend the system
✓ Demonstrate your agent
✓ Explain all your code


═══════════════════════════════════════════════════════════════════════

Good luck! This is a comprehensive lab that will teach you everything about
building AI agents. Take your time, experiment, and have fun!

Questions? Check the documentation or reach out to your instructor.

Happy coding! 🚀

═══════════════════════════════════════════════════════════════════════
