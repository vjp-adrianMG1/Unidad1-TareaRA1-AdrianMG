# 1. Encabezado y definición de clase

**Propósito del módulo:** Modelar un túnel de lavado con estados, reglas de negocio y secuencias de fases.

**Definición de clase Lavadero:** En Python, una clase agrupa datos (atributos) y comportamiento (métodos) de un objeto.

**Docstring de clase:** El texto entre triple comillas describe el objetivo y alcance del componente, útil para documentación y ayuda integrada.

**Nota de fidelidad:** Documentamos tal cual sin corregir incoherencias, señalamos las observaciones cuando afectan al entendimiento.


```python
# lavadero.py

class Lavadero:
    """
    Simula el estado y las operaciones de un túnel de lavado de coches.
    Cumple con los requisitos de estado, avance de fase y reglas de negocio.
    """

```

# 2. Constantes de fase

**Constantes de estado:** Representan fases del proceso como enteros con nombres semánticos, evitando “números mágicos” y mejorando la legibilidad.

**Ventaja:** Cambios futuros en los valores no afectan el código que usa los nombres.

**Listado de fases:** 0 inactivo, 1 cobrando, 2 prelavado, 3 agua, 4 enjabonado, 5 rodillos, 6 secado automático, 7 secado a mano, 8 encerado.


```python
 FASE_INACTIVO = 0
    FASE_COBRANDO = 1
    FASE_PRELAVADO_MANO = 2
    FASE_ECHANDO_AGUA = 3
    FASE_ENJABONANDO = 4
    FASE_RODILLOS = 5
    FASE_SECADO_AUTOMATICO = 6
    FASE_SECADO_MANO = 7
    FASE_ENCERADO = 8
```

# 3. Constructor y estado inicial

**__init__:** Método especial que se ejecuta al crear una instancia. Inicializa el estado interno.

**Atributos “privados”:** El doble guion bajo activa name mangling (convención para desalentar acceso externo directo).

**Estado base:** ingresos 0.0, fase 0 (inactivo), ocupado False, extras False.

**Llamada a terminar():** Refuerza el estado inicial estableciendo los mismos valores. Aunque redundante, asegura consistencia.


```python
    def __init__(self):
        """
        Constructor de la clase. Inicializa el lavadero.
        Cumple con el requisito 1.
        """
        self.__ingresos = 0.0
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False
        self.terminar() 

```

# 4. Propiedades de solo lectura

- **@property:** Permite acceder a métodos como si fueran atributos, ofreciendo encapsulación sin exponer variables internas.  
- **Getters:** Devuelven el estado actual de fase, ingresos, ocupado y las opciones de extras.  
- **Uso:** `obj.fase`, `obj.ingresos`, etc., sin paréntesis, manteniendo interfaz clara.


```python
    @property
    def fase(self):
        return self.__fase

    @property
    def ingresos(self):
        return self.__ingresos

    @property
    def ocupado(self):
        return self.__ocupado
    
    @property
    def prelavado_a_mano(self):
        return self.__prelavado_a_mano

    @property
    def secado_a_mano(self):
        return self.__secado_a_mano

    @property
    def encerado(self):
        return self.__encerado

```

# 5. Reinicio de ciclo con terminar()

- **Función:** Restablece el lavadero a estado inactivo, no ocupado y sin extras.  
- **Momento de uso:** Se invoca al finalizar fases terminales y en el constructor.  
- **Efecto:** Cierra el ciclo y deja el objeto listo para un nuevo lavado.


```python
    def terminar(self):
        self.__fase = self.FASE_INACTIVO
        self.__ocupado = False
        self.__prelavado_a_mano = False
        self.__secado_a_mano = False
        self.__encerado = False

```

# 6. Inicio de lavado y validaciones de negocio

- **`hacerLavado(...)`:** Configura un nuevo ciclo con las opciones dadas.  
- **Validaciones:**  
  - Si el lavadero está ocupado, se levanta `RuntimeError` (no se admite solapamiento de ciclos).  
  - Si se solicita encerado sin secado a mano, se levanta `ValueError` (combinación no permitida).  
