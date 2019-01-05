CREATE TABLE `tb_club_robot` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` tinyint(2) NOT NULL COMMENT '1闲聊',
  `clubId` int(11) NOT NULL COMMENT '俱乐部ID',
  `groupId` varchar(32) NOT NULL COMMENT '群ID',
  `createTime` bigint(16) NOT NULL,
  `updateTime` bigint(16) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_clubid_groupid` (`clubId`,`groupId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
