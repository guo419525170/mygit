CREATE TABLE `tb_activity_config_copy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sort` int(11) DEFAULT NULL COMMENT '排序',
  `enabled` tinyint(2) NOT NULL DEFAULT '1' COMMENT '0无效，1有效',
  `category` tinyint(2) NOT NULL COMMENT '1活动，2公告',
  `title` varchar(64) NOT NULL COMMENT '标签',
  `type` tinyint(2) NOT NULL COMMENT '0文字，1图片，2认证有礼，3投诉建议，4开房奖元宝，5对战奖元宝',
  `content` varchar(2048) DEFAULT NULL,
  `action` tinyint(2) DEFAULT NULL COMMENT '0无，1跳转商城，2跳转网页，3分享',
  `target` varchar(2048) DEFAULT NULL,
  `extend` varchar(1024) DEFAULT NULL COMMENT '扩展参数',
  `conditions` varchar(255) DEFAULT NULL COMMENT '显示条件',
  `startTime` bigint(16) NOT NULL,
  `endTime` bigint(16) NOT NULL,
  `createTime` bigint(16) NOT NULL,
  `updateTime` bigint(16) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_start_time` (`startTime`) USING BTREE,
  KEY `index_end_time` (`endTime`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=COMPACT;
alter table tb_statistics_hour modify column online int(11) default 0 COMMENT '在线人数' AFTER '[]' ;
alter table tb_statistics_hour modify column recharge decimal(12,2) default 0.00 COMMENT '充值金额' AFTER '[]' ;
