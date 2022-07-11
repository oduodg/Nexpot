create database IF NOT EXISTS Nexpot;

set foreign_key_checks = 0;   -- 외래키 체크하지 않는 것으로 설정
drop table IF EXISTS youtube cascade;   -- 기존 student 테이블 제거  
drop table IF EXISTS comments cascade;   -- 기존 course 테이블 제거  
drop table IF EXISTS places cascade;   -- 기존 enroll 테이블 제거  
set foreign_key_checks = 1;   -- 외래키 체크하는 것으로 설정

create table youtube ( 
	videoID CHAR(11) NOT NULL, 
	channelname varchar(15) NOT NULL, 
	title varchar(100) NOT NULL,
    Thumbnail varchar(48) NOT NULL,
    youtime date NOT NULL,
	views int DEFAULT 0,
	youtlikes INT default 0,
    lencomments INT default 0,
    primary key (videoID)
    ) ;
    
create table comments ( 
	commID varchar(20) NOT NULL, 
	videoID CHAR(11) NOT NULL, 
	reply varchar(200) NOT NULL,
	replylikes int DEFAULT 0,
	primary key (commID),
    FOREIGN KEY(videoID) REFERENCES youtube(videoID) 
		ON UPDATE CASCADE ON DELETE CASCADE
    ) ;
    
create table places ( 
	idx int NOT NULL,
    videoID CHAR(11) NOT NULL, 
	placeID varchar(12) NOT NULL, 
	pname varchar(20) NOT NULL,
    paddress varchar(50) NOT NULL,
    pdo varchar(10) NULL,
    psi varchar(15) NULL,
    pphone varchar(13) NULL,
    pdaumURL varchar(30) NULL,
	pX float NOT NULL,
    pY float NOT NULL,
	primary key (placeID),
    FOREIGN KEY(videoID) REFERENCES youtube(videoID) 
		ON UPDATE CASCADE ON DELETE CASCADE
    ) ;
select * from youtube;
select * from places;

use Nexpot;