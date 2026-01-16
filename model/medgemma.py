# care-ops/model/medgemma.py

import subprocess
import tempfile
from pathlib import Path

LLAMA_BIN = Path.home() / "llama.cpp/build/bin/llama-cli"
MODEL_PATH = Path.home() / "care-ops/models/medgemma.Q4_K_M.gguf"


class MedGemma:
    def generate(self, prompt: str) -> str:
        """
        Runs llama-cli once per prompt and returns raw text output.
        This is intentionally stateless and safe.
        """

        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
            f.write(prompt)
            f.flush()
            prompt_file = f.name

        try:
            result = subprocess.run(
                [
                    str(LLAMA_BIN),
                    "-m", str(MODEL_PATH),
                    "--temp", "0.2",
                    "--top-p", "0.9",
                    "--n-predict", "512",
                    "--prompt-file", prompt_file,
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.DEVNULL,
                text=True,
                timeout=120,
            )
            return result.stdout.strip()
        except Exception:
            return ""
