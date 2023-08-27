DROP DATABASE IF EXISTS "datatest"
CREATE DATABASE IF NOT EXISTS "datatest"

CREATE TABLE IF NOT EXISTS "ninjatable"
(
    `id_ninjatable` INT NOT NULL AUTO_INCREMENT,
    `ninja_first_name` VARCHAR(30) NOT NULL UNIQUE,
    `ninja_last_name` varchar(5000) NOT NULL
    PRIMARY KEY(`id_ninjatable`)
)

INSERT INTO `ninjatable` (`ninja_first_name`,`ninja_last_name`)
VALUE
(`Naruto`, `Uzumaki`),
(`Sakura` ,`Haruno`),
(`Sasuke`, `Uchiwa` ),
(`Hinata`,`Hyûga`),