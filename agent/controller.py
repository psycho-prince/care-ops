import json
import re
from model.medgemma import MedGemmaModel


class CareOpsAgent:
    def __init__(self):
        self.model = MedGemmaModel()

    def _extract_json(self, text: str):
        """
        Extract first valid JSON object from model output.
        Returns dict or None.
        """
        if not text:
            return None

        # Try direct parse first
        try:
            return json.loads(text)
        except Exception:
            pass

        # Fallback: regex extract JSON block
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            return None

        try:
            return json.loads(match.group())
        except Exception:
            return None

    def triage(self, user_input: str):
        prompt = f"""
You are a clinical triage assistant.

IMPORTANT RULES:
- Output ONLY valid JSON
- No explanations
- No markdown
- No extra text

TASK:
If information is insufficient:
- Ask up to 5 medically relevant follow-up questions
- status = NEEDS_INFO
- risk = UNKNOWN

If information is sufficient:
- Extract symptoms
- Classify risk: LOW, MODERATE, HIGH
- Recommend next action
- status = TRIAGED

JSON SCHEMA (MANDATORY):

{{
  "status": "NEEDS_INFO | TRIAGED",
  "questions": [string],
  "symptoms": [string],
  "risk": "LOW | MODERATE | HIGH | UNKNOWN",
  "recommendation": string
}}

Patient case:
{user_input}
""".strip()

        raw = self.model.generate(prompt)
        data = self._extract_json(raw)

        if not data:
            return {
                "error": True,
                "message": "Model output could not be parsed",
                "raw_output": raw
            }

        return {
            "error": False,
            "data": data,
            "raw_output": raw
        }
