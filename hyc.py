from honeycomb import Interperter
import os
import sys

inte = Interperter()

try:
    if sys.argv and '.hc' in sys.argv[1]:
        inte.load_file_code(str(sys.argv[1]))
        inte.parse()
        print()
        quit(0)
except IndexError:
    pass

cptr = 0



if __name__ == "__main__":
    print("HoneyComb 1.0.0 BETA REPL, GPL 3.0 License Copyright Mohammed Abdelaal. \nPython 3.9 \n'--help' for more information.\n")
    while True:
        cmd = input(f"in [{cptr}] HoneyComb $$> ").strip()
        if cptr >= 20:
            if os.name == 'nt':
                os.system("cls")
                print("HoneyComb 1.0.0 BETA REPL, GPL 3.0 License Copyright Mohammed Abdelaal. \nPython 3.9 \n'--help' for more information.\n")
                cptr = 0
                pass
            else:
                os.system("clear")
                print("HoneyComb 1.0.0 BETA REPL, GPL 3.0 License Copyright Mohammed Abdelaal. \nPython 3.9 \n'--help' for more information.\n")
                cptr = 0
                pass
        if '--help' in cmd:
            print("HoneyComb 1.0.0 \nHoneyComb is a Esoteric Programming Language (Esolang) made to have a tape like structure simular to a Honeycomb.\nHaving 3D movement throughout the Honeycomb expanding from up and down to entering a sector of a Honeycomb.\nWriten in Python 3.15.0, it is lightweight, memory safe, cleaned up automaticly by Python and the normal interperter itself and modular.")
            pass
        elif "quit" in cmd:
            break
        else:
            inte.add_code(cmd)
            inte.parse()
            print()
        
        cptr += 1
