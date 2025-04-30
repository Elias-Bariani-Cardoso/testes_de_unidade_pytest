import pytest
from src.reserva import SistemaReserva, Voo

def test_fluxo_principal_reserva():
    sistema = SistemaReserva()

    voos = sistema.buscar_voos("Sao Paulo", "Rio de Janeiro")
    assert isinstance(voos, list) and len(voos) > 0

    voo = sistema.selecionar_voo(voos[0].id)
    assert isinstance(voo, Voo)

    info = sistema.obter_info_voo()
    assert all(k in info for k in ("horarios","preco","assentos_disponiveis"))

    assento = sistema.selecionar_assento(info["assentos_disponiveis"][0])
    assert assento not in sistema.selecionado_voo.assentos_disponiveis

    cliente = sistema.inserir_informacoes_passageiro("Alice", "CPF123")
    assert cliente["nome"] == "Alice"

    reserva = sistema.confirmar_reserva()
    assert reserva["voo_id"] == voo.id
    assert sistema.enviar_confirmacao("alice@example.com") is True

def test_alternativo_origem_destino_invalido():
    sistema = SistemaReserva()
    with pytest.raises(ValueError):
        sistema.buscar_voos("", "Rio de Janeiro")
    with pytest.raises(ValueError):
        sistema.buscar_voos("Sao Paulo", "")

def test_alternativo_sem_voos_disponiveis():
    sistema = SistemaReserva()
    with pytest.raises(ValueError):
        sistema.buscar_voos("Sao Paulo", "Paris")

def test_alternativo_assento_indisponivel():
    sistema = SistemaReserva()
    voos = sistema.buscar_voos("Sao Paulo", "Rio de Janeiro")
    sistema.selecionar_voo(voos[0].id)
    with pytest.raises(ValueError):
        sistema.selecionar_assento("99Z")

def test_alternativo_confirmar_sem_dados_completos():
    sistema = SistemaReserva()
    voos = sistema.buscar_voos("Sao Paulo", "Rio de Janeiro")
    sistema.selecionar_voo(voos[0].id)
    sistema.selecionar_assento(sistema.obter_info_voo()["assentos_disponiveis"][0])
    with pytest.raises(ValueError):
        sistema.confirmar_reserva()
