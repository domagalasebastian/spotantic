Authorization Guide
===================

Spotantic supports the Spotify authorization flows. This page summarizes
the high-level steps — consult the :doc:`auth_reference` page for implementation
details and the specific classes/functions provided by the library.

Also, make sure to check the official Spotify documentation to better understand
the authorization concept - `Authorization
<https://developer.spotify.com/documentation/web-api/concepts/authorization>`_.

For step by step instructions, see the :doc:`quickstart` and the
:doc:`examples` pages.

1. Register your application at the Spotify Developer Dashboard and note
   the `Client ID` and `Client Secret`.

2. Choose an authorization flow:

   - **Client Credentials**: server-to-server requests that do not require
     user authorization (no access to user private data).
   - **Authorization Code**: full user authorization flow for server-side
     apps. Returns refresh tokens.
   - **Authorization Code (PKCE)**: browser/native app flow without a
     client secret.

3. Configure Redirect URIs and scopes required by your application.

4. Use the library's auth helpers (see :doc:`auth_reference`) to obtain
   access tokens and attach them to the client.

Localhost redirect URIs
-----------------------

Currently Spotantic only supports redirect URIs that point to localhost.
During the authorization flow Spotantic temporarily hosts a local redirect
endpoint on `localhost` to complete the exchange. Register your app's
redirect URI with the Spotify Developer Dashboard using a localhost URI
(for example `http://localhost:8080/callback`) and ensure the port used
matches the port the library opens during the flow. This restriction means
remote or third-party redirect endpoints are not handled by the library's built-in flow.

Security notes
--------------

- Keep `Client Secret` values private and do not embed them in public
  repositories or frontend bundles.
- Use refresh tokens where available to avoid repeated user prompts.
