from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as pdf_canvas


class Nodo:
    def __init__(self, n):
        self.n = n
        self.izquierdo = None
        self.derecho = None


nodo_raiz = Nodo(60)
resultados = []
numeros = [70, 30, 20, 53, 90, 80, 96, 35, 40, 40, 50]


def insertar_nodo(nodo, n):
    if n <= nodo.n:
        if nodo.izquierdo is None:
            nodo.izquierdo = Nodo(n)
        else:
            insertar_nodo(nodo.izquierdo, n)
    else:
        if nodo.derecho is None:
            nodo.derecho = Nodo(n)
        else:
            insertar_nodo(nodo.derecho, n)


def buscar_numero(nodo, n, camino):
    if nodo is None:
        return False, camino

    resultados.append(camino)  # Guardar el camino actual en la lista de resultados

    if n == nodo.n:
        return True, camino

    if n < nodo.n:
        return buscar_numero(nodo.izquierdo, n, f"{n} <= {nodo.n} -------- va al nodo izquierdo")
    else:
        return buscar_numero(nodo.derecho, n, f"{n} > {nodo.n} ------- va al nodo derecho")


for i in numeros:
    insertar_nodo(nodo_raiz, i)

while True:
    opcion = input("¿Deseas insertar un número? (s/n): ")
    if opcion.lower() == "s":
        x = int(input("Ingresa el número a insertar: "))
        numeros.append(x)
        insertar_nodo(nodo_raiz, x)
        print(f"Lista actualizada: {numeros}")
    else:
        break

x = int(input("Ingresa el número a buscar: "))
encontrado, camino = buscar_numero(nodo_raiz, x, "")
if encontrado:
    print(f"El número {x} se encontró en el árbol. Camino: {camino}")
else:
    print(f"El número {x} no se encontró en el árbol.")
pdf = pdf_canvas.Canvas("resultados.pdf", pagesize=letter)
x = 50
y = 750
line_height = 20
pdf.setFont("Helvetica", 12)
pdf.drawString(x, y, "Resultados del árbol binario:")

for i, camino in enumerate(resultados):
    if camino:
        y -= line_height
        pdf.drawString(x, y, f"Iteración {i}: {camino}")
pdf.save()

print("Los resultados se han guardado en el archivo resultados.pdf.")