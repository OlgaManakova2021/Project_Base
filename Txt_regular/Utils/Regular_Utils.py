import re
import time

def find_name(text: str) -> str:
    reg_name = re.findall(r'Решение\s*№.+по\s*делу\s*№\s*[0-9-/();~а-яА-Я\[\]]+', text)[0]
    return reg_name
