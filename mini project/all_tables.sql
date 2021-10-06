
use fyp;
CREATE TABLE rabia(
   sno int NOT NULL AUTO_INCREMENT,
    groupleader VARCHAR(300),
    institution VARCHAR(300),
    nameofdp varchar(300),
    headofdp varchar(300),
    psupervisor varchar(300),
    nofgroupmembers varchar(300),
    pgmofstudy varchar(300),
    ptitle varchar(300),
    pdiscription varchar(300),
    date_created  DATETIME DEFAULT   CURRENT_TIMESTAMP,
PRIMARY KEY (sno)
);


