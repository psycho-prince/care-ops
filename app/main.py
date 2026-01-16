from agent.controller import CareOpsAgent

def main():
    agent = CareOpsAgent()

    print("CARE-OPS · Agentic Triage System (Offline)")
    print("Type a patient case.")
    print("Commands: /new  /exit\n")

    while True:
        try:
            user_input = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting CARE-OPS.")
            break

        if not user_input:
            continue

        if user_input.lower() in ["/exit", "exit", "quit"]:
            print("Goodbye.")
            break

        if user_input.lower() == "/new":
            agent.reset()
            print("🔄 New patient case started.\n")
            continue

        result = agent.triage(user_input)

        print("\n--- AGENT OUTPUT ---")

        if result["status"] == "NEEDS_INFO":
            print("Status: NEEDS MORE INFORMATION")
            for q in result.get("questions", []):
                print(f"- {q}")

        elif result["status"] == "TRIAGED":
            print("Status: TRIAGED")
            print(f"Risk Level: {result.get('risk')} (confidence {result.get('confidence')}%)")
            print(f"Recommendation: {result.get('recommendation')}")

        else:
            print("⚠️ Unexpected agent state.")

        print("---------------------\n")

if __name__ == "__main__":
    main()
