import random


class Worker:

    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary

    def perform_job(self):
        bonus = random.randint(10, 50)
        total_earned = self.salary + bonus
        print(f"Персонаж працює як {self.job_title} та заробляє ${total_earned} (включаючи бонус ${bonus}).")
        return total_earned


class HomeOwner:

    def __init__(self, house_type):
        self.house_type = house_type
        self.comfort_level = 50

    def clean_house(self):
        self.comfort_level = min(100, self.comfort_level + 20)
        print(f"Персонаж прибирає свій {self.house_type}. Рівень затишку піднявся до {self.comfort_level}.")


class SimCharacter(Worker, HomeOwner):

    def __init__(self, name, job_title, salary, house_type):
        Worker.__init__(self, job_title, salary)
        HomeOwner.__init__(self, house_type)
        self.name = name
        self.money = 100

    def live_day(self, day_number):
        print(f"--- День {day_number} для персонажа {self.name} ---")
        earned = self.perform_job()
        self.money += earned
        self.clean_house()
        print(f"Баланс на кінець дня: ${self.money}. Затишок вдома: {self.comfort_level}.\n")


if __name__ == "__main__":
    character = SimCharacter(name="Олексій", job_title="Програміст", salary=150, house_type="Котедж")

    for day in range(1, 68):
        character.live_day(day)
