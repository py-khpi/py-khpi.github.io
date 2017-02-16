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

1. [Python 3.6.0](https://www.python.org/downloads/release/python-360/) - у комплекті надається інтегроване середовище розробки.

2. [Simple Python style checker](https://github.com/pycqa/pep8) - перевірка початкового кода на відповідність [PEP 8](http://www.python.org/dev/peps/pep-0008).

3. [Doxygen](http://www.stack.nl/~dimitri/doxygen/download.html) <span id="doxy"></span> - система документування початкового коду. Додатково встановити:

- [Graphviz](http://www.graphviz.org/Download.php) - Graph Visualization Software;
- [Mscgen](http://www.mcternan.me.uk/mscgen/) - Message Sequence Chart Renderer.

---

<span id="references"></span>
## Рекомендації

1. **Використовувати:**

- [Style Guide](https://www.python.org/dev/peps/pep-0008).
- [Викиучебник](https://ru.wikibooks.org/wiki/Python).
- [Python Documentation](https://docs.python.org/3).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Tutorial](https://docs.python.org/3/tutorial).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Language Reference](https://docs.python.org/3/reference).
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- [Library Reference](https://docs.python.org/3/library).

2. **Ознайомитись:**

- [What’s New in Python](https://docs.python.org/3/whatsnew).
- [Python HOWTOs](https://docs.python.org/3/howto).
- [Best practices for writing Python code](http://docs.python-guide.org/en/latest).
- [Code Like a Pythonista](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html) ([переклад рос.](https://habrahabr.ru/post/88972/)).
- [Python Tips, Tricks, and Hacks](http://www.siafoo.net/article/52) ([переклад рос.](http://habrahabr.ru/post/85238/), [pdf](http://idzaaus.org/static/files/articles/Python_Tips,_Tricks,_and%20Hacks_\(rus\).pdf)).

---

<span id="labs"></span>
## Лабораторні роботи

|  №  | Тема     |
|:---:|:---------|
|  1  | [1](https://py-khpi.github.io/!nfo/doc/lab/LAB1/lab.htm) |
|  2  | [2](https://py-khpi.github.io/!nfo/doc/lab/LAB2/lab.htm) |
|  3  | [3](https://py-khpi.github.io/!nfo/doc/lab/LAB3/lab.htm) |
|  4  | [4](https://py-khpi.github.io/!nfo/doc/lab/LAB4/lab.htm) |
|  5  | [5](https://py-khpi.github.io/!nfo/doc/lab/LAB5/lab.htm) |
|  6  | [6](https://py-khpi.github.io/!nfo/doc/lab/LAB6/lab.htm) |
|  7  | [7](https://py-khpi.github.io/!nfo/doc/lab/LAB7/lab.htm) |
|  8  | [8](https://py-khpi.github.io/!nfo/doc/lab/LAB8/lab.htm) |
|  9  | [9](https://py-khpi.github.io/!nfo/doc/lab/LAB9/lab.htm) |
| 10  | [10](https://py-khpi.github.io/!nfo/doc/lab/LAB10/lab.htm) |
| 11  | [11](https://py-khpi.github.io/!nfo/doc/lab/LAB11/lab.htm) |
| 12  | [12](https://py-khpi.github.io/!nfo/doc/lab/LAB12/lab.htm) |
| 13  | [13](https://py-khpi.github.io/!nfo/doc/lab/LAB13/lab.htm) |

<span id="lab_todo"></span>
### Спільні завдання

|  №  | Завдання |
|:---:|:---------|
|  1  | Розробити програму для рішення індивідуального завдання |
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

4. **Назву** особистої директорії *surname* з відповідним номером роботи *XX* використовувати для іменування директорій **рішень**, **проектів** і **звітів** лабораторних робіт. Наприклад:

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

5. **Дотримуватися** принципів, що виводяться інтерпретатором *Python* по команді `import this`.

<span id="lab_report"></span>
### Звіт

1. **Оформляється** українською мовою та надається у форматі [Markdown](https://ru.wikipedia.org/wiki/Markdown), або у вигляді електронних документів:

	- що редагується *(docx/doc/odt/html)*,
	- що зручно проглядається *(pdf/djvu/chm)*.

2. **Формат** документа, що друкується:

	- A4 з полями: **2.5 см** зліва, **2 см** праворуч, **2 см** зверху, **2 см** знизу;
	- гарнітура: **Times New Roman**; кегль: **14**; міжрядковий інтервал: **одинарний**;
	- відступ першого рядка абзацу: **1.27 см**; вирівнювання: **у ширину**;
	- приклад див. у файлі [oop_appendix_2.pdf]().

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
