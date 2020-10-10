DROP TABLE PAYROLL CASCADE CONSTRAINTS;
CREATE TABLE PAYROLL
(
	EID		CHAR(5)		PRIMARY KEY,
	EName		VARCHAR2(12),
	ESalary	NUMBER(8,2)
);
INSERT INTO PAYROLL VALUES ('34115', 'Dolenz', 3200);
INSERT INTO PAYROLL VALUES ('09002', 'Jones', 5200);
INSERT INTO PAYROLL VALUES ('83321', 'Nesmith', 4500);
INSERT INTO PAYROLL VALUES ('53099', 'Tork', 4000);
SELECT * FROM PAYROLL;
DROP TABLE WITHHOLD;
CREATE TABLE WITHHOLD
(
	Rate1		NUMBER(2,1),
	Threshold	NUMBER(8,2),
	Rate2		NUMBER(2,1)
);
INSERT INTO WITHHOLD VALUES (2.0, 4000.00, 3.0);
SELECT * FROM WITHHOLD;
COMMIT;

-- anomyous block time boiiii

DECLARE
  rate_1_val WITHHOLD.rate1%TYPE;
  rate_2_val withhold.rate2%TYPE;
  threshold_value withhold.threshold%TYPE;
  
  cursor act_cursor is SELECT rate1, rate2, threshold from WITHHOLD
BEGIN
    
  DBMS_OUTPUT.PUT_LINE(rate_2_val);
  DBMS_OUTPUT.PUT_LINE(threshold_value);
  
  open act_cursor
  loop
    fetch act_cursor into r1,  r2, t;
END;

