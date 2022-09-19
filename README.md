# qa_python
### Описание тестов 'TestBooksCollector' для приложения 'BooksCollector':
1. Метод `test_add_new_book_add_two_books(self)` - проверка добавления книг в словарь books_rating.
2. Метод `test_add_new_book_add_an_existing_book(self)` - проверка, что нельзя добавить одну и ту же книгу дважды в словарь books_rating.
3. Метод `test_set_book_rating_set_rating_for_missing_book(self)` - проверка, что нельзя выставить рейтинг книге, которая не добавлена.
4. Метод `test_set_book_rating_set_rating_less_than_one(self)` - проверка, что нельзя выставить рейтинг меньше 1 добавленной книге.
5. Метод `test_set_book_rating_set_rating_more_than_ten(self)` - проверка, что нельзя выставить рейтинг больше 10 добавленной книге.
6. Метод `test_get_book_rating_return_type_dict(self)` - проверка, что метод `get_book_rating(self, name)` действительно возвращает словарь.
7. Метод `test_get_books_with_specific_rating_get_one_book_by_rating(self)` - проверка, что метод `get_books_with_specific_rating(self, rating)` возвращает список с валидными значениями (наеменованием книги). 
8. Метод `test_add_book_in_favorites_add_one_book(self)` - проверка добавления книги в избранное (список favorites).
9. Метод `test_delete_book_from_favorites_delete_one_book(self)` - проверка удаления имеющейся книги из избранного (список favorites).
10. Метод `test_get_list_of_favorites_books_add_missing_book(self)` - проверка, что нельзя добавить книгу в избранное (список favorites), если её нет в словаре books_rating.