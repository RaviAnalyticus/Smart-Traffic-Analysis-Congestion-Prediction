SELECT * FROM traffic_data LIMIT 20;

--Q-1)BUSIEST LOCATION

SELECT
    location_id,
    AVG(traffic_volume) AS avg_traffic
FROM traffic_data
GROUP BY location_id
ORDER BY avg_traffic DESC;

--Q-2)VEHICLE SPEED BY LOCATION 

SELECT
    location_id,
    ROUND(AVG(avg_vehicle_speed)::numeric,2) AS avg_speed
FROM traffic_data
GROUP BY location_id
ORDER BY avg_speed DESC;

--Q-3)WEATHER IMPACT

SELECT
    weather_condition,
    ROUND(AVG(traffic_volume)::numeric,2) AS avg_traffic
FROM traffic_data
GROUP BY weather_condition
ORDER BY avg_traffic DESC;

--Q-4)ACCIDENT IMPACT

SELECT
    accident_reported,
    ROUND(AVG(traffic_volume)::numeric,2) AS avg_traffic
FROM traffic_data
GROUP BY accident_reported;

--Q-5)SIGNAL STATUS IMPACT

SELECT
    signal_status,
    ROUND(AVG(traffic_volume)::numeric,2) AS avg_traffic
FROM traffic_data
GROUP BY signal_status
ORDER BY avg_traffic DESC;

--Q-6)VEHICLE COMPOSITION

SELECT
    SUM(vehicle_count_cars) AS total_cars,
    SUM(vehicle_count_trucks) AS total_trucks,
    SUM(vehicle_count_bikes) AS total_bikes
FROM traffic_data;

--Q-7)PEAK TRAFFIC HOURS

SELECT
    EXTRACT(HOUR FROM "timestamp") AS hour,
    ROUND(AVG(traffic_volume)::numeric,2) AS avg_traffic
FROM traffic_data
GROUP BY EXTRACT(HOUR FROM "timestamp")
ORDER BY avg_traffic DESC;

--Q-8)TOP 10 HIGHEST TRAFFIC RECORDS

SELECT
    timestamp,
    location_id,
    traffic_volume
FROM traffic_data
ORDER BY traffic_volume DESC
LIMIT 10;
