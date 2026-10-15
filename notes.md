# Exoplanet Explorer

## Mi objetivo

Construir un sistema en Python capaz de analizar datos reales de exoplanetas confirmados y detectar casos estadísticamente inusuales que puedan ser interesantes para un análisis posterior.
La idea es que este proyecto sirva como base para proyectos siguientes relacionados con astronomía, análisis de datos e inteligencia artificial.
*Hipótesis de trabajo: algunos exoplanetas presentan combinaciones de propiedades físicas que se alejan significativamente de los patrones observados en la población conocida, y dichas desviaciones pueden revelar casos físicamente inusuales que justifiquen un análisis más profundo.*

## Datos

Fuente: NASA Exoplanet Archive -> url: <https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,pl_rade,pl_bmasse,pl_dens,pl_orbper+from+pscomppars&format=csv>
Tabla: pscomppars
Variables:

- pl_name
- pl_rade
- pl_bmasse
- pl_dens
- pl_orbper

## Significado de las variables

- pl_name = Nombre del exoplaneta.
- pl_rade = Radio del planeta expresado en radios terrestres.
- pl_bmasse = Mejor estimación disponible de la masa planetaria, expresada en masas terrestres. Dependiendo del sistema puede corresponder a masa o a una estimación basada en M·sin(i).
- pl_dens = Densidad del planeta en g/cm³.
- pl_orbper = Periodo orbital del planeta expresado en días.

## Observaciones iniciales

Dataset inicial: 6375 filas y 5 columnas.

Datos faltantes:

- radio: 50
- masa: 31
- densidad: 145
- periodo orbital: 353

*Un mismo planeta puede tener más de un dato faltante, por lo que no se pueden sumar directamente los valores faltantes de todas las columnas para conocer cuántos planetas están incompletos.*

## Limpieza de datos

Como vi que habian datos faltantes de algunos exoplanetas dentro de las variables que elegi para hacer mi analisis, es decir, radio, masa y densidad. Hice una limpieza de datos para ver cuantos planetas no me sirven para el analisis y ver si es una cantidad que va a afectar mi proyecto o no.

- Dataset original: 6375 planetas
- Dataset post limpieza: 6229 planetas (146 planetas eliminados)

## Estadísticas descriptivas iniciales

Después de limpiar los datos obtuve algunos resultados importantes.

1) Radio
-Media: aproximadamente 5,86 radios terrestres
-Desviación estándar: aproximadamente 5,41
-Mínimo: 0,31
-Máximo: 87,21
-Existe bastante variación en el tamaño de los planetas.

2) Masa
-Media: aproximadamente 391 masas terrestres
-Desviación estándar: aproximadamente 1123
-Mínimo: 0,02
-Máximo: 9535 masas terrestres
-La desviación estándar es mucho mayor que la media, lo que muestra que la distribución de masas tiene una dispersión muy grande y contiene valores extremadamente altos.

3) Densidad
-Media: aproximadamente 4,83 g/cm³
-Desviación estándar: aproximadamente 33,96 g/cm³
-Mínimo: 0,0051 g/cm³
-Máximo: 2000 g/cm³
La densidad también presenta valores extremos. El máximo está enormemente alejado de la mayoría de los datos, por lo que será importante revisar estos casos antes de considerarlos planetas físicamente extraordinarios.

## Relación entre masa, radio y densidad

Voy a relacionar estas variables, ya que la densidad indica cuánta masa hay concentrada en un cierto volumen. Con esto me refiero a que un planeta puede tener mucha masas, pero si también es muy grande, su densidad puede no ser alta.

- Densidad = Masa/Volumen.
- Como un planeta tiene como figura general la esfera, podemos aproximar su volumen a traves del de una esfera. -> Volumen = 4/3 *pi* r^3. Con esta formula observamos que el volumen depende del radio.
- Con lo dicho anteriormente, esta claro que masa, radio y densidda estan relacionados entre sí.

## Interpretación de tres relaciones

Interpretare tres relaciones que a mi parecer serán utiles.

- Masa vs radio
- Densidad vs radio
- Densidad vs periodo orbital

## Interpretación visual de relaciones

Generé tres graficos, uno para cada relación. Estos gráficos se encuentran en la carpeta "figures". A continuación los interpretare:

1) Gráfico: Masa vs radio

