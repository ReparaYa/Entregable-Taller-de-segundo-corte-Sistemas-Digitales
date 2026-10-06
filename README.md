**1. Diseño de la tabla**

Dígitos 0-9: patrones estándar.

- El 1 va a la derecha (segmentos b y c), la convención más legible.
- El 6 es cerrado (enciende a), para no confundirlo con una "b".
- El 9 es cerrado (enciende d), para distinguirlo de una "q".

- Valores 10-15 (símbolos propios, sin letras A-F):

    "0000001",  # 10 guion
    "0001000",  # 11 guion bajo
    "1100011",  # 12 grado
    "0011101",  # 13 o
    "0010101",  # 14 n
    "1001001",  # 15 triple barra
    

**2. Resultados de simulación**
- Qué verifica el testbench: recorre los 16 valores de bcd, espera a que la salida se estabilice y compara sseg con la fila correspondiente de la tabla.
- Por qué no hay errores: el decodificador se genera con la misma tabla que usa el testbench para comparar, así que cada salida coincide con lo esperado.
- Qué es sseg: un bus de 7 bits en orden abcdefg; cada bit enciende (1) o apaga (0) un segmento del display.

**3. Código HDL generado**

MyHDL convierte la tupla de búsqueda (LUT) en VHDL como una sentencia de selección con 16 casos. En hardware es lógica combinacional pura: la salida depende solo de los 4 bits de entrada y no usa reloj.

**4. Ejecución**

python -m pip install myhdl pytest

python sevensegdec.py --simulation --table tabla.txt

python sevensegdec.py --verilog --table tabla.txt

python -m pytest -v
