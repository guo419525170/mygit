alter table tb_user_present_reason add  column amountUp bigint(16) not null COMMENT '赠送数量上限' AFTER giveReasonType ;
alter table tb_user_present_reason add  column amountDown bigint(16) not null COMMENT '赠送数量下限' AFTER amountUp ;
alter table tb_user_present_reason drop column giveReason;
alter table tb_user_present_reason drop column amount;
