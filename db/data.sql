use quera_prj1
go

insert into City(ID, name)
values (0, 'Tehran'), (1, 'Shiraz'), (2, 'Mashhad'),
(3, 'Semnan'), (4, 'Esfahan'), (5, 'Tabriz');
go

insert into SiteUser(email, password, fname, lname)
values ('aaa111@g.com', '123456', 'Ali', 'Bagheri'),
('bbb222@g.com', '123456', 'Yahya', 'Maleki'),
('ccc333@g.com', '123456', 'Morteza', 'Molae'),
('ddd444@g.com', '123465', 'Saeed', 'Hejazi'),
('eee555@g.com', '123456', 'Yekta', 'Rahnama'),
('ZRa@g.com', '123456', 'Zohreh', 'Rasouli');

insert into Developer(email)
values ('aaa111@g.com'),
('bbb222@g.com'),
('ccc333@g.com'),
('ddd444@g.com'),
('eee555@g.com'),
('ZRa@g.com');

insert into EduInst (ID, name, website)
values (0, 'KNTU', 'kntu.ac.ir'),
(1, 'Digikala', 'digikala.com'),
(2, 'Quera', 'quera.ir'),
(3, 'AmirKabir', 'aut.ac.ir');
go

insert into Class(ID, name, edu_inst_id, semester)
values (0, 'Alg-401', 0, 3991),
(1, 'Alg-402', 0, 3992),
(2, 'Alg-403', 0, 4001),
(3, 'Alg-404', 0, 4001),
(4, 'Alg-405', 0, 4002),
(5, 'Alg-406', 3, 4002),
(6, 'Alg-407', 1, 4003),
(7, 'DB-401', 3, 3991);
go

insert into ClassArchive(ID)
values (0), (1), (2), (3), (7);

insert into DevClassReg_rel(dev_id, class_id, stu_id)
values ('aaa111@g.com', 0, 9821111),
('bbb222@g.com', 0, 9821222),
('aaa111@g.com', 1, 9821111),
('bbb222@g.com', 2, 9821222),
('ccc333@g.com', 3, 9821333),
('ddd444@g.com', 4, 9821444),
('eee555@g.com', 5, 9821555),
('aaa111@g.com', 6, 9821111),
('bbb222@g.com', 6, 9821222),
('ccc333@g.com', 6, 9821333),
('ddd444@g.com', 6, 9821444),
('eee555@g.com', 7, 9821555);
go

insert into DevClassReg_rel(dev_id, class_id, role)
values ('ZRa@g.com', 6, 'Lecturer'),
('ZRa@g.com', 2, 'Lecturer');

insert into Exercise(ID, title, deadline, point, class_id)
values (0, 'HW1', '20220617 23:55 PM', 100, 0),
(1, 'Exercise 1', dateadd(hour, 6, getdate()), 50, 6),
(2, 'Exercise 2', dateadd(day, 3, getdate()), 100, 6);
go

insert into Competition (ID, name, edu_inst_id, is_special)
values (0, 'Best Competition', 1, 1),
(1, 'Doroogh 13', 2, 0);

insert into Question(ID, title, point)
values (20, 'DB-01', 50),
(21, 'DB-02', 25),
(22, 'DB-03', 35),
(23, 'DB-04', 15),
(24, 'DB-05', 45),
(25, 'DB-06', 30),
(26, 'DB-07', 55),
(27, 'DB-08', 40),
(28, 'DB-09', 60),
(29, 'DB-10', 65);
go

insert into QueLabel_mvp(label_name, que_id)
values ('Olympiad', 20),
('Olympiad', 21),
('Olympiad', 22),
('Olympiad', 23),
('Technology', 24),
('Contest', 25),
('University', 26),
('University', 27),
('Technology', 28),
('Contest', 29);

insert into CompetitionQuestion_rel(que_id, comp_id)
values (20, 1),
(21, 1),
(22, 1),
(23, 1),
(24, 1),
(25, 1);
go

insert into DevCompetition_rel(dev_id, comp_id)
values ('aaa111@g.com', 1),
('bbb222@g.com', 1);
go

insert into DevQuestionSubmit_rel(dev_id, question_id, mark)
values ('aaa111@g.com', 20, 30),
('aaa111@g.com', 21, 20),
('aaa111@g.com', 22, 35),
('aaa111@g.com', 23, 15),
('bbb222@g.com', 20, 50),
('bbb222@g.com', 23, 15),
('ccc333@g.com', 25, 25),
('ccc333@g.com', 27, 40),
('ccc333@g.com', 28, 58);

insert into Company(ID, name, size, city_id)
values (0, 'Hamrah Aval', 12000, 0),
(1, 'Irancell', 11000, 0),
(2, 'Sheed Group', 100, 3),
(3, 'Komoda', 200, 1),
(4, 'Beh Ara', 3000, 2);
go

insert into JobOpp(ID, title, reg_date, comp_id)
values (0, 'ML Dev', '2020-01-02', 0),
(1, 'Teacher', '2020-09-03', 0),
(2, 'CFO', '2020-11-04', 3),
(3, 'Pilot', '2022-01-05', 1),
(4, 'Software Engineer', '2023-01-06', 0);
go

