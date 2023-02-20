import file_operations
import random
from faker import Faker

skills = [
    'Стремительный прыжок',
    'Электрический выстрел',
    'Ледяной удар',
    'Стремительный удар',
    'Кислотный взгляд',
    'Тайный побег',
    'Ледяной выстрел',
    'Огненный заряд'
]

runic_alphabet = {
    'а': 'а͠',
    'б': 'б̋',
    'в': 'в͒͠',
    'г': 'г͒͠',
    'д': 'д̋',
    'е': 'е͠',
    'ё': 'ё͒͠',
    'ж': 'ж͒',
    'з': 'з̋̋͠',
    'и': 'и',
    'й': 'й͒͠',
    'к': 'к̋̋',
    'л': 'л̋͠',
    'м': 'м͒͠',
    'н': 'н͒',
    'о': 'о̋',
    'п': 'п̋͠',
    'р': 'р̋͠',
    'с': 'с͒',
    'т': 'т͒',
    'у': 'у͒͠',
    'ф': 'ф̋̋͠',
    'х': 'х͒͠',
    'ц': 'ц̋',
    'ч': 'ч̋͠',
    'ш': 'ш͒͠',
    'щ': 'щ̋',
    'ъ': 'ъ̋͠',
    'ы': 'ы̋͠',
    'ь': 'ь̋',
    'э': 'э͒͠͠',
    'ю': 'ю̋͠',
    'я': 'я̋',
    'А': 'А͠',
    'Б': 'Б̋',
    'В': 'В͒͠',
    'Г': 'Г͒͠',
    'Д': 'Д̋',
    'Е': 'Е',
    'Ё': 'Ё͒͠',
    'Ж': 'Ж͒',
    'З': 'З̋̋͠',
    'И': 'И',
    'Й': 'Й͒͠',
    'К': 'К̋̋',
    'Л': 'Л̋͠',
    'М': 'М͒͠',
    'Н': 'Н͒',
    'О': 'О̋',
    'П': 'П̋͠',
    'Р': 'Р̋͠',
    'С': 'С͒',
    'Т': 'Т͒',
    'У': 'У͒͠',
    'Ф': 'Ф̋̋͠',
    'Х': 'Х͒͠',
    'Ц': 'Ц̋',
    'Ч': 'Ч̋͠',
    'Ш': 'Ш͒͠',
    'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠',
    'Ы': 'Ы̋͠',
    'Ь': 'Ь̋',
    'Э': 'Э͒͠͠',
    'Ю': 'Ю̋͠',
    'Я': 'Я̋',
    ' ': ' '
}

fake = Faker('ru_Ru')


def runic(word, alphabet) -> str:
    """

    :param word: - получаем строку для обработки
    :param alphabet:- получаем символы для замены
    :return: - возвращаем измененную строку
    """
    new = ''.join([alphabet[char] for char in word])
    return new


def main() -> None:
    """

    Создаем карточку.
    Генерируем имя, фамилию, город,
    работу, статы и скилы.
    Получившийся результат записываем
    в папку Cards и создаем 10 карточек.
    :return:
    """

    for i in range(1, 11):
        character = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'town': fake.city(),
            'job': fake.job(),
            'strength': random.randint(8, 14),
            'agility': random.randint(8, 14),
            'endurance': random.randint(8, 14),
            'luck': random.randint(8, 14),
            'intelligence': random.randint(8, 14),
            'skill_1': runic(random.choice(skills), runic_alphabet),
            'skill_2': runic(random.choice(skills), runic_alphabet),
            'skill_3': runic(random.choice(skills), runic_alphabet)
        }

        file_operations.render_template('src/charsheet.svg', f'cards/result{i}.svg', character)


if __name__ == '__main__':
    main()
