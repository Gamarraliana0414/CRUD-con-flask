 CRUD  con Flask

Este proyecto es una aplicación web de tipo CRUD (Crear, Leer, Actualizar y Eliminar) desarrollada durante un taller práctico con Python y Flask. Permite gestionar usuarios a través de una API REST simple y funcional.



Descripción del Proyecto

La aplicación proporciona endpoints REST que permiten realizar operaciones sobre una lista de usuarios almacenada en memoria. Además, incluye un cliente escrito en Python que consume esta API para facilitar las pruebas.

Cada usuario contiene los siguientes datos:

- `id` (asignado automáticamente)
- `nombre`
- `edad`



 Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| **Python 3** | Lenguaje de programación base |
| **Flask** | Framework web utilizado para crear la API |
| **Requests** | Librería para hacer peticiones HTTP desde el cliente |
| **Gunicorn** | Servidor WSGI para correr la app en producción |
| **Render** | Plataforma de despliegue web usada para alojar la aplicación |


 Estructura del Proyecto
 ├── app.py # Código principal del servidor Flask
├── cliente.py # Script de prueba que consume la API
├── requirements.txt # Dependencias necesarias para ejecutar la app
└── README.md # Documentación del proyecto


