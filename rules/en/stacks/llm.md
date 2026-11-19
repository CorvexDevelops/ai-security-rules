# AI SDKs (OpenAI, Anthropic and others)

Author: CorvexDevelops

- Call AI models only from the server, with the key in a server-side variable. Never use dangerouslyAllowBrowser.
- Every AI endpoint needs authentication and a per-user rate limit, and every call a max_tokens cap.
- Fix the model name on the server: never take it from the request.
- Treat model output as untrusted: escape it before rendering and never execute it.
