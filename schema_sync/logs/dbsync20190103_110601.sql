alter table tb_user_recharge modify column type tinyint(2) not null default 1 COMMENT '1元宝，2金币，3宝箱, 4金币场新手充值, 5金币场首冲礼包, 6金币场新春红包' AFTER orderId ;
alter table tb_recharge_ladder modify column os varchar(12) not null COMMENT 'money元宝,gold金币,treas宝箱,jipaiqi1一次性记牌器,jipaiqi2限时性记牌器,goldfield1金币场新手充值,goldfield2金币场首冲礼包,goldfieldNewYear金币场新春红包' AFTER id ;
