

class NewItem:

    @classmethod
    def do(cls):
        sql = SQL.do()
        pass


class SqlPlayerGeneration:

    @classmethod
    def do(cls):
        sql = SQL.do()
        sql.execute("""CREATE TABLE IF NOT EXISTS player(
        player_id INT PRIMARY KEY,
        name VARCHAR,
        pass VARCHAR,
        character_id INT,
        equipment_id INT,
        status_id INT,
        skills_id INT
        );""")


class SqlStatusGeneration:

    @classmethod
    def do(cls):
        sql = SQL.do()
        sql.execute("""CREATE TABLE IF NOT EXISTS status(
        status_id INT PRIMARY KEY, 
        health INT,
        max_health INT,
        stamina INT,
        max_stamina INT,
        mana INT,
        max_mana INT
        );""")


class SqlSkillsGeneration:
    @classmethod
    def do(cls):
        sql = SQL.do()
        sql.execute("""CREATE TABLE IF NOT EXISTS skills(
        skills_id INT PRIMARY KEY,
        
        );""")


class SqlCharacterGeneration:
    @classmethod
    def do(cls):
        sql = SQL.do()
        sql.execute("""CREATE TABLE IF NOT EXISTS character(
        character_id INT PRIMARY KEY,
        strength INT,
        dexterity INT,
        intellect INT,
        constitution INT,
        will INT
        );""")


class SqlEquipmentGeneration:
    @classmethod
    sql = SQL.do()
    sql.execute("""CREATE TABLE IF NOT EXISTS equipment(
    
    equipment_id INT,
    
    head INT,
    body INT,
    arms INT,
    legs INT,
    
    first_weapon INT,
    second_weapon INT,
    
    first_artifact INT,
    second_artifact INT,
    third_artefact INT
    );""")


class SQL:

    @classmethod
    def do(cls):

        import sqlite3

        db = sqlite3.connect('database.db')
        return db.cursor()



