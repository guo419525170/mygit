alter table tb_goldfield add  column redpacketInfo varchar(512) COMMENT '' AFTER streakInfo ;
alter table tb_goldfield add  column streakInfo varchar(512) COMMENT '' AFTER recharge ;
alter table tb_user_present add  column giveReasonType varchar(255) COMMENT '' AFTER approverId ;
