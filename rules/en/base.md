# Always

Author: CorvexDevelops

- Never put secrets, API keys or passwords in code or in public env variables (NEXT_PUBLIC_, VITE_, EXPO_PUBLIC_, REACT_APP_). Read them from server-side environment variables.
- Build every database query with parameters or the ORM, never by concatenating or interpolating user input.
- Check authentication and ownership on every server route that reads or changes data: never trust a user id sent by the client.
- Validate and limit every input (type, length, allowed values) on the server, even if the client validates too.
- Escape output by default: no innerHTML, dangerouslySetInnerHTML, v-html or |safe with user data.
- Never run shell commands, eval or templates built from user input.
- Keep debug mode, verbose errors and source maps off in production.
- Pin dependencies and do not add a package you have not verified exists and is maintained.
