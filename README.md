![Init](logouji.png)

# RoboBrisca2022
# Primera competición internacional de programación de bots para jugar a la Brisca

## Presentación
El Instituto de nuevas tecnologías de la imagen
([htttp://www.init.uji.es](http://www.init.uji.es)) junto con la Escuela 
superior de tecnología y ciencias experimentales
([http://www.estce.uji.es](http://www.estce.uji.es)) de la *Universitat
Jaume I* organizan **RoboBrisca2022**.

**RoboBrisca2022** es una competición de programación
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
de correo [montoliu@uji.es](), un programa escrito en *Python 3*, cuyo nombre de fichero tienen
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
6. Los equipos clasificados para la segunda fase podrán modificar su bot y enviar una nueva versión antes del día **TBD**.
7. El día **TBD** se realizarán los cuartos de final entre los equipos 1-8, 2-7, 3-6 y 4-5
según la clasificación obtenida en la primera frase. Posteriormente, se realizarán
las semifinales (con los ganadores de los cuartos de final). Finalmente, se realizará
el partido por el tercer puesto y la gran final.
8. En la segunda fase, se jugarán 100 partidas entre los dos bots, en las que cada uno jugará 
de primero (y tercero) la mitad de las veces. Cada victoria supondra un punto, por lo que,
el número máximo de puntos que se puede obtener es 100.
9. Ambas fases serán retrasmitidas en directo mediante **TBD**.


## Reglas de la Brisca
Se juega con la baraja española de 40 cartas (sin ochos ni nueves) que consiste
en 10 cartas (as, 2, 3, 4, 5, 6, 7, sota, caballo, rey) de cada uno de los cuatro palos:
oros, bastos, copas y espadas. 

Al comenzar la partida se barajan todas las cartas y se reparte una carta a cada jugador
empezando con el jugador que va de primero. Siguiendo el mismo procedimiento, se reparten
 dos cartas más a los jugadores. Por lo tanto, cada jugador recibirá 3 cartas. El resto de
cartas (28) se ponen boca abajo.

La primera carta no repartida es el triunfo que se enseña a todos los jugadores y se situa
al final de la baraja.

En cada mano (o ronda), el jugador que va de primero juega una carta de las tres que tiene, el siguiente jugador
realiza la misma acción y lo mismo ocurre con los otros dos. 

Al finalizar la mano, cada jugador ha jugado una carta. 
Entonces, se mira quien es el ganador siguiendo las siguientes normas:
- En caso de que todas las cartas sean del mismo palo, gana el que haya puesto la más alta.
- En caso de que se echen cartas de diferente palo que no sean triunfo, gana el que haya puesto la carta más alta del palo del que haya echado la primera carta.
- En caso de que alguien eche un triunfo, gana el que haya echado el triunfo más alto, independientemente del valor de las cartas de otro palo que se hayan echado.

El orden de las cartas es, de mejor a peor: as, 3, rey, caballo, sota, 7, 6, 5, 4, 3 y 2.

Tras esto, el jugador que haya ganado la mano recoge las cartas 
y las coloca boca abajo frente a sí. Después los jugadores roban una carta del mazo 
por turnos, comenzando el que haya ganado la mano. 

El que haya ganado empezará entonces una nueva mano echando una carta. 

Se jugará así sucesivamente hasta que se acabe el mazo (siete rondas)
Después de acabarse el mazo, los jugadores jugarán las últimas tres manos 
con las tres cartas que tengan en la mano, sin robar carta tras cada mano.

Al acabar la partida, cada equipo contará los puntos que ha ganado, contando los puntos de las cartas
ganadas por los dos miembros del equipo. 

Los puntos de cada carta son: 11 puntos por cada as (número 1), 10 por cada tres (número 3), 4 por cada rey (número 12),
3 por cada caballo (número 11) y 2 por cada sota (número 10). Las demás cartas, aunque pueden haber servido para ganar manos no cuentan puntos. 

El equipo con más puntos es el que gana la partida. Si hay empate, ganará el equipo que tenga más cartas. 

Existen muchas vaiantes de la Brisca. En el caso particular de esta competición:
- No se puede intercambiar el 7 del palo de triunfo por la carta del triunfo, ni el 2 por el 7.
- No es obligatoria arrastrar.
- No se puede transmitir información entre los jugadores del mismo equipo

Para una descripción completa del juego, 
consultar [https://es.wikipedia.org/wiki/Brisca](https://es.wikipedia.org/wiki/Brisca)

## Como realizar mi primer bot
Para implementar un bot hay que crear un fichero con el nombre del bot y 
situarlo dentro de la carpeta _Players_, por ejemplo, si el 
equipo se llama _IALovers_, el bot se puede llamar _IALoversPlayer.py_. Dentro del fichero
se debe crear una clase con el mismo nombre que heredará de la clase _Player_ y que debe seguir
la siguiente plantilla:

```Python
from Players.Player import Player


class IALoversPlayer(Player):
    def think(self, observation, budget):
        list_actions = observation.get_list_actions()
        action = "Tu codigo para seleccionar una acción incluida en list_actions"
        return action

    def __str__(self):
        return "IALoversPlayer"
```
Hay dos cosas importantes que debes tener en cuenta:
1. La función **think** debe devolver una acción antes del número de segundos
indicados en budget. Si tarda más, el sistema seleccionará una acción al
azar de entre las posibles y no hará caso a tu código.
2. La variable **observation** es la visión desde el punto de vista del jugador del 
estado del juego. Esto quiere decir que será posible acceder a:
- Las cartas del jugador.
- Las cartas que ha ganado cada jugador.
- La carta que es triunfo.
3. El resto de partes del estado del juego, como las cartas de los otros
jugadores y las cartas en la baraja, se pueden acceder desde **observation**,
pero serán una posible configuración de todas las posibles existentes,
no reflejando el estado actual de la partida.

Una vez creada la clase, hay que ir al programa **play_match.py** y en la línea 33,
reemplar _RandomPlayer()_ o _AlwaysFirstPlayer()_, por el constructor de tu bot. Por ejemplo,
si queremos probar el bot _IALoversPlayer_ contra _RandomPlayer()_, la línea 33 deberá ser:
```python
l_players = [IALoversPlayer(), AlwaysFirstPlayer()] 
```

Finalmente, ejecutamos el programa **play_match.py** para robar el funcionamiento del
bot implementado.

## Breve explicación del código fuente
Programas principales:
- **play_match**: Programa principal que permite partidas entre dos bots.
- **play_league**: Programa principal que permite una competición entre varios bots. Este será
el programa que se usará para ejecutar la competición.

Las variables más importantes que controlan las partidas son:
- **budget**: Es el tiempo en segundos que tiene el bot para pensar (en la función think del Player)
- **verbose**: True/False. Si es True mostrará mensajes por la consola.
- **controlling_time**: True/False. Si es True controla el tiempo que tiene el bot para pensar.
- **save_game**: True/False. Si es True guarda en un fichero la partida para su estudio posterior.
- **save_name**: Nombre del fichero donde se guardará la partida.
- **n_matches**: En play_league, número de partidas entre los bots.
- 
Durante la competición, estas variables tendrán los siguientes valores:
```python
budget = 1
verbose = False
controlling_time = True
save_game = True
save_name = "Out/game"
n_matches = 100
```

Bots implementados (en la carpeta Players):
- **Player**: Clase abstracta que contiene la estructura que hay que seguir para implementar un bot.
- **RandomPlayer**: Selecciona al azar una de las tres cartas.
- **SlowPlayer**: Jugadro que siempre tarda más tiempo del requerido para contestar. Se ha creado
para testear que pasa cuando el jugador tarda más tiempo del requerido (budget).
- **HumanPlayer**: Muestra una interfaz texto para un jugador humano seleccione la accion a realizar.
- **AlwaysFirstPlayer**: Siempre juega la primera acción de la lista de posibles acciones del juego.

Clases del juego (en la carpeta Game):
- **Action**: Acción que puede eleguir un jugador.
- **Card**: Cartas del juego.
- **CardCollection**: Colección de cartas. Se incluyen funciones para barajar, repartir, etc.
- **Common**: Código común para varias clases del juego
- **Hueristic**: Contiene la función _get_score_ que dado un estado del juego, devuelve
los puntos que obtiene un jugador. 
- **ForwardModel**: Implementa las reglas del juego. La función más importante
es _play_ que actualiza el estado del juego según la acción realizada por el jugador.
- **GameState**: Implementa el estado del juego.
- **Observation**: Implementa la versión visible del estado del juego. Las partes
no visibles se pueden acceder pero muestran una posible configuración de todas las
exsitentes que no se corresponde con el estado real.
- **BriscaGame**: Clase principal del juego.

## Contacto
Para obtener más información, enviar un email a [montoliu@uji.es]().
