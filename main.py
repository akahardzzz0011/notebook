import pickle
from time import strftime


def main():
    try:
        tiedostonimi = "notebook.dat"
        notebook = open(tiedostonimi, "rb")
    except Exception:
        print("No default notebook was found, created one.")
        notebook = open(tiedostonimi, "ab")

    while True:
        print("(1) Read the notebook\n(2) Add note\n\
(3) Edit a note\n(4) Delete a note\n(5) Save and quit")
        userInput = input("Please select one: ")
        if userInput == "1":
            notebook = open(tiedostonimi, "rb")
            while True:
                try:
                    print(pickle.load(notebook))
                except EOFError:
                    break
        elif userInput == "2":
            notebook = open(tiedostonimi, "ab")
            noteText = input("Write a new note: ")
            noteText = noteText + ":::" + strftime("%X %x")
            pickle.dump(noteText, notebook)
            notebook.close()
        elif userInput == "3":
            notebook = open(tiedostonimi, "rb")
            count = int(0)
            notes = []
            while True:
                try:
                    notes.append(pickle.load(notebook))
                    count += 1
                except EOFError:
                    print("The list has", count, "notes.", sep=" ")
                    break
            notebook = open(tiedostonimi, "wb")
            place = int(input("Which of them will be changed?: "))
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
            print("4")
        elif userInput == "5":
            print("Notebook shutting down, thank you.")
            notebook.close()
            break


if __name__ == "__main__":
    main()