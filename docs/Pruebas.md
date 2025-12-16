# Informe de Pruebas Unitarias – Lavadero

## 1. Código de pruebas


---

``` bash
def test1_estado_inicial_correcto(self):
        """Test 1: Estado inicial debe ser inactivo, sin ingresos y sin opciones."""
        self.assertEqual(self.lavadero.fase, Lavadero.FASE_INACTIVO)
        self.assertEqual(self.lavadero.ingresos, 0.0)
        self.assertFalse(self.lavadero.ocupado)

    def test2_excepcion_encerado_sin_secado(self):
        """Test 2: Encerar sin secado a mano debe lanzar ValueError."""
        with self.assertRaises(ValueError):
            self.lavadero.hacerLavado(False, False, True)

    def test3_excepcion_lavado_ocupado(self):
        """Test 3: Iniciar un lavado mientras otro está en marcha debe lanzar RuntimeError."""
        self.lavadero.hacerLavado(False, False, False)
        with self.assertRaises(RuntimeError):
            self.lavadero.hacerLavado(True, True, True)

    def test4_prelavado_ingresos_y_fases(self):
        """Test 4 y 10: Prelavado a mano -> ingresos 6.50€, fases [0,1,2,3,4,5,6,0]."""
        fases = self.lavadero.ejecutar_y_obtener_fases(True, False, False)
        self.assertEqual(self.lavadero.ingresos, 6.50)
        self.assertEqual(fases, [0,1,2,3,4,5,6,0])

    def test5_secado_ingresos_y_fases(self):
        """Test 5 y 11: Secado a mano -> ingresos 6.00€, fases [0,1,3,4,5,7,0]."""
        fases = self.lavadero.ejecutar_y_obtener_fases(False, True, False)
        self.assertEqual(self.lavadero.ingresos, 6.00)
        self.assertEqual(fases, [0,1,3,4,5,7,0])

    def test6_secado_y_encerado(self):
        """Test 6 y 12: Secado + encerado -> ingresos 7.20€, fases [0,1,3,4,5,7,8,0]."""
        fases = self.lavadero.ejecutar_y_obtener_fases(False, True, True)
        self.assertEqual(self.lavadero.ingresos, 7.20)
        self.assertEqual(fases, [0,1,3,4,5,7,8,0])

    def test7_prelavado_y_secado(self):
        """Test 7 y 13: Prelavado + secado -> ingresos 7.50€, fases [0,1,2,3,4,5,7,0]."""
        fases = self.lavadero.ejecutar_y_obtener_fases(True, True, False)
        self.assertEqual(self.lavadero.ingresos, 7.50)
        self.assertEqual(fases, [0,1,2,3,4,5,7,0])

    def test8_prelavado_secado_encerado(self):
        """Test 8 y 14: Prelavado + secado + encerado -> ingresos 8.70€, fases [0,1,2,3,4,5,7,8,0]."""
        fases = self.lavadero.ejecutar_y_obtener_fases(True, True, True)
        self.assertEqual(self.lavadero.ingresos, 8.70)
        self.assertEqual(fases, [0,1,2,3,4,5,7,8,0])

    def test9_sin_extras(self):
        """Test 9: Lavado rápido sin extras -> ingresos 5.00€, fases [0,1,3,4,5,6,0]."""
        fases = self.lavadero.ejecutar_y_obtener_fases(False, False, False)
        self.assertEqual(self.lavadero.ingresos, 5.00)
        self.assertEqual(fases, [0,1,3,4,5,6,0])
```

## 2. Ejecución inicial (código erróneo)

_Aquí inserto captura de pantalla de la consola mostrando la salida con `ERROR` (AttributeError)._

### Resumen
| Test | Resultado esperado | Resultado obtenido |
|------|-------------------|--------------------|
| Test 1 | Estado inicial correcto | OK |
| Test 2 | ValueError al encerar sin secado | OK |
| Test 3 | RuntimeError al iniciar lavado ocupado | OK |
| Test 4–9 | Secuencias de fases e ingresos correctos | **ERROR** (AttributeError) |

---

## 3. Ejecución intermedia (tras corregir `ejecutar_y_obtener_fases`)

_Aquí inserto captura de pantalla de la consola mostrando la salida con `FAIL` (ingresos y fases incorrectos)._

### Resumen
| Test | Resultado esperado | Resultado obtenido |
|------|-------------------|--------------------|
| Test 4 | Ingresos 6.50€, fases [0,1,2,3,4,5,6,0] | FAIL (Ingresos distintos) |
| Test 5 | Ingresos 6.00€, fases [0,1,3,4,5,7,0] | FAIL (Ingresos 6.20€, fases incorrectas) |
| Test 6 | Ingresos 7.20€, fases [0,1,3,4,5,7,8,0] | FAIL (faltaba fase 8) |
| Test 7 | Ingresos 7.50€, fases [0,1,2,3,4,5,7,0] | FAIL |
| Test 8 | Ingresos 8.70€, fases [0,1,2,3,4,5,7,8,0] | FAIL |
| Test 9 | Ingresos 5.00€, fases [0,1,3,4,5,6,0] | FAIL |

---

## 4. Ejecución final (código corregido)

_Aquí inserto captura de pantalla de la consola mostrando la salida con todos los tests en verde (OK)._

### Resumen
| Test | Resultado esperado | Resultado obtenido |
|------|-------------------|--------------------|
| Test 1–9 | Todos los ingresos y fases correctos | OK |

---

## 5. Conclusión

- **Antes:** el código tenía errores de implementación (`AttributeError`) y de lógica (precios y fases).  
- **Después:** tras corregir el método `ejecutar_y_obtener_fases`, ajustar precios y secuencias de fases, todos los tests unitarios pasan correctamente.  
- Esto demuestra que los **14 requisitos** están validados y el lavadero funciona según lo esperado.
