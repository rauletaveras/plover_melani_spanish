# Spanish support for Plover #

*	Authors: Sonsoles García Martín, Noelia Ruiz Martínez

Plover support for Melani system in Spanish, used at MQD.

Based on this [template](https://github.com/benoit-pierre/plover_template_system).

## Dependencies ##

* [Plover Python dictionary](https://github.com/benoit-pierre/plover_python_dictionary)

## Development ##

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and task running.

### Setup ###

Install uv if you haven't already:
```bash
# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install the project with development dependencies:
```bash
uv sync --all-extras
```

### Pre-commit Hooks (Optional but Recommended) ###

Install pre-commit hooks to automatically run linting and type checking before commits:
```bash
uv run pre-commit install
```

Now ruff and pyright will run automatically on every commit!

### Running Tests ###

```bash
# Run all tests
uv run pytest

# Run tests with arguments
uv run pytest -v
```

### Linting ###

```bash
# Run ruff linter
uv run ruff check

# Run ruff linter and fix issues automatically
uv run ruff check --fix

# Run ruff formatter
uv run ruff format
```

### Type Checking ###

```bash
# Run pyright
uv run pyright
```

### Building ###

```bash
# Build distribution packages
uv build
```

## Versioning ##

We use [SemVer](https://semver.org/).

## Changes ##

[Changelog](https://github.com/nvdaes/plover_spanish_mqd/blob/main/CHANGELOG.md)
