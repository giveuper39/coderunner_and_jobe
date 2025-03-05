## Создание таблицы с ограничениями целостности

**Задача 1: Создание таблицы**

**Описание задачи:**  
Создайте таблицу `students` с полями:
- `id` (INTEGER, PRIMARY KEY)
- `name` (VARCHAR(255))
- `average_score` (NUMERIC, IN [2, 5])

**Global Extra:**

```postgresql
DROP TABLE IF EXISTS students;
```
**Правильный ответ:**

```postgresql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    average_score NUMERIC CHECK(average_score >= 2 AND average_score <= 5)
);
```

**Тесты:**

*Тест 1:*

```postgresql
INSERT INTO students VALUES (1, 'Arnold', 3.5);
SELECT * FROM students;
```

- Ожидаемый результат:
    
    ```1 Arnold 3.5```

*Тест 2:*

```postgresql
SELECT conname, contype, pg_get_constraintdef(oid) AS definition
FROM pg_constraint
WHERE conrelid = 'students'::regclass;
```

- Ожидаемый результат:
```postgresql
students_average_score_check c CHECK (((average_score >= (2)::numeric) AND (average_score <= (5)::numeric)))
students_pkey p PRIMARY KEY (id)
```

## Удаление таблицы

**Задача 2: Удаление таблицы**

**Описание задачи:**
Удалите таблицу `students`.

**Global Extra:**

```postgresql
CREATE TABLE IF NOT EXISTS students (
    id INTEGER
);
```

**Правильный ответ:**

```postgresql
DROP TABLE students;
```

**Тесты**:

*Тест 1*:

```postgresql
CREATE TABLE students (id INTEGER);
INSERT INTO students VALUES (1), (2);
SELECT id FROM students;
```

- Ожидаемый результат:
   ```
  1
  2
  ```

## Изменение таблицы

**Задача 3: Изменение таблицы**

**Описание задачи:**
Создана таблица `students` с полями:

- `id` (INTEGER, PRIMARY KEY)
- `name` (VARCHAR(255))
- `average_score` (NUMERIC)

**Global Extra:**

```postgresql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    average_score NUMERIC
);
```

**Правильный ответ:**

```postgresql
ALTER TABLE students ADD email TEXT;
```

**Тесты:**

*Тест 1:*

```postgresql
INSERT INTO students VALUES (1, 'Arnold', 3.5, 'test@test.test');
SELECT * FROM students;
```

- Ожидаемый результат:

    ```1 Arnold 3.5 test@test.test```
