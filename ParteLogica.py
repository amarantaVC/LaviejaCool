#!/usr/bin/env python
#
#-------------------------------------------------------------------
#
#  Universidad Experimental Simon BOlivar
#  Laboratorio de Algoritmos y Estructuras I
#  Jennifer Gamez 16-10396
#  Amaranta Villegas 16-11247
#
#-------------------------------------------------------------------
#
#IMPORTANDO LIBRERIA
import sys

#-------------------------------------------------------------------
#                  DEFINIENDO PROCEDIMIENTOS Y FUNCIONES
#-------------------------------------------------------------------

# Definicion que crea los tableros N x N
def Tablero_NxN(tamano_Tablero, n):
    # Entrada de la matriz (elementos a rellenar)
    tablero = [[ n for z in range(tamano_Tablero)] for y in range(tamano_Tablero)]
    # Salida del tablero 
    return tablero

# Super Tablero: contiene las dimensiones (conjunto de tableros).
def Super_tablero(tamano):
    #Dimensiones: array que conformado por un conjunto de tableros
    dimensiones = [ z for z in range(tamano)]
    # Cota : Dimensiones -1
    for i in dimensiones:
        dimensiones[i] = Tablero_NxN(tamano, 0)
        # Asigna n == 0, porque inicialmente la matriz esta vacia Tablero_NxN(tamano, n)
    # Salida. Retornando el Super Tablero
    return dimensiones

# Mostrar en la consola el tablero por filas (Da la impresion de un tablero) 
def MostrarTablero(Tab): # Mostrar filas al imprimir
# Aqui definimos un tablero por cada llamada fila en el rango de Tab
    # Cota : DimensionesTab -1
    # DimensionesTab es la parte entera (numero) de Tab.
    for fila in Tab:
        print (fila) 

# Funcion. Determina si una jugada esta dentro de los parametros del tablero y no esta ocupada. 
def Jugada_Valida(fila,columna, tablero):
  while True:
    try:
        Valido = True
        # Verificando que la casilla este vacia.
        assert(tablero[fila][columna] == 0)
        assert(fila >= 0 and columna >= 0)
        break
    except:
        # En caso de estar ocupada o fuera de los parametros  
        Valido = False
    finally:
        # Salida de la Funcion.
        return Valido

# Definiendo las fichas a emplear en los tableros. 
def QueQuiereSer(Jugador1, Jugador2): #El jugador decide si quiere ser X y/o O
    while True:
        try: 
            letra = str(input("\n%s, Quieres ser la ficha X o la ficha O?: " %Jugador1)).upper() 
            # letra = raw_input().upper() #Esto hara que se coloquen mayusculas las letras que introduzcan
            assert(letra == "X" or letra == "O")
            break
        except:
            print ("Intente nuevamente.")
        finally:
            #Asignando las fichas a los jugadores
            if letra == "X" or letra == "O":
                if letra == "X":
                    Asig_1 = "X" #Jugador1
                    Asig_2 = "O" #Jugador2
                    
                else:
                    Asig_1 = "O" #Jugador1
                    Asig_2 = "X" #Jugador2
                # Salida de la Funcion.
                return Asig_1 , Asig_2

# Decidiendo quien comienza la partida primero
def QuienIniciaPartida(Jugador1, Jugador2, ficha1, ficha2):
    # Inicializacion. Estos hacen el papel de sustitutos si es necesario hacer un cambio.
    CambioJugador = 0
    CambioFicha = 0

    # Inicializando el valor de entrada 
    Escoge = -1

    # Salida
    print ("\nJugador1 = %s con la ficha %s" %(Jugador1,ficha1))
    print ("Jugador2 = %s con la ficha %s" %(Jugador2,ficha2))

    while True:
        try:
            # Entrada
            Escoge = int(input("\nQuieres que ese sea el orden de turnos? Primero %s y luego %s; \
1 (Si), 0 (No): " %(ficha1,ficha2)))
            # Si escoge 1 se toma como True, sino se lee 0 y este es False
            assert(float(Escoge).is_integer())
            assert((Escoge == 1 or Escoge == 0) and Escoge >= 0)
            break
        except:
            print ("\nIntente nuevamente.")
        finally:
        
            if Escoge == 1 or Escoge == 0:
                if Escoge:    
                    pass
                else:
                    # Realizando un intercambio del orden de los jugadores con sus respectivas fichas por decision del usuario.
                    CambioJugador = Jugador1
                    Jugador1 = Jugador2
                    Jugador2 = CambioJugador

                    CambioFicha = ficha1
                    ficha1 = ficha2
                    ficha2 = CambioFicha

                    print ("\nJugador1 = %s con la ficha %s" %(Jugador1,ficha1))
                    print ("Jugador2 = %s con la ficha %s" %(Jugador2,ficha2))
                # Salida de la Funcion.
                return Jugador1, Jugador2, ficha1, ficha2
            else: # este se lee en caso de que la entrada sea un string
                pass

