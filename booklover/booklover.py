import pandas as pd

class BookLover:
    '''
    ATTRIBUTES:
    name str
    email str
    fav_genre str
    num_books int
    book_list pandas dataframe
    '''

    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list
    
    def add_book(self, book_name, rating):
        '''
        PURPOSE: adds a book to the object's book list

        INPUTS
        book_name str
        rating int
        '''

        curr_list = self.book_list
        if len(curr_list[curr_list['book_name'] == book_name]) == 0:
            new_book = pd.DataFrame({
                'book_name': [book_name],
                'book_rating': [rating]
            })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index = True)
            self.num_books = len(self.book_list)
        else:
            print('Book is already in your list!')
    
    def has_read(self, book_name):
        '''
        PURPOSE: checks if a book is already in the object's book list

        INPUTS:
        book_name str

        OUTPUTS:
        bool
        '''

        curr_list = self.book_list
        if len(curr_list[curr_list['book_name'] == book_name]) > 0:
            return True
        else:
            return False
    
    def num_books_read(self):
        '''
        PURPOSE: returns the number of books the object has already read

        OUTPUTS:
        int
        '''

        return self.num_books
    
    def fave_books(self):
        '''
        PURPOSE: returns a subset of the book_list dataframe with ratings > 3

        OUTPUTS:
        pandas dataframe
        '''

        curr_list = self.book_list
        return curr_list[curr_list['book_rating'] > 3]