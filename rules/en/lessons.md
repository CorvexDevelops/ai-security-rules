# Common mistakes and the rule that prevents them

Author: CorvexDevelops

- Secrets were hard-coded here: read every key from environment variables and rotate the ones already committed.
- A secret is still in git history: rotate it, removing it from the latest commit is not enough.
- Keep .env files out of git (.gitignore) and commit only .env.example.
- SQL was built from input: always use parameterized queries.
- Shell commands were built from input: use argument arrays and an allow-list.
- eval was used on data: never evaluate strings as code.
- Templates were built from input: pass data as template variables only.
- User data reached the page unescaped: use textContent or framework escaping.
- Untrusted data was deserialized: use safe loaders (yaml.safe_load, JSON).
- Weak crypto or randomness was used: use bcrypt or argon2 for passwords and a CSPRNG for tokens.
- TLS verification was disabled: never turn it off.
- JWTs were decoded without verification: always verify signature and algorithm.
- Debug mode was on: drive it from an environment variable that defaults to off.
- CORS was open to any origin: allow only your own origins.
- A container ran as root: add a non-root USER.
- Dependencies with known flaws were used: upgrade to the first safe version and keep the lockfile.
- Infrastructure files had insecure defaults: pin actions, drop privileges, no public database ports.
- Firebase rules were open: every rule must check request.auth and the owner.
- Supabase tables lacked RLS or had open policies: enable RLS and write owner-based policies.
- The service_role key reached the browser: keep it server-only.
- A secret had a public env prefix: drop the prefix and read it on the server.
- An AI key reached the browser: call models only from the server.
- AI endpoints lacked auth or rate limits: add both before any model call.
- The client chose the AI model: fix it on the server.
- AI calls had no token cap: always set max_tokens.
- Security headers were missing: set CSP, HSTS, frame-ancestors and nosniff.
- Session cookies lacked flags: httpOnly, secure and sameSite on every session cookie.
- Private files were reachable on the site (.env, .git, backups, source maps): never deploy them.
- API endpoints answered without authentication: protect every endpoint by default.
- Sign-in had no attempt limit: add rate limiting and lockout.
- The AI audit found logic or access-control flaws: re-check ownership on every data access.
