
def write_to_file(notes):
    with open('Notes_app/database.txt', 'w') as f:
        for note in notes:
            f.write(f"{note['title']}: {note['text']}\n\n")

def read_from_file():
    with open('Notes_app/database.txt', 'r') as f:
        notes=[]
        for line in f:
            x=line.split(':')
            if len(x)>1:
                notes.append({'title': x[0], 'text': x[1]})
        return notes

notes = read_from_file()