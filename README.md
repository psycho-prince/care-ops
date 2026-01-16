Copy code
Markdown
# CARE-OPS  
## Offline Agentic Medical Triage System (MedGemma)

CARE-OPS is an **offline, agentic clinical triage system** built on **MedGemma (HAI-DEF)** and designed for **edge and low-connectivity environments**.

It simulates a real clinical triage interaction:
- asks medically relevant follow-up questions
- escalates risk based on symptoms and age
- never performs diagnosis
- outputs safe, explainable triage recommendations

---

## Why CARE-OPS?

Many healthcare settings cannot rely on cloud-based LLMs.
CARE-OPS runs **fully offline**, enabling:
- rural clinics
- disaster response
- mobile health units
- privacy-sensitive environments

---

## Key Features

- ✅ **Offline inference** (llama.cpp + MedGemma)
- ✅ **Agentic workflow** (iterative questioning like a clinician)
- ✅ **WHO / NHS / CDC aligned triage logic**
- ✅ **Age-based auto escalation** (infants & elderly)
- ✅ **Explainable rules (no black box)**
- ✅ **Edge-ready** (tested on mobile / Termux)

---

## System Architecture
User Input ↓ CARE-OPS Agent ├── Symptom extraction ├── Follow-up questioning (if needed) ├── Rule-based triage engine ├── Age risk escalation ↓ Triage Output (LOW / MODERATE / HIGH / CRITICAL)
Copy code

---

## Risk Levels

| Level | Meaning |y

|-----|--------|
| LOW | Home care / monitoring |
| MODERATE | Medical review in 24–48h |
| HIGH | Urgent evaluation |
| CRITICAL | Emergency – call services |

---

## Running CARE-OPS

### 1. Setup
```bash
python -m venv venv
source venv/bin/activate
export PYTHONPATH=$PWD
2. Start the agent
Copy code
Bash
python app/main.py
Example Interaction
Copy code

> newborn baby not feeding since morning

Status: TRIAGED
Risk Level: CRITICAL
Recommendation:
Infants with symptoms should be evaluated urgently by a healthcare professional.
Safety & Ethics
CARE-OPS does NOT diagnose
Outputs triage guidance only
Always recommends professional care for emergencies
Designed to reduce delay, not replace clinicians
Competition Alignment (MedGemma Impact Challenge)
✅ Uses MedGemma (HAI-DEF) exclusively
✅ Agentic workflow (special award eligible)
✅ Edge AI (offline, mobile)
✅ Human-centered healthcare focus
✅ Open-source & reproducible
License
MIT License
Open for research and non-commercial healthcare innovation.
Disclaimer
CARE-OPS is a research prototype. It does not replace licensed medical professionals.
