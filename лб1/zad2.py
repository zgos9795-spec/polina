disk_volume = 1.44  # In MB
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
char_size = 4  # In bytes

books_on_disk = int((disk_volume * 1024 ** 2) // (pages_per_book * lines_per_page * chars_per_line * char_size))
print("Number of books that can fit on the disk:", books_on_disk)