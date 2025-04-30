# 📌 Algoritmo de los Puntos Más Cercanos

## 🧠 Descripción del algoritmo

El algoritmo de puntos más cercanos es una solución eficiente para encontrar el par de puntos más próximos en un conjunto de puntos en el plano. Se basa en una técnica de divide y vencerás, logrando una complejidad de tiempo de O(n log n), mucho mejor que la fuerza bruta (O(n²)).

## 🔍 Funcionamiento
Ordenamiento inicial: Se ordenan los puntos por sus coordenadas x y y.

División: Se divide el conjunto en dos mitades según la coordenada x.

Recursión: Se encuentra el par más cercano en cada mitad de forma recursiva.

Zona intermedia: Se revisa una franja vertical alrededor del eje central para detectar posibles pares más cercanos entre las dos mitades.

Comparación final: Se retorna el par con la menor distancia de entre los pares internos y los pares intermedios.

## 🎯 Ejercicio aplicado
### 🗣️ Enunciado

En una fiesta con 30 personas, cada una con un cierto capital (en miles de dólares) y años de experiencia, se desea encontrar a las dos personas más compatibles para emprender un proyecto.
La compatibilidad se mide como la menor distancia euclidiana entre los pares de puntos, donde cada persona se representa como un punto (capital, experiencia).

### 💾 Entrada de datos

Una lista de 30 tuplas, donde cada tupla representa a una persona:


P = [
    (120, 5), (95, 3), (130, 7), ..., (118, 5)
]

Cada tupla representa:

x: Capital en milllones

y: Años de experiencia

### ✅ Salida esperada

El programa imprimirá:

Las dos personas más cercanas según la distancia euclidiana.

Sus índices (posición en la lista original).

Su capital y experiencia.

La distancia entre ellas.


### ⚙️ Estructura del programa

mergesort() → Ordena los puntos por coordenada (x o y).

Euclidean_Distance() → Calcula la distancia entre dos puntos.

BruteForceClosestPair() → Encuentra el par más cercano si hay 3 puntos o menos.

Closest_Pair() → Implementa el algoritmo completo de divide y vencerás.

## 🧪 Ventajas del algoritmo

Eficiente para conjuntos grandes.

No requiere librerías externas.

Muestra claramente la lógica de partición y comparación.