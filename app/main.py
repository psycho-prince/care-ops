from agent.controller import CareOpsAgent

agent = CareOpsAgent()

print("CARE-OPS · Agentic Triage System (Offline)")
print("Type a patient case or Ctrl+C to exit\n")

while True:
    try:
        user_input = input("> ").strip()
        if not user_input:
            continue

        result = agent.triage(user_input)

        print("\n--- AGENT OUTPUT ---")

        if result.get("error"):
            print("⚠️ Model output error. Please rephrase or try again.")
            print("---------------------\n")
            continue

        data = result["data"]

        if data["status"] == "NEEDS_INFO":
            print("Status: NEEDS MORE INFORMATION")
            print("Please answer the following:")
            for q in data.get("questions", []):
                print(f"- {q}")

        else:
            print(f"Status: TRIAGED")
            print(f"Risk Level: {data.get('risk', 'UNKNOWN')}")
            print(f"Symptoms: {', '.join(data.get('symptoms', []))}")
            print(f"Recommended Action: {data.get('recommendation')}")

        print("---------------------\n")

    except KeyboardInterrupt:
        print("\nExiting CARE-OPS.")
        break
