# Supabase

Author: CorvexDevelops

- Enable Row Level Security on every table in a new migration and write policies based on auth.uid().
- Never use using (true) or with check (true) for insert, update or delete.
- The service_role key is server-only: never import it in client components or give it a public prefix.
