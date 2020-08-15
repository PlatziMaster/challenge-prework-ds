# Bienvenido al challenge #2!

Hola Master! Este reto nos permitirá evaluar tu nivel en temas específicos de **Data Science**. No te preocupes si no logras todos los objetivos, será importante ser 100% honestos ya que eso nos permite personalizar el Learning Path acorde a tu nivel.

_Imagina un punto a dónde quieres llegar y traza un plan para llegar allí.
Pero se honesto contigo y establece tu punto de partida_

_-(Jordan Belfort)_

# Descripción

El Instituto Nacional de Antropología e Historia **(INAH)**, contiene un **registro histórico del 2019** detallado de todos los visitantes de **todos los recintos culturales abiertos al público en México**.

Cada registro contiene:

- Estado
- Clave identificadora de recinto (SIINAH)
- Siglas
- Centro de trabajo (Nombre del recinto cultural)
- Año
- Tipo de visitante
- Número de visitante por tipo
- Nacionalidad (Extranjera o Nacional)

## Objetivo general

El objetivo general es desarrollar una plataforma, que permita a los usuarios finales (Investigadores, reporteros y ciudadanos en general), generar búsquedas para obtener indicadores de visitas por tipo de visitante, nacionalidad y cantidad por recinto en año.

Dividiremos este reto en objetivos **específicos** que nos permitirán trabajar distintas áreas **ESENCIALES** para un **Data Scientist**:

- Abstraer un problema utilizando datos crudos y recabados desde una dependencia que puede ser o no controlada por un experto en datos y puede contener errores.
- Manipulación de datos

  - Estructurar datos
  - Limpiar datos
  - Filtrar de datos

- Estadística aplicada (Histogramas, Gráficos de barras, Totales, Promedios, etc.)
- Interpretación estadística. **(El punto más importante)** Cómo podemos interpretar los datos como **Data Scientist** para encontrar soluciones usando los datos.

## Objetivos específicos (Reto)

**Objetivos específicos y numerados:**

1. Leer los datos utilizando un programa que de opción a insertarlo desde una interfaz gráfica simple o bien, desde línea de comandos. Pasando el archivo como un argumento.

**Mostrar datos de archivo desde línea de comandos:**

2. Limpiar los datos, estructurarlos usando python y pandas. Únicamente, utilizaremos: Estado, Clave SIINAH, Centro de trabajo, Año, Mes, Tipo de visitantes, Número de visitas y Nacionalidad.

**Mostrarlos como dataframe en Tabla con los datos mencionados arriba:**

3. Calculen los parámetros estadísticos:

- Totales por Estado por temporalidad (Mes y Año)
- Totales por Estado por tipo de visitante
- Totales por Estado por tipo de visitante y temporalidad (Mes y Año)
- Totales por Centro de trabajo y temporalidad (Mes y año)
- Totales por Centro de trabajo por tipo de visitante (Año)
- Promedio de visitantes totales por estado (Mes y Año)
- Promedio de visitantes por tipo de visitante, por estado (Mes y Año)
- Porcentaje de visitantes por Recinto en visitantes por estado (total por mes).
- Porcentaje de tipo de visitantes por mes y año
- Porcentaje de tipo de visitantes por recinto (Mes y Año)

4. Graficar los parámetros estadísticos con Plotly. Deben tener textos descriptivos, títulos, nombres de ejes, etc.

**Las gráficas deben entenderse por cualquier persona, sea experta o no en área estadística:**

5. Una interfaz gráfica que implemente todo lo anterior (no desde línea de comandos) para poder insertar los datos, filtrarlos, mostrarlos a manera de tabla, realizar búsqueda por parámetro y visualizar los datos.

**Usar PyQT, Tkinter, WxPython, Kivy u otra librería para componentes gráficos a su elección:**

6. Interpretar los resultados de manera sintetizada y concisa en formato de pie para cada gráfico y cálculo.

---

## Pasos a seguir:

1.  Hacer un **"Fork"** de este proyecto.
2.  Revolver los retos propuestos.
3.  Crear un Pull Request hacia este repositorio.

**NOTAS:**

- **Todo debe estar comentado y documentado, cada paso explicado el por qué y para qué de cada acción.**

- **Usar solo variables y funciones en inglés. Todo el código debe estar escrito en inglés, no será bien visto el uso de spanglish**

## Licencia:

challenge-ds-02 se lanza bajo la licencia [MIT](https://opensource.org/licenses/MIT).
