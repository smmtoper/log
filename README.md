# Logging

## Запуск

Запуск производится в "начальной" директории проекта (рядом с папкой `src`).

1. Установить зависимости:

```bash
pip install -r requirements.txt
```

2. Запустить `user_service` с помощью команды:

```bash
fastapi run src/user_service.py
```

3. Запустить `subscriber` с помощью команды:

```bash
python src/subscriber.py
```

4. Запустить `pusblisher` с помощью команды:

```bash
python src/pusblisher.py
```

## Проверка логов

Для проверки логов необходимо выполнить команду:

```bash
python src/log_checker.py
```

При проверки, в случае обнаружения ошибок, в консоль будут выводиться следующие ошибки:

- `Log order error on line N` - обнаружена ошибка в порядке записи логов в файл на строке N
- `Log format error on line N` - ошибка формата лога на строке N

## Уровень логгирования

- `DEBUG` - дебаг информация, в `publisher` - отправляемое значение, в `subscriber` - получаемое
- `INFO` - основная информация
- `WARNING` - предупреждение, в `subscriber` - когда приходит пустое сообщение
- `ERROR` - ошибка, в `publisher` и `subscriber` - когда не удалось получить `user_id`