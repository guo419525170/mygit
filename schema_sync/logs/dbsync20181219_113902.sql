alter table tb_statistics_hour modify column recharge decimal(12,2) default 0.00 COMMENT '充值金额' AFTER '[]' ;
alter table tb_statistics_hour modify column online int(11) default 0 COMMENT '在线人数' AFTER '[]' ;
