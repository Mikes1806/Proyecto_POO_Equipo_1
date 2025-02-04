# Desarrollo
El desarrollo del sitio web **OrganizeMe** se realizó siguiendo las buenas prácticas de programación y control de versiones. Aquí se detallan los aspectos más relevantes:

## Funcionalidades del Proyecto
**Perfil**:

• Agregar y gestionar un perfil con ingresos mensuales.

![Crear Perfil](images/Perfil_1.jpg)

![Modificar Perfil](images/Perfil_2.jpg)

![Código 1](images/Perfil_3.jpg)

![Código 2](images/Perfil_4.jpg)

![Código 3](images/Perfil_5.jpg)

![Código 4](images/Perfil_6.jpg)

**Gestión de Gastos Fijos**:

• **Agregar Gasto**: Seleccionar Categoría, Servicio y Gasto mensual.

![Mis Gastos Fijos](images/GF_1.jpg)

![Agregar Gasto Fijo](images/GF_2.jpg)

![Código 1](images/GF_3.jpg)

![Código 2](images/GF_4.jpg)

![Código 3](images/GF_5.jpg)

![Código 4](images/GF_6.jpg)

• **Modificar o Eliminar**: Selecciona el número del gasto a modificar (Solo descripción y gasto mensual) o eliminar.

![Editar/Modificar Gasto Fijo](images/GF_7.jpg)

![Código 5](images/GF_8.jpg)

![Código 6](images/GF_9.jpg)

![Código 7](images/GF_10.jpg)

**Gestión de Gastos Imprevistos**:

• **Agregar Gasto**: Seleccionar Categoría, Servicio y Gasto mensual.

![Mis Gastos Imprevistos](images/GI_1.jpg)

![Agregar Gasto Imprevisto](images/GI_2.jpg)

![Código 1](images/GI_3.jpg)

![Código 2](images/GI_4.jpg)

![Código 3](images/GI_5.jpg)

• **Modificar o Eliminar**: Selecciona el número del gasto a modificar (Acceso libre) o elimina.

![Editar/Modificar Gasto Imprevisto](images/GI_6.jpg)

![Código 4](images/GI_7.jpg)

![Código 5](images/GI_8.jpg)

**Reporte**:

• **Generar archivo .csv con columnas como**:
Categoría,Servicio,Descripción,Gasto mensual/Costo.

![Generar Reporte 1](images/Reporte_1.jpg)

![Generar Reporte 2](images/Reporte_2.jpg)

![Código 1](images/Reporte_3.jpg)

![Código 2](images/Reporte_4.jpg)

![Código 3](images/Reporte_5.jpg)

## Reportes y Exportación CSV
**Gastos Fijos**:

Categoría, Servicio, Descripción, Gasto mensual

• Vivienda, Alquiler, Costo de vivienda, 900.0

• Entretenimiento, Netflix, Suscripción mensual, 288.0

• Transporte, Gasolina, Costo del combustible, 200.0

**Gastos Imprevistos**:

Categoría, Servicio, Descripción, Costo

• Alimentos, Cita, Tacos del chino, 298.0

• Entretenimiento, Juegos, Halo Infinite, 1500.0

• Alimentos, Pan, Promoción del Globo, 68.0

**¿Cómo Generarlo?**:

1.- Navega en la sección de reporte.

2.- Ubica el archivo que deseas exportar.

3.- Haz clic en "Descargar Reporte".

## Herramientas y Tecnologías Utilizadas
• **Framework**: Streamlit para la creación de la interfaz gráfica interactiva.

• **Repositorio de GitHub**: Gestión del proyecto mediante GitHub, asegurando un control de versiones efectivo.

• **Enlace al repositorio**: <a href="https://github.com/Mac-Fes-Acatlan/Materia_POO_1355.git" target="_blank">https://github.com/Mac-Fes-Acatlan/Materia_POO_1355.git</a>

• **Enlace a los diagramas**: <a href="https://drive.google.com/file/d/1grJWnIwHQLfc6zRseNETxz6f85TmgTlY/view" target="_blank">https://drive.google.com/file/d/1grJWnIwHQLfc6zRseNETxz6f85TmgTlY/view</a>

• **Entorno de Desarrollo**: Visual Studio Code (VS Code) como IDE (Entorno de Desarrollo Integrado) principal.

• **Base de Datos**: CSV para almacenar los datos de usuarios y gastos.

• **Lenguaje de Programación**: Python (versión 3.10+) para backend y lógica principal.

## Funcionalidades Implementadas
**1.- Perfil del Usuario**:

• Ingreso inicial del monto mensual, algún monto extra y datos del usuario.

**2.- Gestión de Gastos**:

• Formulario para agregar, editar y eliminar gastos.

**3.- Generación de Reporte**:

• Exportación de gastos en formato CSV para análisis externo.

## Metodología de Trabajo
**Fases del Desarrollo**:

**1.- Planificación**: Definición de requisitos y diseño inicial del sistema.

**2.- Diagramas**: Realización de diagramas de clases, casos de uso y de procesos.

**3.- Diseño**: Realización del prototipo de la interfaz con Streamlit y esquema del reporte.

**4.- Implementación**: Desarrollo del sistema, desde la creación de modelos hasta la implementación de funcionalidades.

**5.- Pruebas**: Realización de pruebas unitarias y funcionales para asegurar la calidad del código.

**6.- Despliegue**: Sitio web alojado localmente.

**Control de Versiones**:
    
• Cada funcionalidad o corrección de errores se implementó en ramas específicas para mantener el código principal limpio.

## Principales Retos
• Contenedores para imprimir las tarjetas de gastos.

• Tratar de implementar la visualización de gráficas.

• Garantizar la generación de reportes en formato CSV con datos coherentes.