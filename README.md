# 🤖 BoomE - Simulador de Detección de Bombas con Probabilidad de Bayes
#### 🐍 Proyecto sencillo de machine learning con PYTHON.
> BoomE es un robot representado por la letra 'R' que se mueve a través de un terreno desconocido en busca de una bomba escondida. Utiliza el Teorema de Bayes para calcular la probabilidad de que haya una bomba en una celda específica y tomar decisiones basadas en estas probabilidades.

#### Visualización de codigo funcionando
---
![](/Funcionamiento_BoomE.jpg)

#### 🚀 Habilidades de programación adquiridas.
>+ **Probabilidad y Estadística:** 
>   + Implementación del Teorema de Bayes para la toma de decisiones basada en incertidumbre.
>+ **Algoritmos de Búsqueda y Recorrido:** 
>   + Implementación de un patrón de movimiento estructurado en "S" para la exploración del mapa.
>+ **Simulación e Interactividad:** 
>   + Generación y representación visual de un entorno de simulación basado en texto.
>+ **Gestión de Errores e Incertidumbre:** 
>   + Manejo de falsos positivos y negativos en la detección de bombas.
>+ **Desarrollo Modular:** 
>   + Organización del código en funciones y módulos para facilitar su mantenimiento y escalabilidad.
>+ **Optimización y Eficiencia:** 
>   + Reducción de cálculos innecesarios para mejorar el rendimiento del simulador.

#### 📂 Estructura del Proyecto
    boome/
    ├── Mapa.yaml          # Archivo YAML que contiene la representación del mapa
    ├── boome.py           # Script principal con la simulación
    ├── README.md          # Documentación del proyecto

#### 🎮 Funcionamiento
>- Se carga el mapa desde Mapa.yaml.
>- El robot se mueve siguiendo un patrón en "S".
>- En cada celda, el robot usa un detector con posibilidad de error.
>- Se aplica el Teorema de Bayes para calcular la probabilidad de que haya una bomba.
>- Si la probabilidad supera un umbral, el robot actúa en consecuencia.

---
###### ¡Gracias por revisar este proyecto! 
###### Si tienes sugerencias o mejoras, no dudes en contribuir. 🦊
