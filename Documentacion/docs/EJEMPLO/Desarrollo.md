# Desarrollo

## Arquitectura de la Solución

La aplicación se basa en una arquitectura **serverless** utilizando **Streamlit** como interfaz de usuario y **AWS** para el almacenamiento y procesamiento de datos. Los componentes principales incluyen:

1. **Streamlit**: La interfaz de usuario para la gestión de proveedores.
2. **awswrangler**: Biblioteca utilizada para interactuar con los datos almacenados en **Amazon S3** y realizar operaciones con archivos **Parquet**.
3. **Amazon S3**: Almacenamiento de los datos en un formato seguro y escalable.
4. **Lambda Functions** (opcional): Para la ejecución de tareas asíncronas, como la validación de datos o la generación de informes.

## Flujo de Trabajo

El flujo de trabajo de la aplicación es sencillo e intuitivo:

1. **Registro de Proveedores**: El usuario puede agregar nuevos proveedores a través de un formulario en Streamlit, que incluye campos como `name`, `official_name`, `url`, `description`, entre otros. Al enviar el formulario, se genera un ID único utilizando un hash de los datos ingresados.
2. **Almacenamiento de Datos**: Los datos se
