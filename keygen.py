#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
import zxcvbn
import math
import random
import json


def entropy(password):
    symbols = set(password)
    password_length = len(password)

    entropy = 0
    for symbol in symbols:
        symbol_probability = password.count(symbol) / password_length
        if symbol_probability > 0:
            entropy -= symbol_probability * math.log2(symbol_probability)

    return entropy


def judge_password(password):
    result = zxcvbn.zxcvbn(password)
    print("\nСтойкость пароля:", result["guesses_log10"])
    print(f'Entropy: {entropy(password)}')
    print("Время взлома:", result["crack_times_display"]
          ["offline_slow_hashing_1e4_per_second"])
    print("Оценка сложности (0-4):", result["score"])
    print("Подробности:")
    for pattern in result["sequence"]:
        print("-", pattern["pattern"])
    print("Рекомендации:")
    if result["feedback"]["suggestions"] != []:
        print('- '+'\n- '.join(result["feedback"]["suggestions"]))
    else:
        print('- Нет рекомендаций')


def judge_csv_passwords(csv_file):
    output_file = csv_file[:-4] + "_judge.csv"
    with open(csv_file, 'r') as file, open(output_file, 'w', newline='') as output:
        csv_reader = csv.reader(file)
        csv_writer = csv.writer(output)
        csv_writer.writerow(["Password", "Guesses Log10",
                            "Crack Time", "Score", "Patterns", "Suggestions"])
        for row in csv_reader:
            password = row[0]
            result = zxcvbn.zxcvbn(password)
            csv_writer.writerow([password, result["guesses_log10"], result["crack_times_display"]["offline_slow_hashing_1e4_per_second"], result["score"], "; ".join(
                pattern["pattern"] for pattern in result["sequence"]), "; ".join(result["feedback"]["suggestions"])])


def keygen(n, judge):
    with open('/usr/local/bin/say.en.json', 'r', encoding='utf-8') as f:
        say_en = json.load(f)
    with open('/usr/local/bin/say.ru.json', 'r', encoding='utf-8') as f:
        say_ru = json.load(f)

    things = ['BA', 'BE', 'BI', 'BO', 'BU', 'BY', 'DA', 'DE', 'DI', 'DO', 'DU', 'DY', 'FA', 'FE', 'FI', 'FO', 'FU', 'FY', 'GA', 'GE', 'GI', 'GO', 'GU', 'GY', 'HA', 'HE', 'HI', 'HO', 'HU', 'HY', 'JA', 'JE', 'JI', 'JO', 'JU', 'JY', 'KA', 'KE', 'KI', 'KO', 'KU', 'KY', 'LA', 'LE', 'LI', 'LO', 'LU', 'LY', 'MA', 'ME', 'MI', 'MO', 'MU', 'MY', 'NA', 'NE', 'NI', 'NO', 'NU', 'NY', 'PA', 'PE', 'PI', 'PO', 'PU', 'PY', 'RA',
              'RE', 'RI', 'RO', 'RU', 'RY', 'SA', 'SE', 'SI', 'SO', 'SU', 'SY', 'TA', 'TE', 'TI', 'TO', 'TU', 'TY', 'VA', 'VE', 'VI', 'VO', 'VU', 'VY', 'BRA', 'BRE', 'BRI', 'BRO', 'BRU', 'BRY', 'DRA', 'DRE', 'DRI', 'DRO', 'DRU', 'DRY', 'FRA', 'FRE', 'FRI', 'FRO', 'FRU', 'FRY', 'GRA', 'GRE', 'GRI', 'GRO', 'GRU', 'GRY', 'PRA', 'PRE', 'PRI', 'PRO', 'PRU', 'PRY', 'STA', 'STE', 'STI', 'STO', 'STU', 'STY', 'TRA', 'TRE',]

    used_things = []

    for _ in range(n):
        element = random.choice(things)
        while element in used_things:
            element = random.choice(things)

        used_things.append(element)

    pronounce_eng = []
    pronounce_rus = []

    for thing in used_things:
        pronounce_eng.append(say_en[thing])
        pronounce_rus.append(say_ru[thing])

    if judge:
        judge_password(''.join(used_things))

    return ''.join(used_things), used_things, pronounce_eng, pronounce_rus


def main():
    if len(sys.argv) < 3:
        print("Использование:")
        print("- Утилита для генерации запоминающихся надёжных паролей:")
        print("\tkeyjudge generate [n]")
        print("\n- Утилита для оценки надежности паролей:")
        print("\tkeyjudge judge [password]")
        print("\n- Утилита для оценки паролей из CSV файла:")
        print("\tkeyjudge csv [passwords.csv]")
        return

    command = sys.argv[1]
    if command == "judge":
        password = sys.argv[2]
        judge_password(password)

    elif command == "csv":
        csv_file = sys.argv[2]
        try:
            judge_csv_passwords(csv_file)
        except FileNotFoundError:
            print(f'No such file: {csv_file}')

    elif command == "generate":
        n = int(sys.argv[2])
        generated_password, _, pron_en, pron_ru = keygen(n, judge=False)
        print(f'Сгенерированный пароль: {generated_password}')
        print(f'\nСпособы его запомнить:')
        print('На английском:', *pron_en)
        print('На русском:', *pron_ru)
        judge_password(generated_password)

    else:
        print("Неправильная команда. Используйте 'generate', 'judge' или 'csv'.")


if __name__ == "__main__":
    main()
