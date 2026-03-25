# Spotantic

[![PyPI version](https://badge.fury.io/py/spotantic.svg)](https://badge.fury.io/py/spotantic)
[![Documentation Status](https://readthedocs.org/projects/spotantic/badge/?version=latest)](https://spotantic.readthedocs.io/en/latest/?badge=latest)
[![Tests](https://github.com/domagalasebastian/spotantic/actions/workflows/run-tests.yml/badge.svg)](https://github.com/domagalasebastian/spotantic/actions/workflows/run-tests.yml)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An asynchronous Python client library for the Spotify Web API with full type hints, modular endpoint helpers, and support for multiple authorization flows.

## ✨ Features

- **Fully Asynchronous**: Built on `aiohttp` for non-blocking operations
- **Type-Safe**: Leverages Pydantic for request validation and response parsing
- **Multiple Auth Flows**: Support for Client Credentials, Authorization Code, and Authorization Code PKCE flows
- **Modular Endpoints**: Clean, organized endpoint helpers for albums, artists, playlists, tracks, users, and more
- **Request Validation**: All requests are validated before sending to Spotify's API
- **Automatic Token Refresh**: Optional automatic refresh token handling
- **Comprehensive Documentation**: Full API reference and examples included

## 📋 Prerequisites

- **Python 3.12 or higher**
- A Spotify Developer account (get one at [developer.spotify.com](https://developer.spotify.com))
- Client ID and Client Secret from the Spotify Developer Dashboard

## 🔧 Installation

### From PyPI (Recommended)

```bash
# Using uv (recommended)
uv add spotantic
```

Or using pip:

```bash
pip install spotantic
```

### From Source

```bash
git clone https://github.com/domagalasebastian/spotantic.git
cd spotantic

# Create venv and install dependencies
uv sync
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
uv sync --group dev
```

## 🚀 Quick Start

### 1. Configure Your Environment

Create a `.env` file in your project root with your Spotify credentials:

```bash
# Your credentials from Spotify Developer Dashboard
SPOTANTIC_AUTH_CLIENT_ID=your_client_id_here
SPOTANTIC_AUTH_CLIENT_SECRET=your_client_secret_here
SPOTANTIC_AUTH_REDIRECT_URI=http://127.0.0.1:8000/callback

# Scopes you need (space-separated)
SPOTANTIC_AUTH_SCOPE=user-library-read user-library-modify

# Optional: where to store the access token cache
SPOTANTIC_AUTH_ACCESS_TOKEN_FILE_PATH=.token_info_cache
SPOTANTIC_AUTH_STORE_ACCESS_TOKEN=true

# Optional: logging configuration
SPOTANTIC_LOGGING_ENABLE=true
SPOTANTIC_LOGGING_DEBUG=false
SPOTANTIC_LOGGING_LOGS_DIR=logs/
```

For more details on configuration options, see the [Quick Start Guide](https://spotantic.readthedocs.io/en/latest/quickstart.html).

### 2. Create a Client

Choose an authorization flow based on your use case:

#### Authorization Code PKCE Flow (Recommended for user-facing apps)

```python
import asyncio
from spotantic.auth import AuthCodePKCEFlowManager
from spotantic.client import SpotanticClient
from spotantic.models.auth import AuthSettings

async def main():
    # Load settings from .env file
    auth_settings = AuthSettings()

    # Create auth manager (browser opens automatically for authorization)
    auth_manager = AuthCodePKCEFlowManager(
        auth_settings=auth_settings,
        allow_lazy_refresh=True
    )

    # Authorize user
    await auth_manager.authorize()

    # Create client
    client = SpotanticClient(
        auth_manager=auth_manager,
        max_attempts=3,
        check_insufficient_scope=True
    )

    return client

# Run it
client = asyncio.run(main())
```

#### Client Credentials Flow (For server-to-server requests)

```python
from spotantic.auth import ClientCredentialsFlowManager
from spotantic.client import SpotanticClient
from spotantic.models.auth import AuthSettings

async def main():
    auth_settings = AuthSettings()
    auth_manager = ClientCredentialsFlowManager(auth_settings=auth_settings)
    await auth_manager.authorize()

    return SpotanticClient(auth_manager=auth_manager)
```

#### Standard Authorization Code Flow

```python
from spotantic.auth import AuthCodeFlowManager
from spotantic.client import SpotanticClient
from spotantic.models.auth import AuthSettings

async def main():
    auth_settings = AuthSettings()
    auth_manager = AuthCodeFlowManager(
        auth_settings=auth_settings,
        allow_lazy_refresh=True
    )
    await auth_manager.authorize()

    return SpotanticClient(auth_manager=auth_manager)
```

### 3. Make API Requests

```python
from spotantic.endpoints import albums, tracks

async def search_and_get_details(client):
    # Get user's saved albums
    saved_albums = await albums.get_user_saved_albums(client, limit=5)

    # All responses are fully typed
    for album in saved_albums.data.items:
        print(f"Album: {album.album.album_name}")
        print(f"Artist: {album.album.artists[0].artist_name}")

    # Get details for a specific album
    album_id = saved_albums.data.items[0].album.album_id
    album_details = await albums.get_album(client, album_id=album_id)

    print(f"Release Date: {album_details.data.release_date}")
```

For more examples, see the [examples](examples/) directory and [full documentation](https://spotantic.readthedocs.io/).

## 📚 Authorization Flows

Spotantic supports three Spotify authorization flows:

| Flow | Use Case | Refresh Token | Requires Secret |
|------|----------|---------------|-----------------|
| **Client Credentials** | Server-to-server, no user data | ❌ | ✅ |
| **Authorization Code** | Full user authorization, backendapps | ✅ | ✅ |
| **Authorization Code PKCE** | Browser/native apps | ✅ | ❌ |

**Important**: Spotantic only supports localhost redirect URIs. During authorization, the library temporarily hosts a local endpoint to complete the OAuth exchange.

See the [Authorization Guide](https://spotantic.readthedocs.io/en/latest/auth_reference.html) for detailed information.

## 🧪 Testing and Development

### Running Tests

```bash
# Run all unit tests
pytest tests/unit

# Run specific test directory
pytest tests/unit/endpoints/albums

# Run integration tests (requires valid token and network access)
pytest tests/integration

# Run only tests that do not affect user data
pytest tests/integration -m "readonly"
```

### Code Quality Checks

Spotantic uses Ruff for linting and formatting. All contributions must pass these checks:

```bash
# Run pre-commit checks (linting, formatting, type checking)
uv run pre-commit run --all-files

# Or individually:
# Lint and auto-fix
uv run ruff check --fix .

# Format code
uv run ruff format .

# Type checking
pyright
```

### Building Documentation Locally

```bash
cd docs
uv run sphinx-build -b html source/ build/
# Documentation available at build/index.html (open in browser)
```

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Code Style**: All code must pass Ruff linting and formatting checks. Run `pre-commit run --all-files` before submitting a PR.

2. **Type Checking**: Code must pass Pyright type checking (`pyright`).

3. **Testing**:
   - Add tests for any new features
   - Ensure all tests pass: `pytest tests/unit`
   - Tests run on Python 3.12, 3.13, and 3.14

4. **Commit Style**: Follow [Conventional Commits](https://www.conventionalcommits.org/) format.

5. **Documentation**: Update relevant documentation for API changes.

### Development Workflow

```bash
# Setup development environment
uv sync --all-groups

# Activate virtual environment
source .venv/bin/activate

# Make your changes and run checks
uv run pre-commit run --all-files
pytest tests/unit

# Optionally, run integration tests (requires valid token and network access)
pytest tests/integration

# Build docs to verify they work
uv run sphinx-build -b html docs/source docs/build/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Legal Disclaimer

**This project is not affiliated with, endorsed by, or associated with Spotify AB or any of its subsidiaries or affiliates.** Spotantic is an independent, community-maintained library that provides convenient access to the Spotify Web API. All Spotify trademarks, logos, and product names are the property of Spotify AB.

Please ensure your use of this library complies with [Spotify's Developer Terms of Service](https://developer.spotify.com/terms).

## 🔗 Resources

- **[Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api/)**
- **[Project Documentation](https://spotantic.readthedocs.io/)**
- **[GitHub Repository](https://github.com/domagalasebastian/spotantic)**
- **[Examples](examples/)**

---

Made with ❤️ by [Sebastian Domagała](https://github.com/domagalasebastian)
