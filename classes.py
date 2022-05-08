

class SQL:

    @classmethod
    def do(cls):

        import sqlite3

        return sqlite3.connect('database.db')


class NewItem:

    @classmethod
    def do(cls, n):
        db = SQL.do()
        sql = db.cursor()
        sql.execute(n)
        db.commit()


class SqlPlayerGeneration:

    @classmethod
    def do(cls):
        db = SQL.do()
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS player(
        player_id INT PRIMARY KEY,
        name VARCHAR,
        pass VARCHAR,
        character_id INT,
        equipment_id INT,
        status_id INT,
        skills_id INT
        );""")
        db.commit()


class SqlStatusGeneration:

    @classmethod
    def do(cls):
        db = SQL.do()
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS status(
        status_id INT PRIMARY KEY, 
        health INT,
        max_health INT,
        stamina INT,
        max_stamina INT,
        mana INT,
        max_mana INT,
        speed INT,
        
        );""")
        db.commit()


class SqlSkillsGeneration:
    @classmethod
    def do(cls):
        db = SQL.do()
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS skills(
        
        skills_id INT PRIMARY KEY,
        
        swords INT,
        axes INT,
        spears INT,
        hummers INT,
        
        athletics INT,
        analysis INT,
        survival INT,
        magic INT,
        medicine INT,
        stealth Int
        
        );""")
        db.commit()


class SqlCharacterGeneration:
    @classmethod
    def do(cls):
        db = SQL.do()
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS character(
        character_id INT PRIMARY KEY,
        strength INT,
        dexterity INT,
        intellect INT,
        constitution INT,
        will INT
        );""")
        db.commit()


class SqlEquipmentGeneration:
    @classmethod
    def do(cls):
        db = SQL.do()
        sql = db.cursor()
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
        db.commit()


class SqlCurrentItemGeneration:
    @classmethod
    def do(cls):
        db = SQL.do()
        sql = db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS current_item(
        
        item_id INT,
        item_type VARCHAR,
        
        
        thrust_blunting_damage INT,
        thrust_piercing_damage INT,
        thrust_slashing_damage INT,
        thrust_mental_damage INT,
        
        slash_blunting_damage INT,
        slash_piercing_damage INT,
        slash_slashing_damage INT,
        slash_mental_damage INT,
        
        pierce_blunting_damage INT,
        pierce_piercing_damage INT,
        pierce_slashing_damage INT,
        pierce_mental_damage INT,
        
        
        blunting_protection INT,
        piercing_protection INT,
        slashing_protection INT,
        mental_protection INT,
        
        effect_id INT,
        
        durability INT,
        weight INT
        
        );""")
        db.commit()

