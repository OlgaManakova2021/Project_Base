import re
my_date = "27.02.2024"
p = re.compile(r'[0-9][0-9].[0-9][0-9].[0-9][0-9]')
print(p.search(my_date))