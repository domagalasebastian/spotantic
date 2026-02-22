.. Spotantic documentation master file, created by
   sphinx-quickstart on Sun Oct 12 19:37:58 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Spotantic
=========

Spotantic is an asynchronous Python client library for interacting with
the Spotify Web API. It provides typed models, modular endpoint helpers,
and multiple authorization flows to make building playback, search, and
library integrations easier in async applications.

Spotantic leverages Pydantic to validate user request inputs and to
parse Spotify Web API responses into typed models. This ensures request
payloads are checked before sending and incoming JSON responses are
converted into well-typed Pydantic models for safer application code.

.. toctree::
   :maxdepth: 2
   :caption: Getting started

   installation
   authorization
   quickstart
   examples

.. toctree::
   :maxdepth: 1
   :caption: Reference

   api_reference
   auth_reference
   client_reference
   spotantic_models
   spotify_models
   types_reference
