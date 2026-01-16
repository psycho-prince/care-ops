# agent/controller.py

from agent.rules import TRIAGE_RULES
import re


class CareOpsAgent:
    def __init__(self):
        self.reset()

    def reset(self):
        self.history = []

    def _normalize(self, text: str) -> str:
        return re.sub(r"[^a-z0-9 ]+", " ", text.lower())

    def triage(self, text: str) -> dict:
        text_norm = self._normalize(text)

        is_baby = any(k in text_norm for k in ["baby", "newborn", "infant"])
        is_elderly = any(k in text_norm for k in ["elderly", "75 year", "80 year", "senior", "68 year"])

        for rule in TRIAGE_RULES:
            if any(keyword in text_norm for keyword in rule["keywords"]):
                risk = rule["risk"]
                confidence = rule["confidence"]
                recommendation = rule["recommendation"]

                # AGE-BASED ESCALATION
                if (is_baby or is_elderly):
                    if risk == "MODERATE":
                        risk = "CRITICAL"
                        confidence = max(confidence, 85)
                        recommendation = "High-risk patient. Seek emergency medical care immediately."
                    elif risk == "HIGH":
                        risk = "CRITICAL"
                        confidence = max(confidence, 90)
                        recommendation = "This is a medical emergency. Call emergency services immediately."

                return {
                    "status": "TRIAGED",
                    "risk": risk,
                    "confidence": min(confidence, 100),
                    "recommendation": recommendation
                }

        # Default fallback
        return {
            "status": "TRIAGED",
            "risk": "LOW",
            "confidence": 25,
            "recommendation": "Symptoms appear non-urgent. Monitor and seek care if they worsen."
        }
