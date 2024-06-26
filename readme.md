# Hash Finder

Программа создает .txt файлы со случайным содержимым, чтобы найти хеши SHA-1 с последними двумя цифрами (1 байт), соответствующими заданным пользователем символам в кодировке Win-1251. Эти символы пользователь вводит в начале работы программы, и их коды сохраняются в виде файлов в папке "matches".

## Описание

Скрипт генерирует случайные символы, сохраняет их в .txt файлы и вычисляет SHA-1 хеш содержимого файла. Если последние две цифры хеша (1 байт) соответствуют коду заданных пользователем символов в Win-1251, файл сохраняется в папке "matches".

**Эти файлы можно использовать для создания задания на стеганографию, где по последним байтам файлов можно сложить скрытый текст.**

## Использование

1. Запустите скрипт:

    ```bash
    python hash_finder.py
    ```

2. Введите требуемые символы из кодировки windows-1251, когда будет предложено.

## Пример

```bash
Enter the required unique characters from win-1251: Ря
```

## Результат работы, проверка хешей

![Демонстрация работы программы](./Demo.png)
