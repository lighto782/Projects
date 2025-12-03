'''
 A simple calculator to do basic operators. Make it a scientific calculator for added complexity.
'''

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Footer, Header, Static, TextArea, Button

class NumberPad(Static):
    '''Custom Number pad'''
    
    def compose(self) -> ComposeResult:
        with Container(id="numpad"):
            yield Button("9")
            yield Button("8")
            yield Button("7")
            yield Button("(")
            yield Button(")")
            yield Button("6")
            yield Button("5")
            yield Button("4")
            yield Button("*")
            yield Button("/")
            yield Button("3")
            yield Button("2")
            yield Button("1")
            yield Button("+")
            yield Button("-")
            yield Button(".")
            yield Button("0", classes="spantwo")
            yield Button("=", classes="spantwo")

            
class calculator(App):
    
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    
    CSS_PATH = "Calculator.css"
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        # yield TextArea()
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
