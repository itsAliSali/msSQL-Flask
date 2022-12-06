CREATE DATABASE quera_prj1
go
USE quera_prj1
go

CREATE TABLE City(
	ID int PRIMARY KEY,
	name varchar(50)
)
go

CREATE TABLE CV (
  ID int PRIMARY KEY, 
  job_title varchar(50),
  country varchar(50),
  city_id int FOREIGN KEY REFERENCES City(ID), 
  national_id varchar(50),
  birth_date date,
  marreid bit, -- could be marital_status ENUM ('single', 'married') or boolean BUT MS SQl only has bit datatype.
  male bit, -- same as above comment.
  about_me varchar (700)
)

CREATE TABLE Technology(
	ID int PRIMARY KEY,
	title varchar(50)
)

CREATE TABLE Field(
	ID int PRIMARY KEY,
	title varchar(50)
)

CREATE TABLE Company (
	ID int PRIMARY KEY,
	name varchar(50) NOT NULL,
	size int,
	city_id int FOREIGN KEY REFERENCES City(ID) -- implementing Company-City n-1 relation.
)
go
-- implement Company-Technology n-n relation 
CREATE TABLE CompanyTechnology_rel (
	comp_id int NOT NULL FOREIGN KEY REFERENCES Company(ID),
	tech_id int NOT NULL FOREIGN KEY REFERENCES Technology(ID),
)

-- implement Company-Field n-n relation 
CREATE TABLE CompanyField_rel (
	comp_id int NOT NULL FOREIGN KEY REFERENCES Company(ID),
	field_id int NOT NULL FOREIGN KEY REFERENCES Field(ID),
)

CREATE TABLE SiteUser (
	email varchar(200) PRIMARY KEY,
	password varchar(50) NOT NULL,
	fname varchar(50) NOT NULL,
	lname varchar(50) NOT NULL
)
go

CREATE TABLE Developer (
	resume_id int FOREIGN KEY REFERENCES CV(ID) on update cascade,
	email varchar(200) PRIMARY KEY REFERENCES SiteUser(email),
	comp_id int FOREIGN KEY REFERENCES Company(ID) NULL -- implementing Dev-Comp 1-n relation.
)

CREATE TABLE Employer (
	email varchar(200) PRIMARY KEY FOREIGN KEY REFERENCES SiteUser(email),
	comp_id int NOT NULL FOREIGN KEY REFERENCES Company(ID) -- implement Company-Employer 1-n relation
)
go

CREATE TABLE JobOpp (
	ID int PRIMARY KEY,
	title varchar(50) NOT NULL,
	about varchar(500),
	reg_date datetime default GETDATE(),
	employment_form varchar(100), -- part time / full time /... (could be ENUM)
	exp_level varchar(100),
	remote_opp bit,
	salary varchar(100), -- could be ENUM (Ranges: 10M-15M, 15M-20M, ...)

	comp_id int FOREIGN KEY REFERENCES Company(ID), -- implementing the Company-JobOpp 1-n relation.
	city_id int FOREIGN KEY REFERENCES City(ID) -- implementing JobOpp-City n-1 relation.
)
go

-- multivalued properties:
CREATE TABLE JobBenefits_mvp(
	benefit varchar(100) NOT NULL,
	job_id int NOT NULL FOREIGN KEY REFERENCES JobOpp(ID)
)

-- implement JobOpp-Technology n-n relation 
CREATE TABLE JobOppTechnology_rel (
	jobopp_id int NOT NULL FOREIGN KEY REFERENCES JobOpp(ID),
	tech_id int NOT NULL FOREIGN KEY REFERENCES Technology(ID),
)

-- implementing Developer-JonOpp n-n relation
CREATE TABLE DevJob_rel(
	dev_id varchar(200) NOT NULL FOREIGN KEY REFERENCES Developer(email),
	job_id int NOT NULL FOREIGN KEY REFERENCES JobOpp(ID),
	application_date datetime NOT NULL default GETDATE()
)
go

