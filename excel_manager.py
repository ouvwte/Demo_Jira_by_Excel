# loading, saving, crud

import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import datetime as datetime 

EXCEL_FILE = "data.xls"

COLUMNS = ["Процедура", "Пояснение", "Формат", "Наименование поля", "Номер поля", "Публичный синоним", "grant", "Статус разработки"]

STATUS_COLORS = {"Архив": "FFC7CE", "Готово к внедрению": "FFEB9C", "Используется": "C6EFCE"}

def load_data():
    pass

def save_data(df):
    pass

def add_record(record: dict):
    pass

def update_record(index: int, record: dict):
    pass

def delete_record(index: int):
    pass