# Procedimiento por Tablero. Jugadas por tablero 
def JugadaTablero(fila,columna,tablero,ReferenciaTablero,tamano,ficha):
    # Disponibilidad en la dimension a escoger
    n = tamano - 1

    # fail; cuenta si se presenta un error por Casilla ocupada o inexistente
    fail = 0    
    while True:
        try:
            # Entrada.
            fila = int(input("\nFila a trabajar (E: %s filas): " %n))
            columna = int(input("Columna a trabajar (E: %s columnas): " %n))
            assert (fila >= 0 and columna >= 0)
            assert(float(fila).is_integer())
            assert(float(columna).is_integer())
        except:
            print ("Intente nuevamente.")
        finally:  
            if fila >= 0 and columna >= 0:
            # Llamada de Jugada_Valida evalua si la casilla esta ocupada o no exite.
                if Jugada_Valida(fila,columna, tablero) == True: 
                    tablero[fila][columna] =  ficha 
                    print ("\nTablero %s" %ReferenciaTablero)
                    # Salida. Llama la funcion y muestra el tablero por filas..
                    MostrarTablero(tablero)

                elif (Jugada_Valida(fila,columna, tablero) == False) or (Jugada_Valida(fila,columna, tablero) == None):
                    fail = 1
                    print ("\nIntente nuevamente. Casilla ocupada o inexistente.")
                    print ("\nTablero %s" %ReferenciaTablero)
                    # Salida. Llama la funcion y muestra el tablero por filas.
                    MostrarTablero(tablero)

                # Salida de la Funcion y los datos proporcionados de fila y/o columna.
                return fail,fila,columna
            else:
                pass

# Funcion que pide de entrada la eleccion de un Tablero; este verifica si la refencia es valida.
def ChooseTablero(Jugador,TablerosDisponible):
    # Inicializando valor de entrada.
    ReferenciaTablero = -1  

    while True:
        try:     
            # Seleccionar tablero a preferencia por el jugador
            ReferenciaTablero = int(input('\n%s, elije el tablero a jugar. Recuerde que puede elergir un tablero entre: %s tablero(s) \
contando el tablero 0: '%(Jugador, TablerosDisponible)))
            assert(float(ReferenciaTablero).is_integer())
            # COMPROBANDO QUE EL TABLERO SELECCIONADO EXISTA EN EL SUPER TABLERO    
            assert((ReferenciaTablero >= 0) and (ReferenciaTablero <= TablerosDisponible))     
            break
        
        except:
            print ("\nUsted ha elegido un tablero inexistente en la Dimension.")
            print ("Intente nuevamente.")
        
        finally:
            if (ReferenciaTablero >= 0) and (ReferenciaTablero <= TablerosDisponible):
                # Salida. Retornando la referencia valida.
                return ReferenciaTablero
            else:
                pass

# Comprobar / Reafirmar que el tablero seleccionado es el deseado por el usuario.
def OKTablero():
    OK = -1
    while  True:
        try:
            #Condicional de confirmacion de tablero deseado.
            OK = int(input("\nDesea continuar con este tablero?; 1 (Si), 0 (No): "))
            assert(float(OK).is_integer())
            assert( OK == 1 or OK == 0)
            break
        except:
            print ("\nIntente nuevamente. Lea bien la instruccion.")
        finally:
            if OK == 1 or OK == 0:
                if OK:
                    return "OK"
                else:
                    return "NOT OK"

