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

insert into metrobuses (id, date_updated, vehicle_id, vehicle_label, vehicle_current_status, position_latitude, position_longitude, geographic_point, position_speed, position_odometer, trip_schedule_relationship, trip_id, trip_start_date, trip_route_id, alcaldia) values (1, NOW()::timestamp, 1, 1, true, 437, 475, 'Goldenrod', 1, 1, 1, 1, NOW()::timestamp, 1, 'JumpXS');
insert into metrobuses (id, date_updated, vehicle_id, vehicle_label, vehicle_current_status, position_latitude, position_longitude, geographic_point, position_speed, position_odometer, trip_schedule_relationship, trip_id, trip_start_date, trip_route_id, alcaldia) values (2, NOW()::timestamp, 2, 2, true, 393, 977, 'Pink', 2, 2, 2, 2, NOW()::timestamp, 2, 'Mybuzz');
insert into metrobuses (id, date_updated, vehicle_id, vehicle_label, vehicle_current_status, position_latitude, position_longitude, geographic_point, position_speed, position_odometer, trip_schedule_relationship, trip_id, trip_start_date, trip_route_id, alcaldia) values (3, NOW()::timestamp, 3, 3, true, 586, 258, 'Purple', 3, 3, 3, 3, NOW()::timestamp, 3, 'Centizu');
insert into metrobuses (id, date_updated, vehicle_id, vehicle_label, vehicle_current_status, position_latitude, position_longitude, geographic_point, position_speed, position_odometer, trip_schedule_relationship, trip_id, trip_start_date, trip_route_id, alcaldia) values (4, NOW()::timestamp, 4, 4, false, 846, 355, 'Orange', 4, 4, 4, 4, NOW()::timestamp, 4, 'Flashdog');
insert into metrobuses (id, date_updated, vehicle_id, vehicle_label, vehicle_current_status, position_latitude, position_longitude, geographic_point, position_speed, position_odometer, trip_schedule_relationship, trip_id, trip_start_date, trip_route_id, alcaldia) values (5, NOW()::timestamp, 5, 5, false, 553, 710, 'Puce', 5, 5, 5, 5, NOW()::timestamp, 5, 'Zoovu');