from google.cloud import bigquery


def load_sql(file_path):
    with open(file_path, "r") as file:
        return file.read()


def run_query(sql_file):
    client = bigquery.Client()

    query = load_sql(sql_file)

    query_job = client.query(query)

    results = query_job.result()

    for row in results:
        print(f"{row.traffic_source}: {row.session_count} sessions")


if __name__ == "__main__":
    run_query("sql/top_traffic_sources.sql")