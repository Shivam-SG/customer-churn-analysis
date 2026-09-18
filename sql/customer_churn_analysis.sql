SELECT
    COUNT(*) AS total_customers,
    COUNT(*) FILTER (WHERE churn_label = 'Yes') AS churned_customers,
    ROUND(
        100.0 * COUNT(*) FILTER (WHERE churn_label = 'Yes')
        / COUNT(*),
        2
    ) AS churn_rate_percentage
FROM telco_churn
WHERE contract = 'Month-to-month'
  AND internet_service = 'Fiber optic';