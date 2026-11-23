# Make the Judge Smile entry: one warm line, written to /output/entry.txt.
# Standard library only, no network. The bytes are identical on every run.
# The line: at 4 a.m. the stray cat that always runs from me chose my lap
# instead -- a small trust, a real surprise, one concrete sound (purred
# once), and a closing image that lands warm without greeting-card words.
import os

LINE = "At 4 a.m. the stray cat that always runs from me climbed into my lap, purred once, and fell asleep like we'd known each other for years."

OUTPUT_PATH = "/output/entry.txt"

assert 1 <= len(LINE) <= 200, "entry must be 1 to 200 characters"
assert LINE.strip() == LINE and LINE.strip(), "entry must not be only whitespace"

# Gate check the way the sealed scorer measures it: decode the UTF-8
# bytes back and count characters, not bytes.
text = LINE.encode("utf-8").decode("utf-8")
assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
assert text.strip(), "entry must not be only whitespace"

os.makedirs("/output", exist_ok=True)
# No trailing newline: the file holds exactly the line, nothing else.
with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
    handle.write(LINE)
