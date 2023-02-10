import sqlite3
book=sqlite3.connect("book.db")
curbook=book.cursor()
"""
curbook.execute(""""""Create table book(Book_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT(50) NOT NULL,
                Author TEXT(50) NOT NULL,
                Price REAL(10) NOT NULL);"""""")"""

curbook.execute("""insert into book values(1,
"The Diary of a young girl",
"Anne Frank",
107.52);""")
curbook.execute("""insert into book values(2,
"Hamlet",
"William Shakespeare",
152.53);""")
curbook.execute("""insert into book values(3,
"Othello",
"William Shakespeare",
153.52);""")
curbook.execute("""insert into book values(4,
"The prelude",
"William Wordsworth",
95.62);""")
book.commit()
book.close()
