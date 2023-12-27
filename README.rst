Русский перевод документации Python
============================================

.. image:: https://travis-ci.org/python/python-docs-ru.svg?branch=3.12
  :target: https://travis-ci.org/python/python-docs-ru


Соглашение о внесении вкладов в документацию
-------------------------------------------

NOTE REGARDING THE LICENSE FOR TRANSLATIONS: Python's documentation is
maintained using a global network of volunteers. By posting this
project on Transifex, Github, and other public places, and inviting
you to participate, we are proposing an agreement that you will
provide your improvements to Python's documentation or the translation
of Python's documentation for the PSF's use under the CC0 license
(available at
https://creativecommons.org/publicdomain/zero/1.0/legalcode). In
return, you may publicly claim credit for the portion of the
translation you contributed and if your translation is accepted by the
PSF, you may (but are not required to) submit a patch including an
appropriate annotation in the Misc/ACKS or TRANSLATORS file. Although
nothing in this Documentation Contribution Agreement obligates the PSF
to incorporate your textual contribution, your participation in the
Python community is welcomed and appreciated.

You signify acceptance of this agreement by submitting your work to
the PSF for inclusion in the documentation.


Внесение вклада в перевод
-------------------------

Как внести вклад
~~~~~~~~~~~~~~~~

Вы можете внести вклад используя:

- GitHub
- `transifex <https://www.transifex.com/python-doc/public/>`_
- Или просто открыв `issue на GitHub <https://github.com/python/python-docs-ru/issues>`_


Внесение вклада с помощью GitHub
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Предварительные требования:

- `GitHub аккаунт <https://github.com/join>`_.
- `Установленный <https://help.github.com/articles/set-up-git/>`_ ``git`` (для Windows, см. https://gitforwindows.org/).
- Редактор файлов ``.po`` (Используйте `poedit <https://poedit.net/>`_
  если у вас его еще нет).


Давайте начнем:

Вам нужно будет форкнуть `python-docs-ru
<https://github.com/python/python-docs-ru>`_ нажав на его кнопку ``Fork``.
Это создаст копию всего проекта на вашем GitHub,
где у вас есть права на внесение изменений.

Поэтапно:

.. code-block:: bash

    # Клонируйте свой форк на github с помощью ssh (замените JulienPalard):
    git clone git@github.com:JulienPalard/python-docs-ru.git

    # Перейдите в клонированный каталог:
    cd python-docs-ru/

    # Добавьте upstream (публичный репозиторий), используя HTTPS (пароль запрашиваться не будет):
    git remote add upstream https://github.com/python/python-docs-ru.git

Все переводы должны быть сделаны на последнюю версию.
Мы никогда не переводим самую старую версию, например, последний релиз Python
это Python 3.12, мы не хотим переводить непосредственно релиз Python 3.5.
При необходимости переводы будут перенесены на самые старые версии
`командой документации <https://www.python.org/dev/peps/pep-8015/#documentation-team>`_.

Теперь вы готовы приступить к работе. Каждый раз, когда вы будете начинать новую задачу, начинайте с этого места:

.. code-block:: bash

    # Для работы нам понадобится ветка, основанная на актуальной (только что полученной) ветке upstream/3.12.
    # Допустим, мы будем работать над глоссарием, поэтому мы назовём ветку "glossary":
    git fetch upstream
    git checkout -b glossary upstream/3.12

    # Теперь вы можете работать с файлом, обычно используя poedit,
    poedit directory/file.po

    # Когда все чисто (синтаксические ошибки от Sphinx, рендеринг html,
    # семантика, типографика),
    # вы можете зафиксировать свою работу с красивым явным сообщением:
    git commit -a -m "Working on glossary."

    # Затем отправьте изменения в ваш клон на GitHub,
    # поскольку это эфемерные ветки, давайте не будем настраивать git на отслеживание их всех,
    # "origin HEAD" - это "специальный" синтаксис, чтобы сказать "Отправка на origin,
    # в ветку с тем же именем, что и локальная",
    # это хорошо, так как это именно то, что нам нужно:
    git push origin HEAD

    # Предыдущая команда выведет вам ссылку для открытия PR на GitHub.
    # Если вы пропустили её, просто перейдите на
    # https://github.com/python/python-docs-ru/ и через несколько секунд появится
    # приятная кнопка "Compare & pull request",
    # сообщающая, что вы можете запросить pull request.

    # Теперь кто-то просмотрит ваши изменения, и вы захотите исправить их выводы,
    # вернитесь в свою ветку
    # (на случай, если вы начали что-то другое в другой ветке):
    git checkout glossary
    # Исправьте проблемы, а затем снова зафиксируйте работу:
    git commit -a -m "glossary: small fixes."
    git push origin HEAD


Вы могли заметить, что это похоже на треугольник с недостающим сегментом:

- Вы пулите из upstream (публичное общее репо на GitHub)
- Вы пушите в origin (ваш клон на github)

Так что да, это работа кого-то - добавить последний сегмент,
от вашего источника к публичному апстриму, чтобы "замкнуть петлю".
Это роль людей, которые объединяют pull requests после их корректировки.

Вы также могли заметить: никогда не делайте коммиты в ветках
версий (``3.6``, ``3.7``, ...), только пульте из них,
считайте их доступными только для чтения, и вы избежите проблем.


Что переводить
~~~~~~~~~~~~~~

Вы можете начать с простых задач, таких как просмотр нечетких записей, чтобы помочь
поддерживать документацию в актуальном состоянии (найдите их с помощью ``make fuzzy``).

Вы также можете скорректировать уже переведенные записи и, наконец,
перевести непереведенные (найдите их с помощью ``make todo``).

- Не переводите содержимое ``:ref:...`` и ``:term:...``
- Английские слова, если они должны быть использованы, выделяйте *курсивом* (окруженным звездочками).
- Если вы переводите заголовок ссылки, переведите и саму ссылку
  (обычно, если это Википедия и у статьи есть перевод).
  Если перевода цели не существует, не переводите заголовок.


Куда обратиться за помощью
~~~~~~~~~~~~~~~~~~~~~~~~~~


Ресурсы для перевода
---------------------


Глоссарий
---------

Для единообразия наших переводов здесь приведены некоторые предложения
и напоминания о часто встречающихся терминах, которые вам
придется переводить, не стесняйтесь открывать issue, если вы
с ними не согласны.

Чтобы легко найти, как тот или иной термин уже переведен в нашей документации,
вы можете использовать
`find_in_po.py <https://gist.github.com/JulienPalard/c430ac23446da2081060ab17bf006ac1>`_.

========================== ===========================================
Термин                     Предлагаемый перевод
========================== ===========================================
-like
abstract data type
argument
backslash
bound
bug
built-in
call stack
debugging
deep copy
double quote
e.g.
garbage collector
identifier
immutable
installer
interpreter
library
list comprehension
little-endian, big-endian
mutable
namespace
parameter
prompt
raise
regular expression
return
simple quote
socket
statement
subprocess
thread
underscore
expression
========================== ===========================================


Упрощение git различий
----------------------

Различия git часто переполнены бесполезными
изменениями номеров строк, например:

.. code-block:: diff

    -#: ../Doc/library/signal.rst:406
    +#: ../Doc/library/signal.rst:408

Чтобы сообщить git, что эта информация не является полезной,
вы можете сделать следующее после того, как убедитесь,
что ``~/.local/bin/`` находится в вашем ``PATH``.

.. code-block:: bash

    cat <<EOF > ~/.local/bin/podiff
    #!/bin/sh
    grep -v '^#:' "\$1"
    EOF

    chmod a+x ~/.local/bin/podiff

    git config diff.podiff.textconv podiff


Обслуживание
------------

Все эти фрагменты должны запускаться из корня клона ``python-docs-ru``,
а некоторые ожидают найти рядом с ним
обновленный клон CPython, например:

.. code-block:: bash

  ~/
  ├── python-docs-ru/
  └── cpython/

Для клонирования CPython вы можете использовать:

.. code-block:: bash

  git clone --depth 1 --no-single-branch https://github.com/python/cpython.git

Это позволяет избежать загрузки всей истории
(не очень полезной для создания документации),
но при этом получает все ветки.


Слияние файлов pot из CPython
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

  make merge


Поиск нечетких строк
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

  make fuzzy


Запуск тестовой сборки локально
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

  make


Синхронизация перевода с Transifex
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Вам понадобятся ``transifex-client`` и ``powrap`` из Pypi.

Вам нужно будет настроить ``tx`` через ``tx init``,
если это еще не сделано.

.. code-block:: bash

   pomerge --from-files **/*.po
   tx pull -f
   pomerge --to-files **/*.po
   pomerge --from-files **/*.po
   git checkout -- .
   pomerge --to-files **/*.po
   powrap --modified
   git commit -m "tx pull"
   tx push -t -f
