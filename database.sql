# Script to create a user with SELECT and INSERT rights
# It also creates a database with one table

# Sadly someone wasn't very consistent with languages, but it's fine,
# it works I guess.

DROP USER IF EXISTS 'lit'@'localhost';
DROP DATABASE IF EXISTS producten;
CREATE DATABASE producten;
USE producten;
CREATE TABLE IF NOT EXISTS producten(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    barcode VARCHAR(15),
    product CHAR(255)
);

CREATE USER 'lit'@'localhost' IDENTIFIED BY '';
GRANT INSERT ON producten TO 'lit'@'localhost';
GRANT SELECT ON producten TO 'lit'@'localhost';