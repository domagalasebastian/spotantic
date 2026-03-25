# Contributing to Spotantic

Thank you for your interest in contributing to Spotantic! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to be respectful and constructive in all interactions.

## Getting Started

### Prerequisites

- Python 3.12 or higher
- Git
- A fork of the repository

### Setup Development Environment

```bash
# Clone your fork
git clone https://github.com/domagalasebastian/spotantic.git
cd spotantic

# Install development dependencies and activate virtual environment
uv sync --group dev --group docs
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

## How to Contribute

### 1. Open an Issue

Before starting work on a new feature or bug fix, please open an issue to discuss:
- What you're trying to fix/add
- Your proposed approach
- Any potential impact on the API

### 2. Create a Feature Branch

```bash
git checkout -b feat/your-feature-name
# or for bug fixes:
git checkout -b fix/your-fix-name
```

### 3. Make Your Changes

- Keep commits small and focused
- Follow [Conventional Commits](https://www.conventionalcommits.org/) format
- Write clear commit messages

### 4. Code Quality

Ensure all code quality checks pass:

```bash
# Run pre-commit checks
uv run pre-commit run --all-files

# Run tests
pytest tests/unit -v

# Build documentation (if updating docs)
uv run sphinx-build -b html docs/source docs/build/
```

### 5. Testing Requirements

- **Add tests** for any new functionality
- **Ensure existing tests** still pass
- **Unit tests** are required for all features
- **Integration tests** are optional but recommended for API-related changes

Test structure:
- Endpoint tests: `tests/unit/endpoints/<resource>/test_*.py`
- Model tests: `tests/unit/models/<resource>/requests/test_*.py`
- Use markers: `@pytest.mark.readonly`, `@pytest.mark.mutation`, etc.

### 6. Documentation

- Update docstrings for public APIs (use Google style)
- Update relevant `.rst` files in `docs/source/` if changing API
- Add type hints to all functions

### 7. Submit a Pull Request

- Fill out the PR template completely
- Reference any related issue with `Closes #123`
- Ensure all CI checks pass
- Request reviews from maintainers

## Code Style Guidelines

### Formatting

- Line length: 120 characters
- Use double quotes for strings
- Indent with 4 spaces
- Run `uv run ruff format .` to auto-format

### Linting

- Follow all Ruff rules
- Run `uv run ruff check --fix .` before committing

### Type Hints

- All public functions must have type hints
- Use `from __future__ import annotations` for forward references
- Use Pydantic models for API responses

### Docstrings

- Use Google-style docstrings
- Document parameters, return types, and exceptions
- Example:

```python
def authorize(self) -> None:
    """Authorize the user with Spotify.

    Initiates the OAuth flow and opens browser for user authorization.

    Raises:
        AuthorizationError: If authorization fails.
    """
```

## Commit Message Convention

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`

**Examples**:
- `feat(auth): add support for refresh token rotation`
- `fix(client): handle connection timeouts gracefully`
- `docs: update quickstart guide with PKCE example`

## Testing Best Practices

### Unit Tests

- Test in isolation
- Mock external dependencies
- Keep tests fast

### Integration Tests

- Require valid Spotify credentials
- Test real API interactions

## Questions?

- Open a GitHub Discussion
- Check existing issues
- Review documentation at https://spotantic.readthedocs.io

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
