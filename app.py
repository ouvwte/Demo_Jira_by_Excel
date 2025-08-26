# user visual form for work

from nicegui import ui
import excel_manager as em 
from datetime import date 

def refresh_table():
    pass

def add_entry():
    pass

def edit_entry(idx: int):
    pass

def save_edit():
    pass

def delete_entry(idx: int):
    pass

ui.label("Учет процедур Excel").classes("text-h5")

ui.run(native=True)