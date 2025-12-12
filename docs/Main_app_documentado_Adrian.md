# Bloque 1: Importación

- **from lavadero import Lavadero:** Importa la clase `Lavadero` definida en el archivo `lavadero.py`.  
- **Función:** Permite usar en este script todas las operaciones y atributos del lavadero.  
- **Nota:** En Python, la importación busca el archivo en el mismo directorio o en el `PYTHONPATH`.



```python
# main_app.py

from lavadero import Lavadero

```

# Bloque 2: Definición de la función ejecutarSimulacion

- **Propósito:** Simular un ciclo de lavado con las opciones dadas.  
- **Parámetros:**  
  - `lavadero`: instancia de la clase Lavadero.  
  - `prelavado`: booleano, indica si se solicita prelavado a mano.  
  - `secado_mano`: booleano, indica si se solicita secado a mano.  
  - `encerado`: booleano, indica si se solicita encerado.  
- **Flujo de ejecución:**  
  - Imprime las opciones seleccionadas.  
  - Llama a `hacerLavado()` para iniciar el ciclo.  
  - Imprime el estado inicial del lavadero.  
  - Avanza fase por fase en un bucle controlado por contador (máx. 20 pasos).  
  - Imprime cada fase recorrida.  
  - Al finalizar, muestra el estado final y los ingresos acumulados.  
- **Manejo de excepciones:**  
  - `ValueError`: si se intenta encerar sin secado a mano.  
  - `RuntimeError`: si se intenta iniciar un lavado estando ocupado.  
  - `Exception`: cualquier otro error inesperado.



```python
def ejecutarSimulacion(lavadero, prelavado, secado_mano, encerado):
    """
    Simula el proceso de lavado para un vehículo con las opciones dadas.
    Ahora acepta una instancia de lavadero.
    """
    
    print("--- INICIO: Prueba de Lavado con Opciones Personalizadas ---")
    print(f"Opciones solicitadas: [Prelavado: {prelavado}, Secado a mano: {secado_mano}, Encerado: {encerado}]")

    try:
        lavadero.hacerLavado(prelavado, secado_mano, encerado)
        print("\nCoche entra. Estado inicial:")
        lavadero.imprimir_estado()

        print("\nAVANZANDO FASE POR FASE:")
        
        pasos = 0
        while lavadero.ocupado and pasos < 20: 
            lavadero.avanzarFase()
            print(f"-> Fase actual: ", end="")
            lavadero.imprimir_fase()
            print() 
            pasos += 1
        
        print("\n----------------------------------------")
        print("Lavado completo. Estado final:")
        lavadero.imprimir_estado()
        print(f"Ingresos acumulados: {lavadero.ingresos:.2f} €")
        print("----------------------------------------")
        
    except ValueError as e: # Captura la excepción de regla de negocio (Requisito 2)
        print(f"ERROR DE ARGUMENTO: {e}")
    except RuntimeError as e: # Captura la excepción de estado (Requisito 3)
        print(f"ERROR DE ESTADO: {e}")
    except Exception as e:
        print(f"ERROR INESPERADO: {e}")

```

# Bloque 3: Punto de entrada (main) con ejemplos

- **if __name__ == "__main__":**  
  - Garantiza que el bloque se ejecute solo si el archivo se ejecuta directamente, no cuando se importa como módulo.  
- **lavadero_global = Lavadero():**  
  - Se crea una única instancia de Lavadero para acumular ingresos entre simulaciones.  
- **Ejemplos de ejecución:**  
  - **Ejemplo 1:** Prelavado + Secado a mano + Encerado → ingresos esperados 8.70 €.  
  - **Ejemplo 2:** Sin extras → ingresos esperados 5.00 €.  
  - **Ejemplo 3:** Encerado sin secado → debe lanzar `ValueError`.  
  - **Ejemplo 4:** Solo prelavado → ingresos esperados 6.50 €.  
- **Función:** Demostrar distintos casos de uso, validar reglas de negocio y mostrar acumulación de ingresos.



