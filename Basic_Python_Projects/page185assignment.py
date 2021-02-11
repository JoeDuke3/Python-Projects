# Import the needed module(s)
import sqlite3
# Assign 'connect' method to a variable for ease of use
conn = sqlite3.connect('dot_txt.db')
# Start a 'with' statement
with conn:
    # Assign 'cursor' method to a variable for ease of use
    cur = conn.cursor()
    # Use 'execute' method to create a new table and
    # put some columns in the table
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt \
        (fileID INTEGER PRIMARY KEY AUTOINCREMENT, \
        fileName TEXT \
        )")
    # Commit table to connected database
    conn.commit()

conn = sqlite3.connect('dot_txt.db')
# Create a tuple to iterate through
fileTuple = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg',)
# Use a for loop to iterate through the tuple
for file in fileTuple:
    if file.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # Insert selected files into table
            cur.execute("INSERT INTO tbl_txt (fileName) VALUES (?)", (file,))
            # Print selected files to console
            print(file)
# Terminate connection
conn.close()
