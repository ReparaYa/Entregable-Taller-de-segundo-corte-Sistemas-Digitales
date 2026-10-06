"""Pruebas unitarias (pytest) del decodificador de 7 segmentos."""
import pytest
from myhdl import Signal, intbv, Simulation, delay, instance

from sevensegdec import sevensegdec, read_table

ESPERADO = [
    "1111110",  # 0
    "0110000",  # 1
    "1101101",  # 2
    "1111001",  # 3
    "0110011",  # 4
    "1011011",  # 5
    "1011111",  # 6 cerrado
    "1110000",  # 7
    "1111111",  # 8
    "1111011",  # 9 cerrado
    "0000001",  # 10 guion
    "0001000",  # 11 guion bajo
    "1100011",  # 12 grado
    "0011101",  # 13 o
    "0010101",  # 14 n
    "1001001",  # 15 triple barra
]


def decodificar(valor, tabla):
    bcd = Signal(intbv(0)[4:])
    sseg = Signal(intbv(0)[7:])
    resultado = []

    dut = sevensegdec(bcd, sseg, tabla)

    @instance
    def estimulo():
        bcd.next = valor
        yield delay(10)
        resultado.append(int(sseg.val))

    Simulation(dut, estimulo).run(quiet=True)
    return resultado[0]


def test_formato_tabla():
    """tabla.txt tiene 16 líneas de 7 bits (0 o 1)."""
    with open("tabla.txt") as f:
        lineas = [l.strip() for l in f if l.strip()]
    assert len(lineas) == 16
    assert all(len(l) == 7 and set(l) <= {"0", "1"} for l in lineas)


@pytest.mark.parametrize("entrada", range(16))
def test_decodificador(entrada):
    """Para cada entrada 0-15, la salida debe ser el patrón esperado."""
    tabla = read_table("tabla.txt")
    esperado = int(ESPERADO[entrada], 2)
    assert decodificar(entrada, tabla) == esperado