- Archivo:`figures/masa_vs_radio.png`
- Interpretación: Existe una relación positiva clara entre el radio y la masa de los exoplanetas: en general, a medida que aumenta el radio, también aumenta la masa. Sin embargo, la relación no parece seguir una única línea recta. En escala logarítmica se observa una estructura más compleja, con distintas regiones de concentración y una dispersión considerable para radios similares. También existen planetas que se alejan claramente del comportamiento principal. Esto sugiere que el radio por sí solo no determina completamente la masa y que podrían existir diferentes poblaciones de planetas con propiedades físicas distintas.
*fíjarme en la zona aproximadamente entre 10 y 20 radios terrestres, ya que hay muchísima variación de masa para radios relativamente parecidos.*

1) Gráfico: Gráfico: Densidad vs radio

-Archivo: `figures/densidad_vs_radio.png`
-Interpretación:La relación entre radio y densidad presenta una tendencia general negativa en buena parte de la población: al aumentar el radio, la densidad tiende a disminuir. Sin embargo, la relación no es estrictamente lineal ni uniforme. Se observan diferentes concentraciones de planetas y una dispersión considerable, especialmente en radios pequeños. También aparecen algunos valores de densidad extremadamente altos o bajos.
-Estructura aproximada:

            radio pequeño
                  ↓
      densidad generalmente mayor
                  ↓
 zona de densidades relativamente altas
                  ↓
            radio aumenta
                  ↓
      densidad generalmente disminuye

1) Gráfico: Densidad vs periodo orbital

- Archivo:`figures/densidad_vs_periodo.png`
- Interpretación: La distribución muestra una alta concentración de observaciones en determinadas regiones y algunos valores considerablemente alejados del conjunto principal. Visualmente no se aprecia una relación lineal clara entre el periodo orbital y la densidad. Esto sugiere que conocer únicamente cuánto demora un planeta en completar su órbita no permite predecir directamente su densidad. Sin embargo, la amplitud de los valores y la presencia de casos extremos pueden estar dificultando la observación de patrones más sutiles. Será necesario mejorar la escala del gráfico y posteriormente medir la relación estadísticamente antes de concluir que ambas variables no están relacionadas.En escala lineal, la presencia de periodos orbitales extremadamente grandes comprime casi toda la población en una pequeña región del gráfico, dificultando cualquier interpretación. Al utilizar escalas logarítmicas, la distribución se vuelve mucho más visible. La mayoría de los exoplanetas presenta densidades aproximadamente entre 0,1 y varias decenas, distribuidas a lo largo de un amplio rango de periodos orbitales. A simple vista no se observa una relación clara entre ambas variables: planetas con periodos similares pueden presentar densidades muy diferentes. Existen algunos casos extremos tanto en densidad como en periodo orbital que deberán estudiarse individualmente.

## Interpretación visual en escala logaritmica

Los gráficos originales están tan afectados por valores extremos que esconden gran parte de la estructura real de los datos.
Antes los ejes eran lineales (0, 10, 20, 30, 40) Y ahora logaritmicos (0.1, 1, 10, 100, 1000). Esto es muy útil, ya que los datos son muy amplios, distribuyendose en varios órdenes de magnitud.

1) Interpretación Masa vs Radio: Al representar masa y radio en escala logarítmica, la relación entre ambas variables se vuelve mucho más clara. La mayor parte de los exoplanetas parece seguir una tendencia aproximadamente lineal en este espacio transformado, aunque existen varios puntos que se alejan de la tendencia principal. Estos casos pueden ser candidatos interesantes para un análisis posterior, ya que podrían representar planetas con combinaciones de masa y radio poco comunes respecto del patrón general. Algunos valores siguen siendo extremos incluso después del cambio de escala, lo que sugiere que no se trataba únicamente de un problema de visualización.

2) Interpretación Densidad vs Radio: Se observa una tendencia hacia una relación inversa, ya que cuando aumenta el radio, la densidad tiende a disminuir. Sin embargo, la nube de puntos sigue presentando bastante dispersión y existen datos atípicos que se alejan claramente del patrón.
Esto hace interesante estudiar no solamente los valores extremos, sino cuánto se aleja cada planeta del comportamiento esperado para planetas de tamaño parecido.

3) Interpretación Densidad vs Periodo Orbital: Existe una concentración importante de datos en la zona central, junto con varios valores atípicos.
Incluso utilizando escala logarítmica no aparece una tendencia clara entre ambas variables.
La gran diferencia entre algunos valores también explica por qué la desviación estándar de la densidad es tan elevada.

