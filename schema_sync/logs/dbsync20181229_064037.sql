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
alter table tb_goldfield add  column redpacketInfo varchar(512) COMMENT '' AFTER streakInfo ;
alter table tb_goldfield add  column streakInfo varchar(512) COMMENT '' AFTER recharge ;
alter table tb_goldfield modify column lowerLimit int(11) default null COMMENT '入场金币下限' AFTER award ;
alter table tb_goldfield_redpacket add  column reason varchar(64) not null COMMENT '' AFTER status ;
alter table tb_goldfield_redpacket add  column userId int(11) not null COMMENT '' AFTER fieldId ;
