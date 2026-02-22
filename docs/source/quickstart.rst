Quickstart
==========

Prerequisites
-------------

1. Spotantic is installed. Refer to the :doc:`installation` page.

2. The user is familiar with the Authorization concept. See the :doc:`authorization` page.

Authorization step-by-step
--------------------------

1. Configure environment variables with your user credentials and other
   configuration options. The most convenient way to do this is by creating a `.env`
   file in your project root directory. Alternatively, you can set
   them manually using the `export` command (for Linux). Below is
   a template for the `.env` file with a short description of each field.

   .. code-block:: bash

      # Your application Client ID from the Spotify Developer Dashboard
      SPOTANTIC_AUTH_CLIENT_ID=...
      # Your application Client Secret from the Spotify Developer Dashboard
      SPOTANTIC_AUTH_CLIENT_SECRET=...
      # Remote or third-party redirect endpoints are not supported
      SPOTANTIC_AUTH_REDIRECT_URI=http://127.0.0.1:8000/callback
      # Space-separated list of scopes to be granted
      SPOTANTIC_AUTH_SCOPE=user-library-read user-library-modify
      # File path where the access token information should be stored
      SPOTANTIC_AUTH_ACCESS_TOKEN_FILE_PATH=.token_info_cache
      # If `true`, Spotantic will save access token information every time the token is obtained.
      # The token is stored in the filepath indicated by SPOTANTIC_AUTH_ACCESS_TOKEN_FILE_PATH
      SPOTANTIC_AUTH_STORE_ACCESS_TOKEN=true

      # Controls package-level logging; if `false`, logging is completely disabled
      SPOTANTIC_LOGGING_ENABLE=false
      # Controls logging level; if `true`, logging includes debug messages
      SPOTANTIC_LOGGING_DEBUG=true
      # Directory to store session logs; if not provided, logs are only written to STDOUT
      SPOTANTIC_LOGGING_LOGS_DIR=logs/

2. Activate your virtual environment, if applicable.

   .. code-block:: bash

    source .venv/bin/activate

3. Now we can go straight to the code. Below is an example step-by-step instruction
   from an IPython session, but you can run it in the default Python REPL or directly in your
   script. IPython is highly recommended since it automatically sets up the
   asyncio event loop.

   .. code-block:: python

      In [1]: from spotantic.models.auth import AuthSettings
      # If you set up all of the environment variables in step 1, then no additional parameters are needed
      In [2]: auth_settings = AuthSettings()
      # Optional: If your .env file is located somewhere other than the project root directory, you can define
      # the path with the _env_file parameter
      In [3]: auth_settings = AuthSettings(_env_file=".env")
      # Optional: If you want to override any setting at runtime, you are allowed to do so
      In [4]: auth_settings = AuthSettings(scope="user-library-read")

      # Import the Auth Manager of your choice; in this example we will use the PKCE option
      In [5]: from spotantic.auth import AuthCodePKCEFlowManager
      # With allow_lazy_refresh set, the access token will be automatically refreshed upon expiration
      In [6]: auth_manager = AuthCodePKCEFlowManager(auth_settings=auth_settings, allow_lazy_refresh=True)
      # If possible, the browser will open automatically. Otherwise, the user will be prompted with
      # a link to the Spotify authorization webpage. During this step Spotantic temporarily hosts a local redirect
      # endpoint on `localhost` to complete the exchange.
      In [7]: await auth_manager.authorize()

      In [8]: from spotantic.client import SpotanticClient
      In [9]: client = SpotanticClient(auth_manager=auth_manager, max_attempts=3, check_insufficient_scope=True)
      # Congrats! At this point your client is fully operational!

4. Issue a request to check that everything is working correctly:

   .. code-block:: python

      In [10]: from spotantic.endpoints import albums
      In [11]: data = await albums.get_user_saved_albums(client, limit=1)

      In [12]: type(data.data)
      Out[12]: spotantic.models.spotify._paged_result_model.PagedResultModel[SavedAlbumModel]

      In [13]: type(data.request)
      Out[13]: spotantic.models.albums.requests._get_user_saved_albums.GetUserSavedAlbumsRequest

      In [14]: type(data.response)
      Out[14]: dict

5. For refreshable access tokens, you can reuse them in subsequent app sessions
   (only if you store them somewhere):

   .. code-block:: python

      In [1]: from spotantic.models.auth import AuthSettings, AccessTokenInfo

      In [2]: from spotantic.auth import AuthCodePKCEFlowManager

      In [3]: auth_settings = AuthSettings()

      In [4]: token_info = AccessTokenInfo.load_token(".token_info_cache")

      In [5]: auth_manager = AuthCodePKCEFlowManager(auth_settings=auth_settings, allow_lazy_refresh=True, access_token_info=token_info)

      In [6]: from spotantic.client import SpotanticClient

      In [7]: client = SpotanticClient(auth_manager=auth_manager, max_attempts=3, check_insufficient_scope=True)

      In [8]: from spotantic.endpoints import albums
      # The token is automatically refreshed if allow_lazy_refresh is set to True; otherwise you need to call auth_manager.refresh() manually
      In [9]: data = await albums.get_user_saved_albums(client, limit=1)

See the :doc:`client_reference` and :doc:`auth_reference` pages for integration details
and specific constructor examples.
