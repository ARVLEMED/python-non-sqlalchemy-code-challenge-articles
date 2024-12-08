class Article:
    all = []

    def __init__(self, author, magazine, title):
        # Validate title
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        
        self._title = title
        self.author = author
        self.magazine = magazine

        # Append to the global Article.all list
        Article.all.append(self)
        
        # Also add to the magazine's list of articles
        self.magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise ValueError("Cannot change the title of an article once it is set")

    def __repr__(self):
        return f"Article(title={self.title}, author={self.author.name}, magazine={self.magazine.name})"

class Author:
    def __init__(self, name):
        # Validate name
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if len(name) == 0:  
            raise ValueError("Name cannot be empty.")
        
        self._name = name
        self._articles = []  # List to store articles authored by this author

    @property
    def name(self):
        return self._name

    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("article must be an instance of Article")
        # Add the article to the author's list of articles if not already present
        if article not in self._articles:
            self._articles.append(article)

    def articles(self):
        return self._articles  # Return the list of articles for this author

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def topic_areas(self):
        # Get unique topic areas for this author
        return list(set([article.magazine.category for article in self.articles()]))

    def __repr__(self):
        return f"Author(name={self.name})"

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")  # Changed to ValueError
        self._name = name
        self.category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Check if the value is a string, if not raise a ValueError
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")  # Changed to ValueError
        self._name = value

    def add_article(self, article):
        if article not in self._articles:
            self._articles.append(article)

    def articles(self):
        return self._articles

    def contributors(self):
        # Returns unique authors who have contributed to this magazine
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        # Returns a list of titles of all articles in the magazine
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        # Returns the authors who have contributed to this magazine
        return self.contributors()

    def __repr__(self):
        return f"Magazine(name={self.name}, category={self.category})"