# Funcion que determina la existencia de linea entre tablero y en el tablero
def HayAlinea(SuperTablero, Tablero, Tamano, Fila, Columna, Ficha):
  #SuperTablero: contiene los tableros de todas las dimensiones
  #Tablero: el tablero que selecciona el usuario a realizar su jugada

  def HayAlineaHorizontal(Tablero,Fila,Tamano,Ficha):
    # Valor booleano
    HaylineaHorizontal = 0
    # Tablero
    tab = Tablero[Fila]
    # Evaluando entre tablero si se cumple la condicion
    if all(tab[i] == Ficha for i in range(Tamano) if Tablero[i] != 0 ):
      HaylineaHorizontal = 1
    elif all(tab[i] != Ficha or tab[i] == 0 for i in range(Tamano) if Tablero[i] != 0 ):
      pass
    # Retornando la existencia de Linea Horizontal
    return HaylineaHorizontal

  def HayAlineaVertical(Tablero,Columna,Tamano, Ficha):
    # Valor booleano
    HaylineaVertical = 0
    # Inicializando contador
    cont_vertical = 0
    # Evaluando entre tablero si se cumple la condicion
    # Cota : Tamano -1
    for i in range(Tamano):
      if Tablero[i][Columna] == Ficha and Tablero[i][Columna] != 0: 
        cont_vertical = cont_vertical + 1
      elif Tablero[i][Columna] != Ficha or Tablero[i][Columna] == 0:
        pass
    # Evaluando existencia
    if cont_vertical == Tamano:
      HaylineaVertical = 1
    else:
      pass
    # Retornando la existencia de Linea Vertical
    return HaylineaVertical

  def HayAlineaDiagonal(Tablero,Tamano,Ficha):
    # Valor booleano
    HayAlineaDiagonal= 0
    # Inicializando contador
    cont_diagonal = 0
    # Evaluando entre tablero si se cumple la condicion
    # Cota : Tamano -1
    for i in range(0,Tamano):
      # Cota : Tamano -1
      for j in range (0,Tamano):  
        if Tablero[i][j] == Ficha and i == j: 
          cont_diagonal = cont_diagonal + 1
        else: 
          pass
    # Evaluando existencia      
    if cont_diagonal == Tamano:
      HayAlineaDiagonal = 1
    elif cont_diagonal != Tamano:
      pass
    # Retornando la existencia de Linea Diagonal
    return HayAlineaDiagonal
  
  def HayAlineaTableros(SuperTablero,Fila,Columna,Tamano, Ficha):
    # Posicion del primero tablero a escoger. Valor fijo. Ctte.
    k = 0  
    # Tablero ctte, nuestro tablero a comparar sera el fijo
    TableroFijo = SuperTablero[k] 
    # Valor de existencia.
    HayAlineaTablero = 0
    # Contador 
    contador_lineaTablero = 0

    # Evaluando entre tablero si se cumple la condicion
    # Cota : DimensionesTab -1  
    # DimensionesTab es el entero (numero) de SuperTablero
    for Tablero in SuperTablero:
      if (TableroFijo[Fila][Columna] == Tablero[Fila][Columna] == Ficha):
        contador_lineaTablero = contador_lineaTablero + 1
      else:
        pass
    # Evaluando existencia
    if contador_lineaTablero == Tamano:
       HayAlineaTablero = 1
    else:
      pass
    # Retornando existencia
    return HayAlineaTablero  

  ###LLAMADA DE LAS FUNCIONES INTERNAS###
  return HayAlineaHorizontal(Tablero,Fila,Tamano,Ficha), HayAlineaVertical(Tablero,Columna,Tamano,Ficha),\
HayAlineaDiagonal(Tablero,Tamano,Ficha), HayAlineaTableros(SuperTablero,Fila,Columna,Tamano, Ficha)

# Definicion Suma de Linea  
def SumarLinea(LineaJugador, LineaHorizontal, LineaVertical,LineaDiag,LineaTableros):
  # Inicializa en cero LineaJugador.
  # Este condicional lee 1 como True y 0 False.
  if LineaHorizontal or LineaVertical or LineaDiag or LineaTableros: 
    LineaJugador =  LineaHorizontal + LineaVertical + LineaDiag + LineaTableros # actualiza el contador cuando retorna esto
  else:
    pass # No actualiza el contador si no cumple la condicion de existencia
  return LineaJugador

