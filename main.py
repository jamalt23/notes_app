from database import notes, write_to_file, read_from_file; import pyperclip
# Show all notes
def all_notes():
    print('All your notes: ')
    for note in notes:
        print(f' {note["title"]}')

# Add note
def add():
    title = input("Enter note title: ")
    text = input("Enter note text: ")
    notes.append({'title': title,'text': text})

# Delete note
def delete():
    temp=input('What note do you want to delete? (Enter title)\n').title()
    for note in notes:
        if note['title'].title()==temp:
            print(f'Note with title {note["title"]} was deleted.')
            notes.remove(note);return True
    print(f'Note with title {temp} was not found.');return False

# Rename note
def rename():
    temp=input('What note do you want to rename? (Enter title)\n').title()
    for note in notes:
        if note['title'].title()==temp:
            new_title=input('Enter new title: ').title()
            note['title']=new_title
            print(f'Note was succesfully renamed!');return True
    print(f'Note {temp} was not found.');return False

# Edit note
def edit():
    temp=input('What note do you want to edit? (Enter title)\n').title()
    for note in notes:
        if note['title'].title()==temp:
            pyperclip.copy(note['text'])
            new_text=input('Enter new text (previous text copied to clipboard):\n')
            note['text']=new_text
            print(f'Note was succesfully edited!');return True
        
# Start
print('\nWelcome to your notes app!')
all_notes()
operation=input('\nWhat do you want to do? (add, delete, rename, edit, quit)\nI want to ')
while True:
    if operation=='add':
        add()
    elif operation=='delete':
        delete()
    elif operation=='rename':
        rename()
    elif operation=='edit':
        edit()
    elif operation=='quit':
        quit()
    else:
        print('Invalid operation.')
    write_to_file(notes)
    all_notes()
    operation=input('What do you want to do? (add,delete,rename,edit)\nI want to ')