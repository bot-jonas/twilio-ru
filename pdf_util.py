from cardapio_ru import get_data
import weasyprint as wsp

def table_to_html(table):
	html = '<table>'

	html += '<tr>'
	for col in table[0]:
		html += f'<th>{col}</th>'
	html += '</tr>'

	for row in table[1:]:
		html += '<tr>'
		for col in row:
			html += f'<td>{col}</td>'
		html += '</tr>'

	html += '</table>'

	return html

css_style = '''
* {
	font-family: monospace;
}

@page {
	padding: 0px;
	margin: 0px;
}

table {
	border-collapse: collapse;
	margin-bottom: 10px;
	font-size: 10pt;
}

tr:nth-child(odd) {
	background-color: #DDD;
}

th, td {
	padding: 5px;
	border: 1px solid;
	text-align: center;
}
'''

def generate_pdf(filename):
	title, lunch_table, dinner_table = get_data()

	html_string = f'<h2>{title}</h2>' + table_to_html(lunch_table) + table_to_html(dinner_table)

	# with open("test.html", "w") as f:
	# 	f.write(f"<style>{css_style}</style>" + html_string)

	css = wsp.CSS(string=css_style)
	html = wsp.HTML(string=html_string)
	html.write_pdf(filename, stylesheets=[css])