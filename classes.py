

class Character:

    def __init__(self):

        self.alive = True

        self.reserve = {

                            'health': 100,
                            'stamina': 100,
                            'concentration': 100,
        }

        self.resource = {

                            'health': self.reserve['health'],
                            'stamina': self.reserve['stamina'],
                            'concentration': self.reserve['concentration'],
        }

        self.skill = {
                            'speed': 1,
                            'strength': 1,
                            'constitution': 1,
                            'intellect': 1,
        }

        self.equipment = {

                            'weapon': ['Simple Longsword', {'thrust': 1, 'slash': 1, 'blunt': 1}],
                            'head': ['Black Hat', {'thrust': 2, 'slash': 3, 'blunt': 1}],
                            'body': ['Black Jacket', {'thrust': 2, 'slash': 2, 'blunt': 2}],
                            'arms': ['Black Gloves', {'thrust': 2, 'slash': 2, 'blunt': 1}],
                            'legs': ['Black Boots', {'thrust': 2, 'slash': 1, 'blunt': 1}],


        }

    def take_damage(self, damage):

        self.resource['health'] -= damage
        if self.resource['health'] <= 0:
            self.alive = False

    def deal_damage(self):

        return self.equipment['weapon'][1]['thrust'] * (0.05 * self.skill['strength']), \
               self.equipment['weapon'][1]['slash'] * (0.04 * self.skill['slash']), \
               self.equipment['weapon'][1]['blunt'] * (0.04 * self.skill['blunt'])

    def add_skill_level(self, skill):
        self.skill[skill] += 1

    def put_on(self, item):
        """ ('type', 'name', {'thrust': value, 'slash': value, 'blunt': value}) """

        self.equipment[item[0]] = [item[1], item[2]]

    def __str__(self):
        return 'hero'


class Fight:

    def __init__(self, hero, enemy):
        from random import choice

        self.position = [
            'High', 'Vom Tag Left', 'Vom Tag Right', 'Ochs Left', 'Ochs Right',
            'Long', 'Alber Left', 'Alber Right', 'Plug Left', 'Plug Right']
        self.hero = hero
        self.hero_position = choice(self.position)
        self.enemy = enemy
        self.enemy_position = choice(self.position)

    def menu(self):
        pass

    def change_position(self, character, new_position):
        if character == 'hero':
            self.hero_position = new_position

        elif character == 'enemy':
            self.enemy_position = new_position

        else:
            print('ChangePositionError: unknown character. ')

    @staticmethod
    def change_position_logic(position):

        if position == 'Long':
            return 'High', 'Vom Tag Left', 'Vom Tag Right', 'Ochs Left', 'Ochs Right', 'Alber Left', 'Alber Right'

        elif position == 'High':
            return 'Vom Tag Left', 'Vom Tag Right', 'Ochs Left', 'Ochs Right', 'Long'

        elif position == 'Vom Tag Left':
            return 'High', 'Long', 'Plug Left'

        elif position == 'Vom Tag Right':
            return 'High', 'Long', 'Plug Right'

        elif position in ['Ochs Left', 'Ochs Right']:
            return 'High', 'Long'

        elif position == 'Alber Left':
            return 'Long', 'Plug Left'

        elif position == 'Alber Right':
            return 'Long', 'Plug Right'

        elif position == 'Plug Left':
            return 'Vom Tag Left', 'Alber Left'

        elif position == 'Plug Right':
            return 'Vom Tag Right', 'Alber Right'

        else:
            print('ChangePositionLogicError: unknown position. ')

    @staticmethod
    def change_position_accept(position):

        accepted_positions = Fight.change_position_logic(position)
        count = 0
        for i in accepted_positions:
            count += 1
            print(f'{count}: {i}')
        return accepted_positions

