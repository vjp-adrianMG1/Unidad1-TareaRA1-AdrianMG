# Índice del proyecto

Autor: Adrian  Muñoz Garcia
Fecha: (añadir fecha)  
 - [Elementos de Python](#elementos-de-python)
 - [Ejecución y Depuración](#ejecución-y-depuración)
 - [Pruebas](#pruebas)
 - [Ejecución en Sandbox](#ejecución-en-sandbox)
 - [Reflexión](#reflexión)

## Elementos de Python
Enlace para ver el código comentado con Markdown:

 - [Código comentado: lavadero_documentado_Adrian.md](lavadero_documentado_Adrian.md)

 - [Código comentado: Main_app_documentado_Adrian.md](Main_app_documentado_Adrian.md)

## Ejecución y Depuración
Problemas encontrados (ejemplos concisos):
- Error de encoding al leer ficheros.
- Excepciones no capturadas por entradas inválidas.
- Fallos al importar módulos por ruta.

Soluciones aplicadas:
- Especificar encoding UTF-8 en la apertura de ficheros.
- Añadir validación de entradas y bloques try/except.
- Ajustar `PYTHONPATH` o usar imports relativos.

Instrucciones para reproducir y depurar:
1. Crear entorno virtual: `python -m venv .venv && source .venv/bin/activate`
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar: `python -m src.main`

Capturas de pantalla:
- Inserta capturas a pantalla completa en `assets/screenshots/` (p. ej. `debug-fullscreen-1.png`).
- Nota obligatoria: las capturas deben ser a pantalla completa y debe verse el terminal con tu nombre y/o la imagen de la plataforma Moodle para verificación.
- Ejemplo de inclusión en Markdown:

## Pruebas
Descripción de las pruebas realizadas:
- Unitarias con `pytest`.
- Tests de integración básicos para flujos críticos.



Ejecución de las pruebas:
- Local: `pytest -q`
- Ver salida en IDE (incluir captura de pantalla completa con la ventana del IDE y el terminal).

Errores detectados en pruebas y correcciones:
- Fallos por valores límites -> añadir validaciones y tests adicionales.
- Mocking de dependencias externas para aislar pruebas.

## Ejecución en Sandbox
Proceso sugerido para ejecutar en una Sandbox (p. ej. Gitpod, Repl.it, o sandbox institucional):
1. Importar el repositorio en la sandbox.
2. Crear/activar el entorno y ejecutar `pip install -r requirements.txt`.
3. Ejecutar tests y flujos principales: `pytest` y `python -m src.main`.
4. Tomar capturas de pantalla de todo el proceso (pantalla completa) y guardarlas en .

Incluir comandos concretos y resultado esperado en el README para que el evaluador pueda reproducir el proceso.

## Reflexión
Comparación breve de la infraestructura de seguridad entre lenguajes (relacionada con la ejecución en Sandbox):
- Python: gestión sencilla de dependencias, pero vulnerable a paquetes maliciosos y ejecución dinámica; la seguridad mejora con virtual environments, análisis de dependencias (pip-audit, Safety) y sandboxing.
- Lenguajes compilados (C/C++): riesgo de memory safety (buffer overflow) y explotación; requieren herramientas de análisis estático y mitigaciones (ASLR, DEP).
- Lenguajes gestionados (Java, .NET): mejor aislamiento de memoria pero vulnerables a dependencias y configuración incorrecta.
Conclusión: la ejecución en Sandbox reduce riesgos operativos y facilita la verificación de comportamiento, pero no sustituye el análisis de dependencias ni las buenas prácticas de validación y manejo de errores.
