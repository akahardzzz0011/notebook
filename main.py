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
        print("(1) Read the notebook\n(2)Add note\n\
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
        elif userInput == "3":
            print("3")
        elif userInput == "4":
            print("4")
        elif userInput == "5":
            print("Notebook shutting down, thank you.")
            notebook.close()
            break


if __name__ == "__main__":
    main()