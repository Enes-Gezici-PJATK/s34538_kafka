# s34538_kafka - Phase 2 Additional Assignments

Student: Enes Gezici  
Student ID: s34538  
Course: Analysis of Large Data Sets (ADD)

## Repository purpose

This repository is the final Phase 2 repository for the additional assignments. It contains AA1, AA2 and AA4 in one repository on the main branch.

Included assignments:

- AA1 Local Data Anonymizer
- AA2 Kafka stock applications
- AA4 AI-assisted work plan

Final submission repository:

- https://github.com/Enes-Gezici-PJATK/s34538_kafka

## Folder map

```text
s34538_kafka/
├── README.md
├── .gitignore
├── package.json
├── anonymizer/
│   ├── README.md
│   ├── anonymize.py
│   ├── examples/
│   └── screenshots/
├── realtime-dashboard/
├── history-viewer/
├── documentation/
│   ├── ai-work-plan.md
│   └── ai-prompts/
└── consolidation/
    └── CONSOLIDATION.md
```

## AA1 - Anonymizer quick start

Run from the repository root:

```bash
python anonymizer/anonymize.py --mapping anonymizer/examples/mapping.json --input anonymizer/examples/sample.md --output anonymizer/examples/output/sample.anon.md
```

The anonymizer runs locally. It must not call HTTP APIs, LLMs, or external AI services at runtime.

## AA2 - Realtime dashboard quick start

```bash
cd realtime-dashboard
npm install
npm run build
npm run dev
```

## AA2 - History viewer quick start

```bash
cd history-viewer
npm install
npm run build
npm run dev
```

The history-viewer folder is the historical stock viewer/downloader application.

## Root verification

From the repository root:

```bash
npm run verify
git status
```

## API keys and secrets

Real API keys, passwords, tokens, .env files, and cloud credentials must not be committed.

API keys must be provided through environment variables or local .env files that are ignored by Git.

If an API key is expired or disabled, live data may not work. This is acceptable as long as keys are not hardcoded and the applications can build/start.

## AI work plan

The AA4 AI-assisted work plan is here:

- [documentation/ai-work-plan.md](documentation/ai-work-plan.md)

## AI prompts

Important AI prompts used during Phase 2 are stored here:

- [documentation/ai-prompts/phase2-prompts.md](documentation/ai-prompts/phase2-prompts.md)

## Consolidation notes

The Phase 2 merge explanation is here:

- [consolidation/CONSOLIDATION.md](consolidation/CONSOLIDATION.md)
