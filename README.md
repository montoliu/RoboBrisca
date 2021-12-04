# RoboBrisca: Primera competición internacional de programación de bots para jugar a la Brisca
 
## Presentación
RoboBrisca es una competición de programación
de bots para jugar a la *Brisca*, un juego de cartas muy popular 
en muchos países.

El objetivo de esta competición es fomentar entre estudiantes de grado, master o doctorado,
pero también abierto a público en general, la programación de algoritmos
de inteligencia artificial capaces de jugar de forma autónoma a
juegos de cartas.

## Quien puede participar
La competición está abierta a todo el que quiera participar.
Se puede participar tanto de forma individual, como en equipo.

## Cómo participar
Para participar hay que rellenar el siguiente formulario **TBD** donde
se deberá especificar los siguiente datos:
- El nombre del equipo.
- El nombre de los integrantes del equipo y si son de la *Universitat Jaume I* o no.
- Una dirección email de contacto.

## Premios
Los equipos que queden clasificados en los tres primeros puesto
recibirán un diploma acreditativo.

Además, existirá un premio **TBD** para los tres primeros equipos
de la competición. 

**IMPORTANTE**: Para obtar al premio, al menos un integrante de equipo
tiene que ser estudiante de la *Universitat Jaume I*.

## Reglas de la competición

1. Para apuntarse a la competición hay que rellenar el formulario **TBD**.
2. Antes de la fecha límite, los equipos apuntados tendrán que enviar, a la dirección
de correo [montoliu@uji.es](), un programa escrito en Python, cuyo nombre de fichero tienen
que tener el siguiente formato: "equipo.py", donde *equipo* es el nombre del equipo. 
Como la Brisca es un juego de cuatro jugadores en equipos de 2, el mismo bot se utilizará
para los dos jugadores de cada equipo. La fecha límite es el día **TBD**.

3. El día **TBD** se realizará la primera fase de la competición. En esta
primera fase, participarán todos los equipos que hayan enviado su bot,
en el formato correcto, antes de la fecha límite. En esta fase, los bots jugaran 
una serie de partidas contra tres bots realizados por los organizadores de
la competición y que no serán públicos. Fruto de esta fase, se realizará una
clasificación donde los equipos con más victorias contra los bots de la organización, ocuparán los puestos más altos. En caso de empate, se sortearán los puestos.
Los 8 primeros se clasificarán para la segunda fase.
4. En la primera fase, cada bot jugará 100 partidas contra cada uno de los tres bots de
la organización, 50 jugando como primero (y tercero) y 50 como segundo (y cuarto). Si se gana
la partida, se obtendrá un punto. Por lo tanto, la puntuación máxima que se puede obtener en la primera
fase es de 300 puntos.
5. Una vez finalizada la primera fase, se harán publicos los resultados y el código
fuente de los bots de la organización. También se proporcionará a cada equipo,
unos ficheros que servirán para estudiar las partidas que ha jugado su bot.
6. Los equipos clasificados para la segunda fase, podrán modificar su bot y enviar una nueva versión antes del día **TBD**.
7. El día **TBD** se realizarán los cuartos de final entre los equipos 1-8, 2-8, 3-6 y 4-5
según la clasificación obtenida en la primera frase. Posteriormente, se realizarán
las semifinales (con los ganadores de los cuartos de final). Finalmente se realizará
el partido por el tercer puesto y la gran final.
8. En la segunda fase, se jugarán 100 partidas entre los dos bots, en las que cada uno jugará 
de primero (y tercero) la mitad de las veces. Cada victoria supondra un punto, por lo que,
el número máximo de puntos que se puede obtener es 100.
9. Ambas fases serán retrasmitidas en directo mediante **TBD**.


## Reglas de la Brisca
Se juega con la baraja española de 40 cartas (sin ochos ni nueves).

Al comenzar la partida se barajan todas las cartas y se reparte una carta a cada jugador
empezando con el jugador que va de primero. Siguiendo el mismo procedimiento, se reparten
 dos cartas más a los jugadores. Por lo tanto, cada jugador recibirá 3 cartas.

La primera carta no repartida es el triunfo que se enseña a todos los jugadores y se situa
al final de la baraja.

En cada mano (o ronda), el jugador que va de primero juega una carta de las tres que tiene, el siguiente jugador
realiza la misma acción y lo mismo ocurre con los otros dos. 

Al finalizar la mano, se mira quien es el ganador siguiendo las siguientes normas:
- En caso de que todas las cartas sean del mismo palo, gana el que haya puesto la más alta.
- En caso de que se echen cartas de diferente palo que no sean triunfo, gana el que haya puesto la carta más alta del palo del que haya echado la primera carta.
- En caso de que alguien eche un triunfo, gana el que haya echado el triunfo más alto, independientemente del valor de las cartas de otro palo que se hayan echado.

Tras esto, el jugador que haya ganado la mano recoge las cartas 
y las coloca boca abajo frente a sí. Después los jugadores roban una carta del mazo 
por turnos, comenzando el que haya ganado la mano. 

El que haya ganado empezará entonces una nueva mano echando una carta. 

Se jugará así sucesivamente hasta que se acabe el mazo (siete rondas)
Después de acabarse el mazo, los jugadores jugarán las últimas tres manos 
con las tres cartas que tengan en la mano, sin robar carta tras cada mano.

Al acabar la partida, cada equipo contará los puntos que ha ganado, contando, 
11 puntos por cada as (número 1), 10 por cada tres (número 3), 4 por cada rey (número 12),
3 por cada caballo (número 11) y 2 por cada sota (número 10). 
Las demás cartas, aunque pueden haber servido para ganar manos no cuentan puntos. 
El equipo que más puntos consiga vence. 
Puede darse el caso de que se empate a sesenta, en el cual ganará el que más cartas tenga. 

En la variante implementada no se puede intercambiar la carta de triunfo por el 7. Tampoco
se puede obligar a arrastrar.

Para una descripción completa del juego, 
consultar [https://es.wikipedia.org/wiki/Brisca](https://es.wikipedia.org/wiki/Brisca)

## Como realizar mi primer bot

## Breve explicación del código fuente

## Contacto
Para obtener más información, enviar un email a [montoliu@uji.es]().
