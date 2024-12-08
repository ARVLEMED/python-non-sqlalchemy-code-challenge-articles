class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters")
        
        self._title = title
        self.author = author
        self.magazine = magazine

        # Append to the global Article.all list
        Article.all.append(self)
        # Add article to the magazine
        self.magazine.add_article(self)  # Ensure the article is added to the magazine

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
        """Initialize the Author with a name."""
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []  # To hold the articles written by the author

    @property
    def name(self):
        """Return the author's name."""
        return self._name

    def add_article(self, magazine, title):
        """Receives a Magazine instance and a title as arguments.
        Creates and returns a new Article instance and associates it with this author and the provided magazine.
        """
        # Create a new Article object and associate it with this author and magazine
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def articles(self):
        """Returns a list of all articles the author has written."""
        return self._articles

    def topic_areas(self):
        """Returns a unique list of categories of the magazines the author has contributed to.
        Returns None if the author has no articles.
        """
        if not self._articles:
            return None
        # Return unique categories for all magazines the author has written for
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    all = []  # Class variable to store all magazine instances

    def __init__(self, name, category):
        """Initialize the Magazine with a name and category."""
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        
        self._name = name
        self._category = category
        self._articles = []  # To hold articles related to this magazine
        Magazine.all.append(self)  # Keep track of all magazine instances

    @property
    def name(self):
        """Return the name of the magazine."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Change the magazine name if valid."""
        if not isinstance(new_name, str) or len(new_name) < 2 or len(new_name) > 16:
            raise ValueError("Magazine name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        """Return the category of the magazine."""
        return self._category

    @category.setter
    def category(self, new_category):
        """Change the category if valid."""
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        """Returns a list of all articles published in the magazine."""
        return self._articles

    def article_titles(self):
        """Returns a list of titles of all articles written for this magazine.
        Returns None if the magazine has no articles.
        """
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def add_article(self, article):
        """Add an article to the magazine."""
        if not isinstance(article, Article):
            raise ValueError("Only Article instances can be added.")
        self._articles.append(article)

    def contributors(self):
        """Returns a list of unique authors who have contributed to this magazine."""
        # Use a set to ensure uniqueness, then return the list
        contributors = set(article.author for article in self._articles)
        return list(contributors)

    def contributing_authors(self):
        """Returns a list of authors who have written more than 2 articles for the magazine.
        Returns None if no authors have written more than 2 articles.
        """
        authors_count = {}
        for article in self._articles:
            author = article.author
            authors_count[author] = authors_count.get(author, 0) + 1
        
        # Get authors who have written more than 2 articles
        contributing_authors = [author for author, count in authors_count.items() if count > 2]
        
        if not contributing_authors:
            return None
        return contributing_authors

    @classmethod
    def top_publisher(cls):
        """Returns the magazine with the most articles."""
        if not cls.all:  # If no magazines are present
            return None
        
        # Find the magazine with the most articles
        top_magazine = max(cls.all, key=lambda magazine: len(magazine.articles()))
        
        # Check if the magazine has articles
        if len(top_magazine.articles()) == 0:
            return None
        
        return top_magazine
