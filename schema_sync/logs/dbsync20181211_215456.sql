SET @START_TIME = UNIX_TIMESTAMP('2015-12-14')*1000;
SET @END_TIME = UNIX_TIMESTAMP('2018-12-15')*1000 - 1;
SELECT 
FROM_UNIXTIME(createTime/1000,'%Y-%m-%d')日期,
SUM(amount)金额 
FROM 
tb_user_recharge 
WHERE
 createTime BETWEEN @START_TIME AND @END_TIME
GROUP BY 日期;
