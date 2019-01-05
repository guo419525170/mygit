CREATE TABLE `tb_goldfield_new_year_activity` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
