# from db import main_db
# import flet as ft


# def main(page: ft.Page):
#     page.theme_mode = ft.ThemeMode.LIGHT

#     task_list = ft.Column(spacing=25)

#     filter_tupe = 'all'

#     def load_tasks():
#         task_list.controls.clear()
#         for task_id, task_text,completed in main_db.get_tasks(filter_tupe):
#             task_list.controls.append(view_task(task_id=task_id, task_text=task_text, completed = completed))


#     def view_task(task_id, task_text, completed= None):
#         task_field = ft.TextField(read_only=True,value=task_text,expand=True)

#         chekbox = ft.Checkbox(value=bool(completed), on_change=lambda e: toggle_task(task_id, e.control.value))
#         main_db.add_task(task_text)
#         main_db.get_tasks(filter_tupe)


    
#         def enable_edit(_):
#             if task_field.read_only == True:
#                 task_field.read_only = False
#             else:
#                 task_field.read_only = True
        

#         edit_button = ft.IconButton(icon=ft.Icons.EDIT,on_click=enable_edit)

        
#         def save_task(_):
#             main_db.update_task(task_id, new_task=task_field.value)
#             task_field.read_only = True
    

#         save_button = ft.IconButton(icon=ft.Icons.SAVE,on_click=save_task)

        
#         def delete_task(_):
#             main_db.delete_task(task_id=task_id)        
#             task_list.controls.remove(task_row)        
    

#         delete_button = ft.IconButton(icon=ft.Icons.DELETE,on_click=delete_task,bgcolor="red",icon_color="white")

#         def clear_task(_):
#            main_db.clear_task()
#            load_tasks()

#         clear_button = ft.IconButton(icon=ft.Icons.CLEAR, on_click=clear_task )

        

#         task_row = ft.Row([chekbox,task_field, edit_button, save_button, delete_button,clear_button])

#         return task_row
    

#     def toggle_task(task_id,is_completed):
#         print(is_completed)
#         main_db.update_task(task_id=task_id, completed=int(is_completed))
#         load_tasks()


#     def add_task_add(_):
#         if task_input.value:
#             task_text = task_input.value
#             new_task_id = main_db.add_task(task=task_text)

#             print(f'задача "{task_text}" успешно добавлена! Его ID - {new_task_id}')

#             task_list.controls.append(view_task(task_id=new_task_id, task_text=task_text))

#             task_input.value = None
        

#     task_input = ft.TextField(label='Введите задание',expand=True,on_submit=add_task_add)

#     task_add_button = ft.IconButton(icon=ft.Icons.ADD,on_click=add_task_add)

#     def set_filter(filter_value):
#         nonlocal filter_tupe
#         filter_tupe = filter_value
#         load_tasks()

#     filter_buttons = ft.Row([
#         ft.ElevatedButton('Все задачи', on_click=lambda e: set_filter('all'), icon=ft.Icons.ALL_INBOX),
#         ft.ElevatedButton('В работе', on_click=lambda e: set_filter('uncompleted'), icon= ft.Icons.WATCH_LATER),
#         ft.ElevatedButton('Готово',on_click=lambda e: set_filter('completed'), icon=ft.Icons.CHECK_BOX)
#     ],alignment=ft.MainAxisAlignment.SPACE_EVENLY)

#     input_row = ft.Row([task_input, task_add_button])
    


#     page.add(input_row,filter_buttons, task_list)
#     load_tasks()

# if __name__ == '__main__':
#     main_db.init_db()
#     ft.run(main)


# # ------------------------ ШАГ 1: Импортируем библиотеки ------------------------
# from db import main_db   # работа с базой данных
# import flet as ft        # GUI-фреймворк Flet

# # ------------------------ ШАГ 2: Главная функция приложения ------------------------
# def main(page: ft.Page):
#     # 2.1. Устанавливаем тему страницы
#     page.theme_mode = ft.ThemeMode.LIGHT

#     # 2.2. Создаем колонку для отображения задач
#     task_list = ft.Column(spacing=25)

