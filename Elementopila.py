class ElementoPila:
    def __init__(self, fuente, tipo):
        self.fuente = fuente
        self.tipo = tipo

    def __str__(self):
        return f"{self.fuente} {self.tipo}"
    
class Terminal(ElementoPila):
    def __init__(self, fuente, tipo):
        super().__init__(fuente, tipo)

class NoTerminal(ElementoPila):
    def __init__(self, fuente, tipo):
        super().__init__(fuente, tipo)

    def __str__(self):
        return f"No terminal {self.fuente} {self.tipo}"
class Estado(ElementoPila):
    def __init__(self, fuente, tipo):
        super().__init__(fuente, tipo)
