CREATE DATABASE ParkEase;
USE ParkEase;


CREATE TABLE parking_space (
    Parking_id VARCHAR(2) NOT NULL,
    Status varchar(255) DEFAULT 'Active',
    PRIMARY KEY (Parking_id)
);

CREATE TABLE Vehicle_in (
    Date DATE,
    Type TEXT NOT NULL,
    Owner_type TEXT NOT NULL,
    Vehicle_no VARCHAR(50) NOT NULL,
    P_id VARCHAR(2) NOT NULL,
    ID VARCHAR(13) NOT NULL,
    PRIMARY KEY (ID),
    FOREIGN KEY (P_id) REFERENCES parking_space(Parking_id)
);

CREATE TABLE student (
    Contact VARCHAR(10) NOT NULL,
    ID VARCHAR(13) NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Semester INT CHECK (Semester > 0 AND Semester < 9),
    PRIMARY KEY (ID),
    UNIQUE (Name)
);

CREATE TABLE faculty (
    Contact VARCHAR(10) NOT NULL,
    ID VARCHAR(13) NOT NULL,
    Name VARCHAR(50) NOT NULL,
    PRIMARY KEY (ID)
);

CREATE TABLE VehicleType (
    Type_ID INT AUTO_INCREMENT,
    TypeName VARCHAR(20) NOT NULL,
    O_type VARCHAR(20),
    Vehicleid VARCHAR(20), 
    PRIMARY KEY (Type_ID)
);

INSERT INTO student(Contact, ID, Name, Semester) VALUES 
    ("9680346789", "PES2UG21CS147", "Chocku", "5"),
    ("9569324152", "PES2UG21CS154", "Darshan", "5"),
    ("9632687172", "PES2UG20CS130", "Harsha", "5"),
    ("9443215678", "PES2UG20CS172", "Gagan", "5"),
    ("9089786756", "PES2UG20CS190", "Harshan", "5");

INSERT INTO faculty(Contact, ID, Name) VALUES 
    ("9980764324", "PES2EICS100", "Prof.Niveditha"),
    ("9900112233", "PES2EICS101", "Prof.Alpha"),
    ("9988776655", "PES2EICS102", "Prof.Animesh"),
    ("9977668855", "PES2EICS103", "Prof.Sheela"),
    ("9955667744", "PES2EICS104", "Prof.Sudeepa");

INSERT INTO parking_space(Parking_id, Status) VALUES 
    ('A1', 'Active'),
    ('A2', 'Active'),
    ('A3', 'Active'),
    ('A4', 'Active'),
    ('A5', 'Active'),
    ('A6', 'Active'),
    ('A7', 'Active'),
    ('A8', 'Active');

DELIMITER //
CREATE PROCEDURE StatusUpdation (IN parking_id VARCHAR(2))
BEGIN
    UPDATE parking_space SET Status="Occupied" WHERE parking_space.Parking_id = parking_id;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER SETSTATUS AFTER INSERT ON Vehicle_in
FOR EACH ROW
BEGIN
    CALL StatusUpdation(NEW.P_id);
END //
DELIMITER ;

DELIMITER $$ 
CREATE FUNCTION Amount_calc(Owner_type VARCHAR(20), t VARCHAR(20)) 
RETURNS INT
DETERMINISTIC 
BEGIN 
    DECLARE VALUE INT; 
    IF Owner_type = 'Teacher' THEN 
        SET VALUE = 0; 
    ELSE
        IF t = 'Two Wheeler' THEN
            SET VALUE = 10; 
        ELSE 
            SET VALUE = 30;
        END IF; 
    END IF;

    RETURN VALUE; 
END;$$ 
DELIMITER ;

SELECT COUNT(*) AS total_students FROM student; 
SELECT COUNT(*) AS total_faculty FROM faculty; 
SELECT COUNT(*) AS total_vehicles_entered FROM Vehicle_in; 
SELECT COUNT(*) AS total_parking_lots FROM parking_space; 

SELECT Name FROM faculty  
UNION  
SELECT Name FROM student; 

SELECT Parking_id FROM parking_space  
UNION  
SELECT P_id FROM Vehicle_in; 

SELECT Name FROM student  
UNION  
SELECT owner_type FROM Vehicle_in;

SELECT P_id, COUNT(*) AS TotalVehicles
FROM Vehicle_in
GROUP BY P_id;

SELECT s.Name, v.Vehicle_no, p.Status
FROM student s
JOIN Vehicle_in v ON s.ID = v.ID
JOIN parking_space p ON v.P_id = p.Parking_id;

SELECT Name
FROM faculty
WHERE ID IN (
    SELECT DISTINCT v.ID
    FROM Vehicle_in v
    JOIN VehicleType vt ON v.Type = vt.TypeName
    WHERE vt.TypeName = 'Four Wheeler'
);