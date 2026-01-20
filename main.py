from db import main_db
import flet as ft

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    task_list = ft.Column(spacing=25)

    def view_task(task_id, task_text):
        task_field = ft.TextField(read_only=True,value=task_text,expand=True)

    
        def enable_edit(_):
            if task_field.read_only == True:
                task_field.read_only = False
            else:
                task_field.read_only = True
        

        edit_button = ft.IconButton(icon=ft.Icons.EDIT,on_click=enable_edit)

        
        def save_task(_):
            main_db.update_task(task_id, new_task=task_field.value)
            task_field.read_only = True
    

        save_button = ft.IconButton(icon=ft.Icons.SAVE,on_click=save_task)

        
        def delete_task(_):
            main_db.delet_task(task_id=task_id)        
            task_list.controls.remove(task_row)        
    

        delete_button = ft.IconButton(icon=ft.Icons.DELETE,on_click=delete_task,bgcolor="red",icon_color="white")

    
        task_row = ft.Row([task_field, edit_button, save_button, delete_button])

        return task_row


    def add_task_add(_):
        if task_input.value:
            task_text = task_input.value
            new_task_id = main_db.add_task(task=task_text)

            print(f'задача "{task_text}" успешно добавлена! Его ID - {new_task_id}')

            task_list.controls.append(view_task(task_id=new_task_id, task_text=task_text))

            task_input.value = None
        

    task_input = ft.TextField(label='Введите задание',expand=True,on_submit=add_task_add)

    task_add_button = ft.IconButton(icon=ft.Icons.ADD,on_click=add_task_add)

    input_row = ft.Row([task_input, task_add_button])

    page.add(input_row, task_list)



ft.app(target=main)
