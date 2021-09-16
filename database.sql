DROP USER IF EXISTS 'lit'@'localhost';
DROP DATABASE IF EXISTS producten;
CREATE DATABASE producten;
USE producten;
CREATE TABLE IF NOT EXISTS producten(
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    barcode VARCHAR(15),
    product CHAR(255)
);
INSERT INTO producten (barcode, product) VALUES ('3471829019548', 'Dalphin Water');

CREATE USER 'lit'@'localhost' IDENTIFIED BY '';
GRANT INSERT ON producten TO 'lit'@'localhost';
GRANT SELECT ON producten TO 'lit'@'localhost';