- **Configuración:** Define `ocupado=True`, resetea fase a inactivo y guarda las opciones.



```python
    def hacerLavado(self, prelavado_a_mano, secado_a_mano, encerado):
        """
        Inicia un nuevo ciclo de lavado, validando reglas de negocio.
        
        :raises RuntimeError: Si el lavadero está ocupado (Requisito 3).
        :raises ValueError: Si se intenta encerar sin secado a mano (Requisito 2).
        """
        if self.__ocupado:
            raise RuntimeError("No se puede iniciar un nuevo lavado mientras el lavadero está ocupado")
        
        if not secado_a_mano and encerado:
            raise ValueError("No se puede encerar el coche sin secado a mano")
        
        self.__fase = self.FASE_INACTIVO  
        self.__ocupado = True
        self.__prelavado_a_mano = prelavado_a_mano
        self.__secado_a_mano = secado_a_mano
        self.__encerado = encerado

```

# 7. Cálculo y acumulación de ingresos

- **`_cobrar()`:** Método interno (por convención) que calcula el coste del lavado y lo suma a los ingresos acumulados.  
- **Tarifa:** Base 5.00; extras: +1.50 (prelavado), +1.20 (secado a mano), +1.00 (encerado).  
- **Retorno:** Devuelve el importe cobrado para imprimirlo al avanzar la primera fase.  
- **Nota:** Los importes están definidos en código; no están parametrizados externamente.



```python
    def _cobrar(self):
        """
        Calcula y añade los ingresos según las opciones seleccionadas (Requisitos 4-8).
        Precio base: 5.00€ (Implícito, 5.00€ de base + 1.50€ de prelavado + 1.00€ de secado + 1.20€ de encerado = 8.70€)
        """
        coste_lavado = 5.00
        
        if self.__prelavado_a_mano:
            coste_lavado += 1.50 
        
        if self.__secado_a_mano:
            coste_lavado += 1.20 
            
        if self.__encerado:
            coste_lavado += 1.00 
            
        self.__ingresos += coste_lavado
        return coste_lavado

```

# 8. Avance de fase y lógica de transición

- **`avanzarFase()`:** Orquesta la progresión de fases según el estado y las opciones.  
- **Guard clause:** Si no está ocupado, retorna sin cambios (evita operar fuera de ciclo).  
- **Cobro al inicio:** De fase 0 (inactivo) a 1 (cobrando) se ejecuta `_cobrar()` y se imprime el importe.  
- **Ramas principales:**  
  - 1 → 2 si hay prelavado, en otro caso 1 → 3.  
  - Secuencia 2 → 3 → 4 → 5.  
  - En 5, decisión de secado: si `secado_a_mano` True, va a 6 (automático); si False, va a 7 (mano). Observación: semántica invertida respecto al nombre del flag.  
- **Fases 6/7/8:** Terminan el ciclo llamando a `terminar()`. La fase 8 (encerado) no se alcanza por transición en el código actual.  
- **Error de fase:** Si aparece un estado no contemplado, `RuntimeError` con mensaje explicativo.



```python
    def avanzarFase(self):
       
        if not self.__ocupado:
            return

        if self.__fase == self.FASE_INACTIVO:
            coste_cobrado = self._cobrar()
            self.__fase = self.FASE_COBRANDO
            print(f" (COBRADO: {coste_cobrado:.2f} €) ", end="")

        elif self.__fase == self.FASE_COBRANDO:
            if self.__prelavado_a_mano:
                self.__fase = self.FASE_PRELAVADO_MANO
            else:
                self.__fase = self.FASE_ECHANDO_AGUA 
        
        elif self.__fase == self.FASE_PRELAVADO_MANO:
            self.__fase = self.FASE_ECHANDO_AGUA
        
        elif self.__fase == self.FASE_ECHANDO_AGUA:
            self.__fase = self.FASE_ENJABONANDO

        elif self.__fase == self.FASE_ENJABONANDO:
            self.__fase = self.FASE_RODILLOS
        
        elif self.__fase == self.FASE_RODILLOS:
            if self.__secado_a_mano:
                self.__fase = self.FASE_SECADO_AUTOMATICO 

            else:
                self.__fase = self.FASE_SECADO_MANO
        
        elif self.__fase == self.FASE_SECADO_AUTOMATICO:
            self.terminar()
        
        elif self.__fase == self.FASE_SECADO_MANO:

            self.terminar() 
        
        elif self.__fase == self.FASE_ENCERADO:
            self.terminar() 
        
        else:
            raise RuntimeError(f"Estado no válido: Fase {self.__fase}. El lavadero va a estallar...")

```

