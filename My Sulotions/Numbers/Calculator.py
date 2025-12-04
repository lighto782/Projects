'''
 A simple calculator to do basic operators. Make it a scientific calculator for added complexity.
'''

from textual import events, on
from textual.reactive import reactive
from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, Static, TextArea, Button

class NumberPad(Static):
    '''Custom Number pad'''
    
    def compose(self) -> ComposeResult:
        with Container(id="numpad"):
            yield Button("9", id="n9")
            yield Button("8", id="n8")
            yield Button("7", id="n7")
            yield Button("(", id="rightB")
            yield Button(")", id="leftB")
            yield Button("6", id="n6")
            yield Button("5", id="n5")
            yield Button("4", id="n4")
            yield Button("*", id="multi")
            yield Button("/", id="divide")
            yield Button("3", id="n3")
            yield Button("2", id="n2")
            yield Button("1", id="n1")
            yield Button("+", id="add")
            yield Button("-", id="sub")
            yield Button("0", id="n0")
            yield Button(".", id="point")
            yield Button("+/-", id="neg")
            yield Button("=", id="equal",  classes="spantwo")

class Display(Static):
    text = reactive("Hello")
    

            
class calculator(App):
    
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    
    CSS_PATH = "Calculator.css"
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        with Container(id="calculator"):
            yield Display("HHHH", id="screen")
            yield NumberPad()
        
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )
        



if __name__ == "__main__":
    app = calculator()
    app.run()
# end main
