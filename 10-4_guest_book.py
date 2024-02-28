from pathlib import Path

path_guest_book = Path('guest_book.txt')

active = True     #flag to end program when false
new_guests = ''

while active:
    new_guest = input('\nWelcome! Please sign our guest book or type "exit" to close the guest book:  ')
    if new_guest.lower() == 'exit' or new_guest.lower() == 'x':
        active = False   
        print("Bye!") 
    else:
        new_guests = new_guests + new_guest + '\n'
        path_guest_book.write_text(new_guests)
        print(f"\n**********\nThank you, {new_guest}!\n**********")
