s34538_kafka - Phase 2 Additional Assignments

Student: Enes Gezici
Student ID: s34538
Course: Analysis of Large Data Sets (ADD)

📌 Overview

This repository contains the final Phase 2 submission for the Additional Assignments (AA1, AA2, and AA4).

It demonstrates:

Local data anonymization (AA1)
Real-time and historical stock applications (AA2)
AI-assisted planning and development workflow documentation (AA4)

The project is structured as a modular monorepo with separate components for each assignment.

📁 Repository Structure
s34538_kafka/
├── README.md
├── .gitignore
├── package.json
│
├── anonymizer/                 # AA1 - Local Data Anonymizer
│   ├── anonymize.py
│   ├── README.md
│   ├── examples/
│   │   ├── mapping.json
│   │   ├── sample.md
│   │   └── output/
│   └── screenshots/
│
├── realtime-dashboard/        # AA2 - Real-time stock dashboard
│
├── history-viewer/            # AA2 - Historical stock viewer
│
├── documentation/             # AA4 - AI-assisted workflow docs
│   ├── ai-work-plan.md
│   └── ai-prompts/
│       └── phase2-prompts.md
│
└── consolidation/
    └── CONSOLIDATION.md
🔐 Security & Data Policy
No API keys, secrets, or credentials are stored in the repository
Environment variables (.env) are used locally and ignored by Git
The anonymizer runs fully locally (no external APIs or AI services)
All data used in examples is synthetic or anonymized
🧹 AA1 - Local Data Anonymizer

A Python-based tool that replaces sensitive information in text files using a mapping configuration.

▶️ Run
python anonymizer/anonymize.py \
  --mapping anonymizer/examples/mapping.json \
  --input anonymizer/examples/sample.md \
  --output anonymizer/examples/output/sample.anon.md
Features
JSON-based replacement rules
Case-sensitive / insensitive support
UTF-8 safe processing
Dry-run mode
Fully offline execution
📊 AA2 - Real-Time Dashboard

A frontend application for displaying live stock data.

▶️ Run
cd realtime-dashboard
npm install
npm run build
npm run dev
📈 AA2 - History Viewer

A frontend application for viewing historical stock data.

▶️ Run
cd history-viewer
npm install
npm run build
npm run dev
🧠 AA4 - AI-Assisted Development

This project includes AI-assisted planning, debugging, and workflow documentation.

📄 See: documentation/ai-work-plan.md

Includes:
Project planning strategy
Debugging workflow
AI-assisted development decisions
Error handling and iteration notes
💬 AI Prompts

All AI prompts used during development are stored in:

📄 documentation/ai-prompts/phase2-prompts.md

🧩 Consolidation

Final integration notes:

📄 consolidation/CONSOLIDATION.md

Explains how AA1, AA2, and AA4 were merged into a single repository.

🚀 Quick Start
Install dependencies
npm install
Run anonymizer
python anonymizer/anonymize.py --help
Run applications
cd realtime-dashboard && npm run dev
cd history-viewer && npm run dev
📌 Notes
Project built for academic purposes
Fully modular architecture
AI used for planning and documentation support (AA4)
All components are independently runnable
✅ Status

✔ AA1 Completed
✔ AA2 Completed
✔ AA4 Completed
✔ Documentation included
✔ Ready for submission
