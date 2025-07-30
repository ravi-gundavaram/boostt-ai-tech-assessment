-- Table DDL
CREATE TABLE IF NOT EXISTS customer_daily (
    customer_id STRING,
    treatment INT64,
    pre_spend FLOAT64,
    post_spend FLOAT64,
    geo STRING,
    factor_a INT64,
    factor_b INT64,
    event_date DATE
);

-- Scheduled Query 1: Write CUPED theta
CREATE OR REPLACE TABLE cuped_theta AS
SELECT
  DATE(event_date) AS day,
  CORR(pre_spend, post_spend) * STDDEV(post_spend) / STDDEV(pre_spend) AS theta
FROM customer_daily
GROUP BY day;

-- Scheduled Query 2: Write experiment lift
CREATE OR REPLACE TABLE experiments_lift AS
SELECT
  DATE(event_date) AS day,
  AVG(IF(treatment=1, post_spend, NULL)) AS treatment_avg,
  AVG(IF(treatment=0, post_spend, NULL)) AS control_avg,
  SAFE_DIVIDE(AVG(IF(treatment=1, post_spend, NULL)) - AVG(IF(treatment=0, post_spend, NULL)), AVG(IF(treatment=0, post_spend, NULL))) * 100 AS lift_percent
FROM customer_daily
GROUP BY day;
