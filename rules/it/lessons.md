# Errori comuni e la regola che li evita

Author: CorvexDevelops

- Qui c'erano segreti scritti nel codice: leggi ogni chiave da variabili d'ambiente e ruota quelle già pubblicate.
- Un segreto è ancora nella cronologia git: ruotalo, toglierlo dall'ultimo commit non basta.
- Tieni i file .env fuori da git (.gitignore) e pubblica solo .env.example.
- Qui l'SQL veniva costruito con l'input: usa sempre query parametrizzate.
- Qui i comandi di shell usavano l'input: usa liste di argomenti e valori ammessi.
- Qui c'era eval su dati: mai valutare stringhe come codice.
- Qui i template venivano costruiti con l'input: passa i dati solo come variabili.
- Qui dati dell'utente arrivavano nella pagina senza codifica: usa textContent o la codifica del framework.
- Qui si deserializzavano dati non fidati: usa caricatori sicuri (yaml.safe_load, JSON).
- Qui c'era crittografia debole: bcrypt o argon2 per le password e un generatore crittografico per i token.
- Qui la verifica TLS era spenta: non spegnerla mai.
- Qui i JWT venivano letti senza verifica: verifica sempre firma e algoritmo.
- Qui il debug era acceso: comandalo da una variabile d'ambiente spenta per default.
- Qui il CORS accettava ogni origine: ammetti solo le tue.
- Qui un container girava come root: aggiungi un USER senza privilegi.
- Qui c'erano dipendenze con falle note: aggiorna alla prima versione sicura e tieni il lockfile.
- Qui l'infrastruttura aveva impostazioni insicure: azioni fissate, privilegi minimi, porte dei database non pubbliche.
- Qui le regole Firebase erano aperte: ogni regola controlla request.auth e il proprietario.
- Qui le tabelle Supabase erano senza RLS o con policy aperte: attiva la RLS e scrivi policy sul proprietario.
- Qui la chiave service_role arrivava al browser: tienila solo sul server.
- Qui un segreto aveva un prefisso pubblico: togli il prefisso e leggilo sul server.
- Qui una chiave AI arrivava al browser: chiama i modelli solo dal server.
- Qui gli endpoint AI erano senza accesso o senza limiti: aggiungi entrambi prima di ogni chiamata.
- Qui il client sceglieva il modello AI: fissalo sul server.
- Qui le chiamate AI non avevano tetto di token: imposta sempre max_tokens.
- Qui mancavano intestazioni di sicurezza: imposta CSP, HSTS, frame-ancestors e nosniff.
- Qui i cookie di sessione erano senza protezioni: httpOnly, secure e sameSite su ognuno.
- Qui file privati erano raggiungibili dal sito (.env, .git, backup, source map): non pubblicarli mai.
- Qui alcune API rispondevano senza accesso: proteggi ogni endpoint per default.
- Qui l'accesso non aveva limite ai tentativi: aggiungi limiti e blocco.
- L'audit AI ha trovato falle di logica o di accesso: ricontrolla il proprietario a ogni accesso ai dati.
