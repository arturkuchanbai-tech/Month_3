
from db import main_db
import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=25)

    filter_tupe = 'all'

    def load_tasks():
        task_list.controls.clear()
        for task_id, task_text, completed in main_db.get_tasks(filter_tupe):
            task_list.controls.append(view_task(task_id=task_id, task_text=task_text, completed=completed))
        page.update()

    def view_task(task_id, task_text, completed=None):
        task_field = ft.TextField(value=task_text, read_only=True, expand=True)

        checkbox = ft.Checkbox(
            value=bool(completed),
            on_change=lambda e: toggle_task(task_id, e.control.value)
        )

        def enable_edit(_):
            task_field.read_only = not task_field.read_only
            page.update()

        def save_task(_):
            main_db.update_task(task_id, new_task=task_field.value)
            task_field.read_only = True
            page.update()

        def delete_task(_):
            main_db.delete_task(task_id)
            task_list.controls.remove(task_row)
            page.update()

        task_row = ft.Row([
            checkbox,
            task_field,
            ft.IconButton(ft.Icons.EDIT, on_click=enable_edit),
            ft.IconButton(ft.Icons.SAVE, on_click=save_task),
            ft.IconButton(ft.Icons.DELETE, on_click=delete_task, bgcolor="red", icon_color="white")
        ])

        return task_row

    def toggle_task(task_id, is_completed):
        main_db.update_task(task_id=task_id, completed=int(is_completed))
        load_tasks()

    def add_task_add(_):
        if task_input.value:
            task_text = task_input.value
            new_task_id = main_db.add_task(task=task_text)
            task_list.controls.append(view_task(task_id=new_task_id, task_text=task_text))
            task_input.value = None
            page.update()

    task_input = ft.TextField(label='Введите задание', expand=True, on_submit=add_task_add)
    task_add_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task_add)

    def set_filter(filter_value):
        nonlocal filter_tupe
        filter_tupe = filter_value
        load_tasks()

    filter_buttons = ft.Row([
        ft.ElevatedButton(content=ft.Text('Все задачи'), on_click=lambda e: set_filter('all'), icon=ft.Icons.ALL_INBOX),
        ft.ElevatedButton(content=ft.Text('В работе'), on_click=lambda e: set_filter('uncompleted'), icon=ft.Icons.WATCH_LATER),
        ft.ElevatedButton(content=ft.Text('Готово'), on_click=lambda e: set_filter('completed'), icon=ft.Icons.CHECK_BOX),
    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

    def clear_completed(_):
        main_db.clear_task()
        load_tasks()

       
    clear_completed_button = ft.ElevatedButton(content=ft.Row([ft.Text("Очистить выполненные"),
    ft.Icon(ft.Icons.DELETE_SWEEP, size=20)],alignment=ft.MainAxisAlignment.END,spacing=1),
    bgcolor="red",color="white",on_click=clear_completed)

    input_row = ft.Row([task_input, task_add_button])

    full_task = ft.Row([filter_buttons,clear_completed_button])

    page.add(input_row,full_task,task_list)

    load_tasks()

if __name__ == '__main__':
    main_db.init_db()
    ft.run(main)
