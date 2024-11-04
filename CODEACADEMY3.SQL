SELECT * FROM trips;
SELECT * FROM riders;
SELECT * FROM cars;
select riders.first,cars.model from riders ,cars;
select * from trips
left join riders
  on riders.id = trips.rider_id;
SELECT trips.date,
   trips.pickup,
   trips.dropoff,
   trips.type,
   trips.cost,
   riders.first,
   riders.last,
   riders.username
FROM trips
LEFT JOIN riders
  ON trips.rider_id = riders.id;
SELECT *
FROM trips
INNER JOIN cars
  ON trips.car_id = cars.id;
SELECT * FROM riders
UNION
SELECT * FROM riders2;
ELECT AVG(cost)
FROM trips;
SELECT *
FROM riders
WHERE total_trips < 500
UNION
SELECT *
FROM riders2
WHERE total_trips < 500;
SELECT COUNT(*)
FROM cars
WHERE status = 'active';
SELECT *
FROM cars
ORDER BY trips_completed DESC
LIMIT 2;


