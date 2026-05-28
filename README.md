Project Overview

This repository contains the final Phase 2 submission for the Additional Assignments (AA1, AA2, AA4).
It combines data anonymization, real-time stock applications, and AI-assisted development workflow documentation in a single structured repository.

The system demonstrates:

Local data anonymization (AA1)
Real-time dashboard and history viewer applications (AA2)
AI-assisted development workflow documentation (AA4)
Clean modular project structure with separation of concerns
s34538_kafka/
├── README.md
├── .gitignore
├── package.json
│
├── anonymizer/                 # AA1 - Local Data Anonymizer
│   ├── README.md
│   ├── anonymize.py
│   ├── examples/
│   │   ├── mapping.json
│   │   ├── sample.md
│   │   └── output/
│   └── screenshots/
│
├── realtime-dashboard/        # AA2 - Live stock dashboard (frontend)
│
├── history-viewer/            # AA2 - Historical stock viewer application
│
├── documentation/             # AA4 - AI-assisted workflow documentation
│   ├── ai-work-plan.md
│   └── ai-prompts/
│       └── phase2-prompts.md
│
└── consolidation/
    └── CONSOLIDATION.md
🔐 Important Rules (Security & Compliance)
❌ No API keys, tokens, or secrets are stored in the repository
✅ Environment variables or .env files are used locally (ignored by Git)
❌ No external AI/LLM calls are made inside AA1 anonymizer at runtime
✅ Applications must build and run without hardcoded credentials
🧹 AA1 - Local Data Anonymizer

The anonymizer processes local files and replaces sensitive information using a mapping file.

▶️ Run Anonymizer
python anonymizer/anonymize.py \
  --mapping anonymizer/examples/mapping.json \
  --input anonymizer/examples/sample.md \
  --output anonymizer/examples/output/sample.anon.md
Features
JSON-based replacement rules
Case-sensitive and case-insensitive support
UTF-8 safe file handling
Dry-run capability
Fully local execution (no external dependencies)
📊 AA2 - Realtime Dashboard

A frontend application for live stock visualization.

▶️ Run Dashboard
cd realtime-dashboard
npm install
npm run build
npm run dev
Features
Live stock data visualization
Real-time updates
Modular frontend architecture
📈 AA2 - History Viewer

Application for viewing and analyzing historical stock data.

▶️ Run History Viewer
cd history-viewer
npm install
npm run build
npm run dev
Features
Historical data exploration
Stock data filtering
Downloadable datasets
🧠 AA4 - AI-Assisted Work Plan

The AI-assisted development workflow, planning, and debugging strategy is documented here:

📄 documentation/ai-chat-history.md

Includes:
Project breakdown strategy
AI-assisted debugging workflow
Development planning approach
Error simulation and debugging steps
💬 AI Prompts Used (Phase 2)

All prompts used during development are documented in:

📄 documentation/ai-prompts/phase2-prompts.md

This includes:

Planning prompts
Debugging prompts
Implementation guidance
Refactoring instructions
🧩 Consolidation Notes

Final integration and merging notes are documented in:

📄 consolidation/CONSOLIDATION.md

This explains:

How AA1, AA2, and AA4 were merged
Structural decisions
Final repository architecture
🚀 How to Run Entire Project

From repository root:

Install dependencies
npm install
Run AA1
python anonymizer/anonymize.py --help
Run AA2 Dashboard
cd realtime-dashboard
npm run dev
Run AA2 History Viewer
cd history-viewer
npm run dev
📌 Notes
This project is designed for educational purposes
All components are modular and independently runnable
The anonymizer is fully local and does not use external APIs
AI was used for planning, debugging support, and documentation assistance (AA4)