## Correlaciones

Para complementar los gráficos calculé tres tipos de correlación:

1) Pearson

2) Spearman

3) Kendall

Esto permite medir las relaciones entre variables desde diferentes perspectivas.

1) Pearson: Pearson mide principalmente relaciones lineales y puede verse bastante afectado por valores extremos.
Resultados principales:
-Masa vs radio: 0,452
-Densidad vs radio: -0,044
-Densidad vs periodo orbital: 0,001
Según Pearson, solamente masa y radio muestran una relación positiva moderada. Sin embargo, los gráficos y las otras correlaciones muestran que Pearson está perdiendo parte importante de la estructura de los datos.

2) Spearman: Spearman analiza si existe una relación ordenada o monotónica entre las variables, sin exigir que la relación sea una línea recta.
Resultados principales:
-Masa vs radio: 0,935
-Densidad vs radio: -0,642
-Masa vs densidad: -0,419
-Densidad vs periodo orbital: -0,084
Estos resultados son mucho más coherentes con lo observado visualmente.

3) Kendall:
Kendall también analiza relaciones monotónicas utilizando el orden de los datos.
Resultados principales:
-Masa vs radio: 0,817
-Densidad vs radio: -0,578
-Masa vs densidad: -0,404
-Densidad vs periodo orbital: -0,069
Los resultados son similares a Spearman, aunque los valores son algo menores.

## Interpretación estadística de las relaciones

1) Masa vs radio
-Spearman = 0,935
-Kendall = 0,817
Existe una relación positiva muy fuerte, esta nos dice que en general mayor radio = mayor masa.
Sin embargo, Pearson solamente da aproximadamente 0,45, lo que indica que la relación no es simplemente una línea recta. Esto coincide con lo observado en los gráficos.
La diferencia entre Pearson y Spearman también puede indicar que los valores extremos afectan bastante la correlación lineal.

2) Densidad vs radio
-Spearman = -0,642
-Kendall = -0,578
En la población analizada existe una asociación monotónica negativa considerable entre radio y densidad, compatible tanto con la definición física de densidad (rho = M/(4/3)\(pi*r³)) como con las diferencias de masa y composición entre distintas poblaciones planetarias.

3) Masa vs densidad
-Spearman = -0,419
-Kendall = -0,404
Existe una relación negativa moderada, lo que demuestra que tener más masa no significa necesariamente tener más densidad. Un planeta puede ser muy masivo pero también tener un volumen enorme, por lo que su densidad puede seguir siendo relativamente baja.

4) Densidad vs periodo orbital
-Spearman = -0,084
-Kendall = -0,069
La relación es prácticamente inexistente, ya que hasta ahora no aparece una relación monotónica general importante entre estas dos variables.

## Análisis de datos atípicos

Utilizando el método IQR sobre la densidad encontré 319 posibles outliers de densidad.
Algunos de los casos más extremos son:
-KOI-2513.01 → 2000 g/cm³
-Kepler-245 e → 902 g/cm³
-Kepler-37 e → 879 g/cm³
-Kepler-80 f → 703 g/cm³
-Kepler-238 b → 526 g/cm³
-Kepler-391 c → 400 g/cm³
-Kepler-391 b → 380 g/cm³
Estos valores son extremadamente diferentes del conjunto principal.
*Sin embargo, todavía no puedo concluir que estos planetas sean físicamente extraordinarios.*

## Problema importante detectado con los outliers

Un planeta que aparece como outlier estadístico no necesariamente es un planeta realmente extraordinario.
Un valor extremo podría deberse a:
-Una característica física real.
-Una medición muy incierta.
-Una estimación de masa o radio.
-Datos obtenidos mediante métodos diferentes.
-Información proveniente de distintas publicaciones.
-Alguna característica particular del catálogo.
-Un dato que necesita ser revisado antes de interpretarlo.

## Evolución de la hipótesis

Inicialmente pensaba buscar principalmente valores extremos.
Después de observar los gráficos y las correlaciones, parece más interesante buscar planetas que se alejen del patrón general. Por ejemplo, dos planetas pueden tener densidades relativamente normales individualmente, pero uno de ellos podría tener una densidad muy extraña considerando su masa y su radio.
Se me ocurre como nuevo objetivo detectar planetas cuyas combinaciones de masa, radio y densidad se alejan significativamente de lo esperado para la población general.
