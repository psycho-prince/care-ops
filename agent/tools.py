def emergency_override(text: str):
    red_flags = [
        "sudden severe headache",
        "loss of consciousness",
        "neck stiffness",
        "weakness on one side",
        "seizure"
    ]
    t = text.lower()
    return any(r in t for r in red_flags)
