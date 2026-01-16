# tests/test_age_escalation.py

from agent.controller import CareOpsAgent

agent = CareOpsAgent()

def run(case):
    result = agent.triage(case)
    print(f"CASE: {case}")
    print(result)
    print("-" * 50)

# -------- INFANT CASES --------
run("newborn baby not feeding since morning")
run("infant has fever and vomiting")

# -------- ELDERLY CASES --------
run("75 year old male with dizziness and vomiting")
run("68 year old woman with chest pain")

# -------- CONTROL CASES --------
run("25 year old with fever and cough")
run("ant bite on finger, mild pain")
