-- Create a DataBase hbnb_test_db for test enviroment
-- Create a User hbnb_dev to manage the database test enviroment

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test '@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_test '@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test '@'localhost';
FLUSH PRIVILEGES;
