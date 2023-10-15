-- displays the average temperature in Fahrenheit by city, ordered by temperature in descending order
SELECT 
    city,
    AVG((temperature_celsius * 9/5) + 32) AS average_temperature_fahrenheit
FROM temperature_data
GROUP BY city
ORDER BY average_temperature_fahrenheit DESC;