# Deficiones Dimensiones a trabajar
def Dimension():    
    DimensionesTab = -1
    while True: # Dimensiones / Tamano
        try:
            # Entrada. Dimension o tamano de los tableros a jugar.    
            DimensionesTab = int(input("\nIndique las dimesiones del tablero a jugar = "))
            # Aseguramos que la entrada sea un entero estrictamente .is_integer()
            assert(float(DimensionesTab).is_integer())  
            assert ( DimensionesTab >= 2)
            break                                           
        except:
            print ("Las dimesiones del tablero son estrictamente numericas y mayores iguales a 2.")
            print ("Intente nuevamente.")
        finally:
            # Se ejecuta si las aserciones se cumplen.
            if DimensionesTab >= 2:
               return DimensionesTab
            else:
                pass

# Funcion de Entrada Identificacion de los usuarios
def Identificacion(J1,J2):
    while True: # Identificacion
        try:    
            #ENTRADA.
            J1 = str(input("\nIngrese el nombre del Jugador 1: ")).upper()
            J2 = str(input("Ingrese el nombre del Jugador 2: ")).upper()

            assert(len(J1) > 0)
            assert(len(J2) > 0)
            break

        except:
            print ("\nLa identificacion de los jugadores es esencial.")
            print ("Por favor ingrese una identificacion valida.")

        finally:
            # Se ejecuta si las aserciones se cumplen.
            if len(J1) > 0 and len(J2) > 0:
                # SALIDA DE LA IDENTIFICACION DE LOS JUGADORES
                return J1, J2
            else:
                pass


    
#-------------------------------------------------------------------
#
#                   PROCEDIMIENTO PRINCIPAL
#                       
#-------------------------------------------------------------------


