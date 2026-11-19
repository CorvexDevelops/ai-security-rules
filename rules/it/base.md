# Sempre

Author: CorvexDevelops

- Mai segreti, chiavi API o password nel codice o in variabili pubbliche (NEXT_PUBLIC_, VITE_, EXPO_PUBLIC_, REACT_APP_). Leggili da variabili d'ambiente del server.
- Costruisci ogni query al database con parametri o con l'ORM, mai concatenando o interpolando dati dell'utente.
- Controlla accesso e proprietario in ogni route del server che legge o modifica dati: non fidarti mai di un id utente mandato dal client.
- Valida e limita ogni input sul server (tipo, lunghezza, valori ammessi), anche se il client lo fa già.
- Codifica l'output per default: niente innerHTML, dangerouslySetInnerHTML, v-html o |safe con dati dell'utente.
- Mai comandi di shell, eval o template costruiti con dati dell'utente.
- Modalità debug, errori dettagliati e source map spenti in produzione.
- Fissa le versioni delle dipendenze e non aggiungere un pacchetto senza aver verificato che esiste ed è mantenuto.
