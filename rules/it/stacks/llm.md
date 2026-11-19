# SDK AI (OpenAI, Anthropic e altri)

Author: CorvexDevelops

- Chiama i modelli AI solo dal server, con la chiave in una variabile del server. Mai dangerouslyAllowBrowser.
- Ogni endpoint AI vuole accesso e un limite di richieste per utente, e ogni chiamata un tetto max_tokens.
- Fissa il nome del modello sul server: mai prenderlo dalla richiesta.
- Tratta la risposta del modello come non fidata: codificala prima di mostrarla e non eseguirla mai.