def OtraPartida():
                            
    # Llamada de la funcion Dimension
    DimensionesTab = Dimension()
    
    # Mensaje de las Dimensiones seleccionada por los usuario
    print ("\nHas elegido un tablero: %s x %s." %(DimensionesTab,DimensionesTab))
    print ("Dimensiones a jugar: %s Dimensiones." %DimensionesTab)
    
    # Identificacion de Jugadores
    Jugador1, Jugador2 = Identificacion(0,0)

    print ("\nJugador1 = %s" %Jugador1)
    print ("Jugador2 = %s" %Jugador2)

    # Asigando las fichas
    ficha_jug1, ficha_jug2 = QueQuiereSer(Jugador1,Jugador2)

    # Monstrando los resultados. Se llama la funcion para reafirmar la informacion proporcionada por los usuarios.
    Jugador1, Jugador2, ficha_jug1, ficha_jug2 = QuienIniciaPartida(Jugador1, Jugador2, ficha_jug1, ficha_jug2)

    # Construyendo los tableros en la dimension / tamano seleccionada.
    SuperTableros = Super_tablero(DimensionesTab)

    # Disponibilidad de tablero a escoger.
    n = DimensionesTab - 1 

    # Fichas entre todos los tableros
    Fichas = DimensionesTab * DimensionesTab * DimensionesTab 

    # Fichas entre el mismo tablero
    PartidaTablero = DimensionesTab * DimensionesTab 

    # Inicializando Contador de Lineas.
    LineaJugador1 = 0
    LineaJugador2 = 0 

    # JUGANDO EN LOS TABLEROS
    # Cota : Fichas -1
    for i in range (Fichas):

        if i % 2 == 0 : # Par: Jugador 1
            # Salida. Mensaje
            print ("\nJuegan las: %s, Jugador: %s." %(ficha_jug1,Jugador1))

            print ("Fichas disponible(s): %s" %Fichas)

            # Referencia del tablero a escoger.
            refe = ChooseTablero(Jugador1, n)

            # Tablero
            Tablero = SuperTableros[refe]    
            print ("\nTablero %s" %refe)
            MostrarTablero(Tablero)

            while True:
                try:
                    # Confirmacion de tablero deseado
                    OK = OKTablero()
                    assert(OK == "OK")
                    break
                except:
                    # Referencia del tablero a escoger.
                    refe = ChooseTablero(Jugador1, n)

                    # Tablero
                    Tablero = SuperTableros[refe]    
                    print ("\nTablero %s" %refe)
                    MostrarTablero(Tablero)

                finally:                              
                    if OK == "OK":
                        turno_fail,fila,columna = JugadaTablero(-1,-1,Tablero,refe,DimensionesTab,ficha_jug1)
                        # Condicional por si la fila y/o columna seleccionada se salen de la dimension.
                        if turno_fail > 0: # Se sale de la dimension
                            JugadaTablero(-1,-1,Tablero,refe,DimensionesTab,ficha_jug1)
                        elif turno_fail == 0: # Se mantiene en la dimension
                            # Verificando si hay Linea.
                            LineaHorizontal,LineaVertical,LineaDiag,LineaTableros= HayAlinea(SuperTableros,\
Tablero, DimensionesTab, fila, columna, ficha_jug1)

                            # Sumando si hay linea.
                            LineaJugador1 =  LineaJugador1 + SumarLinea(LineaJugador1, LineaHorizontal,\
LineaVertical,LineaDiag,LineaTableros)
                            # Salida de los resultados obtenidos con la jugada del jugador.
                            print ("\nLinea(s) Realizadas = %s" %LineaJugador1)
                    else:
                        pass
        elif i % 2 != 0: # Impar: Jugador 2
            # Jugador actual.
            print ("\nJuegan las: %s, Jugador: %s." %(ficha_jug2,Jugador2))

            print ("Fichas disponible(s): %s" %Fichas)

            # Referencia del tablero a escoger.
            refe = ChooseTablero(Jugador2, n)

            # Tablero
            Tablero = SuperTableros[refe]    
            print ("\nTablero %s" %refe)
            MostrarTablero(Tablero)

            while True:
                try:
                    # Confirmacion de tablero deseado
                    OK = OKTablero()
                    assert(OK == "OK")
                    break
                except:
                    # Referencia del tablero a escoger.
                    refe = ChooseTablero(Jugador2, n)

                    # Tablero
                    Tablero = SuperTableros[refe]    
                    print ("\nTablero %s" %refe)
                    MostrarTablero(Tablero)

                finally:                              
                    if (OK ==str("OK")):
                        turno_fail,fila,columna = JugadaTablero(-1,-1,Tablero,refe,DimensionesTab,ficha_jug2) 
                        # Condicional por si la fila y/o columna seleccionada se salen de la dimension.
                        if turno_fail > 0: # Se sale de la dimension
                            JugadaTablero(-1,-1,Tablero,refe,DimensionesTab,ficha_jug2)
                        elif turno_fail == 0: # Se mantiene en la dimension
                            # Verificando si hay Linea.
                            LineaHorizontal,LineaVertical,LineaDiag,LineaTableros= HayAlinea(SuperTableros,\
Tablero, DimensionesTab, fila, columna, ficha_jug2)

                            # Sumando si hay linea.
                            LineaJugador2 = LineaJugador2 +  SumarLinea(LineaJugador2, LineaHorizontal,\
LineaVertical,LineaDiag,LineaTableros)
                            # Salida de los resultados obtenidos con la jugada del jugador.
                            print ("\nLinea(s) Realizadas = %s" %LineaJugador2)
                    else:
                        pass                                                  
        # Cada vez que juega disminuye una ficha
        Fichas = Fichas - 1     

    # Al acabarse la partida.    
    # Quien es el ganador?                        
    if LineaJugador1 > LineaJugador2:
      print ("\nHAZ GANADO! %s" %(Jugador1))
    elif LineaJugador1 < LineaJugador2:
      print ("\nHAZ GANADO! %s" %(Jugador2)) 
    elif LineaJugador1 == LineaJugador2:
        print ("\nEMPATE!")
    # Resultados obtenidos de la partida
    print ("\nTotal resultados: %s= %s lineas. %s= %s lineas" %(Jugador1,LineaJugador1,Jugador2,LineaJugador2))

    # Y si queremos volver a dar otra jugada. Una revancha o mas nivel en el tablero.
    while True:
        try:
            Otra = int(input("\nDesean jugar otra partida?; 1 (Si), 0 (No):"))
            assert(float(Otra).is_integer())
            assert( Otra == 1 or Otra == 0)
            break
        except:
            print ("\nIntente nuevamente.")
        finally:
            if Otra == 1 or Otra == 0:
                if Otra:
                    # Otra partida.
                    OtraPartida()
                else:
                    # Se acabo.
                    print ("\nExcelente partida.")                            

# Llamando el procedimiento principal
OtraPartida()