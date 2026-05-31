# ucv-ate-si-laboratorio08
Google ADK + Poetry + GitHub + SonarQube

# Agente Académico Inteligente - UCV (Laboratorio 08)

Este proyecto consiste en el diseño e implementación de un agente inteligente avanzado para la Universidad César Vallejo, utilizando tecnologías de IA generativa y automatización de procesos.

##  Tecnologías Utilizadas
* **Google ADK (Agent Development Kit 2.1.0):** Framework para la orquestación del agente.
* **Gemini 2.5 Flash:** Modelo fundacional de lenguaje de Google encargado del razonamiento.
* **Poetry:** Gestor profesional de dependencias y entornos virtuales en Python.
* **GitHub Actions:** Pipeline de Integración Continua (CI) para automatizar tareas.
* **SonarCloud:** Plataforma en la nube para el análisis estático de calidad de código.

##  Herramientas Integradas (Function Calling)
El agente es capaz de razonar bajo demanda y activar las siguientes funciones en paralelo:
1. `explicar_concepto`: Busca y extrae definiciones técnicas desde la base de datos.
2. `calcular_promedio`: Procesa notas académicas y resuelve operaciones matemáticas exactas.

##  Instalación y Ejecución Local

1. Instalar las dependencias con Poetry:
   ```bash
   poetry install