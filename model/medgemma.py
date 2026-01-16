# model/medgemma.py
import time
from pathlib import Path

IN_PIPE = Path("/data/data/com.termux/files/home/care-ops/in.pipe")
OUT_PIPE = Path("/data/data/com.termux/files/home/care-ops/out.pipe")

class MedGemmaModel:
    def generate(self, prompt: str) -> str:
        # send prompt
        IN_PIPE.write_text(prompt + "\n")

        # read response
        start = time.time()
        output = []

        while time.time() - start < 30:
            try:
                chunk = OUT_PIPE.read_text()
                if chunk.strip():
                    output.append(chunk)
                    break
            except:
                pass
            time.sleep(0.2)

        return "".join(output).strip()
