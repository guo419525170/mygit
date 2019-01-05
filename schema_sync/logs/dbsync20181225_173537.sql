alter table tb_club modify column avatar varchar(256) not null COMMENT '' AFTER status ;
alter table tb_club modify column admins varchar(256) not null default [] COMMENT '管理员列表' AFTER creator ;
