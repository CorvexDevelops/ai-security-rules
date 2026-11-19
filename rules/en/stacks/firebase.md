# Firebase

Author: CorvexDevelops

- Firestore, Storage and Realtime Database rules must require request.auth and check the document owner. Never allow read, write: if true.
- The web apiKey is public: security comes only from the rules.
