# agent/rules.py

TRIAGE_RULES = [
    # ---------------- CRITICAL ----------------
    {
        "keywords": [
            "heart attack", "cardiac arrest", "not breathing",
            "unconscious", "chest pain", "chest tightness"
        ],
        "risk": "CRITICAL",
        "confidence": 95,
        "recommendation": "This is a medical emergency. Call emergency services immediately."
    },
    {
        "keywords": ["snake bite", "rat poison", "poisoning", "overdose"],
        "risk": "CRITICAL",
        "confidence": 95,
        "recommendation": "This is a medical emergency. Go to the nearest emergency department immediately."
    },
    {
        "keywords": ["heavy bleeding", "bleeding from head", "severe bleeding"],
        "risk": "CRITICAL",
        "confidence": 90,
        "recommendation": "Apply pressure if possible and seek emergency medical care immediately."
    },

    # ---------------- HIGH ----------------
    {
        "keywords": ["high fever", "persistent vomiting", "severe headache"],
        "risk": "HIGH",
        "confidence": 75,
        "recommendation": "Seek urgent medical evaluation as soon as possible."
    },
    {
        "keywords": ["baby", "newborn", "infant"],
        "risk": "HIGH",
        "confidence": 80,
        "recommendation": "Infants with symptoms should be evaluated urgently by a healthcare professional."
    },

    # ---------------- MODERATE ----------------
    {
        "keywords": ["vomiting", "dizziness", "back pain", "fever"],
        "risk": "MODERATE",
        "confidence": 45,
        "recommendation": "Consult a healthcare provider within 24–48 hours and monitor symptoms."
    },

    # ---------------- LOW ----------------
    {
        "keywords": ["mild pain", "ant bite", "small cut", "cough"],
        "risk": "LOW",
        "confidence": 30,
        "recommendation": "Home care and monitoring are appropriate unless symptoms worsen."
    },
]
