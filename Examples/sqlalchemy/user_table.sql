-- DROP STATEMENTS --
DROP TABLE IF EXISTS Users;

-- CREATE Tables --
/**
 * Simple User Table
 */
CREATE TABLE IF NOT EXISTS Users (
  userID 								  SERIAL		  NOT NULL	UNIQUE,
  email                   TEXT        NOT NULL,
  firstName 							TEXT 				NOT NULL,
  lastName 								TEXT 				NOT NULL,
  PRIMARY KEY (userID)
);


INSERT INTO Users(email, firstName, lastName) VALUES ('james.crowley1@marist.edu', 'Jim', 'Crowley');

SELECT * FROM Users;

SELECT firstname, lastname FROM Users
  WHERE email = 'james.crowley1@marist.edu';


