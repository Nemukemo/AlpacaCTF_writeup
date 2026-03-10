import os
import subprocess

assert os.getenv("FLAG").startswith("Alpaca{")

subprocess.run(["bash", "-i"], env={"FLAG": "🦙"})
