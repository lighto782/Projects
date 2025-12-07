import curses


def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.addstr(0,1,"Unit Converter",curses.A_BOLD)
    stdscr.addstr(1, 3, "Choose which units you want to convert:")
    menu_items = ["Tempreture (C°, F°, K°)", "Weight (Kg, G, Lb, Ton, Oz, ....)", "Length (M, Km, Ft, Mile, Inch, .....)", "Exit"]
    Units = [
    ["Celsius", "Fahrenheit", "Kelvin"],
    ["Kilogram", "Gram", "Milligram", "Metric ton", "Pound", "Ounce", "Carat"],
    ["Kilometer", "Meter", "Centimeter", "Millemeter", "Mile", "Yard", "Foot", "Inch"],
    []
    ]
    
    whereis = 0
    
    selected = 0
    selected_from = 0
    selected_to = 0
    
    debug_win = curses.newwin(8, 15, 0, 30)
    
    From_Unit_win = curses.newwin(10, 14, 9, 5)
    To_Unit_win = curses.newwin(10, 14, 9, 21)
    Input_Field_win = curses.newwin(3, 14, 20, 5)
    Output_Field_win = curses.newwin(3, 14, 20, 21)
    
    while True:
        for i, item in enumerate(menu_items):
            if i == selected and whereis % 4 == 0:
                stdscr.move(i+3,1)
                stdscr.clrtoeol()
                stdscr.addstr(i+3, 4, f"> {item}", curses.A_REVERSE)
            else:
                stdscr.move(i+3,1)
                stdscr.clrtoeol()
                stdscr.addstr(i+3, 4, item)
        
        From_Unit_win.clear()
        From_Unit_win.box()
        for j, conv in enumerate(Units[selected]):
            if j == selected_from and whereis % 4 == 1:
                From_Unit_win.move(j+1,0)
                From_Unit_win.clrtoeol()
                From_Unit_win.addstr(j+1, 1, f"> {conv}", curses.A_REVERSE)
            else:
                From_Unit_win.addstr(j+1, 1, f"{conv}")
        From_Unit_win.refresh()
        
        To_Unit_win.clear()
        To_Unit_win.box()
        for k, conv in enumerate(Units[selected]):
            if k == selected_to and whereis % 4 == 2:
                To_Unit_win.move(k+1,0)
                To_Unit_win.clrtoeol()
                To_Unit_win.addstr(k+1, 1, f"> {conv}", curses.A_REVERSE)
            else:
                To_Unit_win.addstr(k+1, 1, f"{conv}")
        To_Unit_win.refresh()
        
        Input_Field_win.clear()
        Input_Field_win.box()
        Input_Field_win.addstr(1,1,"")
        Input_Field_win.refresh()
        
        Output_Field_win.clear()
        Output_Field_win.box()
        Output_Field_win.addstr(1,1,"")
        Output_Field_win.refresh()
        
        debug_win.clear()
        key = stdscr.getch()
        
        if whereis % 4 == 3:
            curses.curs_set(1)              
            Input_Field_win.clear()
            Input_Field_win.box()
            Input_Field_win.refresh()

            Input_Field_win.move(1, 1)

            user_text = ""
            while True:
                ch = Input_Field_win.getch()

                if ch in (curses.KEY_ENTER, 10, 13):
                    break
                elif ch in (curses.KEY_BACKSPACE, 127):
                    if user_text:
                        user_text = user_text[:-1]
                        Input_Field_win.move(1, 1)
                        Input_Field_win.clrtoeol()
                        Input_Field_win.box()
                        Input_Field_win.addstr(1,1, user_text)
                        Input_Field_win.refresh()
                elif chr(ch).isdigit() or chr(ch) == '.':
                    user_text += chr(ch)
                    Input_Field_win.addstr(1,1, user_text)
                    Input_Field_win.refresh()

            curses.curs_set(0)
            
            whereis += 1
            continue
            
        if key == curses.KEY_UP and selected > 0 and whereis % 4 == 0:
            selected -= 1
            debug_win.addnstr(str(selected), 1, 1)
            debug_win.refresh()
        elif key == curses.KEY_UP and selected_from > 0 and whereis % 4 == 1:
            selected_from -=1
            debug_win.addnstr(str(selected), 1, 1)
            debug_win.refresh()
        elif key == curses.KEY_UP and selected_to > 0 and whereis % 4 == 2:
            selected_to -=1
            debug_win.addnstr(str(selected), 1, 1)
            debug_win.refresh()
        elif key == curses.KEY_DOWN and selected < len(menu_items) - 1 and whereis % 4 == 0:
            selected += 1
            debug_win.addnstr(str(selected), 1, 1)
            debug_win.refresh()
        elif key == curses.KEY_DOWN and selected_from < len(Units[selected]) - 1 and whereis % 4 == 1:
            selected_from +=1
            debug_win.addnstr(str(selected), 1, 1)
            debug_win.refresh()
        elif key == curses.KEY_DOWN and selected_to < len(Units[selected]) - 1 and whereis % 4 == 2:
            selected_to +=1
            debug_win.addnstr(str(selected), 1, 1)
            debug_win.refresh()
        elif key == ord('\n'):
            if selected == len(menu_items) - 1 and whereis % 4 == 0:
                break
            else:
                whereis += 1
        elif key == ord('q'):
            break
        stdscr.refresh()


curses.wrapper(main)
