from google.cloud import bigquery


def run_query():
    client = bigquery.Client()

    query = """
    SELECT
        1 AS test_value,
        CURRENT_TIMESTAMP() AS current_time
    """

    query_job = client.query(query)

    results = query_job.result()

    for row in results:
        print(f"test_value: {row.test_value}")
        print(f"current_time: {row.current_time}")


if __name__ == "__main__":
    run_query()