# 9. Impresión de fase legible

- **`imprimir_fase()`:** Traduce la fase actual a un texto amigable usando un diccionario `fases_map`.  
- **`print(..., end="")`:** Evita salto de línea, permitiendo concatenar mensajes de estado en la misma línea.  
- **Fallback:** Si la fase no está mapeada, imprime un mensaje con el número de fase y “estado no válido”.



```python
    def imprimir_fase(self):
        fases_map = {
            self.FASE_INACTIVO: "0 - Inactivo",
            self.FASE_COBRANDO: "1 - Cobrando",
            self.FASE_PRELAVADO_MANO: "2 - Haciendo prelavado a mano",
            self.FASE_ECHANDO_AGUA: "3 - Echándole agua",
            self.FASE_ENJABONANDO: "4 - Enjabonando",
            self.FASE_RODILLOS: "5 - Pasando rodillos",
            self.FASE_SECADO_AUTOMATICO: "6 - Haciendo secado automático",
            self.FASE_SECADO_MANO: "7 - Haciendo secado a mano",
            self.FASE_ENCERADO: "8 - Encerando a mano",
        }
        print(fases_map.get(self.__fase, f"{self.__fase} - En estado no válido"), end="")

```

# 10. Impresión de estado completo

- **`imprimir_estado()`:** Presenta un resumen del estado actual: ingresos acumulados, si está ocupado, opciones seleccionadas y fase.  
- **Formato:** Usa separadores y formatea ingresos con dos decimales (`{self.ingresos:.2f}`).  
- **Composición:** Llama a `imprimir_fase()` para no duplicar lógica de texto de fase.



```python
    def imprimir_estado(self):
        print("----------------------------------------")
        print(f"Ingresos Acumulados: {self.ingresos:.2f} €")
        print(f"Ocupado: {self.ocupado}")
        print(f"Prelavado a mano: {self.prelavado_a_mano}")
        print(f"Secado a mano: {self.secado_a_mano}")
        print(f"Encerado: {self.encerado}")
        print("Fase: ", end="")
        self.imprimir_fase()
        print("\n----------------------------------------")

```

# 11. Método auxiliar para pruebas unitarias (no funcional)

- **Objetivo declarado:** Ejecutar un ciclo completo devolviendo la lista de fases visitadas.  
- **Inconsistencia clave:** Usa `self.lavadero` (atributo inexistente en la clase). Cualquier llamada lanzaría `AttributeError`.  
- **Estructura prevista:** Parecería querer contener una instancia interna o pasarla como parámetro; tal como está, no debe usarse.  
- **Límite de seguridad:** Comprueba que no se excedan 15 pasos para evitar bucles infinitos, buena práctica en simulaciones.  
- **Conclusión:** Método útil conceptualmente, pero incorrecto en la implementación actual.



```python
    # Esta función es útil para pruebas unitarias, no es parte del lavadero real
    # nos crea un array con las fases visitadas en un ciclo completo

    def ejecutar_y_obtener_fases(self, prelavado, secado, encerado):
        """Ejecuta un ciclo completo y devuelve la lista de fases visitadas."""
        self.lavadero.hacerLavado(prelavado, secado, encerado)
        fases_visitadas = [self.lavadero.fase]
        
        while self.lavadero.ocupado:
            # Usamos un límite de pasos para evitar bucles infinitos en caso de error
            if len(fases_visitadas) > 15:
                raise Exception("Bucle infinito detectado en la simulación de fases.")
            self.lavadero.avanzarFase()
            fases_visitadas.append(self.lavadero.fase)
            
        return fases_visitadas

```
