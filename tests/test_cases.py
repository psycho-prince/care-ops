import sys
import os

# add project root to PYTHONPATH
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

from agent.controller import CareOpsAgent

agent = CareOpsAgent()

cases = [
    "25 year old with severe headache and vomiting",
    "Sudden severe headache with neck stiffness",
    "Mild headache after long screen use"
]

for c in cases:
    print("\nCASE:", c)
    result = agent.triage(c)
    print(result)
    print("=" * 50)
