class Voo:
    def __init__(self, id, origem, destino, horarios, preco, assentos):
        self.id = id
        self.origem = origem
        self.destino = destino
        self.horarios = horarios
        self.preco = preco
        self.assentos_disponiveis = assentos.copy()

class SistemaReserva:
    def __init__(self):
        self.voos = [
            Voo(1, "Sao Paulo", "Rio de Janeiro", "08:00-10:00", 200.0, ["1A","1B","1C"]),
            Voo(2, "Sao Paulo", "Brasilia",      "09:00-11:30", 300.0, ["2A","2B"]),
        ]
        self.selecionado_voo     = None
        self.assento_selecionado = None
        self.passageiro          = None
        self.reserva_confirmada  = None

    def buscar_voos(self, origem: str, destino: str):
        if not origem or not destino:
            raise ValueError("Local de partida ou destino inválido.")
        encontrados = [
            voo for voo in self.voos
            if voo.origem == origem and voo.destino == destino
        ]
        if not encontrados:
            raise ValueError("Nenhum voo disponível para essa rota.")
        return encontrados

    def selecionar_voo(self, voo_id: int) -> Voo:
        for voo in self.voos:
            if voo.id == voo_id:
                self.selecionado_voo = voo
                return voo
        raise ValueError("Voo não encontrado.")

    def obter_info_voo(self) -> dict:
        if not self.selecionado_voo:
            raise ValueError("Nenhum voo selecionado.")
        v = self.selecionado_voo
        return {
            "horarios": v.horarios,
            "preco": v.preco,
            "assentos_disponiveis": v.assentos_disponiveis.copy()
        }

    def selecionar_assento(self, assento: str) -> str:
        if not self.selecionado_voo:
            raise ValueError("Nenhum voo selecionado.")
        if assento not in self.selecionado_voo.assentos_disponiveis:
            raise ValueError("Assento não disponível.")
        self.selecionado_voo.assentos_disponiveis.remove(assento)
        self.assento_selecionado = assento
        return assento

    def inserir_informacoes_passageiro(self, nome: str, documento: str) -> dict:
        if not nome or not documento:
            raise ValueError("Informações do passageiro incompletas.")
        self.passageiro = {"nome": nome, "documento": documento}
        return self.passageiro

    def confirmar_reserva(self) -> dict:
        if not (self.selecionado_voo and self.assento_selecionado and self.passageiro):
            raise ValueError("Não foi possível confirmar a reserva.")
        self.reserva_confirmada = {
            "voo_id": self.selecionado_voo.id,
            "assento": self.assento_selecionado,
            "passageiro": self.passageiro
        }
        return self.reserva_confirmada

    def enviar_confirmacao(self, email: str) -> bool:
        if not self.reserva_confirmada:
            raise ValueError("Nenhuma reserva para enviar confirmação.")
        if "@" not in email:
            raise ValueError("E-mail inválido.")
        return True
