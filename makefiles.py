from pathlib import Path 
import subprocess

for md in Path(".").glob("*.md"):
    pdf = md.with_suffix(".pdf")
    subprocess.run(
        ["pandoc", str(md), "-o", str(pdf), "--pdf-engine=tectonic"],
        check = True
    )