# 📘 Guía de la charla - Agentes Autónomos con IA

## Introducción

Esta guía acompaña la charla **"Agentes Autónomos con IA"**, donde exploramos la evolución desde los asistentes conversacionales tradicionales hacia sistemas capaces de percibir un entorno, tomar decisiones y ejecutar acciones.

El objetivo es comprender que un agente de IA no es solamente un chatbot, sino un sistema compuesto por un modelo de inteligencia artificial, instrucciones, herramientas y mecanismos de ejecución.

---

# 1. ¿Qué entendemos por agente de IA?

Durante esta charla utilizaremos la siguiente definición:

Un agente de IA es un sistema que recibe un objetivo, analiza información de su entorno, razona utilizando modelos de inteligencia artificial y puede ejecutar acciones para alcanzar dicho objetivo.

Un agente puede combinar:

- Modelo de lenguaje (LLM).
- Instrucciones y contexto.
- Herramientas externas.
- Fuentes de información.
- Capacidad de ejecutar acciones.

---

# 2. Agentes conversacionales vs Agentes autónomos

## Agentes conversacionales

Los agentes conversacionales están diseñados principalmente para interactuar con usuarios mediante lenguaje natural.

Ejemplos:

- Chatbots.
- Asistentes virtuales.
- Copilots.

Su flujo habitual es:

Usuario → Pregunta → Modelo IA → Respuesta


## Agentes autónomos

Los agentes autónomos tienen un objetivo y pueden actuar sin una interacción constante del usuario.

Características:

- Observan un entorno.
- Analizan información.
- Deciden una acción.
- Utilizan herramientas.
- Ejecutan tareas.

Ejemplo:

Objetivo:
"Aumentar el alcance de una cuenta en redes sociales"

El agente puede:

- Analizar publicaciones.
- Evaluar contenido.
- Decidir una estrategia.
- Generar respuestas.
- Ejecutar acciones.

---

# 3. Plataformas Low-Code para agentes

Actualmente existen plataformas que permiten construir agentes mediante configuraciones visuales y componentes predefinidos.

Ventajas:

- Desarrollo rápido.
- Menor necesidad de programación.
- Integración con servicios empresariales.

Ejemplos:

- Microsoft Copilot Studio.
- Azure AI Foundry Agents.

Sin embargo, no todos los escenarios pueden resolverse mediante configuraciones visuales.

Cuando se necesita:

- Automatización avanzada.
- Control total del comportamiento.
- Integraciones personalizadas.
- Ejecución sobre entornos específicos.

puede ser necesario desarrollar agentes utilizando código y arquitecturas propias.

---

# 4. Tipos de agentes autónomos

Los agentes pueden adoptar diferentes formas según el problema que resuelven:

## Browser Agents

Agentes capaces de interactuar con aplicaciones web mediante un navegador.

Ejemplos:

- Automatización de procesos web.
- Navegación inteligente.
- Gestión de tareas repetitivas.


## Coding Agents

Agentes especializados en desarrollo de software.

Pueden:

- Analizar código.
- Generar soluciones.
- Crear pruebas.
- Resolver errores.


## Data Agents

Agentes orientados al análisis de información.

Pueden:

- Consultar datos.
- Generar reportes.
- Detectar patrones.


## Multi-Agent Systems

Sistemas donde varios agentes colaboran para resolver problemas complejos.

---

# 5. Arquitectura del Browser Agent utilizado en la demo

La demostración utiliza una arquitectura distribuida:

## Servidor Central

Responsable de:

- Registrar agentes.
- Administrar tareas.
- Coordinar ejecuciones.
- Recibir estados.


## Cliente Browser

Cada usuario ejecuta un navegador con extensiones instaladas.

Estas extensiones:

- Se conectan periódicamente al servidor.
- Consultan nuevas tareas.
- Ejecutan el agente localmente.


## Browser Agent

El agente ejecuta las acciones necesarias:

- Observa el contenido de una página.
- Analiza información.
- Solicita decisiones a un modelo de IA.
- Ejecuta acciones.


## Azure AI Foundry

Se utiliza como plataforma de inteligencia artificial para:

- Proporcionar modelos de lenguaje.
- Procesar instrucciones.
- Analizar contenido.
- Generar decisiones y respuestas.

---

# 6. Microsoft Azure AI Foundry

Azure AI Foundry permite construir y administrar soluciones basadas en inteligencia artificial.

Durante la demostración se utilizan:

- Proyecto de Azure AI Foundry.
- Deployment de un modelo.
- Playground.
- Consumo desde aplicaciones externas.

La plataforma proporciona las capacidades de IA, mientras que la lógica del agente pertenece a la aplicación que lo utiliza.

---

# 7. Tool Use / Function Calling

Una característica fundamental de los agentes modernos es la capacidad de utilizar herramientas externas.

El flujo general es:

1. El usuario plantea una necesidad.
2. El modelo analiza la solicitud.
3. El modelo determina que necesita una herramienta.
4. La aplicación ejecuta la herramienta.
5. El resultado vuelve al modelo.
6. El modelo genera la respuesta final.

Esto permite conectar modelos de IA con:

- APIs.
- Bases de datos.
- Sistemas empresariales.
- Servicios externos.

---

# 8. Conclusión

Los agentes de IA representan una evolución desde sistemas que solamente responden hacia sistemas capaces de razonar y actuar.

Las plataformas Low-Code permiten acelerar la creación de agentes, pero los escenarios más avanzados requieren arquitecturas personalizadas donde la aplicación, las herramientas y los modelos trabajan en conjunto.

---

## Contacto | Connect

**LinkedIn:**  
https://www.linkedin.com/in/esteban-calabria-7a44401a/

**Instagram:**  
https://www.instagram.com/mct.esteban.calabria/
