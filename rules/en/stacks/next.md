# Next.js

Author: CorvexDevelops

- Route handlers and server actions run on the server: check the session at the top of each one.
- Only NEXT_PUBLIC_ variables reach the browser: never give that prefix to a secret.
- Add security headers (CSP, frame-ancestors, HSTS) in next.config or middleware.
