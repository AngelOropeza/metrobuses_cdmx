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