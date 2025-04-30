import pytest
from atividade.src.media import Media

def test_notas_invalidas():
    m = Media([10, -5, 'a'])
    assert m.verificar_notas() == False

def test_notas_validas():
    m = Media([7.5, 8, 9])
    assert m.verificar_notas() == True

def test_media_com_notas_invalidas():
    m = Media([8, -3, 7])
    assert m.verificar_notas() == False
    with pytest.raises(ValueError):
        m.calcular_media()

def test_media_com_notas_validas():
    m = Media([10, 8, 6])
    assert m.verificar_notas() == True

def test_exibir_media_sem_calculo():
    m = Media([])
    assert m.verificar_notas() == True
    with pytest.raises(ValueError):
        m.calcular_media()

def test_exibir_media_apos_calculo():
    m = Media([5, 5, 5])
    assert m.verificar_notas() == True
    assert m.calcular_media() == 5
