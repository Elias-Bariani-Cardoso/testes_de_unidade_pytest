class Media:
    def __init__(self, notas):
        self.notas = notas

    def verificar_notas(self):
        for nota in self.notas:
            if not (isinstance(nota, (int, float)) and nota >= 0):
                return False
        return True

    def calcular_media(self):
        if not self.verificar_notas() or len(self.notas) == 0:
            raise ValueError("Notas inválidas ou lista vazia.")
        return sum(self.notas) / len(self.notas)
