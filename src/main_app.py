# main_app.py

# Importar la clase desde el otro archivo (módulo)
from lavadero import Lavadero

# MODIFICACIÓN CLAVE AQUÍ: La función ahora acepta 3 argumentos
def ejecutarSimulacion(lavadero, prelavado, secado_mano, encerado):
    """
    Simula el proceso de lavado para un vehículo con las opciones dadas.
    Ahora acepta una instancia de lavadero.

    :param lavadero: Instancia de Lavadero.
    :param prelavado: bool, True si se solicita prelavado a mano.
    :param secado_mano: bool, True si se solicita secado a mano.
    :param encerado: bool, True si se solicita encerado.
    """
    
    print("--- INICIO: Prueba de Lavado con Opciones Personalizadas ---")
    
    # Mostrar las opciones solicitadas
    print(f"Opciones solicitadas: [Prelavado: {prelavado}, Secado a mano: {secado_mano}, Encerado: {encerado}]")

    # 1. Iniciar el lavado
    try:
        # Esto establece las opciones y pasa a Fase 0 (Inactivo, pero Ocupado=True)
        lavadero.hacerLavado(prelavado, secado_mano, encerado)
        print("\nCoche entra. Estado inicial:")
        lavadero.imprimir_estado()

        # 2. Avanza por las fases
        print("\nAVANZANDO FASE POR FASE:")
        
        # Usamos un contador para evitar bucles infinitos en caso de error o bucles inesperados
        pasos = 0
        while lavadero.ocupado and pasos < 20: 
            # El cobro ahora ocurre en la primera llamada a avanzarFase (transición 0 -> 1)
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


# Punto de entrada (main): Aquí pasamos los parámetros
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
    ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=False, encerado=False)

        # EJEMPLO 5: Lavado con secado a mano (Requisito 5 y 11)
    # Precio esperado: 5.00 + 1.00 = 6.00 €
    print("\n=======================================================")
    print("EJEMPLO 5: Secado a mano (S)")
    ejecutarSimulacion(lavadero_global, prelavado=False, secado_mano=True, encerado=False)

    # EJEMPLO 6: Lavado con secado a mano + encerado (Requisito 6 y 12)
    # Precio esperado: 5.00 + 1.00 + 1.20 = 7.20 €
    print("\n=======================================================")
    print("EJEMPLO 6: Secado a mano (S), Encerado (S)")
    ejecutarSimulacion(lavadero_global, prelavado=False, secado_mano=True, encerado=True)

    # EJEMPLO 7: Lavado con prelavado + secado a mano (Requisito 7 y 13)
    # Precio esperado: 5.00 + 1.50 + 1.00 = 7.50 €
    print("\n=======================================================")
    print("EJEMPLO 7: Prelavado (S), Secado a mano (S)")
    ejecutarSimulacion(lavadero_global, prelavado=True, secado_mano=True, encerado=False)

    # EJEMPLO 8: Intentar iniciar un lavado mientras otro está en marcha (Requisito 3)
    print("\n=======================================================")
    print("EJEMPLO 8: ERROR (Lavado en marcha, intento de iniciar otro)")
    try:
        lavadero_global.hacerLavado(prelavado=False, secado_mano=False, encerado=False)
        lavadero_global.hacerLavado(prelavado=True, secado_mano=True, encerado=True)  # Debe lanzar RuntimeError
    except RuntimeError as e:
        print(f"ERROR DE ESTADO: {e}")
    