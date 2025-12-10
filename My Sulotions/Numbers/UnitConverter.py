import curses


def Converter(n: float, Utype, From_Unit, To_Unit) -> float:
    Unit_type = {
        #Tempreture
        0: [
            #meta unit is celsius
            #transforming to celsius
            {
                0: lambda n: n,
                1: lambda n: ((n - 32) * 5) / 9,
                2: lambda n: n - 273.15,
            },
            #transforming from celsius
            {
                0: n,
                1: lambda n: ((9 * n) / 5) + 32,
                2: lambda n: n + 273.15,
            }
        ],
        #Weight
        1: [
            #meta unit is gram
            #transforming to gram
            {
                0: lambda n: n * 1000,
                1: lambda n: n,
                2: lambda n: n / 1000,
                3: lambda n: n * 1000000,
                4: lambda n: n * 453.59237,
                5: lambda n: n * 28.34952,
                6: lambda n: n / 5
            },
            #transforming from gram
            {
                0: lambda n: n / 1000,
                1: lambda n: n,
                2: lambda n: n * 1000,
                3: lambda n: n / 1000000,
                4: lambda n: n / 453.59237,
                5: lambda n: n / 28.34952,
                6: lambda n: n * 5
            }
        ],
        #Length
        2: [
            #meta unit is meter
            #transforming to meter
            {
                0: lambda n: n * 1000,
                1: lambda n: n,
                2: lambda n: n / 100,
                3: lambda n: n / 1000,
                4: lambda n: n * 1609.344,
                5: lambda n: n * 0.9144,
                6: lambda n: n * 0.3048,
                7: lambda n: n * 0.0254 
            },
            #transforming from meter
            {
                0: lambda n: n / 1000,
                1: lambda n: n,
                2: lambda n: n * 100,
                3: lambda n: n * 1000,
                4: lambda n: n / 1609.344,
                5: lambda n: n / 0.9144,
                6: lambda n: n / 0.3048,
                7: lambda n: n / 0.0254 
            },
        ]
    }
    
    return Unit_type[Utype][1][To_Unit](Unit_type[Utype][0][From_Unit](n))
    
# def Length(n: float)
    
class menu():
    def __init__(self, win, menu: list, selected: int, title:str):
        self.win = win
        self.menu = menu
        self.selected = selected
        self.title = title
    
    def draw_title(self) -> None:
        height, width = self.win.getmaxyx()
        self.win.addstr(0,int((width // 2) - (len(self.title) // 2) - len(self.title) % 2), self.title,curses.A_BOLD)

    def draw_menu(self, focused:bool) -> None:
        self.win.erase()
        self.win.box()
        self.draw_title()
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
    def draw_title(win, title, dim) -> None:
        height, width = dim
        win.box()
        win.addstr(0,int((width // 2) - (len(title) // 2) - len(title) % 2),title,curses.A_BOLD)
    
        
    curses.curs_set(0)
    stdscr.erase()
    titles = ["Unit Converter", "Type", "From", "To"]
    hint = "Choose which units you want to convert"
    
    menu_items = ["Tempreture (C°, F°, K°)", "Weight (Kg, G, Lb, Ton, Oz, ....)", "Length (M, Km, Ft, Mile, Inch, .....)"]
    
    Units = [
    ["Celsius", "Fahrenheit", "Kelvin"],
    ["Kilogram", "Gram", "Milligram", "Metric ton", "Pound", "Ounce", "Carat"],
    ["Kilometer", "Meter", "Centimeter", "Millemeter", "Mile", "Yard", "Foot", "Inch"],
    ]
    
    UNIT, FROM, TO, INPUT = range(4)
    
    height, width = stdscr.getmaxyx()    

    draw_title(stdscr, titles[0], stdscr.getmaxyx())
    stdscr.addstr(2, int((width // 2) - (len(hint) // 2) - len(hint) % 2), hint)
    
    
    current_window = 0
    
    Units_win = menu(curses.newwin(len(menu_items) + 2, 48, 3, int((width // 2) - 24)), menu_items, 0,titles[1])
    From_Unit_win = menu(curses.newwin(10, 22, len(menu_items) + 5, (width // 2) - 24) , Units[0], 0,titles[2])
    To_Unit_win = menu(curses.newwin(10, 22, len(menu_items) + 5, (width // 2) + 2), Units[0], 0, titles[3])    
    
    Input_Field_win = curses.newwin(3, 22, len(menu_items) + 15, (width // 2) - 24)
    draw_title(Input_Field_win, titles[2], Input_Field_win.getmaxyx())
    Output_Field_win = curses.newwin(3, 22, len(menu_items) + 15, (width // 2) + 2)
    draw_title(Output_Field_win, titles[3], Output_Field_win.getmaxyx())
    
    stdscr.refresh()
    
    
    Input_Field_win.refresh()
    Output_Field_win.refresh()
    
    while True:
        if (height, width) != stdscr.getmaxyx():
            height, width = stdscr.getmaxyx()
            #recentering main title
            stdscr.erase()
            draw_title(stdscr, titles[0], stdscr.getmaxyx())
            stdscr.addstr(2, int((width // 2) - (len(hint) // 2) - len(hint) % 2), hint)
            
            # recentering menus
            Units_win.win.mvwin(3,int((width // 2) - 24))
            From_Unit_win.win.mvwin(len(menu_items) + 5, (width // 2) - 24)
            To_Unit_win.win.mvwin(len(menu_items) + 5, (width // 2) + 2)
            
            #recentering text fields
            Input_Field_win.mvwin(len(menu_items) + 15, (width // 2) - 24)
            draw_title(Input_Field_win, titles[2], Input_Field_win.getmaxyx())
            
            Output_Field_win.mvwin(len(menu_items) + 15, (width // 2) + 2)
            draw_title(Output_Field_win, titles[3], Output_Field_win.getmaxyx())
            
            
            stdscr.refresh()
            
            Input_Field_win.refresh()
            Output_Field_win.refresh()
            
        
        
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
                elif ch == ord('q'):
                    break
            
            output = Converter(float(user_input), Units_win.selected, From_Unit_win.selected, To_Unit_win.selected)

            Output_Field_win.addstr(1,1,str(output))
            Output_Field_win.refresh()
            
            curses.curs_set(0)
            
            current_window = (current_window + 1) % 4
            continue
        
        key = stdscr.getch()
        
        if current_window == UNIT:
            Units_win.handle_key(key)
        elif current_window == FROM:
            From_Unit_win.handle_key(key)
        elif current_window == TO:
            To_Unit_win.handle_key(key)
        
        if key == ord('\n'):
            current_window = (current_window + 1) % 4
        elif key == 9:
            current_window = (current_window + 1) % 4
        elif key == ord('q'):
            break
        stdscr.refresh()


curses.wrapper(main)
