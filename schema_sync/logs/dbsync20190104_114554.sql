alter table tb_club_robot add unique (type,clubId);
alter table tb_club_robot drop  key index_clubid_groupid ;