CREATE TABLE Question(
	ID int PRIMARY KEY,
	title varchar(50) NOT NULL,
	point int,
	content varchar(200),
	solution varchar(1000),
)
go

-- multivalued properties:
CREATE TABLE QueLabel_mvp(
	label_name varchar(100) NOT NULL,
	que_id int NOT NULL FOREIGN KEY REFERENCES Question(ID)
)

CREATE TABLE QueGroup_mvp(
	group_name varchar(100) NOT NULL,
	que_id int NOT NULL FOREIGN KEY REFERENCES Question(ID)
)

-- implement Developer submitting Questions n-n relation 
CREATE TABLE DevQuestionSubmit_rel (
	dev_id varchar(200) NOT NULL FOREIGN KEY REFERENCES Developer(email),
	question_id int NOT NULL FOREIGN KEY REFERENCES Question(ID),
	solution varchar(1000),
	mark int,
	duration time,
)

CREATE TABLE EduInst (
	ID int PRIMARY KEY,
	name varchar(50) NOT NULL,
	website varchar(100),
	inst_type varchar(100), -- could be ENUM.
	user_email varchar(200) FOREIGN KEY REFERENCES SiteUser(email), -- implementing User-EduInst 1-n relation.
	city_id int FOREIGN KEY REFERENCES City(ID) -- implementing EduInst-City n-1 relation.
)
go

CREATE TABLE Class (
	ID int PRIMARY KEY,
	name varchar(50) NOT NULL,
	edu_inst_id int NOT NULL FOREIGN KEY REFERENCES EduInst(ID) --implementin Class-EduInst 1-n relation
)
go

CREATE TABLE ClassArchive (
	ID int PRIMARY KEY FOREIGN KEY REFERENCES Class(ID)
)

CREATE TABLE Exercise (
	ID int PRIMARY KEY,
	title varchar(50) NOT NULL,
	deadline datetime NOT NULL,
	point varchar(100) NOT NULL,
	class_id int NOT NULL FOREIGN KEY REFERENCES Class(ID) -- implementing Task-Class 1-n relation.
)
go

CREATE TABLE Task (
	ID int PRIMARY KEY,
	title varchar(50) NOT NULL,
	task_explanation varchar(200),
	solution varchar(500),
	point varchar(100),
	exercise_id int FOREIGN KEY REFERENCES Exercise(ID) -- implementing Exercise-Task 1-n relation.
)

-- implement Developer submitting Tasks in Class n-n relation 
CREATE TABLE DevTaskSubmit_rel (
	dev_id varchar(200) FOREIGN KEY REFERENCES Developer(email) NOT NULL,
	task_id int FOREIGN KEY REFERENCES Task(ID) NOT NULL,
	submit_time datetime default CURRENT_TIMESTAMP,
	solution varchar(1000),
	mark int
)

CREATE TABLE Competition (
	ID int PRIMARY KEY,
	name varchar(50) NOT NULL,
	edu_inst_id int FOREIGN KEY REFERENCES EduInst(ID), --implementin Competition-EduInst 1-n relation
	organizer varchar(50),
	organizer_ssn varchar(50),
	organizer_email varchar(200),
	organizer_phone varchar(50),
	start_time datetime,
	end_time datetime,
	is_special bit,
)
go

-- implement Competition-Question n-n relation
CREATE TABLE CompetitionQuestion_rel (
	que_id int FOREIGN KEY REFERENCES Question(ID),
	comp_id int FOREIGN KEY REFERENCES Competition(ID)
)

-- implement Developer enrolling in Class n-n relation 
CREATE TABLE DevClassReg_rel (
	dev_id varchar(200) FOREIGN KEY REFERENCES Developer(email) NOT NULL,
	class_id int FOREIGN KEY REFERENCES Class(ID), 
	stu_id int,
)

-- implement Developer Competing in Competition n-n relation
CREATE TABLE DevCompetition_rel (
	dev_id varchar(200) FOREIGN KEY REFERENCES Developer(email),
	comp_id int FOREIGN KEY REFERENCES Competition(ID),
)
go
