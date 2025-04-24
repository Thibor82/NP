### 📘 Guía de instalación de XAMPP y WordPress en Windows

---

#### ✅ Requisitos previos

* Windows 10 o superior
* Conexión a internet
* Permisos de administrador en el equipo

---

## 🧰 Paso 1: Instalar XAMPP

1. Ir a la web oficial: [https://www.apachefriends.org/es/index.html]()
2. Descargar la versión para Windows.
3. Ejecutar el instalador y seguir los pasos del asistente:

   * Selecciona los componentes por defecto (puedes dejar todo marcado).
   * Instala en `C:\xampp` (recomendado).
   * Desactiva Bitnami si no vas a usarlo.
4. Al finalizar, abre el  **Panel de Control de XAMPP** .
5. Inicia los módulos:

   * Apache: `Start`
   * MySQL: `Start`

   > ⚠️ Si Apache no inicia, puede haber conflicto con otro software (como Skype o IIS). Intenta cambiar el puerto en `Config > httpd.conf` (puerto 8080 por ejemplo).
   >

---

## 📁 Paso 2: Descargar y copiar WordPress

1. Ve a [https://es.wordpress.org/download/]()
2. Descarga el archivo `.zip` de WordPress.
3. Extrae la carpeta `wordpress` y renómbrala como `mi-web`.
4. Copia la carpeta `mi-web` dentro de:

   ```bash
   C:\xampp\htdocs 
   ```

   Al final, tendrás algo como:

   ```bash
   C:\xampp\htdocs\mi-web\
   ```

---

## 🧱 Paso 3: Crear base de datos en phpMyAdmin

1. Abre tu navegador y ve a:
   ```bash
   http://localhost/phpmyadmin
   ```
2. Haz clic en la pestaña  **Base de datos** .
3. En **Crear base de datos** escribe:
   ```bash
   mi_web_db
   ```
4. Deja el cotejamiento por defecto (utf8mb4_general_ci) y haz clic en  **Crear** .

---

## ⚙️ Paso 4: Configurar `wp-config.php`

1. En la carpeta `C:\xampp\htdocs\mi-web`, busca el archivo:
   ```bash
   wp-config-sample.php
   ```
2. Cópialo y renómbralo como:
   ```bash
   wp-config.php
   ```
3. Ábrelo con un editor de texto (como Notepad++ o VS Code) y modifica estas líneas:

```php
// Nombre de la base de datos
define( 'DB_NAME', 'mi_web_db' );

// Usuario (por defecto en XAMPP)
define( 'DB_USER', 'root' );

// Contraseña (vacía por defecto en XAMPP)
define( 'DB_PASSWORD', '' );

// Servidor de base de datos
define( 'DB_HOST', 'localhost' );
```

4. Guarda y cierra el archivo.

---

## 🚀 Paso 5: Instalar WordPress

1. En el navegador, accede a:
   ```bash
   http://localhost/mi-web
   ```
2. Selecciona el idioma.
3. Completa los datos del sitio:
   * Título del sitio
   * Usuario administrador
   * Contraseña
   * Correo electrónico
4. Marca la casilla de "Disuadir a los motores de búsqueda..." (si solo es para pruebas).
5. Haz clic en  **Instalar WordPress** .
6. Al terminar, podrás iniciar sesión con el usuario creado.

---

## 🎉 ¡Listo!

Tu sitio de WordPress ahora está corriendo localmente en:

[http://localhost/mi-web](http://localhost/mi-web)

---

### 🔧 Consejos adicionales

* Para acceder a phpMyAdmin: `http://localhost/phpmyadmin`
* Para reiniciar servicios: usa el **Panel de Control de XAMPP**
* Para cambiar el idioma del panel de WordPress: Ajustes > Generales > Idioma del sitio
