Проектування серверних додатків
==================================

## Мета

- **Вивчити** основи мови програмування [Python](https://ru.wikipedia.org/wiki/Python).
- **Ознайомитись** з [серверним програмуванням](https://en.wikipedia.org/wiki/Server-side_scripting).
- **Отримати** навички розробки програм з використанням принципів архітектури [клієнт-сервер](https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B8%D0%B5%D0%BD%D1%82-%D1%81%D0%B5%D1%80%D0%B2%D0%B5%D1%80).

---

## Зміст

[Програмні засоби та інструменти](#soft)<br />
[Рекомендації](#references)<br />
[Лабораторні роботи](#labs)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Завдання](#lab_todo)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Вимоги](#lab_requirements)<br />
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Звіт](#lab_report)<br />
[Примітки](#notes)<br />

---

<span id="soft"></span>
## Програмні засоби та інструменти

1. [Python 3.5.1](https://www.python.org/downloads/release/python-351/) - у комплекті надається інтегроване середовище розробки.

2. [Simple Python style checker](https://github.com/pycqa/pep8) - перевірка початкового кода на відповідність [PEP 8](http://www.python.org/dev/peps/pep-0008).

3. [Doxygen](http://www.stack.nl/~dimitri/doxygen/download.html) <span id="doxy"></span> - система документування початкового коду. Додатково встановити:

	- [Graphviz](http://www.graphviz.org/Download.php) - Graph Visualization Software;
	- [Mscgen](http://www.mcternan.me.uk/mscgen/) - Message Sequence Chart Renderer.

4. [TortoiseSVN](http://tortoisesvn.net/downloads.html) <sup><abbr title="SVN-репозиторій використовувати за розсудом викладача">[1](#note_svn)</abbr></sup> - Subversion (SVN) client. В лабораторіях ОЦ НТУ "ХПІ" включити використання *proxy-сервера* в меню *TortoiseSVN/Settings/Network*:

	- Enable Proxy Server;
	- Server address: `172.17.10.2`;
	- Port: `3128`.

5. [SVN Hosting](https://www.assembla.com) <sup><abbr title="SVN-репозиторій використовувати за розсудом викладача">[1](#note_svn)</abbr></sup> - веб-сервіс управління версіями:

	- потрібна попередня реєстрація [GET STARTED WITH FREE REPOSITORIES](https://www.assembla.com/repositories);
	- при реєстрації обов'язково вказувати **Username** у вигляді **surname_name** - прізвище та ім'я розробника [латинкою в нижньому регістрі](http://translit.kh.ua/?lat&passport);

---

<span id="references"></span>
## Рекомендації

- **Використовувати:**

	- [Style Guide](https://www.python.org/dev/peps/pep-0008).
	- [Викиучебник](https://ru.wikibooks.org/wiki/Python).
	- [Python Documentation](https://docs.python.org/3).
		- [Tutorial](https://docs.python.org/3/tutorial).
		- [Language Reference](https://docs.python.org/3/reference).
		- [Library Reference](https://docs.python.org/3/library).

- **Ознайомитись:**

	- [What’s New in Python](https://docs.python.org/3/whatsnew).
	- [Python HOWTOs](https://docs.python.org/3/howto).
	- [Best practices for writing Python code](http://docs.python-guide.org/en/latest).
	- [Code Like a Pythonista](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html) ([переклад рос.](https://habrahabr.ru/post/88972/)).
	- [Python Tips, Tricks, and Hacks](http://www.siafoo.net/article/52) ([переклад рос.](http://habrahabr.ru/post/85238/), [pdf](http://idzaaus.org/static/files/articles/Python_Tips,_Tricks,_and%20Hacks_\(rus\).pdf)).

---

<span id="labs"></span>
## Лабораторні роботи

|  №  | Тема     |
|----:|:---------|
|  1  | [Основы языка Python.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB1/lab.htm?_format=raw) |
|  2  | [Модули. Строки.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB2/lab.htm?_format=raw) |
|  3  | [ABC-классы. Списки.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB3/lab.htm?_format=raw) |
|  4  | [Кортежи. Диапазоны. Двоичные последовательности.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB4/lab.htm?_format=raw) |
|  5  | [Множества. Словари. Генераторы.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB5/lab.htm?_format=raw) |
|  6  | [Разработка функций и модулей пользователя.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB6/lab.htm?_format=raw) |
|  7  | [Разработка CGI скриптов на языке Python.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB7/lab.htm?_format=raw) |
|  8  | [Работа с файлами на языке Python.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB8/lab.htm?_format=raw) |
|  9  | [Регулярные выражения.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB9/lab.htm?_format=raw) |
| 10  | [Использование технологии AJAX.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB10/lab.htm?_format=raw) |
| 11  | [Создание пользовательских классов.](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab/LAB11/lab.htm?_format=raw) |

<span id="lab_todo"></span>
### Спільні завдання

|  №  | Завдання |
|:---:|:---------|
|  1  | Розробити програму для рішення [індивідуального завдання](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/lab). |
|  2  | Виконати [рефакторинґ](https://refactoring.guru/) з урахуванням загальних [вимог](#lab_requirements). |
|  3  | Підготувати до перевірки опис розробленої програми у вигляді [звіту](#lab_report). |
|  4  | Виправити програму з урахуванням отриманих зауважень. |

<span id="lab_requirements"></span>
### Вимоги

1. **Проекти** розміщувати в директоріях `surname/src/surnameXX`, де:

	- *surname* - назва особистої директорії в спільному сховищі *Subversion*;
	- *XX* - номер роботи.

2. **Звіти** розташовувати в директоріях `surname/doc/surnameXX`.

3. **Коментувати** текст програми для обробки пакетом [Doxygen](#doxy).

4. **Початковий** код розташовувати в репозиторії лише той, що успішно компілюється та відповідає [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008).

5. **Повідомлення** до коміту - що саме ви зберігаєте - має бути зрозумілим. На початку повідомлення вказувати:

	- **номер** тікета (завдання) - номер у [таблиці](#lab_todo), що містить список спільних завдань та зауважень;
	- **тему/компонент** до якого належить коміт. Наприклад:

		```
#1, #3 shevchenko01: завдання виконано, звіт підготовлений до перевірки
#2 task01: отформатирован текст и добавлены комментарии
#4 Locator: алгоритм пошуку оптимізовано
#4 task02: удалены лишние файлы
#4 raeth: fix regression after [a002b90]
		```

6. **Назву** особистої директорії *surname* з відповідним номером роботи *XX* використовувати для іменування директорій **рішень**, **проектів** і **звітів** лабораторних робіт. Наприклад:

	- студент з особистим каталогом `shevchenko`
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

7. **Checkout URL** для доступу до особистої директорії формується додаванням до *Checkout URL* спільного сховища назви особистої директорії. Наприклад:

	- загальне сховище має *Checkout URL:*

		`https://subversion.assembla.com/svn/kitXX-2016-py/`

	- тоді *Checkout URL* для доступу до особистої директорії *shevchenko*:

		`https://subversion.assembla.com/svn/kitXX-2016-py/shevchenko`

8. **Дотримуватися** принципів, що виводяться інтерпретатором *Python* по команді `import this`.

<span id="lab_report"></span>
### Звіт

1. **Оформляється** українською мовою та надається у форматі [Markdown](https://ru.wikipedia.org/wiki/Markdown), або у вигляді електронних документів:

	- що редагується *(docx/doc/odt/html)*,
	- що зручно проглядається *(pdf/djvu/chm)*.

2. **Формат** документа, що друкується:

	- A4 з полями: **2.5 см** зліва, **2 см** праворуч, **2 см** зверху, **2 см** знизу;
	- гарнітура: **Times New Roman**; кегль: **14**; міжрядковий інтервал: **одинарний**;
	- відступ першого рядка абзацу: **1.27 см**; вирівнювання: **у ширину**;
	- приклад див. у файлі [oop_appendix_2.pdf](https://www.assembla.com/spaces/khpi-py/subversion/source/HEAD/!nfo/doc/oop_appendix_2.pdf?_format=raw).

3. **Структура** звіту:

| Обов'язковий розділ | Зауваження |
|:--------------------|:-----------|
| **Номер і тема роботи** | Вказується з вирівнюванням по центру рядка. |
| **Мета: ...** | Відповідає темі та завданню. |
| **1 ІНДИВІДУАЛЬНЕ ЗАВДАННЯ** | Повне формулювання завдання. |
| **2 РОЗРОБКА ПРОГРАМИ** | Особливості рішення, структура проекту, схеми та ілюстрації. |
| **&nbsp;&nbsp;&nbsp;2.1 Засоби Python** | Особливості Python, що використовувалися. |
| **&nbsp;&nbsp;&nbsp;2.2 Опис програми** | Коментарі до програми. |
| **&nbsp;&nbsp;&nbsp;2.3 Важливі фрагменти програми** | Частини тексту програми, що демонструють рішення задачі. |
| **3 РЕЗУЛЬТАТИ РОБОТИ** | Копії екрану (screenshots) та їхній опис. |
| **ВИСНОВКИ** | Заключення стосовно повноти досягнення мети. |

---

<span id="notes"></span>
## Примітки

1. <span id="note_svn"></span>*SVN-репозиторій* та веб-сервіс управління версіями використовувати за розсудом викладача.

2. <span id="note_summary"></span>Уточнення завдання і засобів розробки за розсудом викладача.
