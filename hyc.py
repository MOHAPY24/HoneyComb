from honeycomb import Interperter
import os

cptr = 0

if __name__ == "__main__":
    print("HoneyComb 0.0.1 BETA REPL, GPL 3.0 License Copyright Mohammed Abdelaal. \nPython 3.9 \n'--help' for more information.\n")
    inte = Interperter()
    while True:
        cmd = input(f"in [{cptr}] HoneyComb $$> ").strip()
        if cptr >= 20:
            if os.name == 'nt':
                os.system("cls")
                print("HoneyComb 0.0.1 BETA REPL, GPL 3.0 License Copyright Mohammed Abdelaal. \nPython 3.9 \n'--help' for more information.\n")
                cptr = 0
                pass
            else:
                os.system("clear")
                print("HoneyComb 0.0.1 BETA REPL, GPL 3.0 License Copyright Mohammed Abdelaal. \nPython 3.9 \n'--help' for more information.\n")
                cptr = 0
                pass
        if '--help' in cmd:
            print("HoneyComb 0.0.1 \nHoneyComb is a Esoteric Programming Language (Esolang) made to have a tape like structure simular to a Honeycomb.\nHaving 3D movement throughout the Honeycomb expanding from up and down to entering a sector of a Honeycomb.\nWriten in Python 3.15.0, it is lightweight (written under 300 lines), memory safe, cleaned up automaticly by Python and the normal interperter itself and modular.\n\n '+' -- Add one to current cell in current axis in current comb.\n '-' -- Minus one from current cell in current axis in current comb.\n '.' -- Print raw value of current cell in current axis in current comb.")
            pass
        if "quit" in cmd:
            break
        inte.add_code(cmd)
        inte.parse()
        cptr += 1