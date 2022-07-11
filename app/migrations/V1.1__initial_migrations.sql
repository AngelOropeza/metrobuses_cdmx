CREATE EXTENSION unaccent;

CREATE TABLE IF NOT EXISTS metrobuses (
    id SERIAL PRIMARY KEY,
    date_updated TIMESTAMP NOT NULL,
    vehicle_id INT NOT NULL,
    vehicle_label INT NOT NULL,
    vehicle_current_status BOOLEAN NOT NULL,
    position_latitude REAL NOT NULL,
    position_longitude REAL NOT NULL,
    geographic_point VARCHAR(35) NOT NULL,
    position_speed INT NOT NULL,
    position_odometer INT NOT NULL,
    trip_schedule_relationship INT NOT NULL,
    trip_id INT,
    trip_start_date TIMESTAMP,
    trip_route_id INT,
    alcaldia VARCHAR(80)
);

COPY metrobuses(id, date_updated, vehicle_id, vehicle_label, vehicle_current_status, position_latitude, position_longitude, geographic_point, position_speed, position_odometer, trip_schedule_relationship, trip_id, trip_start_date, trip_route_id, alcaldia)
FROM '/mb_data/clean_mb_data.csv'
DELIMITER ','
CSV HEADER;