# Requisitos mínimos para aprobar el proyecto web (Django + CSS)

| Área                                  | Requisito mínimo                                                                                             | Justificación                                  |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **Repositorio & entorno**        | *README* claro, repositorio Git y `requirements.txt`/`pyproject.toml`.                                  | Portabilidad y buenas prácticas de versionado. |
| **Arquitectura Django**          | Un proyecto y ≥ 1**app** con estructura estándar (`settings`, `urls`, `templates`, `static`). | Orden y escalabilidad.                          |
| **Modelado de datos**            | ≥ 2 modelos relacionados (ej.`Post`, `Tag`) con migraciones correctas.                                   | Dominio del ORM y relaciones.                   |
| **Autenticación**               | Registro, login, logout, casilla “Recuérdame”.                                                             | Núcleo de cualquier sitio real.                |
| **Autorización**                | Solo autor o super-usuario puede editar/borrar sus posts y comentarios.                                       | Seguridad básica.                              |
| **CRUD completo**                | Listar, crear, ver detalle, actualizar y eliminar **Posts** con vistas genéricas.                     | Consolidar `ListView`, `DetailView`, etc.   |
| **Comentarios**                  | Formulario embebido en `PostDetailView` (FormMixin).                                                        | Integrar varios conceptos.                      |
| **Sistema de tags**              | Crear/borrar tags y listar posts por tag; mostrar tags en detalle.                                            | Manejo Many-To-Many y filtrado.                 |
| **Interfaz & CSS**               | Layout responsive (Flexbox/Grid), convención BEM; hoja `style.css` ≤ 300 líneas.                         | Maquetación y legibilidad.                     |
| **Accesibilidad & UX**           | Etiquetas `label`, contraste suficiente, navegación con teclado básica.                                   | Sitio usable por todos.                         |
| **Preferencias de usuario**      | Cookie `theme` (claro/oscuro) con botón de alternancia; banner RGPD solo si hay analítica.                | Aplicar manejo de cookies y normativa.          |
| **Favicon & estáticos**         | Favicon servido sin 404/500; CSS y JS con MIME correcto.                                                      | Profesionalidad.                                |
| **Páginas de error**            | 404, 403 y 500 personalizadas extendiendo `base.html`.                                                      | Experiencia de usuario pulida.                  |
| **Deploy local “producción”** | `DEBUG=False`, `ALLOWED_HOSTS=['127.0.0.1']`, Whitenoise configurado, `collectstatic` funcional.        | Entender paso a producción.                    |
| **Documentación**               | Instrucciones para clonar, crear*venv*, migrar, crear superuser y ejecutar `runserver --nostatic`.        | Garantizar reproducción por el evaluador.      |

---

## Puntos extra (para nota superior)

* Paginación en la lista de posts.
* Animaciones CSS (`transition`, `@keyframes`).

---

## Proceso de evaluación

1. Clonar repositorio y seguir tu README.
2. Navegar como invitado → no deben aparecer botones de edición.
3. Registrarme y crear post, comentario, cambiar tema.
4. Intentar editar/borrar recurso ajeno → prohibido salvo super-usuario.
5. Revisar layout en 375 px / 768 px / 1280 px.
6. Ver cookies `sessionid`, `csrftoken`, `theme` en DevTools.
7. Forzar URL inexistente → ver 404 personalizada.
8. Revisar código (nombres BEM, convenciones Django, CSS ≤ 300 líneas).
