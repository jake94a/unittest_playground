A project to play around with unit testing

Using pytest and pytest-docker to spin up a postgresql testing database

# HOW TO

1. Clone repo
2. Create new venv
3. `pip install -r requirements.txt`
4. Verify installation of `docker compose`
   1. If using V1 (`docker-compose`) update `conftest.py`
5. Run `pytest`
   1. Use `pytest -rP` to read `print` statements
   2. This will spin up the `postgres` container as specified in `/tests/docker-compose.yml` allowing tests to run against it
