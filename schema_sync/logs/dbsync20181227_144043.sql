alter table tb_user_present_reason add  column limit bigint(16) COMMENT '限制次数' AFTER amountDown ;
alter table tb_user_present_reason modify column giveReasonType varchar(255) not null COMMENT '赠送类别' AFTER id ;
