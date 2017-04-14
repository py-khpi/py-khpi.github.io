**Проектування серверних додатків**

## &lt;Aim&gt;<br /> Мета

- **Вивчити** основи мови програмування [Python](https://ru.wikipedia.org/wiki/Python).
- **Ознайомитись** з [серверним програмуванням](https://en.wikipedia.org/wiki/Server-side_scripting).
- **Отримати** навички розробки програм з використанням принципів архітектури [клієнт-сервер](https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B8%D0%B5%D0%BD%D1%82-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80).

---

## &lt;Tools&gt;<br /> Програмні засоби та інструменти

1. [Python](https://www.python.org/downloads/) - у комплекті надається інтегроване середовище розробки.

2. [Simple Python style checker](https://github.com/pycqa/pep8) - перевірка початкового кода на відповідність [PEP 8](http://www.python.org/dev/peps/pep-0008).

3. [Doxygen](http://www.stack.nl/~dimitri/doxygen/download.html) <span id="doxy"></span> - система документування початкового коду. Додатково встановити:
	- [Graphviz](http://www.graphviz.org/Download.php) - Graph Visualization Software;
	- [Mscgen](http://www.mcternan.me.uk/mscgen/) - Message Sequence Chart Renderer.

---

## &lt;Guidelines&gt;<br /> Рекомендації

1. **Використовувати:**
	- [Style Guide](https://www.python.org/dev/peps/pep-0008).
	- [Викиучебник](https://ru.wikibooks.org/wiki/Python).
	- [Python Documentation](https://docs.python.org/3).
		- [Tutorial](https://docs.python.org/3/tutorial).
		- [Language Reference](https://docs.python.org/3/reference).
		- [Library Reference](https://docs.python.org/3/library).

2. **Ознайомитись:**
	- [What’s New in Python](https://docs.python.org/3/whatsnew).
	- [Python HOWTOs](https://docs.python.org/3/howto).
	- [Best practices for writing Python code](http://docs.python-guide.org/en/latest).
	- [Code Like a Pythonista](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html) ([переклад рос.](https://habrahabr.ru/post/88972/)).
	- [Python Tips, Tricks, and Hacks](http://www.siafoo.net/article/52) ([переклад рос.](http://habrahabr.ru/post/85238/), [pdf](http://idzaaus.org/static/files/articles/Python_Tips,_Tricks,_and%20Hacks_\(rus\).pdf)).

---

## &lt;Practice&gt;<br /> Лабораторні роботи

|  №  | Тема |
|:---:|:-----|
|  1  | [Основы языка Python](https://py-khpi.github.io/!nfo/doc/lab/LAB1/lab.htm) |
|  2  | [Модули. Строки](https://py-khpi.github.io/!nfo/doc/lab/LAB2/lab.htm) |
|  3  | [ABC-классы. Списки](https://py-khpi.github.io/!nfo/doc/lab/LAB3/lab.htm) |
|  4  | [Кортежи. Диапазоны. Двоичные последовательности](https://py-khpi.github.io/!nfo/doc/lab/LAB4/lab.htm) |
|  5  | [Множества. Словари. Генераторы](https://py-khpi.github.io/!nfo/doc/lab/LAB5/lab.htm) |
|  6  | [Разработка функций и модулей пользователя](https://py-khpi.github.io/!nfo/doc/lab/LAB6/lab.htm) |
|  7  | [Разработка CGI скриптов на языке Python](https://py-khpi.github.io/!nfo/doc/lab/LAB7/lab.htm) |
|  8  | [Работа с файлами на языке Python](https://py-khpi.github.io/!nfo/doc/lab/LAB8/lab.htm) |
|  9  | [Регулярные выражения](https://py-khpi.github.io/!nfo/doc/lab/LAB9/lab.htm) |
| 10  | [Использование технологии AJAX при разработке клиент-серверного приложения](https://py-khpi.github.io/!nfo/doc/lab/LAB10/lab.htm) |
| 11  | [Создание пользовательских классов](https://py-khpi.github.io/!nfo/doc/lab/LAB11/lab.htm) |
| 12  | [Наследование классов](https://py-khpi.github.io/!nfo/doc/lab/LAB12/lab.htm) |
| 13  | [Разработка графического интерфейса](https://py-khpi.github.io/!nfo/doc/lab/LAB13/lab.htm) |

### &lt;Tasks&gt;<br /> Спільні завдання

|  №  | Завдання |
|:---:|:---------|
|  1  | Розробити програму для рішення індивідуального завдання |
|  2  | Виконати [рефакторинґ](https://refactoring.guru/) з урахуванням загальних вимог |
|  3  | Підготувати до перевірки опис розробленої програми у вигляді звіту |
|  4  | Виправити програму з урахуванням отриманих зауважень |

### &lt;Requirements&gt;<br /> Вимоги

1. **Проекти** розміщувати в директоріях **surname/src/surnameXX**, де:
	- *surname* - назва особистої директорії;
	- *XX* - номер роботи.

2. **Звіти** розташовувати в директоріях **surname/doc/surnameXX**.

3. **Назву** особистої директорії *surname* з відповідним номером роботи *XX* використовувати для іменування директорій *рішен*, *проектів* і *звітів* лабораторних робіт. Наприклад:
	- студент з особистим каталогом **shevchenko**
	- для проектів двох лабораторних робіт використовує наступні шляхи і назви файлів:
	```
shevchenko/src/shevchenko01/shevchenko01.py
shevchenko/src/shevchenko02/shevchenko02.py
	```
	- для звітів:
	```
shevchenko/doc/shevchenko01/shevchenko01.odt
shevchenko/doc/shevchenko01/shevchenko01.pdf
shevchenko/doc/shevchenko02/shevchenko02.odt
shevchenko/doc/shevchenko02/shevchenko02.pdf
	```

4. **Дотримуватися** принципів, що виводяться інтерпретатором *Python* по команді `import this`.

5. **Коментувати** текст програми для обробки пакетом [Doxygen](#doxy).

---

## &lt;Report&gt;<br /> Звіт

1. **Оформляється** українською мовою та надається у форматі [Markdown](https://ru.wikipedia.org/wiki/Markdown), або у вигляді електронних документів:
	- що редагується - *odt/docx/doc/html*,
	- та що зручно проглядається - *pdf/djvu*.

2. **Формат** документа, що друкується:
	- A4 з полями: **2.5 см** зліва, **2 см** праворуч, **2 см** зверху, **2 см** знизу;
	- гарнітура: **Times New Roman**; кегль: **14**; міжрядковий інтервал: **одинарний**;
	- відступ першого рядка абзацу: **1.25 см**; вирівнювання: **у ширину**;

3. **Структура** звіту:

| Обов'язковий розділ | Зауваження |
|:--------------------|:-----------|
| **X. Тема** | Номер і тема роботи. Відповідає меті та завданню |
| **Мета: ...** | Перелік напрямків і галузей для дослідження. Відповідає темі та завданню |
| **1 ІНДИВІДУАЛЬНЕ ЗАВДАННЯ** | Повне формулювання завдання. Відповідає темі та меті |
| **&nbsp;&nbsp;&nbsp;1.1 Розробник** | Інформація про розробника: чи є студентом, прізвище, ім'я, по батькові; назва академічної групи; номер варіанту |
| **&nbsp;&nbsp;&nbsp;1.2 Вимоги** | Зауваження, загальне завдання та вимоги |
| **&nbsp;&nbsp;&nbsp;1.3 Задача** | Прикладна задача відповідно до варіанта |
| **2 РОЗРОБКА ПРОГРАМИ** | Особливості рішення, структура проекту, схеми та ілюстрації |
| **&nbsp;&nbsp;&nbsp;2.1 Засоби Python** | Особливості Python, що використовувалися |
| **&nbsp;&nbsp;&nbsp;2.2 Опис програми** | Коментарі до програми |
| **&nbsp;&nbsp;&nbsp;2.3 Важливі фрагменти програми** | Частини тексту програми, що демонструють рішення задачі |
| **3 РЕЗУЛЬТАТИ РОБОТИ** | Копії екрану (screenshots) та їхній опис |
| **ВИСНОВКИ** | Заключення стосовно повноти досягнення мети |

---

## &lt;Additional&gt;<br /> Розрахункове завдання

1. Розробити програму для перетворення слів української мови латиницею відповідно до [правил транслітерації](http://zakon1.rada.gov.ua/laws/show/55-2010-%D0%BF) ([вікі](https://uk.wikipedia.org/wiki/%D0%9B%D0%B0%D1%82%D0%B8%D0%BD%D1%96%D0%B7%D0%B0%D1%86%D1%96%D1%8F_%D1%83%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D0%BE%D1%97_%D0%BC%D0%BE%D0%B2%D0%B8), [перевірка](http://translit.kh.ua/#lat/passport)).

	GUI (Graphical User Interface) програми повинен містити:
	
	- панель для введення текста українською мовою;
	- панель для відображення результатів транслітерації;
	- інформацію про кількість символів, слів та рядків початкового та перетвореного тексту.

	Перетворення має виконуватися синхронно, або після натиснення відповідної кнопки.

2. Звіт, що відповідає [типовій структурі](#report-), надати у вигляді електронного документа.

3. Початковий код і звіт розмістити у відповідному проекті [GitLab](http://gitlab.com) та забезпечити до нього доступ викладачу.
