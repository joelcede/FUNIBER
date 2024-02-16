from colorama import Fore, Style

class TypeResponses:
    def __init__(self):
        self.error_color = Fore.RED
        self.succes_color = Fore.GREEN
        self.generic_color = Fore.BLUE
        self.clean = Style.RESET_ALL
    
    def colorMessage(self, color, message):
        return color + message + self.clean
    def error(self, message):
        return self.colorMessage(self.error_color, message)
    def succes(self, message):
        return self.colorMessage(self.succes_color, message)
    def generic(self, message):
        return self.colorMessage(self.generic_color, message)