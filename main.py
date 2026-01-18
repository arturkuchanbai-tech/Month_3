
from db import main_db
import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=25)

    # функция для создания строки задачи
    def view_tasks(task_id, task_text):
        task_field = ft.TextField(read_only=True, value=task_text, expand=True)

        # кнопка редактирования
        def enable_edit(_):
            task_field.read_only = not task_field.read_only
            page.update()

        edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)

        # кнопка сохранения
        def save_task(_):
            main_db.update_task(task_id=task_id, new_task=task_field.value)
            task_field.read_only = True
            page.update()

        save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)

        # строка задачи
        task_row = ft.Row([task_field, edit_button, save_button])

        # кнопка удаления
        def delete_task(_):
            main_db.delet_task(task_id=task_id)
            if task_row in task_list.controls:
                task_list.controls.remove(task_row)
            page.update()

        delet_button = ft.IconButton(icon=ft.Icons.DELETE, icon_color=ft.Colors.RED, on_click=delete_task)
        task_row.controls.append(delet_button)

        return task_row

    # функция добавления задачи в базу и интерфейс
    def add_task_db(_):
        if task_input.value:
            task_text = task_input.value
            new_task_id = main_db.add_task(task=task_text)
            task_list.controls.append(view_tasks(task_id=new_task_id, task_text=task_text))
            task_input.value = ""
            page.update()

    # поля ввода и кнопка добавления
    task_input = ft.TextField(label='Введите задание', expand=True, on_submit=add_task_db)
    task_add_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task_db)
    input_row = ft.Row([task_input, task_add_button])

    # добавляем элементы на страницу
    page.add(input_row, task_list)

if __name__ == '__main__':
    main_db.init_db()
    ft.run(main)