from booklover.booklover import BookLover
import unittest

class BookLoverTestSuite(unittest.TestCase):
    '''
    Test functions for testing the BookLover class.
    '''

    def test_1_add_book(self):
        '''
        PURPOSE: tests the BookLover.add_book() method
        '''

        book_lover = BookLover(name = 'Eric', email = 'emt4wf@virginia.edu', fav_genre = 'Science')
        book_name = 'Learning Python'
        book_rating = 4
        book_lover.add_book(book_name = book_name, rating = book_rating)
        
        self.assertTrue(book_name in book_lover.book_list['book_name'].values, 'book not added properly')
    
    def test_2_add_book(self):
        '''
        PURPOSE: tests the BookLover.add_book() method for adding duplicate books
        '''

        book_lover = BookLover(name = 'Eric', email = 'emt4wf@virginia.edu', fav_genre = 'Science')
        book_name = 'Learning Python'
        book_rating = 4
        book_lover.add_book(book_name = book_name, rating = book_rating)
        book_lover.add_book(book_name = book_name, rating = book_rating)

        book_list = book_lover.book_list
        expected_len = 1

        self.assertEqual(len(book_list[book_list['book_name'] == book_name]), expected_len)
    
    def test_3_has_read(self):
        '''
        PURPOSE: tests the BookLover.has_read() method
        '''

        book_lover = BookLover(name = 'Eric', email = 'emt4wf@virginia.edu', fav_genre = 'Science')
        book_name = 'Learning Python'
        book_rating = 4
        book_lover.add_book(book_name = book_name, rating = book_rating)
        
        self.assertTrue(book_lover.has_read(book_name = book_name), 'book not marked as read')
    
    def test_4_has_read(self):
        '''
        PURPOSE: tests the BookLover.has_read() method for books that haven't been added
        '''

        book_lover = BookLover(name = 'Eric', email = 'emt4wf@virginia.edu', fav_genre = 'Science')
        book_name = 'Learning Python'
        
        self.assertFalse(book_lover.has_read(book_name = book_name), 'non-existent book marked as read')
    
    def test_5_num_books_read(self):
        '''
        PURPOSE: tests the BookLover.num_books_read() method
        '''

        book_lover = BookLover(name = 'Eric', email = 'emt4wf@virginia.edu', fav_genre = 'Science')
        book_lover.add_book(book_name = 'Learning Python', rating = 4)
        book_lover.add_book(book_name = 'Surfing the Data Pipeline', rating = 5)

        total_books = 2

        self.assertEqual(book_lover.num_books_read(), total_books)
    
    def test_6_fav_books(self):
        '''
        PURPOSE: tests the BookLover.fav_books() method
        '''

        book_lover = BookLover(name = 'Eric', email = 'emt4wf@virginia.edu', fav_genre = 'Science')
        book_lover.add_book(book_name = 'Learning Python', rating = 4)
        book_lover.add_book(book_name = 'Surfing the Data Pipeline', rating = 5)
        book_lover.add_book(book_name = 'Math', rating = 3)

        fav_books = book_lover.fave_books()
        filtered_fav_books = fav_books[fav_books['book_rating'] > 3]

        self.assertEqual(len(fav_books), len(filtered_fav_books))

if __name__ == '__main__':
    unittest.main(verbosity = 3)