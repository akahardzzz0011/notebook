import pickle

def countNotes():
    filename = "notebook.dat"
    notebook = open(filename, "rb")
    count = int(0)
    notes = []
    while True:
        try:
            notes.append(pickle.load(notebook))
            count += 1
        except EOFError:
            print("The list has", count, "notes.", sep=" ")
            break
    return count, notes