'''
 A simple calculator to do basic operators. Make it a scientific calculator for added complexity.
'''

from decimal import Decimal

from textual import events, on
from textual.reactive import reactive, var
from textual.app import App, ComposeResult
from textual.containers import Container, VerticalGroup
from textual.widgets import Footer, Header, Static, Button, Digits

class NumberPad(Static):
    '''Custom Number pad'''
    
    def compose(self) -> ComposeResult:
        with Container(id="numpad"):
            yield Button("9", id="n9", classes="number")
            yield Button("8", id="n8", classes="number")
            yield Button("7", id="n7", classes="number")
            yield Button("(", id="lbracket", variant="warning")
            yield Button(")", id="rbracket", variant="warning")
            yield Button("6", id="n6", classes="number")
            yield Button("5", id="n5", classes="number")
            yield Button("4", id="n4", classes="number")
            yield Button("*", id="multi", variant="warning")
            yield Button("/", id="divide", variant="warning")
            yield Button("3", id="n3", classes="number")
            yield Button("2", id="n2", classes="number")
            yield Button("1", id="n1", classes="number")
            yield Button("+", id="add", variant="warning")
            yield Button("-", id="sub", variant="warning")
            yield Button("C", id="reset", variant="error")
            yield Button("0", id="n0", classes="number")
            yield Button(".", id="point", variant="primary")
            yield Button("=", id="equal",  classes="spantwo", variant="success")


class Display(Static):
    
    def compose(self) -> ComposeResult:
        with VerticalGroup(id ="screen"):
            yield Static("0", id="equation")
            yield Digits("0", id="result")
        

            
class calculator(App):
    
    
    CSS_PATH = "Calculator.css"
    
    numbers = var("0")
    
    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Footer()
        with VerticalGroup(id="calculator"):
            yield Display()
            yield NumberPad()
        
        
    @on(Button.Pressed, ".number")
    def number_pressed(self, event: Button.Pressed) -> None:
        """Pressed a number."""
        assert event.button.id is not None
        number = event.button.id[-1]
        sc = self.query_one("#equation", Static)
        sc.update(number)



if __name__ == "__main__":
    app = calculator()
    app.run()
# end main
