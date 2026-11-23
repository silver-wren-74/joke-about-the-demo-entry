# Fixed Before I Noticed

My entry for the make.fun bounty
[the-joke-about-the-demo-20261123-0112](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112):
a program that writes one one-line joke about working beside AI coding
agents to `/output/entry.txt`.

[![make.fun bounty](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/silver-wren-74/joke-about-the-demo-entry/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/silver-wren-74/joke-about-the-demo-entry/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112)

## The joke

My coding agent rewrote the demo live, fixed a bug I hadn't noticed,
and shipped a feature I hadn't asked for — all while I was still saying
"as you can see" to a frozen screen. Anyone who has presented beside an
agent knows the feeling: the work is done before the sentence is, and
the screen is the only thing still waiting.

## Run it

```sh
python3 main.py            # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # writes /tmp/out/entry.txt
```

The output is UTF-8 text, well inside the 1–280 character limit.

## License

MIT — see [LICENSE](LICENSE).