```python
if __name__ == "__main__":
    
    lavadero_global = Lavadero() # Usamos una única instancia para acumular ingresos
    
    # EJEMPLO 1: Lavado completo con prelavado, secado a mano, con encerado (Requisito 8 y 14)
    # Precio esperado: 5.00 + 1.50 + 1.00 + 1.20 = 8.70 €
    print("\n=======================================================")
    print("EJEMPLO 1: Prelavado (S), Secado a mano (S), Encerado (S)")
    ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=True, encerado=True)
    
    # EJEMPLO 2: Lavado rápido sin extras (Requisito 9)
    # Precio esperado: 5.00 €
    print("\n=======================================================")
    print("EJEMPLO 2: Sin extras (Prelavado: N, Secado a mano: N, Encerado: N)")
    ejecutarSimulacion(lavadero_global, prelavado=False, secado_mano=False, encerado=False)

    # EJEMPLO 3: Lavado con encerado, pero sin secado a mano (Debe lanzar ValueError - Requisito 2)
    print("\n=======================================================")
    print("EJEMPLO 3: ERROR (Encerado S, Secado a mano N)")
    ejecutarSimulacion(lavadero_global, prelavado=False, secado_mano=False, encerado=True)

    # EJEMPLO 4: Lavado con prelavado a mano (Requisito 4 y 10)
    # Precio esperado: 5.00 + 1.50 = 6.50 €
    print("\n=======================================================")
    print("EJEMPLO 4: Prelavado (S), Secado a mano (N), Encerado (N)")
    ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=False)

```

    
    =======================================================
    EJEMPLO 1: Prelavado (S), Secado a mano (S), Encerado (S)
    --- INICIO: Prueba de Lavado con Opciones Personalizadas ---
    Opciones solicitadas: [Prelavado: True, Secado a mano: True, Encerado: True]
    
    Coche entra. Estado inicial:
    ----------------------------------------
    Ingresos Acumulados: 0.00 €
    Ocupado: True
    Prelavado a mano: True
    Secado a mano: True
    Encerado: True
    Fase: 0 - Inactivo
    ----------------------------------------
    
    AVANZANDO FASE POR FASE:
     (COBRADO: 8.70 €) -> Fase actual: 1 - Cobrando
    -> Fase actual: 2 - Haciendo prelavado a mano
    -> Fase actual: 3 - Echándole agua
    -> Fase actual: 4 - Enjabonando
    -> Fase actual: 5 - Pasando rodillos
    -> Fase actual: 6 - Haciendo secado automático
    -> Fase actual: 0 - Inactivo
    
    ----------------------------------------
    Lavado completo. Estado final:
    ----------------------------------------
    Ingresos Acumulados: 8.70 €
    Ocupado: False
    Prelavado a mano: False
    Secado a mano: False
    Encerado: False
    Fase: 0 - Inactivo
    ----------------------------------------
    Ingresos acumulados: 8.70 €
    ----------------------------------------
    
    =======================================================
    EJEMPLO 2: Sin extras (Prelavado: N, Secado a mano: N, Encerado: N)
    --- INICIO: Prueba de Lavado con Opciones Personalizadas ---
    Opciones solicitadas: [Prelavado: False, Secado a mano: False, Encerado: False]
    
    Coche entra. Estado inicial:
    ----------------------------------------
    Ingresos Acumulados: 8.70 €
    Ocupado: True
    Prelavado a mano: False
    Secado a mano: False
    Encerado: False
    Fase: 0 - Inactivo
    ----------------------------------------
    
    AVANZANDO FASE POR FASE:
     (COBRADO: 5.00 €) -> Fase actual: 1 - Cobrando
    -> Fase actual: 3 - Echándole agua
    -> Fase actual: 4 - Enjabonando
    -> Fase actual: 5 - Pasando rodillos
    -> Fase actual: 7 - Haciendo secado a mano
    -> Fase actual: 0 - Inactivo
    
    ----------------------------------------
    Lavado completo. Estado final:
    ----------------------------------------
    Ingresos Acumulados: 13.70 €
    Ocupado: False
    Prelavado a mano: False
    Secado a mano: False
    Encerado: False
    Fase: 0 - Inactivo
    ----------------------------------------
    Ingresos acumulados: 13.70 €
    ----------------------------------------
    
    =======================================================
    EJEMPLO 3: ERROR (Encerado S, Secado a mano N)
    --- INICIO: Prueba de Lavado con Opciones Personalizadas ---
    Opciones solicitadas: [Prelavado: False, Secado a mano: False, Encerado: True]
    ERROR DE ARGUMENTO: No se puede encerar el coche sin secado a mano
    
    =======================================================
    EJEMPLO 4: Prelavado (S), Secado a mano (N), Encerado (N)



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[21], line 26
         24 print("\n=======================================================")
         25 print("EJEMPLO 4: Prelavado (S), Secado a mano (N), Encerado (N)")
    ---> 26 ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=False)


    TypeError: ejecutarSimulacion() missing 1 required positional argument: 'encerado'

