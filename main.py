# Имортируем нужные модули, создаем функции и объявляем необходимые переменные
import ttkbootstrap as ttk
import file_connection
from tkinter import messagebox, Listbox
articles = file_connection.get_articles()
def show_article() -> None:
    """
    Функция для вывода статьи на экран.
    """
    selected_index = listbox.curselection()
    if selected_index:        
        title = listbox.get(selected_index)
        text = articles[title]
        read_window = ttk.Toplevel(root)
        read_window.resizable(0, 0)
        read_window.configure(padx=20, pady=20)
        read_window.title(title)
        title_label = ttk.Label(read_window, text=title, font=("Gabriola", 18))
        title_label.grid()
        text_box = ttk.Text(read_window, wrap="word")
        text_box.grid()
        text_box.insert("end", text)
        text_box.configure(state="disabled")
def write_article() -> None:
    """
    Фунция для написания статьи.
    """
    global articles
    def save():
        new_title = entry_title.get()
        new_text = entry_text.get("1.0", "end")
        file_connection.add_article(new_title, new_text)
        articles[new_title] = new_text
        listbox.insert("end", new_title)
        write_window.destroy()
    title = "Добавить статью."
    write_window = ttk.Toplevel(root)
    write_window.resizable(0, 0)
    write_window.configure(padx=20, pady=20)
    write_window.title(title)
    
    label_title = ttk.Label(write_window, text = "Введите название статьи: ")
    label_title.grid()
    
    entry_title = ttk.Entry(write_window)
    entry_title.grid(sticky="we")
    
    label_text = ttk.Label(write_window, text = "Введите текст статьи: ")
    label_text.grid()
    
    entry_text = ttk.Text(write_window)
    entry_text.grid(sticky="we")
    save_button = ttk.Button(write_window, text = "Сохранить", style="info", command=save)
    save_button.grid()

def delete_article() -> None:
    """
    Функция для удаления статьи.
    """
    global articles
    def delete():
        file_connection.del_article(title)
        listbox.delete(selected_index)
        del_window.destroy()
    selected_index = listbox.curselection()
    if selected_index:        
        title = listbox.get(selected_index)
        del_window = ttk.Toplevel(root)
        del_window.resizable(0, 0)
        del_window.configure(padx=20, pady=20)
        del_window.title(f"Удаление статьи {title}")
        del_button = ttk.Button(del_window, text = "Удалить", style="dark", command=delete)
        del_button.grid(column=1, row=1)
        cancel_button = ttk.Button(del_window, text = "Отменить удаление", style="light", command=del_window.destroy)
        cancel_button.grid(column=3, row=1)

# Создаем окно
root = ttk.Window(themename="superhero") # Создаем окно и добавляем тему
root.title("Энциклопедия кошек") # Называем окно
root.resizable(0, 0) # Запрещаем изменение размеров окна пользователю
root.configure(padx=20, pady=20) # Изменяем размеры окна сами

# Создаем список статей
listbox = Listbox(root) # (root) - указываем на каком окне список будет находится
listbox.grid(column=0, row=0, columnspan=3, sticky="we") # Распологаем список на окне: column и row - по сути координаты, columnspan=3 - теперь список будет занимать три колонки, sticky - прилипание, we - по ширине (west east)
# Добавляем элементы в список 
for article in articles:
    listbox.insert("end", article)
# Кнопка для чтения
read_button = ttk.Button(root, text = "Прочитать", style = "success", command=show_article)
read_button.grid(column=0, row=1)

# Кнопка для написания статьи
add_button = ttk.Button(root, text = "Написать", style = "info", command=write_article)
add_button.grid(column=1, row=1)
# Кнопка для удаления статьи
del_button = ttk.Button(root, text = "Удалить", style = "danger", command=delete_article)
del_button.grid(column=2, row=1)

# Открываем основное окно
root.mainloop()