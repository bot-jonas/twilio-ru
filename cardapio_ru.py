from itertools import islice
import requests
import re
import os

EVERYTHING = "(?:.|\n)*?"

REGEX = {
    "table": f"<table(?:.*?)>({EVERYTHING})</table>",
    "rows": f"<tr(?:.*?)>({EVERYTHING})</tr>",
    "cols": f"<td(?:.*?)>({EVERYTHING})</td>",
}


def get_text(html_str):
    return re.sub("</?(?:.*?)/?>|&nbsp;", "", html_str).strip()


def parse_table(table_text):
    table = []
    rows = re.findall(REGEX["rows"], table_text)

    for row in rows:
        cols = re.findall(REGEX["cols"], row)

        table.append([get_text(col).strip() for col in cols])

    return table

def get_data():
    r = requests.get("https://sobral.ufc.br/ru/cardapio/")
    title = get_text(re.findall(f'<h1 class="entry-title">({EVERYTHING})</h1>', r.text)[0])

    [lunch_match, dinner_match] = islice(re.finditer(REGEX["table"], r.text), 2)

    lunch_table = parse_table(lunch_match.group(0))
    dinner_table = parse_table(dinner_match.group(0))

    return title, lunch_table, dinner_table