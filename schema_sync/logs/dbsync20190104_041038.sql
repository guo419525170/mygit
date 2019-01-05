CREATE TABLE `tb_goldfield_new_year_activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createDate` bigint(16) NOT NULL,
  `userId` int(11) NOT NULL COMMENT '用户ID',
  `day1` int(11) DEFAULT NULL COMMENT '第一天领取',
  `day2` int(11) DEFAULT NULL COMMENT '第二天领取',
  `day3` int(11) DEFAULT NULL COMMENT '第三天领取',
  `day4` int(11) DEFAULT NULL COMMENT '第四天领取',
  `day5` int(11) DEFAULT NULL COMMENT '第五天领取',
  `day6` int(11) DEFAULT NULL COMMENT '第六天领取',
  `day7` int(11) DEFAULT NULL COMMENT '第七天领取',
  `createTime` bigint(16) NOT NULL COMMENT '创建时间',
  `updateTime` bigint(16) DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_userId` (`userId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='金币场-春节红包活动';
CREATE TABLE `tb_goldfield_streak` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fieldId` int(11) NOT NULL COMMENT '场次ID',
  `userId` int(11) NOT NULL COMMENT '用户ID',
  `status` tinyint(2) NOT NULL COMMENT '0进行中，1完成，-1失败',
  `lastGameStatus` tinyint(2) DEFAULT NULL COMMENT '最近一场状态-1输，0复活，1赢，null未打',
  `game1` tinyint(2) DEFAULT NULL COMMENT '0复活成功,-1失败,1成功,null未闯关',
  `game2` tinyint(2) DEFAULT NULL,
  `game3` tinyint(2) DEFAULT NULL,
  `game4` tinyint(2) DEFAULT NULL,
  `game5` tinyint(2) DEFAULT NULL,
  `game6` tinyint(2) DEFAULT NULL,
  `game7` tinyint(2) DEFAULT NULL,
  `createTime` bigint(16) NOT NULL,
  `updateTime` bigint(16) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_user_id` (`userId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;
alter table tb_recharge_ladder modify column os varchar(64) not null COMMENT 'money元宝,gold金币,treas宝箱,jipaiqi1一次性记牌器,jipaiqi2限时性记牌器,goldfield1金币场新手充值,goldfield2金币场首冲礼包,goldfieldNewYear金币场新春红包' AFTER id ;
alter table tb_goldfield_redpacket add  column fieldId int(11) not null COMMENT '' AFTER id ;
