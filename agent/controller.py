import json
import re
from model.medgemma import MedGemma

SYSTEM_PROMPT = """
You are a clinical triage assistant.

Rules:
- Output ONLY valid JSON
- No markdown
- No explanations
- No thoughts

If info is insufficient:
{
  "status": "NEEDS_INFO",
  "questions": [string],
  "risk": "UNKNOWN"
}

If info is sufficient:
{
  "status": "TRIAGED",
  "symptoms": [string],
  "risk": "LOW | MODERATE | HIGH",
  "recommendation": string
}
"""

def extract_json(text: str):
    if not text:
        return None
    m = re.search(r"\{[\s\S]*\}", text)
    if not m:
        return None
    try:
        return json.loads(m.group())
    except json.JSONDecodeError:
        return None

class CareOpsAgent:
    def __init__(self):
        self.llm = MedGemma()
        self.context = None

    def triage(self, user_input: str):
        if self.context:
            full_case = f"""
Original case:
{self.context}

Additional answers:
{user_input}
"""
        else:
            full_case = user_input

        prompt = f"""{SYSTEM_PROMPT}

Patient case:
{full_case}
"""

        raw = self.llm.generate(prompt)
        data = extract_json(raw)

        # retry once with stricter instruction
        if not data:
            retry = self.llm.generate(prompt + "\nREMEMBER: OUTPUT JSON ONLY.")
            data = extract_json(retry)
            raw = retry

        if not data:
            return {
                "error": True,
                "raw": raw
            }

        if data["status"] == "NEEDS_INFO":
            self.context = full_case
        else:
            self.context = None

        data["raw"] = raw
        return data
