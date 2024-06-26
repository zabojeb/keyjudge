![KeyJudge](banner.png)

KeyJudge - это утилита командной строки, разработанная для оценки стойкости паролей и генерации надежных паролей на основе собственного алгоритма.

> [!WARNING] 
> Никому не говорите, что вы используете keyjudge! Эта информация может угрожать безопасности ваших паролей!
### Возможности

- Оценка стойкости паролей с помощью zxcvbn и Min-Entropy
- Генерация легкозапоминающихся произносимых паролей без потери надёжности на основе собственного алгоритма
- Оценка паролей из csv файла
  
### Установка

1. **Перемещение исполняемого файла и JSON файлов:**
   Исполняемый файл был перенесен в директорию `/usr/local/bin/`, что обеспечивает доступ к утилите из любой точки системы. JSON файлы были также перенесены в эту директорию (хотя их расположение не обязательно), и их путь был изменен в коде утилиты.

2. **Настройка переменной PATH:**
   Для того, чтобы утилита была доступна для запуска из любой директории, была добавлена строка в файл `~/.bashrc`:
   ```bash
   export PATH="/usr/local/bin:$PATH"
   ```
   
3. После этого изменения нужно выполнить команду чтобы изменения вступили в силу:
   ```bash
   source ~/.bashrc
   ```

В качестве альтернативного пути установки вы можете настроить alias на keyjudge в вашем .bashrc файле.

### Использование

KeyJudge предоставляет несколько команд для оценки стойкости паролей и их генерации.

**Оценка стойкости пароля:**
```bash
keyjudge judge [password]
```
Где `[password]` - оцениваемый пароль.


**Оценка стойкости паролей из CSV файла:**
```bash
keyjudge csv [passwords.csv]
```
Где `[passwords.csv]` - путь к файлу CSV с оцениваемыми паролями.


**Генерация надежного пароля:**
```bash
keyjudge generate [n]
```
Где `[n]` - количество слогов для генерации пароля.

### Пример

```bash
keyjudge judge password123
```
Результат: Password123: 1/4 (Слабый)

```bash
keyjudge csv passwords.csv
```
Результат:
```
Password1: 0/4 (Очень слабый)
CorrectHorseBatteryStaple: 4/4 (Сильный)
123456: 0/4 (Очень слабый)
a6#hcZ91L: 2/4 (Слабый)
```

```bash
keyjudge generate 6
```
Результат: TREKONMALUTRAGEN: 4/4 (Сильный)

### Вопросы и обратная связь

Если у вас возникли вопросы или предложения по улучшению утилиты, пожалуйста, создайте Issue в этом репозитории!

### Лицензия

Этот проект лицензирован в соответствии с [MIT License](LICENSE).

---
Создано в ходе ВСОШ по Информационной Безопасности

Автор: **Ярослав Воропаев**
