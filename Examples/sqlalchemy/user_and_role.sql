-- DROP STATEMENTS --
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Roles;


-- CREATE Tables --
/**
 *  Role Table
 */
CREATE TABLE IF NOT EXISTS Roles (
  role_id 								  SERIAL		  NOT NULL	UNIQUE,
  role_name                TEXT        NOT NULL,
  PRIMARY KEY (role_id)
);


/**
 * User Table
 */
CREATE TABLE IF NOT EXISTS Users (
  user_id 								  SERIAL		  NOT NULL	UNIQUE,
  email                   TEXT        NOT NULL,
  password                TEXT        NOT NULL,
  first_name 							TEXT 				NOT NULL,
  last_name 								TEXT 				NOT NULL,
  phone_number             BIGINT,
  role_id                  INT        NOT Null,
  PRIMARY KEY (user_id),
  FOREIGN KEY (role_id) REFERENCES Roles(role_id)
);


INSERT INTO Roles(role_name) VALUES ('Administrator');
INSERT INTO Roles(role_name) VALUES ('Student');
INSERT INTO Roles(role_name) VALUES ('Worker');


INSERT INTO Users(email, password, first_name, last_name, phone_number, role_id) VALUES ('james.crowley1@marist.edu', 'password', 'Jim', 'Crowley', '5183764600', 1);
INSERT INTO Users(email, password, first_name, last_name, phone_number, role_id) VALUES ('jordan@gmail.com', 'dssdafds', 'jordan', 'Temp', '4343435345', 2);
INSERT INTO Users(email, password, first_name, last_name, role_id) VALUES ('jeff@marist.edu', 'onetwothree', 'Jeff', 'Smith', 3);


SELECT * FROM Roles;
SELECT * FROM Users;

SELECT * FROM Users
  where role_id = 1;

SELECT * FROM Users
  INNER JOIN Roles ON Roles.role_id = Users.role_id;

SELECT Users.first_name, Users.last_name, Roles.role_name FROM Users
    INNER JOIN Roles ON Roles.role_id = Users.role_id;
