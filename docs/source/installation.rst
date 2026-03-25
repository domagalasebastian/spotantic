Installation
============

Install Spotantic from PyPI or from source. **Note: Spotantic requires Python 3.12 or newer!**

Further details and optional dependencies are documented in the project's `pyproject.toml`.

Using package manager
---------------------

Install the released package using package manager:

.. code-block:: bash

   # using uv (recommended)
   uv add spotantic
   # or
   uv pip install spotantic

   # using pip
   python -m pip install spotantic


From source
-----------

Virtual environments
^^^^^^^^^^^^^^^^^^^^

We recommend using a virtual environment (venv, virtualenv, or conda)
to keep dependencies isolated. If you use the Astral `uv` helper tool to
manage project environments, you can use it to create and activate
the repository virtual environment and run install commands inside it.
Learn more about `uv` `here <https://docs.astral.sh/uv/>`_.

Example setup steps
^^^^^^^^^^^^^^^^^^^

To install the repository locally from source:

.. code-block:: bash

   git clone https://github.com/domagalasebastian/spotantic.git
   cd spotantic

   # Create venv and install dependencies
   uv sync
   source .venv/bin/activate

   # Alternatively
   python -m pip install -e .
