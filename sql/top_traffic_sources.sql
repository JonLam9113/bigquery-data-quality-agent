SELECT
    trafficSource.source AS traffic_source,
    COUNT(*) AS session_count
FROM
    `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
    _TABLE_SUFFIX BETWEEN '20170801' AND '20170807'
GROUP BY
    traffic_source
ORDER BY
    session_count DESC
LIMIT 10