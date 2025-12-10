'''
 A simple calculator to do basic operators. Make it a scientific calculator for added complexity.
'''

from decimal import Decimal

from textual import events, on
from textual.reactive import var
from textual.app import App, ComposeResult
from textual.containers import Container, VerticalGroup
from textual.widgets import Footer, Header, Static, Button, Digits

class NumberPad(Static):
    '''Custom Number pad'''
    
    def compose(self) -> ComposeResult:
        with Container(id="numpad"):
            yield Button("ANS", id="answer", variant="success")
            yield Button("PWR", id="power", variant="warning", classes="operator")
            yield Button("MOD", id="percent", variant="warning", classes="operator")
            yield Button("CLR", id="reset", variant="error")
            yield Button("DEL", id="backspace", variant="error")
            yield Button("9", id="n9", classes="number")
            yield Button("8", id="n8", classes="number")
            yield Button("7", id="n7", classes="number")
            yield Button("(", id="lbracket", variant="warning", classes="bracket")
            yield Button(")", id="rbracket", variant="warning", classes="bracket")
            yield Button("6", id="n6", classes="number")
            yield Button("5", id="n5", classes="number")
            yield Button("4", id="n4", classes="number")
            yield Button("*", id="multi", variant="warning", classes="operator")
            yield Button("/", id="divide", variant="warning", classes="operator")
            yield Button("3", id="n3", classes="number")
            yield Button("2", id="n2", classes="number")
            yield Button("1", id="n1", classes="number")
            yield Button("+", id="add", variant="warning", classes="operator")
            yield Button("-", id="sub", variant="warning", classes="operator")
            yield Button("0", id="n0", classes="number span-two")
            yield Button(".", id="point", variant="primary", classes="operator")
            yield Button("=", id="equal",  classes="span-two", variant="success")


class Display(Static):
    
    def compose(self) -> ComposeResult:
        with VerticalGroup(id ="screen"):
            yield Static("0", id="equation")
            yield Digits("0", id="result")
        

            
class calculator(App):
    
    
    CSS_PATH = "Calculator.css"
    
    OPERATORS = {
        "multi" : "*",
        "divide" : "/",
        "add" : "+",
        "sub" : "-",
        "percent" : "%",
        "power" : "**",
        "point" : ".",
        "lbracket" : "(",
        "rbracket" : ")"
    }
    
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
        equation = self.query_one("#equation", Static)
        if equation.content[-1] == '0' and len(equation.content) == 1:
            equation.update(equation.content.lstrip('0') + number)
        else:
            equation.update(equation.content + number)
    
    @on(Button.Pressed, ".operator")
    def operator_pressed(self, event: Button.Pressed) -> None:
        """Pressed an operator."""
        assert event.button.id is not None
        operator = self.OPERATORS[event.button.id]
        equation = self.query_one("#equation", Static)
        if equation.content[-1] not in '/*+-.%(':
            equation.update(equation.content + str(operator))
    
    @on(Button.Pressed, ".bracket")
    def bracket_pressed(self, event: Button.Pressed) -> None:
        """Pressed a bracket."""
        assert event.button.id is not None
        bracket = self.OPERATORS[event.button.id]
        equation = self.query_one("#equation", Static)
        if bracket == '(' and equation.content[-1] in '0123456789':
            equation.update(equation.content + "*" + str(bracket))
        elif bracket == ')' and equation.content[-1] in '+-*/.(':
            return
        else:
            equation.update(equation.content + str(bracket))
        
    @on(Button.Pressed, "#equal")
    def solve_pressed(self) -> None:
        """Gettin the result using eval()"""
        res = self.query_one("#result", Digits)
        equation = self.query_one("#equation", Static)
        try:
            res.update(str(Decimal(eval(equation.content))))
        except ZeroDivisionError:
            res.update("E2")
        except SyntaxError:
            res.update("E1")
        except:
            res.update("E0")
        
    @on(Button.Pressed, "#reset")
    def reset_pressed(self) -> None:
        """Restting equation and result"""
        equation = self.query_one("#equation", Static)
        res = self.query_one("#result", Digits)
        equation.update('0')
        res.update('0')
        
    @on(Button.Pressed, "#backspace")
    def point_pressed(self) -> None:
        """Delete last inserted digit"""
        equation = self.query_one("#equation", Static)
        if equation.content == "0":
            pass
        elif len(equation.content) == 1:
            equation.update('0')    
        else:
            equation.update(equation.content[:-1])
    
    @on(Button.Pressed, "#answer")
    def answer_pressed(self) -> None:
        """Get the final answer and put in the equation"""
        equation = self.query_one("#equation", Static)
        res = self.query_one("#result", Digits)
        equation.update(res.value)
        res.update("0")
        

if __name__ == "__main__":
    app = calculator()
    app.run()
# end main


"""
Things to add in the future:
- a parser instead of using eval()
- scintific mode
- allowing the use of keyboard keys to interact with the calculator
- pollishing the code
"""