# ai-security-rules

Author: CorvexDevelops

Security rules for AI coding agents: Claude Code, Codex and every tool that reads `AGENTS.md`, Cursor, GitHub Copilot and Windsurf. Put them in your project and the agent that writes your code stops repeating the same flaws: secrets in public variables, databases open to everyone, AI endpoints with no limits, queries built from user input.

Made by [Corvex](https://corvex.dev), the team of security agents that tests your web platforms, code, network and computer. After every scan Corvex writes these rules into your project, plus the lessons from the flaws it found there. This repository is the general part, free to use.

## Use them in one minute

Copy the file for your tool from `ready/en/` (or `ready/it/` in Italian). It contains every stack:

| Tool | File |
|---|---|
| Claude Code | `ready/en/CLAUDE.md` |
| Codex, Jules and other agents | `ready/en/AGENTS.md` |
| Cursor | `ready/en/.cursor/rules/security.mdc` |
| GitHub Copilot | `ready/en/.github/copilot-instructions.md` |
| Windsurf | `ready/en/.windsurfrules` |

Or build a file with only the stacks you use (Python 3.9+, no dependencies):

```bash
python3 build.py --format claude --stack next,supabase,llm > CLAUDE.md
python3 build.py --format cursor --stack all --write path/to/project
```

The rules sit between two markers. Running the generator again, or a Corvex scan, replaces only that block: everything else you wrote in the file stays.

## What the rules cover

| Section | Rules |
|---|---|
| [Always](rules/en/base.md) | secrets, queries, ownership checks, input validation, output escaping, shell and eval, debug mode, dependencies |
| [Next.js](rules/en/stacks/next.md) | server actions, public variables, security headers |
| [Supabase](rules/en/stacks/supabase.md) | Row Level Security, open policies, the service_role key |
| [Firebase](rules/en/stacks/firebase.md) | Firestore, Storage and Realtime Database rules |
| [AI SDKs](rules/en/stacks/llm.md) | keys in the browser, rate limits, token caps, model chosen by the client |
| [Express](rules/en/stacks/express.md) | headers, CORS, rate limits, cookies |
| [Python](rules/en/stacks/python.md) | debug mode, unsafe loading, randomness |
| [Docker and GitHub Actions](rules/en/stacks/docker.md) | root containers, secrets in images, pinned actions |

[`rules/en/lessons.md`](rules/en/lessons.md) lists the most common mistakes found by Corvex scans and the rule that prevents each one.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Licence

Apache License 2.0, see `LICENSE` and `NOTICE`.