#     # 2.3. Переменная для текущего фильтра
#     filter_type = 'all'

#     # ------------------------ ШАГ 3: Функции работы с задачами ------------------------
    
#     # 3.1. Загрузка задач из базы в интерфейс
#     def load_tasks():
#         task_list.controls.clear()  # очищаем текущий список
#         for task_id, task_text, completed in main_db.get_tasks(filter_type):
#             task_list.controls.append(view_task(task_id, task_text, completed))
#         page.update()  # обновляем страницу

#     # 3.2. Создание строки задачи для интерфейса
#     def view_task(task_id, task_text, completed=False):
#         task_field = ft.TextField(read_only=True, value=task_text, expand=True)
#         checkbox = ft.Checkbox(
#             value=bool(completed),
#             on_change=lambda e: toggle_task(task_id, e.control.value)
#         )

#         # 3.2.1. Переключение редактирования
#         def enable_edit(_):
#             task_field.read_only = not task_field.read_only
#             page.update()

#         # 3.2.2. Сохранение изменений
#         def save_task(_):
#             main_db.update_task(task_id, new_task=task_field.value)
#             task_field.read_only = True
#             page.update()

#         # 3.2.3. Удаление задачи
#         def delete_task(_):
#             main_db.delete_task(task_id)
#             task_list.controls.remove(task_row)
#             page.update()

#         # 3.2.4. Кнопки управления задачей
#         edit_button = ft.IconButton(icon=ft.Icons.EDIT, on_click=enable_edit)
#         save_button = ft.IconButton(icon=ft.Icons.SAVE, on_click=save_task)
#         delete_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=delete_task, bgcolor="red", icon_color="white")

#         # 3.2.5. Формируем строку задачи
#         task_row = ft.Row([checkbox, task_field, edit_button, save_button, delete_button])
#         return task_row

#     # 3.3. Переключение статуса задачи (чекбокс)
#     def toggle_task(task_id, is_completed):
#         main_db.update_task(task_id=task_id, completed=int(is_completed))
#         load_tasks()  # обновляем список после изменения

#     # 3.4. Добавление новой задачи
#     def add_task(_):
#         if task_input.value:
#             task_text = task_input.value
#             new_task_id = main_db.add_task(task_text)
#             task_list.controls.append(view_task(new_task_id, task_text))
#             task_input.value = ""
#             page.update()

#     # 3.5. Изменение фильтра задач
#     def set_filter(filter_value):
#         nonlocal filter_type
#         filter_type = filter_value
#         load_tasks()  # подгружаем задачи согласно фильтру

#     # ------------------------ ШАГ 4: Элементы интерфейса ------------------------
    
#     # 4.1. Поле ввода новой задачи
#     task_input = ft.TextField(label='Введите задание', expand=True, on_submit=add_task)
#     task_add_button = ft.IconButton(icon=ft.Icons.ADD, on_click=add_task)
#     input_row = ft.Row([task_input, task_add_button])

#     # 4.2. Кнопки фильтра задач
#     filter_buttons = ft.Row([
#         ft.ElevatedButton('Все задачи', on_click=lambda e: set_filter('all'), icon=ft.Icons.ALL_INBOX),
#         ft.ElevatedButton('В работе', on_click=lambda e: set_filter('uncompleted'), icon=ft.Icons.WATCH_LATER),
#         ft.ElevatedButton('Готово', on_click=lambda e: set_filter('completed'), icon=ft.Icons.CHECK_BOX)
#     ], alignment=ft.MainAxisAlignment.SPACE_EVENLY)

#     # 4.3. Добавляем элементы на страницу
#     page.add(input_row, filter_buttons, task_list)

#     # 4.4. Загружаем задачи при старте
#     load_tasks()

# # ------------------------ ШАГ 5: Запуск приложения ------------------------
# if __name__ == '__main__':
#     main_db.init_db()  # инициализация базы данных
#     ft.run(main)       # запуск приложения
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
