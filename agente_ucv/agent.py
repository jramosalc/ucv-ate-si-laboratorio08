from dotenv import load_dotenv
load_dotenv(override=True)

from google.adk.agents import Agent


def explicar_concepto(concepto: str) -> dict:
    conceptos = {
        "api": "Interfaz de programación de aplicaciones que permite la comunicación entre sistemas.",
        "devops": "Cultura y conjunto de prácticas que automatizan los procesos entre desarrollo y operaciones.",
        "ia": "Simulación de procesos de inteligencia humana por parte de sistemas informáticos.",
        "algoritmo": "Conjunto ordenado de pasos para resolver un problema.",
        "base de datos": "Sistema para almacenar y gestionar información."
    }

    if not isinstance(concepto, str) or not concepto.strip():
        return {"status": "error", "explicacion": "Entrada inválida."}

    concepto = concepto.lower().strip()

    if concepto in conceptos:
        return {"status": "success", "explicacion": conceptos[concepto]}

    return {"status": "not_found", "explicacion": "Concepto no registrado."}


def calcular_promedio(notas: str) -> dict:
    try:
        lista = [float(x.strip()) for x in notas.split(",")]

        for nota in lista:
            if nota < 0 or nota > 20:
                return {
                    "status": "error",
                    "mensaje": "Las notas deben estar entre 0 y 20."
                }

        return {
            "status": "success",
            "promedio": round(sum(lista) / len(lista), 2)
        }

    except ValueError:
        return {
            "status": "error",
            "mensaje": "Formato inválido."
        }


root_agent = Agent(
    name="agente_ucv",
    model="gemini-2.5-flash",
    description="Asistente académico UCV",
    instruction="""
    Eres un asistente académico de la UCV.
    Responde siempre en español.
    Cuando el usuario pregunte por API, DevOps, IA, algoritmo o base de datos,
    utiliza la herramienta explicar_concepto.
    Cuando solicite un promedio, utiliza calcular_promedio.
    """,
    tools=[explicar_concepto, calcular_promedio]
)