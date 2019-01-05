alter table tb_club_robot modify column clubId int(11) not null COMMENT '俱乐部ID' AFTER type ;
alter table tb_club_robot modify column groupId varchar(32) not null COMMENT '群ID' AFTER clubId ;
