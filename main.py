import pickle
from time import strftime
import countnotes

def main():
    try:
        filename = "notebook.dat"
        notebook = open(filename, "rb")
    except Exception:
        print("No default notebook was found, created one.")
        notebook = open(filename, "ab")

    while True:
        print("(1) Read the notebook\n(2) Add note\n\
(3) Edit a note\n(4) Delete a note\n(5) Save and quit")
        userInput = input("Please select one: ")

        if userInput == "1":
            notebook = open(filename, "rb")
            while True:
                try:
                    print(pickle.load(notebook))
                except EOFError:
                    notebook.close()
                    break

        elif userInput == "2":
            notebook = open(filename, "ab")
            noteText = input("Write a new note: ")
            noteText = noteText + ":::" + strftime("%X %x")
            pickle.dump(noteText, notebook)
            notebook.close()

        elif userInput == "3":
            count, notes = countnotes.countNotes()
            notebook = open(filename, "wb")
            place = int(input("Which of them will be changed?: "))
            place -= 1
            print(notes[place])
            noteEdit = input("Give the new note: ")
            noteEdit = noteEdit + ":::" + strftime("%X %x")
            notes[place] = noteEdit
            i = int(0)
            while i < count:
                pickle.dump(notes[i], notebook)
                i += 1
            notebook.close()

        elif userInput == "4":
            count, notes = countnotes.countNotes()
            place = int(input("Which of them will be deleted?: "))
            place -= 1
            try:
                print("Deleted note", notes[place])
                notes.pop(place)
            except IndexError:
                print("Invalid index!")
                continue
            i = int(0)
            notebook = open(filename, "wb")
            while i < len(notes):
                pickle.dump(notes[i], notebook)
                i += 1
            notebook.close()
        elif userInput == "5":
            print("Notebook shutting down, thank you.")
            notebook.close()
            break

if __name__ == "__main__":
    main()