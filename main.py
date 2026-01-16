from db import main_db
import flet as ft 


def main(page: ft.Page):
    # print('hello')
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=25)

    def view_tasks(task_id, task_text):
        task_field = ft.TextField(read_only=True, value=task_text, expand=True)

        edit_button = ft.IconButton(icon=ft.Icons.EDIT)

        return ft.Row([task_field, edit_button])

    def add_task_db(_):
        if task_input.value:
            task_text = task_input.value
            new_task_id = main_db.add_task(task=task_text)
            print(f"Задача {task_text} успешно добавлена! Его ID - {new_task_id}")

            task_list.controls.append(view_tasks(task_id=new_task_id, task_text=task_text))

            task_input.value = ""


    task_input = ft.TextField(label='Введите задание:', expand=True, on_submit=add_task_db)
    task_add_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task_db)

    input_row = ft.Row([task_input, task_add_button])

    page.add(input_row, task_list)


if __name__ == '__main__':
    main_db.init_db()
    ft.run(main, view=ft.AppView.WEB_BROWSER)