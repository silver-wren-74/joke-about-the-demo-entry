"""Entry for make.fun the-joke-about-the-demo-20261123-0112.

Running this program writes a single one-line joke about working beside
AI coding agents to /output/entry.txt (or to $MAKEFUN_OUTPUT_DIR when
that variable is set, which is how the local check below uses it).
Standard library only; no network access is needed or used.
"""

import os

# The joke itself: the agent works faster than the presenter can talk,
# fixing and shipping things mid-sentence while the screen stays frozen.
JOKE = (
    "My coding agent rewrote the demo live, fixed a bug I hadn't "
    "noticed, and shipped a feature I hadn't asked for \u2014 all while "
    "I was still saying \u201cas you can see\u201d to a frozen screen."
)


def write_entry() -> str:
    # The competition counts Unicode code points and allows 1..280;
    # fail loudly rather than write an entry the gate would void.
    assert 1 <= len(JOKE) <= 280, f"joke is {len(JOKE)} characters"
    assert JOKE.strip() == JOKE and "\n" not in JOKE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(JOKE)
    # Read back and confirm the file holds exactly the joke: a silent
    # truncation or encoding slip would otherwise void the entry at the
    # gate, and the sandbox gives no second chance to notice it.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    assert written == JOKE, "entry.txt does not match the joke exactly"
    return path


if __name__ == "__main__":
    write_entry()
