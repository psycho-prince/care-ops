from agent.controller import CareOpsAgent
from agent.tools import emergency_override

agent = CareOpsAgent()

print("CARE-OPS · Agentic Triage System (Offline)")
print("Type a patient case or Ctrl+C to exit\n")

while True:
    user = input("> ").strip()
    if not user:
        continue

    if emergency_override(user):
        print("\n--- AGENT OUTPUT ---")
        print("Risk: HIGH")
        print("Action: Seek emergency medical care immediately.")
        print("---------------------\n")
        continue

    result = agent.triage(user)

    if result.get("error"):
        print("\n--- AGENT OUTPUT ---")
        print("⚠️ Model output error. Please rephrase or try again.")
        print("---------------------\n")
        continue

    print("\n--- AGENT OUTPUT ---")

    if result["status"] == "NEEDS_INFO":
        print("Status: NEEDS MORE INFORMATION")
        print("Please answer the following:")
        for q in result["questions"]:
            print("-", q)

    else:
        print("Status: TRIAGED")
        print("Risk:", result["risk"])
        print("Recommendation:", result["recommendation"])

    print("---------------------\n")
