import curses


def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0,0,"Unit Converter",curses.A_BOLD)
    stdscr.addstr(1, 0, "Choose which units you want to convert:")
    menu_items = ["Tempreture (C° <=> F°)", "Weight (Kg <=> Lb)", "Speed (Km/h <=> Mi/h)", "Distence (Meter <=> Feet)","Exit"]
    selected = 0

    while True:
        for i, item in enumerate(menu_items):
            if i == selected:
                stdscr.move(i+3,1)
                stdscr.clrtoeol()
                stdscr.addstr(i+3, 1, f"> {item}", curses.A_REVERSE)
            else:
                stdscr.move(i+3,1)
                stdscr.clrtoeol()
                stdscr.addstr(i+3, 1, item)

        key = stdscr.getch()
        if key == curses.KEY_UP and selected > 0:
            selected -= 1
        elif key == curses.KEY_DOWN and selected < len(menu_items) - 1:
            selected += 1
        elif key == ord('\n'):
            if selected == len(menu_items) - 1:
                break
            else:
                stdscr.addstr(len(menu_items)+3, 1, f"You selected {menu_items[selected]}")
                stdscr.refresh()
                stdscr.getch()
        elif key == ord('q'):
            break
        stdscr.refresh()


curses.wrapper(main)
