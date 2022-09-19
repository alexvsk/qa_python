from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_an_existing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        collector.add_new_book('Тестирование Дот Ком')
        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_set_rating_for_missing_book(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        collector.set_book_rating('Программируем на Python', 2)
        assert collector.get_books_rating().get('Программируем на Python') is None

    def test_set_book_rating_set_rating_less_than_one(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        collector.set_book_rating('Тестирование Дот Ком', 0)
        assert collector.get_books_rating().get('Тестирование Дот Ком') == 1

    def test_set_book_rating_set_rating_more_than_ten(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        collector.set_book_rating('Тестирование Дот Ком', 11)
        assert collector.get_books_rating().get('Тестирование Дот Ком') == 1

    def test_get_book_rating_return_type_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        assert dict(collector.get_books_rating())

    def test_get_books_with_specific_rating_get_one_book_by_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        collector.set_book_rating('Тестирование Дот Ком', 5)
        collector.add_new_book('Программируем на Python')
        collector.set_book_rating('Программируем на Python', 3)
        assert collector.get_books_with_specific_rating(3)[0] == 'Программируем на Python'

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        collector.add_book_in_favorites('Тестирование Дот Ком')
        assert 'Тестирование Дот Ком' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Тестирование Дот Ком')
        collector.add_book_in_favorites('Тестирование Дот Ком')
        collector.delete_book_from_favorites('Тестирование Дот Ком')
        assert 'Тестирование Дот Ком' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_add_missing_book(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Тестирование Дот Ком')
        assert 'Тестирование Дот Ком' not in collector.get_list_of_favorites_books()
