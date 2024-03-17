import random

class Soldier:
    def __init__(self, unique_number, team):
        self.unique_number = unique_number
        self.team = team
        
    def follow_hero(self, hero):
        print(f"Солдат {self.unique_number} теперь следует за героем {hero.unique_number}.")

class Hero:
    def __init__(self, unique_number, team, level=1):
        self.unique_number = unique_number
        self.team = team
        self.level = level
        
    def increase_level(self):
        self.level += 1

team1_hero = Hero(unique_number=1, team='Команда 1')
team2_hero = Hero(unique_number=2, team='Команда 2')

team1_soldiers = []
team2_soldiers = []

num_soldiers = 10

for _ in range(num_soldiers):
    random_team = random.choice(['Команда 1', 'Команда 2'])
    if random_team == 'Команда 1':
        team1_soldiers.append(Soldier(unique_number=random.randint(100, 999), team=random_team))
    else:
        team2_soldiers.append(Soldier(unique_number=random.randint(100, 999), team=random_team))

print(f"Количество солдат в Команде 1: {len(team1_soldiers)}")
print(f"Количество солдат в Команде 2: {len(team2_soldiers)}")

if len(team1_soldiers) > len(team2_soldiers):
    team1_hero.increase_level()
    soldier_to_follow = team1_soldiers[0]
    soldier_to_follow.follow_hero(team1_hero)

print(f"Герой {team1_hero.unique_number} - Уровень: {team1_hero.level}")
print(f"Герой {team2_hero.unique_number} - Уровень: {team2_hero.level}")
