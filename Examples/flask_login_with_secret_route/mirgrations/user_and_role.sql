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
  password_hash           TEXT        NOT NULL,
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

-- password
INSERT INTO Users(email, password_hash, first_name, last_name, phone_number, role_id) VALUES ('james.crowley1@marist.edu', 'pbkdf2:sha256:150000$lf2vi6Wt$e580ea376557d73978b4c5ca6a1c71c4882b06a64ee53cfa1ce1b5135cfaac33', 'Jim', 'Crowley', '5183764600', 1);

-- test
INSERT INTO Users(email, password_hash, first_name, last_name, phone_number, role_id) VALUES ('jordan@gmail.com', 'pbkdf2:sha256:150000$CsGhRQet$ccd18cfb92fe075acea12bcb9b9472ce72b8c032dd2adf200111adf21a4e0e25', 'jordan', 'Temp', '4343435345', 2);

-- onetwothree
INSERT INTO Users(email, password_hash, first_name, last_name, role_id) VALUES ('jeff@marist.edu', 'pbkdf2:sha256:150000$eckN1I4H$ab14ca84fbabc5861b4b2bcbdc546fb97b7fdff43b426275492c97b9906a0ec7', 'Jeff', 'Smith', 3);


SELECT * FROM Roles;
SELECT * FROM Users;

SELECT * FROM Users
  where role_id = 1;

SELECT * FROM Users
  INNER JOIN Roles ON Roles.role_id = Users.role_id;

SELECT Users.first_name, Users.last_name, Roles.role_name FROM Users
    INNER JOIN Roles ON Roles.role_id = Users.role_id;
