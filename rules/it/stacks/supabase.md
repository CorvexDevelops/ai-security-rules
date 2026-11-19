# Supabase

Author: CorvexDevelops

- Attiva la Row Level Security su ogni tabella con una nuova migrazione e scrivi policy basate su auth.uid().
- Mai using (true) o with check (true) per insert, update o delete.
- La chiave service_role è solo per il server: mai nei componenti del browser né con un prefisso pubblico.
