import pytest

from pytoolstest.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['jorge.plautz@gmail.com', 'lindalene.plautz@gmail.com']
)
def test_remetente(remetente):
    # o nome do parametro da função parametrize para como argumento da função
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,                       # from
        'jorgeluiz.plautz@carritech.com',   # to
        'Curso Python pro',                 # assunto
        'Teste com modulo Pytools'          # Corpo
    )

    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['', 'lindalene.plautz']
)
def test_remetente_invalido(remetente):
    # Aqui será usado um gerenciado de contexto
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,                          # from
            'jorgeluiz.plautz@carritech.com',   # to
            'Curso Python pro',                 # assunto
            'Teste com modulo Pytools'          # Corpo
        )
