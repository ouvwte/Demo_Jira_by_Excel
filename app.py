# user visual form for work

from nicegui import ui
import excel_manager as em 
from datetime import date, datetime 

YES_NO = ["YES", "NO"]
STATUSES = ["Архив", "Готово к внедрению", "Используется"]


data = em.load_data()

# Обновление таблицы на экране
def refresh_table():
    with table:
        table.clear()
        for i, row in data.iterrows():
            ui.label(row["Процедура"])
            ui.label(row["Пояснение"])
            ui.label(row["Формат"])
            ui.label(row["Наименование поля"])
            ui.label(str(row["Номер поля"]))
            ui.label(row["Публичный синоним"])
            ui.label(row["Грант"])
            ui.label(row["Статус разработки"])
            ui.label(str(row["Дата обновления"]))
            ui.button("Редактировать", on_click=lambda i=i: edit_record(i))
            ui.button("Удалить", on_click=lambda i=i: delete_record(i))

# Открыытие формы для добавления записи
def add_record_dialog():
    with ui.dialog() as dialog, ui.card():
        inputs = {}
        for col in em.COLUMNS:
            if col == "Дата обновления":
                inputs[col] = ui.input(label=col, value=datetime.now().strftime("%Y-%m-%d"))
            elif col == "Статус разработки":
                inputs[col] = ui.select(["Архив", "Готово к внедрению", "Используется"], label=col)
            else:
                inputs[col] = ui.input(label=col)

        def save():
            record = {c: inp.value for c, inp in inputs.items()}
            em.add_record(record)
            global data
            data = em.load_data()
            refresh_table()
            dialog.close()

        ui.button("Сохранить", on_click=save)
    dialog.open()

# Открытие формы для редактирования записи
def edit_record(index):
    row = data.iloc[index]
    with ui.dialog() as dialog, ui.card():
        inputs = {}
        for col in em.COLUMNS:
            if col == "Статус разработки":
                inputs[col] = ui.select(["Архив", "Готово к внедрению", "Используется"], value=row[col], label=col)
            else:
                inputs[col] = ui.input(label=col, value=str(row[col]))

        def save():
            record = {c: inp.value for c, inp in inputs.items()}
            em.update_record(index, record)
            global data
            data = em.load_data()
            refresh_table()
            dialog.close()    

        ui.button("Сохранить", on_click=save)
    dialog.open()

# Удаление записи
def delete_record(index):
    em.delete_record(index)
    global data
    data = em.load_data()
    refresh_table()

# Интерфейс
with ui.row():
    ui.button("Добавить запись", on_click=add_record_dialog)

with ui.column().classes("w-full"):
    with ui.scroll_area().classes("w-full h-96"):
        table = ui.column()
        refresh_table()

ui.run(native=True)