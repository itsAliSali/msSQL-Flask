class CV:

    def __init__(self, id_, job_title, country, city, national_id,
                    birthdate, married, male, about_me ):
        self.id__ = id_
        self.job_title = job_title
        self.country = country
        self.city = city
        self.national_id = national_id
        self.birthdate = birthdate
        self.married = married
        self.male = male
        self.about_me = about_me


class City:

    def __init__(self, id_, name):
        self.id_ = id_
        self.name = name


class Technology:

    def __init__(self, id_, title):
        self.id_ = id_
        self.title = title


class Field:

    def __init__(self, id_, name):
        self.id_ = id_
        self.title = title


class Company:

    def __init__(self, id_, name, size, city_id):
        self.id_ = id_
        self.name = name
        self.size = size
        self.city_id
    

class CompanyTechnology_rel:

    def __init__(self, comp_id, tech_id):
        self.comp_id = comp_id
        self.tech_id = tech_id    


class CompanyField_rel:

    def __init__(self, comp_id, field_id):
        self.comp_id = comp_id
        self.field_id = field_id


class SiteUser:

    def __init__(self, email, password, fname, lname):
        self.email = email
        self.password = password
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f"(({self.fname}, {self.lname}, {self.password}, {self.email}))"


class Developer:

    def __init__(self, resume_id, email, comp_id):
        self.resume_id = resume_id
        self.email = email
        self.comp_id = comp_id


class Employer:

    def __init__(self, email, comp_id):
        self.email = email
        self.comp_id = comp_id


class JobOpp:

    def __init__(self, id_, title, about, reg_date, employment_form,
                    exp_level, remote_opp, salary, comp_id, city_id):
        self.id_ = id_
        self.title = title
        self.about = about
        self.reg_date = reg_date
        self.employment_form, = employment_form,
        self.exp_level = exp_level
        self.remote_opp = remote_opp
        self.salary = salary
        self.comp_id = comp_id
        self.city_id = city_id
        

class JobBenefits_mvp:

    def __init__(self, benefit, job_id):
        self.benefit = benefit
        self.job_id = job_id


class JobOppTechnology_rel:

    def __init__(self, jobopp_id, tech_id):
        self.jobopp_id = jobopp_id
        self.tech_id = tech_id


class DevJob_rel:

    def __init__(self, dev_id, job_id, application_date):
        self.dev_id = dev_id
        self.job_id = job_id
        self.application_date = application_date


class Question:

    def __init__(self, id_, title, point, content, solution):
        self.id_ = id_
        self.title = title
        self.point = point
        self.content = content
        self.solution = solution


class QueLabel_mvp:

    def __init__(self, label_name, que_id):
        self.label_name = label_name
        self.que_id = que_id


class QueGroup_mvp:

    def __init__(self, group_name, que_id):
        self.group_name = group_name
        self.que_id = que_id


class DevQuestionSubmit_rel:

    def __init__(self, dev_id, question_id, solution, mark, duration):
        self.dev_id = dev_id
        self.question_id = question_id
        self.solution = solution
        self.mark = mark
        self.duration = duration


class EduInst:

    def __init__(self, id_, name, website, inst_type, user_email, city_id):
        self.id_ = id_
        self.name = name
        self.website = website
        self.inst_type = inst_type
        self.user_email = user_email
        self.city_id = city_id


class Class:

    def __init__(self, id_, name, edu_inst_id):
        self.id_ = id_
        self.name = name
        self.edu_inst_id = edu_inst_id


class ClassArchive:

    def __init__(self, id_):
        self.id_ = id_


class Exercise:

    def __init__(self, id_, title, deadline, point, class_id):
        self.id_ = id_
        self.title = title
        self.deadline = deadline
        self.point = point
        self.class_id = class_id


class Task:

    def __init__(self, id_, title, task_explanation, solution, point, exercise_id):
        self.id_ = id_
        self.title = title
        self.task_explanation = task_explanation
        self.solution = solution
        self.point = point
        self.exercise_id = exercise_id


class DevTaskSubmit_rel:

    def __init__(self, dev_id, task_id, submit_time, solution, mark):
        self.dev_id = dev_id
        self.task_id = task_id
        self.submit_time = submit_time
        self.solution = solution
        self.mark = mark


class Competition:

    def __init__(self, id_, name, edu_inst_id, organizer, organizer_ssn,
                    organizer_email, organizer_phone, start_time, end_time, is_special):
        self.id_ = id_
        self.name = name
        self.edu_inst_id = edu_inst_id
        self.organizer = organizer
        self.organizer_ssn = organizer_ssn
        self.organizer_email = organizer_email
        self.organizer_phone = organizer_phone
        self.start_time = start_time
        self.end_time = end_time
        self.is_special = is_special


class CompetitionQuestion_rel:

    def __init__(self, que_id, comp_id):
        self.que_id = que_id
        self.comp_id = comp_id


class DevClassReg_rel:

    def __init__(self, dev_id, class_id, stu_id):
        self.dev_id = dev_id
        self.class_id = class_id
        self.stu_id = stu_id


class DevCompetition_rel:

    def __init__(self, dev_id, comp_id):
        self.dev_id = dev_id
        self.comp_id = comp_id

