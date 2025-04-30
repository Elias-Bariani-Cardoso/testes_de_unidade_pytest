import pytest
from atividade.src.idade import coletar_idade

@pytest.mark.parametrize("idade, esperado", [
    (17, False),
    (18, True),
    (69, True),
    (70, False),
])
def test_coletar_idade(idade, esperado):
    assert coletar_idade(idade) is esperado
