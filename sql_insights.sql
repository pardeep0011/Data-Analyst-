-- ============================================================
--  UBER REQUEST DATA — SQL INSIGHTS
--  Tool: DuckDB (in-process SQL on the CSV)
--  Analyst: Internship Project
-- ============================================================

-- ── INSIGHT 1: Overall Request Status Breakdown ──────────────
SELECT
    Status,
    COUNT(*)                                          AS total_requests,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 2) AS pct_share
FROM uber
GROUP BY Status
ORDER BY total_requests DESC;

-- ── INSIGHT 2: Fulfilment Rate by Pickup Point ───────────────
SELECT
    pickup_point,
    COUNT(*)                                                            AS total,
    SUM(CASE WHEN Status = 'Trip Completed'    THEN 1 ELSE 0 END)      AS completed,
    SUM(CASE WHEN Status = 'No Cars Available' THEN 1 ELSE 0 END)      AS no_cars,
    SUM(CASE WHEN Status = 'Cancelled'         THEN 1 ELSE 0 END)      AS cancelled,
    ROUND(100.0 * SUM(CASE WHEN Status = 'Trip Completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS completion_rate_pct
FROM uber
GROUP BY pickup_point;

-- ── INSIGHT 3: Peak Demand Hours ─────────────────────────────
SELECT
    hour,
    COUNT(*)                                          AS total_requests,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(), 2) AS pct_of_day
FROM uber
GROUP BY hour
ORDER BY total_requests DESC
LIMIT 10;

-- ── INSIGHT 4: Time Slot Performance ─────────────────────────
SELECT
    time_slot,
    COUNT(*)                                                            AS requests,
    SUM(CASE WHEN Status = 'Trip Completed'    THEN 1 ELSE 0 END)      AS completed,
    SUM(CASE WHEN Status = 'No Cars Available' THEN 1 ELSE 0 END)      AS no_cars,
    SUM(CASE WHEN Status = 'Cancelled'         THEN 1 ELSE 0 END)      AS cancelled,
    ROUND(100.0 * SUM(CASE WHEN Status = 'No Cars Available' THEN 1 ELSE 0 END) / COUNT(*), 2) AS no_car_rate_pct
FROM uber
GROUP BY time_slot
ORDER BY requests DESC;

-- ── INSIGHT 5: Daily Demand Trend ────────────────────────────
SELECT
    req_date,
    COUNT(*)                                                       AS total_requests,
    SUM(CASE WHEN Status = 'Trip Completed' THEN 1 ELSE 0 END)    AS completed,
    ROUND(100.0 * SUM(CASE WHEN Status = 'Trip Completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS completion_rate_pct
FROM uber
GROUP BY req_date
ORDER BY req_date;

-- ── INSIGHT 6: Average Trip Duration by Pickup Point ─────────
SELECT
    pickup_point,
    ROUND(AVG(trip_duration_mins), 2)  AS avg_duration_mins,
    ROUND(MIN(trip_duration_mins), 2)  AS min_duration_mins,
    ROUND(MAX(trip_duration_mins), 2)  AS max_duration_mins,
    COUNT(*)                           AS completed_trips
FROM uber
WHERE Status = 'Trip Completed'
  AND trip_duration_mins IS NOT NULL
GROUP BY pickup_point;

-- ── INSIGHT 7: Most Active Drivers (Top 10) ──────────────────
SELECT
    driver_id,
    COUNT(*)                                                        AS total_trips,
    SUM(CASE WHEN Status = 'Trip Completed' THEN 1 ELSE 0 END)     AS completed,
    SUM(CASE WHEN Status = 'Cancelled'      THEN 1 ELSE 0 END)     AS cancelled,
    ROUND(100.0 * SUM(CASE WHEN Status = 'Cancelled' THEN 1 ELSE 0 END) / COUNT(*), 2) AS cancellation_rate_pct
FROM uber
WHERE driver_id IS NOT NULL
GROUP BY driver_id
ORDER BY total_trips DESC
LIMIT 10;

-- ── INSIGHT 8: Gap Analysis — Supply vs Demand by Hour ───────
SELECT
    hour,
    COUNT(*)                                                             AS total_demand,
    SUM(CASE WHEN Status = 'No Cars Available' THEN 1 ELSE 0 END)       AS supply_gap,
    ROUND(100.0 * SUM(CASE WHEN Status = 'No Cars Available' THEN 1 ELSE 0 END) / COUNT(*), 2) AS gap_rate_pct,
    CASE
        WHEN ROUND(100.0 * SUM(CASE WHEN Status = 'No Cars Available' THEN 1 ELSE 0 END) / COUNT(*), 2) > 60 THEN 'CRITICAL'
        WHEN ROUND(100.0 * SUM(CASE WHEN Status = 'No Cars Available' THEN 1 ELSE 0 END) / COUNT(*), 2) > 40 THEN 'HIGH'
        WHEN ROUND(100.0 * SUM(CASE WHEN Status = 'No Cars Available' THEN 1 ELSE 0 END) / COUNT(*), 2) > 20 THEN 'MODERATE'
        ELSE 'LOW'
    END AS supply_pressure
FROM uber
GROUP BY hour
ORDER BY gap_rate_pct DESC;

-- ── INSIGHT 9: Airport — Inbound vs Outbound Problem ─────────
SELECT
    pickup_point,
    time_slot,
    COUNT(*)                                                             AS requests,
    SUM(CASE WHEN Status = 'No Cars Available' THEN 1 ELSE 0 END)       AS no_cars,
    ROUND(100.0 * SUM(CASE WHEN Status = 'No Cars Available' THEN 1 ELSE 0 END) / COUNT(*), 2) AS no_car_rate_pct
FROM uber
GROUP BY pickup_point, time_slot
ORDER BY no_car_rate_pct DESC;

-- ── INSIGHT 10: Rolling 3-Hour Demand Window ─────────────────
SELECT
    hour,
    COUNT(*) AS requests_this_hour,
    SUM(COUNT(*)) OVER (
        ORDER BY hour
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_3hr_demand
FROM uber
GROUP BY hour
ORDER BY hour;
