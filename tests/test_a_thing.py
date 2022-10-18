import psycopg2
import pytest


def postgres_conn(ip, port):
    dbname = "test"
    user = "postgres"
    password = "test"
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            host=ip,
            port=port,
            password=password,
        )
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE test (hello VARCHAR(24));")
        cursor.execute("INSERT INTO test (hello) VALUES (123);")
        cursor.execute("SELECT * FROM test;")
        records = cursor.fetchall()
        print("records", records)
        cursor.close()
        conn.close()
        return True
    except:
        # don't raise an exception here - it will cause docker_services to fail
        return False


@pytest.fixture(scope="session")
def db_service(docker_ip, docker_services):
    """Ensure that db service is up and responsive."""

    # `port_for` takes a container port and returns the corresponding host port
    port = docker_services.port_for("db", 5432)
    docker_services.wait_until_responsive(
        timeout=60.0, pause=0.1, check=lambda: postgres_conn(docker_ip, port)
    )
    return True


def test_postgres_conn(db_service):
    # db_service will timeout if it doesn't succeed
    assert db_service is True
