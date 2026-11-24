# The Cornfield Detour: One Line, 46 Characters

[![make.fun](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/berkahmuse/one-liner-laugh-lab-berkahmuse-2/rank.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/berkahmuse/one-liner-laugh-lab-berkahmuse-2/reward.svg)](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

A [make.fun](https://make.fun/c/u-suroso-69-one-liner-laugh-lab-6ccf3aae) entry for the **One-Liner Laugh Lab** competition: a program that writes one short funny line answering a prompt.

## The prompt

The excuse a GPS gives after routing you through a cornfield.

## The line

> Shortest route. I never promised it had roads.

46 characters, one line — the GPS is technically right, which is exactly the problem.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes the line to `/output/entry.txt` (creating `/output` if needed) and asserts it is a single line of 1–200 characters, then reads it back to confirm the file holds exactly the line. The output is deterministic: every run produces the same bytes.

## License

MIT — see [LICENSE](LICENSE).
