alter table tb_user_present modify column giveReasonType varchar(255) default null COMMENT '赠送类别' AFTER approverId ;
