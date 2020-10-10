/*
Michael Lenckos
CSC 355 Section 501
Assignment 2
1/22/2020
*/

DROP TABLE booking;
DROP TABLE traveler;
DROP TABLE tour;

CREATE TABLE Traveler (
    TrID char(5),
    TrName varchar(255),
    TrPhone varchar(255),
    --CONSTRAINT TrID CHECK(LENGTH(TrID) = 5),
    CONSTRAINT TrName CHECK(LENGTH(TrName) < 40),
    CONSTRAINT TrPhone CHECK(LENGTH(TrPhone) = 10),
    PRIMARY KEY (TrID)
);

CREATE TABLE Tour (
    TID char(4),
    DestinationName varchar(255),
    TLength int,
    TCost int,
    CONSTRAINT TID CHECK(LENGTH(TID) = 4),
    CONSTRAINT TLength CHECK(LENGTH(TLength) > 0),
    CONSTRAINT TLength2 CHECK(LENGTH(TLength) <= 999),
    CONSTRAINT TCost CHECK(LENGTH(TCost) >= 0),
    CONSTRAINT TCost2 CHECK(LENGTH(TCost) <= 9999.99),
    PRIMARY KEY (TID)
);

CREATE TABLE Booking (
    TourID char(4),
    TravelerID char(5),
    TourDate DATE,
    CONSTRAINT TourID CHECK(LENGTH(TourID) = 4),
    CONSTRAINT TravelerID CHECK(LENGTH(TravelerID) = 5),
    PRIMARY KEY (TourID,TravelerID),
    FOREIGN KEY (TourID) REFERENCES TOUR(TID),
    FOREIGN KEY (TravelerID) REFERENCES Traveler(TRID)
    
);


-- Populate Tour Table
INSERT INTO TOUR(TID,DestinationName,TLength,TCost)
VALUES (1111, 'France', 1,100);
INSERT INTO TOUR(TID,DestinationName,TLength,TCost)
VALUES (2222, 'Germany', 7,5000);
INSERT INTO TOUR(TID,DestinationName,TLength,TCost)
VALUES (3333, 'Italy', 10,100);
INSERT INTO TOUR(TID,DestinationName,TLength,TCost)
VALUES (4444, 'China', 100,100);

-- Populate Travleer Table
INSERT INTO Traveler(TrID,TrName,TrPhone)
VALUES (00001, 'Michael Lenckos',1234567890);
INSERT INTO Traveler(TrID,TrName,TrPhone)
VALUES (00002, 'Jonathan Hawker',1234567893);
INSERT INTO Traveler(TrID,TrName,TrPhone)
VALUES (00003, 'Julios Harris',1234567896);

-- Populate Booking Table
INSERT INTO booking (TourID,TravelerID,TourDate)
VALUES (1111,00001,DATE '2019-01-01');
INSERT INTO booking (TourID,TravelerID,TourDate)
VALUES (1111,00002,DATE '2019-01-01');
INSERT INTO booking (TourID,TravelerID,TourDate)
VALUES (1111,00003,DATE '2019-01-01');
INSERT INTO booking (TourID,TravelerID,TourDate)
VALUES (2222,00001,DATE '2019-08-01');
INSERT INTO booking (TourID,TravelerID,TourDate)
VALUES (3333,00001,DATE '2022-01-01');

-- Output thingy
SELECT * FROM booking;
SELECT * FROM tour;
SELECT * FROM traveler; 