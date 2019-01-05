CREATE TABLE `tb_user_present_reason` (
  `id` bigint(16) NOT NULL AUTO_INCREMENT,
  `giveReasonType` varchar(255) NOT NULL COMMENT '赠送类别',
  `type` tinyint(4) NOT NULL COMMENT '类型：1元宝,3金币',
  `amountUp` bigint(16) NOT NULL COMMENT '赠送数量上限',
  `amountDown` bigint(16) NOT NULL COMMENT '赠送数量下限',
  `limit` bigint(16) DEFAULT NULL COMMENT '限制次数',
  `createTime` bigint(16) NOT NULL,
  `updateTime` bigint(16) DEFAULT NULL,
  `state` tinyint(4) NOT NULL DEFAULT '1' COMMENT '0无效 1有效',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='赠送原因类型数量';
