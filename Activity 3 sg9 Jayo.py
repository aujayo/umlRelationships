class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    # Getters and Setters for encapsulation
    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def display_info(self):
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")


class Book(Publication):
    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.__number_of_pages = 0
        self.set_number_of_pages(number_of_pages)

    def get_number_of_pages(self):
        return self.__number_of_pages

    def set_number_of_pages(self, number_of_pages):
        if number_of_pages > 0:
            self.__number_of_pages = number_of_pages
        else:
            print("The number of pages must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.__number_of_pages}")


class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = 0
        self.set_issue_number(issue_number)

    def get_issue_number(self):
        return self.__issue_number

    def set_issue_number(self, issue_number):
        if issue_number > 0:
            self.__issue_number = issue_number
        else:
            print("The issue number must be positive.")

    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.__issue_number}")


# --- Testing the Classes ---
if __name__ == "__main__":
    print("=== PUBLICATIONS ===")
    pub1 = Publication("School Charter", "Admin Office")
    pub2 = Publication("Annual Research Journal", "Science Department")
    
    pub1.display_info()
    print("-" * 25)
    pub2.display_info()

    print("\n=== BOOKS ===")
    book1 = Book("To Kill a Mockingbird", "Harper Lee", 281)
    book2 = Book("1984", "George Orwell", 328)
    
    book1.display_info()
    print("-" * 25)
    book2.display_info()

    print("\n=== MAGAZINES ===")
    mag1 = Magazine("National Geographic", "Various Authors", 145)
    mag2 = Magazine("Time Magazine", "Time Editorial Board", 89)
    
    mag1.display_info()
    print("-" * 25)
    mag2.display_info()

    print("\n=== VALIDATION TEST ===")
    invalid_book = Book("Sample Book", "Unknown", -5)
    invalid_mag = Magazine("Sample Mag", "Editor", 0)
