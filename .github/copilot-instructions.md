# Copilot Instructions for Spotantic Repository

## Repository Overview
Spotantic is an asynchronous Spotify API client built using Python. It provides a robust and efficient way to interact with Spotify's API, supporting various authentication flows (Authorization Code Flow, Authorization Code PKCE Flow, and Client Credentials Flow) and offering a range of endpoints for interacting with Spotify's services.

### Key Details:
- **Project Type**: Python library
- **Primary Language**: Python (requires Python >= 3.12)
- **Frameworks/Tools**:
  - `aiohttp` for asynchronous HTTP requests
  - `pydantic` for data validation and settings management
  - `pytest` and `pytest-asyncio` for testing
  - `sphinx` for documentation
- **Documentation**: Sphinx-based, located in `docs/`

## Build and Validation Instructions

### Environment Setup
1. **Python Environment**:
   - Ensure Python 3.12 or higher is installed.
   - Use a virtual environment:
     ```bash
     source .venv/bin/activate
     ```
   - Install dependencies:
     ```bash
     uv pip install -e .
     ```

2. **Install Development Dependencies** (if contributing):
   ```bash
   uv pip install -e .[dev]
   ```

### Linting
- Run Ruff to lint and auto-fix code (use the workspace venv if available):
  ```bash
  uv run ruff check --fix .
  # or, if ruff is installed in the venv:
  python -m ruff check --fix .
  ```

### Testing
- Run tests using pytest (the venv includes pytest):
  ```bash
  pytest
  # or for more control / faster iteration:
  python -m pytest tests/unit/endpoints/shows tests/unit/models/shows/requests -q
  ```
- Most tests are in `tests/unit/` and follow a naming convention:
  - endpoint tests: `tests/unit/endpoints/<resource>/test_*.py`
  - request-model tests: `tests/unit/models/<resource>/requests/test_*.py`
- Endpoint tests generally:
  - patch `Request.build()`
  - patch `.model_validate()` for response models
  - assert the returned `APICallModel` has `request`, `response`, and parsed `data`
- Request-model tests generally cover:
  - proper endpoint/params serialization
  - required scopes and HTTP method
  - validation errors (e.g. list length limits, numeric bounds)

### Documentation
- Build the documentation using Sphinx:
  ```bash
  uv run sphinx-build -b html docs/source docs/build/
  ```
  - The generated documentation will be available in `docs/build/html/index.html`.

### Running the Project
- Example client setup scripts are available in `examples/create_client.py`. To run the example:
  ```bash
  python examples/create_client.py
  ```

## Project Layout
- **Root Directory**:
  - `pyproject.toml`: Project configuration, including dependencies, linting, and testing settings.
  - `README.md`: Currently empty.
  - `docs/`: Contains Sphinx documentation source files and build outputs.
  - `examples/`: Example scripts for setting up and using the Spotantic client.
  - `logs/`: Contains log files organized by timestamp.
  - `src/`: Main source code for the Spotantic library.
  - `tests/`: Contains test cases for the project.

- **Key Configuration Files**:
  - `pyproject.toml`: Defines dependencies, development tools (Ruff, Pyright, Pytest), and project metadata.
  - `docs/source/conf.py`: Sphinx documentation configuration.

- **Authentication**:
  - Authentication flows are implemented in `src/spotantic/auth/`.
  - Example usage of authentication flows is provided in `examples/create_client.py`.

## Validation and CI/CD
- **Pre-commit Hooks**:
  - Run pre-commit checks:
    ```bash
    uv run pre-commit run --all-files
    ```

- **Continuous Integration**:
  - No CI/CD configuration files (e.g., GitHub Actions) were found in the repository.

## Additional Notes
- Trust these instructions for building, testing, and running the project. Perform additional searches only if these instructions are incomplete or incorrect.
- The repository is actively using Ruff for linting and Pyright for type checking. Ensure all changes pass these checks before committing.
- The `tests/` directory contains test cases. Use `pytest` to validate changes.
- The `examples/` directory provides example scripts for using the Spotantic client.
- The `docs/` directory contains Sphinx documentation. Update and rebuild documentation as needed for changes to the API or usage.

By following these instructions, you can efficiently navigate and contribute to the Spotantic repository.
