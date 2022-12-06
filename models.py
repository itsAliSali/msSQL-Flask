import pymssql 

from entities import *


class BaseModel:
    
    connection = None
    
    @classmethod
    def set_connection(cls, database_settings):
        conn = pymssql.connect(server=database_settings['Server'],
                                user=database_settings['UID'],
                                password=database_settings['PWD'],
                                database=database_settings['Database'],
                                autocommit=True)
        # conn.autocommit(True)
        cls.connection = conn
    
    @classmethod
    def close_connection(cls):
        cls.connection.commit()
        return cls.connection.close()
    
    @classmethod
    def get_cursor(cls):
        return cls.connection.cursor()

    def find_by_id(self, id_):
        pass

    def find_by_ids(self, ids):
        pass
    
    def find_all(self):
        pass
    
    def delete_by_id(self, id_):
        pass

    def delete_by_ids(self, ids):
        pass
    
    def save(self, e):
        pass


class CVDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        id_ = result[0]
        job_title = result[1]
        country = result[2]
        city = result[3]
        national_id = result[4]
        birthdate = result[5]
        married = result[6]
        male = result[7]
        about_me = result[8]
        
        return CV(id_, job_title, country, city, national_id,
                    birthdate, married, male, about_me)

    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result) 

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e): 
        query = f"""INSERT INTO {self.table_name} (email, password, fname, lname)
                        VALUES('{e.email}', '{e.password}', '{e.fname}', '{e.lname}')"""
        cursor = BaseModel().get_cursor().execute(query)


class CityDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        id_ = result[0]
        name = result[1]
        
        return City(id_, name)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (id_, name)
                        VALUES('{e.id_}', '{e.name}')"""
        cursor = BaseModel().get_cursor().execute(query)


class TechnologyDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        id_ = result[0]
        title = result[1]
        
        return Technology(id_, title)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (id_, title)
                        VALUES('{e.id_}', '{e.title}')"""
        cursor = BaseModel().get_cursor().execute(query)


class FieldDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        id_ = result[0]
        title = result[1]
        
        return Field(id_, title)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (id_, title)
                        VALUES('{e.id_}', '{e.title}')"""
        cursor = BaseModel().get_cursor().execute(query)


class CompanyDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        id_ = result[0]
        name = result[1]
        size = result[2]
        city_id = result[3]

        return Company(id_, name, size, city_id)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (ID, name, size, city_id)
                        VALUES('{e.id_}', '{e.name}', '{e.size}', '{e.city_id}')"""
        cursor = BaseModel().get_cursor().execute(query)


class CompanyTechnology_relDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        comp_id = result[0]
        tech_id = result[1]
        
        return CompanyTechnology_rel(comp_id, tech_id)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (comp_id, tech_id)
                        VALUES('{e.comp_id}', '{e.tech_id}')"""
        cursor = BaseModel().get_cursor().execute(query)


class CompanyField_relDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        comp_id = result[0]
        field_id = result[1]
        
        return CompanyField_rel(comp_id, field_id)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (comp_id, field_id)
                        VALUES('{e.comp_id}', '{e.field_id}')"""
        cursor = BaseModel().get_cursor().execute(query)


class SiteUserDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        email = result[0]
        password = result[1]
        fname = result[2]
        lname = result[3]

        return SiteUser(email, password, fname, lname)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (email, password, fname, lname)
                        VALUES('{e.email}', '{e.password}', '{e.fname}', '{e.lname}')"""
        cursor = BaseModel().get_cursor().execute(query)


class DeveloperDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        resume_id = result[0]
        email = result[1]
        comp_id = result[1]
        
        return Developer(resume_id, email, comp_id)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (resume_id, email, comp_id)
                        VALUES('{e.resume_id}', '{e.email}', '{e.comp_id}')"""
        cursor = BaseModel().get_cursor().execute(query)


class EmployerDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        email = result[0]
        comp_id = result[1]
        
        return Employer(email, comp_id)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (email, comp_id)
                        VALUES('{e.email}', '{e.comp_id}')"""
        cursor = BaseModel().get_cursor().execute(query)


class JobOppDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        id_ = result[0]
        title = result[1]
        about = result[2]
        reg_date = result[3]
        employment_form = result[4]
        exp_level = result[5]
        remote_opp = result[6]
        salary = result[7]
        comp_id = result[8]
        city_id = result[8]
        
        return JobOpp(id_, title, about, reg_date, employment_form,
                        exp_level, remote_opp, salary, comp_id, city_id)

    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result) 

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e): 
        query = f"""INSERT INTO {self.table_name} (ID, title, about, reg_date, employment_form, exp_level, remote_opp, salary, comp_id, city_id)
                        VALUES('{e.id_}', '{e.title}', '{e.about}', '{e.reg_date}', '{e.employment_form}', '{e.exp_level}', '{e.remote_opp}', '{e.salary}', '{e.comp_id}', '{e.city_id}')"""
        print('DD: ', query)
        cursor = BaseModel().get_cursor().execute(query)


class jobBenefits_mvpDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        benefit = result[0]
        job_id = result[1]
        
        return JobBenefits_mvp(benefit, job_id)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (benefit, job_id)
                        VALUES('{e.benefit}', '{e.job_id}')"""
        cursor = BaseModel().get_cursor().execute(query)


class JobOppTechnology_relDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        jobopp_id = result[0]
        tech_id = result[1]
        
        return JobOppTechnology_rel(jobopp_id, tech_id)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (jobopp_id, tech_id)
                        VALUES('{e.jobopp_id}', '{e.tech_id}')"""
        cursor = BaseModel().get_cursor().execute(query)


class DevJob_rel(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        dev_id = result[0]
        job_id = result[1]
        application_date = result[2]

        return DevJob_rel(dev_id, job_id, size)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (dev_id, job_id, size)
                        VALUES('{e.dev_id}', '{e.job_id}', '{e.size}')"""
        cursor = BaseModel().get_cursor().execute(query)


class QuestionDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        id_ = result[0]
        title = result[1]
        point = result[2]
        content = result[3]
        solution = result[4]

        return Question(id_, title, point, content, solution)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (ID, title, point, content, solution)
                        VALUES('{e.id_}', '{e.title}', '{e.point}', '{e.content}', '{e.solution}')"""
        cursor = BaseModel().get_cursor().execute(query)


class QueLabel_mvpDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        label_name = result[0]
        que_id = result[1]
        
        return QueLabel_mvp(label_name, que_id)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (label_name, que_id)
                        VALUES('{e.label_name}', '{e.que_id}')"""
        cursor = BaseModel().get_cursor().execute(query)


class QueGroup_mvpDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        group_name = result[0]
        que_id = result[1]
        
        return QueGroup_mvp(group_name, que_id)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (group_name, que_id)
                        VALUES('{e.group_name}', '{e.que_id}')"""
        cursor = BaseModel().get_cursor().execute(query)




class DevQuestionSubmit_relDAO(BaseModel):
    
    def __init__(self, tb_name, PK):
        self.table_name = tb_name
        self.PK = PK

    def _create_entity(self, result):
        dev_id = result[0]
        question_id = result[1]
        solution = result[2]
        mark = result[3]
        duration = result[4]

        return DevQuestionSubmit_rel(dev_id, question_id, solution, mark, duration)


    def find_by_id(self, id_):
        """query by entity's PK.
            returns None if nothing was found.
            otherwise returns the first match."""

        query = f"""SELECT * FROM {self.table_name}
                        WHERE {self.PK} = '{id_}'; """
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        result = results[0]

        return self._create_entity(result)
        

    def find_by_ids(self, ids):
        user_list = []
        for id_ in ids:
            user = self.find_by_id(id_)
            user_list.append(user)
        return user_list

    def find_all(self):
        query = f"""SELECT * FROM {self.table_name};"""
        cursor = BaseModel().get_cursor().execute(query)
        results = cursor.fetchall()
        
        if len(results) == 0:
            return None

        user_list = []
        for result in results:
            user_list.append(self._create_entity(result))

        return user_list

    
    def delete_by_id(self, id_):
        stat = True
        try:
            query = f"""DELETE FROM {self.table_name}
                            WHERE {self.PK} = '{id_}'; """
            cursor = BaseModel().get_cursor().execute(query)
        except:
            print(f"delete could not be performed id_: {id_}")
            stat = False

        return stat

    def delete_by_ids(self, ids):
        stat = True
        for id_ in ids:
            stat *= self.delete_by_id(id_)
        return stat
    
    def save(self, e):
        query = f"""INSERT INTO {self.table_name} (dev_id, question_id, solution, mark, duration)
                        VALUES('{e.dev_id}', '{e.question_id}', '{e.solution}', '{e.mark}', '{e.duration}')"""
        cursor = BaseModel().get_cursor().execute(query)



