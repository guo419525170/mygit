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
CREATE TABLE `tb_club_robot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` tinyint(2) NOT NULL COMMENT '1闲聊',
  `clubId` int(11) NOT NULL COMMENT '俱乐部ID',
  `groupId` varchar(32) NOT NULL COMMENT '群ID',
  `createTime` bigint(16) NOT NULL,
  `updateTime` bigint(16) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_type_clubid` (`type`,`clubId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
CREATE TABLE `tb_goldfield_new_year_activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userId` int(11) NOT NULL COMMENT '用户ID',
  `createDate` bigint(16) NOT NULL,
  `lastRecvDate` bigint(16) DEFAULT NULL COMMENT '最新领取日期(yyyymmdd)',
  `days` varchar(256) DEFAULT NULL COMMENT '领取情况',
  `createTime` bigint(16) NOT NULL COMMENT '创建时间',
  `updateTime` bigint(16) DEFAULT NULL COMMENT '修改时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_userId` (`userId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='金币场-春节红包活动';
alter table tb_goldfield_redpacket add  column createTime bigint(16) not null COMMENT '' AFTER reason ;
alter table tb_goldfield_redpacket add  column amount decimal(12,2) not null COMMENT '' AFTER userId ;
