# Next.js

Author: CorvexDevelops

- Route handler e server action girano sul server: controlla la sessione in cima a ognuno.
- Solo le variabili NEXT_PUBLIC_ arrivano al browser: mai quel prefisso per un segreto.
- Aggiungi le intestazioni di sicurezza (CSP, frame-ancestors, HSTS) in next.config o nel middleware.
