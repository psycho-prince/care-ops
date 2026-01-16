import time
from pathlib import Path

PROMPT_FILE = Path("/data/data/com.termux/files/home/care-ops/tmp_prompt.txt")
OUTPUT_FILE = Path("/data/data/com.termux/files/home/care-ops/tmp_output.txt")

class MedGemma:
    def generate(self, prompt: str) -> str:
        PROMPT_FILE.write_text(prompt)

        # wait for llama-cli to write output
        for _ in range(60):
            if OUTPUT_FILE.exists() and OUTPUT_FILE.stat().st_size > 0:
                text = OUTPUT_FILE.read_text()
                OUTPUT_FILE.unlink()
                return text.strip()
            time.sleep(0.5)

        return ""
