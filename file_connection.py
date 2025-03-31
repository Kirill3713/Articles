# Импортируем модули
import json

# Создаем функции
def get_articles() -> dict:
    """
    Функция, для прочтения статей
    """
    with open("articles.json", 'r', encoding="utf-8") as json_file:
        articles = json.load(json_file)
        return articles

def add_article(name: str, text: str) -> None:
    """
    Функция, для добавления статьи
    """
    articles = get_articles()
    articles[name] = text
    with open("articles.json", "w", encoding="utf-8") as json_file:
        json.dump(articles, json_file, ensure_ascii=False)

def del_article(name: str) -> None:
    """
    Функця, для удаления статьи
    """
    articles = get_articles()
    del articles[name]
    with open("articles.json", "w", encoding="utf-8") as json_file:
        json.dump(articles, json_file, ensure_ascii=False)

# Точка входа
if __name__ == "__main__":
    get_articles()
    add_article("1", "456yuhnjj")
    del_article("1")