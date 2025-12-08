import curses

class menu():
    def __init__(self, win, menu: list, selected: int):
        self.win = win
        self.menu = menu
        self.selected = selected

    def draw_menu(self, focused:bool) -> None:
        self.win.erase()
        self.win.box()
        for i, item in enumerate(self.menu):
                if i == self.selected and focused:
                    self.win.addstr(i+1, 2, f"> {item}", curses.A_REVERSE | curses.A_ITALIC)
                else:
                    self.win.addstr(i+1, 2, item)
        self.win.refresh()
    
    def handle_key(self, key):
        if key == curses.KEY_UP and self.selected > 0:
            self.selected -= 1
        elif key == curses.KEY_DOWN and self.selected < len(self.menu) - 1:
            self.selected += 1
        


def main(stdscr):
    curses.curs_set(0)
    stdscr.erase()
    stdscr.box()
    stdscr.addstr(1,10,"Unit Converter",curses.A_BOLD)
    stdscr.addstr(2, 3, "Choose which units you want to convert:")
    menu_items = ["Tempreture (C°, F°, K°)", "Weight (Kg, G, Lb, Ton, Oz, ....)", "Length (M, Km, Ft, Mile, Inch, .....)", "Exit"]
    Units = [
    ["Celsius", "Fahrenheit", "Kelvin"],
    ["Kilogram", "Gram", "Milligram", "Metric ton", "Pound", "Ounce", "Carat"],
    ["Kilometer", "Meter", "Centimeter", "Millemeter", "Mile", "Yard", "Foot", "Inch"],
    []
    ]
    
    UNIT, FROM, TO, INPUT = range(4)
    
    current_window = 0
    
    Units_win = menu(curses.newwin(len(Units) + 2, 50, 3, 1), menu_items, 0)
    From_Unit_win = menu(curses.newwin(10, 15, 11, 5) , Units[0], 0)
    To_Unit_win = menu(curses.newwin(10, 15, 11, 21), Units[0], 0)
    
    Input_Field_win = curses.newwin(3, 15, 25, 5)
    Input_Field_win.box()
    Output_Field_win = curses.newwin(3, 15, 25, 21)
    Output_Field_win.box()
    
    stdscr.refresh()
    
    
    Input_Field_win.refresh()
    Output_Field_win.refresh()
    
    while True:
        
        From_Unit_win.menu = Units[Units_win.selected]
        To_Unit_win.menu = Units[Units_win.selected]
        
        Units_win.draw_menu(current_window == UNIT)
        From_Unit_win.draw_menu(current_window == FROM)
        To_Unit_win.draw_menu(current_window == TO)
        

        if current_window == INPUT:
            curses.curs_set(1)
            Input_Field_win.move(1, 1)

            Input_Field_win.refresh()

            user_input = ""
            while True:
                ch = Input_Field_win.getch()

                if ch in (curses.KEY_ENTER, 10, 13,9):
                    Input_Field_win.addstr(1, 1, ' '*len(user_input))
                    break
                
                elif ch in (curses.KEY_BACKSPACE, 127):
                    if user_input:
                        user_input = user_input[:-1]
                        Input_Field_win.addstr(1,len(user_input) + 1, ' ')
                        Input_Field_win.move(1, len(user_input) +1)
                        Input_Field_win.refresh()
                
                elif chr(ch).isdigit() or (chr(ch) == '.' and '.' not in user_input):
                    user_input += chr(ch)
                    Input_Field_win.addstr(1,1, user_input)
                    Input_Field_win.refresh()

            curses.curs_set(0)
            
            current_window = 0
            continue
        
        key = stdscr.getch()
        
        if current_window == UNIT:
            Units_win.handle_key(key)
        elif current_window == FROM:
            From_Unit_win.handle_key(key)
        elif current_window == TO:
            To_Unit_win.handle_key(key)
        
        if key == ord('\n'):
            if Units_win.selected == len(menu_items) - 1 and current_window == UNIT:
                break
            else:
                current_window += 1
        elif key == 9:
            current_window += 1
        elif key == ord('q'):
            break
        stdscr.refresh()


curses.wrapper(main)
