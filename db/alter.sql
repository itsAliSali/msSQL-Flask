use quera_prj1
go

alter table DevClassReg_rel add role varchar(200) default 'student'
go

-- add registration date to the table SiteUser, default value is current date and time
alter table SiteUser add reg_date datetime default current_timestamp
go

-- add semester as int to Class table
alter table Class add semester int
go

-- add acceptance status bit to DevJob_rel table, default value is 0
alter table DevJob_rel add acceptance_status bit default 0
go

-- add capacity to JobOpp as int
alter table JobOpp add capacity int
go

-- add multi-valued 'Skills' attribute to CV table
create table CVSkills(
    cv_id int foreign key references CV(ID) on update cascade,
    skill varchar(200),
    primary key(cv_id, skill),
)
go
