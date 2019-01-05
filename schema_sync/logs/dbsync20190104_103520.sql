alter table tb_club_robot add  column type tinyint(2) not null COMMENT '1闲聊' AFTER id ;
alter table tb_club_robot modify column groupId varchar(32) not null COMMENT '群ID' AFTER clubId ;
alter table tb_club_robot modify column clubId int(11) not null COMMENT '俱乐部ID' AFTER type ;
