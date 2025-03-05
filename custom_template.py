import psycopg2
import os
import hashlib

username = "{{ STUDENT.username }}"
schema_name = "schema_" + hashlib.md5(username.encode()).hexdigest()[:10]

student_answer = """{{ STUDENT_ANSWER | e('py') }}""".rstrip()
if not student_answer.endswith(';'):
    student_answer += ';'

SEPARATOR = "#<ab@17943918#@>#"

db_config = {
    'dbname': 'moodle_db',
    'user': 'moodle',
    'password': 'moodle',
    'host': 'localhost',
    'port': '5432'
}

{% for TEST in TESTCASES %}


create_schema = f"""CREATE SCHEMA IF NOT EXISTS {schema_name};
SET search_path TO {schema_name};"""
extra = """{{ TEST.extra | e('py') }}"""
globalextra = """{{ QUESTION.globalextra | e('py') }}"""
testcode = """{{ TEST.testcode | e('py') }}"""
remove_schema = f"""DROP SCHEMA IF EXISTS {schema_name} CASCADE;"""

code_to_run = '\n'.join([
    create_schema, 
    globalextra,
    extra,
    student_answer,
    testcode,
])

try:
    conn = psycopg2.connect(**db_config)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(code_to_run)
    
    try:
        output = cur.fetchall()
        for row in output:
            print(' '.join(map(str, row)))
    except psycopg2.ProgrammingError:
        pass
    
    cur.execute(remove_schema)
    cur.close()
    conn.close()
except Exception as e:
    raise Exception("Ошибка выполнения запроса: " + str(e))

{% if not loop.last %}
print(SEPARATOR)
{% endif %}
{% endfor %}

