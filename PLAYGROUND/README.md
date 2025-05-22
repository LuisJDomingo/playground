# Playground Messenger

## Descripción

**Playground Messenger** es una aplicación web desarrollada con Django que implementa un sistema de mensajería privada entre usuarios registrados. Permite a los usuarios crear hilos de conversación (threads), enviar y recibir mensajes, y gestionar perfiles de usuario con avatares y biografía.

## Características principales

- **Registro y autenticación de usuarios** (usando `django-registration` y el sistema de auth de Django).
- **Perfiles de usuario** con avatar, biografía y enlace personal.
- **Sistema de mensajería privada**:
  - Creación automática de hilos entre dos usuarios.
  - Solo los usuarios participantes pueden ver y escribir en un hilo.
  - Los mensajes se muestran en tiempo real en la interfaz mediante AJAX.
- **Panel de administración** para gestionar usuarios, perfiles y mensajes.
- **Soporte para CKEditor** para edición enriquecida de contenido (aunque con advertencia de seguridad en la versión actual).

## Estructura de la aplicación

- **core**: Página principal y base del proyecto.
- **Profiles**: Gestión de perfiles de usuario.
- **messenger**: Lógica de hilos y mensajes privados.
- **pages**: Páginas estáticas o de contenido adicional.
- **registration**: Registro y autenticación de usuarios.

## Funcionamiento básico

1. **Registro/Iniciar sesión**: Los usuarios pueden registrarse y autenticarse.
2. **Perfiles**: Cada usuario tiene un perfil editable con avatar y bio.
3. **Mensajería**:
   - Desde el perfil de otro usuario, puedes iniciar un hilo de conversación.
   - Solo los usuarios del hilo pueden ver y enviar mensajes en él.
   - Los mensajes se agregan y muestran dinámicamente.
4. **Panel de hilos**: Los usuarios ven una lista de sus hilos activos y pueden acceder a cada uno para continuar la conversación.

## Aplicaciones prácticas

- Plataforma de mensajería interna para comunidades, foros o equipos de trabajo.
- Sistema de soporte o atención al cliente entre usuarios y administradores.
- Red social privada o entorno educativo para comunicación entre alumnos y profesores.
- Aplicación de networking profesional.

## Mejoras sugeridas

- **Notificaciones en tiempo real** usando WebSockets (Django Channels).
- **Búsqueda y filtrado de hilos y mensajes**.
- **Soporte para archivos adjuntos** (imágenes, documentos).
- **Mensajes grupales** (hilos con más de dos usuarios).
- **Sistema de borrado y edición de mensajes**.
- **Mejoras en la interfaz de usuario** (responsive, dark mode, etc.).
- **Historial de mensajes y paginación**.
- **Integración con email para notificaciones**.
- **Mejoras de seguridad** (actualizar CKEditor, validaciones adicionales).
- **Internacionalización y localización** para soporte multilenguaje.

---

**Nota:**  
Este proyecto es una base funcional para un sistema de mensajería privada en Django, ideal para expandir y adaptar a necesidades específicas.