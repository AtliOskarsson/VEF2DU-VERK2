from application import app

class book:
	def __init__(self, booklist):
		self.book = booklist["book"]
		self.author = booklist["author"]
		self.release = booklist["release"]
		self.publisher = booklist["publisher"]
		self.url = booklist["url"]

	def book(self):
		return self.book

	def url(self):
		return self.url

	def about(self):
		return "{book} is written by {author} released in {release} by {publisher}".format(book = self.book, author = self.author, release = self.release, publisher = self.publisher)

class urlCheck:
	def __init__(self, booklist, url):
		self.booklist = booklist
		self.url = url

	def check(self):
		for x in self.booklist:
			if self.url == x.url:
				return x

booklist = [book({"book":"The Fellowship Of The Ring","publisher":"George Allen & Unwin","release":"1954","author":"J. R. R. Tolkein","url":"The-Fellowship-Of-The-Ring"}),
           book({"book":"The Two Towers","publisher":"George Allen & Unwin","release":"1954","author":"J. R. R. Tolkein","url":"The-Two-Towers"}),
           book({"book":"Return Of The King","publisher":"George Allen & Unwin","release":"1955","author":"J. R. R. Tolkein","url":"Return-Of-The-King"})]