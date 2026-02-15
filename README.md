# 🧮 Calculadora con Flet (T.A.P.)

Este repositorio contiene el código fuente de una interfaz de calculadora básica desarrollada como práctica para la asignatura de **Tópicos Avanzados de Programación**.

## 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python
* **Framework:** [Flet](https://flet.dev/) (basado en Flutter)

## 🚀 Cómo ejecutar el proyecto
1. Asegúrate de tener Python instalado.
3. Instala la librería necesaria:
En mi caso, Git bash
3.Ahora deberás crear una carpeta donde vas a trabajar a partir de ahora.
Se va adescargar flet usando el siguiente código dentro de la carpeta creada:
   pip install flet
4.Una vez descargado usaremos los siguientes códigos:
   source .venv/Scripts/activate
5.Ejecutar el código:
   python main.py
   
🔍 Explicación Paso a Paso
Paso 1: Configuración de la Ventana. Aquí se define el "cascarón". Se pone el título y se fija un tamaño pequeño (250x400) para que parezca una calculadora real.

Paso 2: La Pantalla (Display). Se crea el cuadro gris superior. Lo más importante es la alineación, configurada para que el número aparezca a la derecha.

Paso 3: La Cuadrícula (Grid). Se prepara un espacio que divide el contenido en 2 columnas para que los botones se acomoden solos.

Paso 4: Agregar los Botones. Usamos el comando .append para ir "metiendo" los botones de colores dentro de la cuadrícula. 

Paso 5 y 6: Organización y Ejecución. Se apilan los elementos (pantalla arriba, botones abajo) y se le dice a Python que muestre todo en la ventana.
  
Aquí te dejó el código completo para ejecutarlo de acuerdo a los pasos anteriores:


    import flet as ft

    def main(page: ft.Page):
    # 1. Configuración de la ventana
    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20

    # 2. Definición del Display (Pantalla)
    display = ft.Container(
        content=ft.Text("0", size=30),
        bgcolor=ft.Colors.BLACK12,
        border_radius=5,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=250, 
        height=70,
    )

    # 3. Definición de la Cuadrícula (Grid)
    grid = ft.GridView(
        runs_count=2,
        spacing=10,
        run_spacing=10,
        width=250, 
        height=200, 
        expand=False
    )

    # 4. Agregar elementos al Grid
    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.PRIMARY, border_radius=5))
    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.SECONDARY, border_radius=5))
    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.TERTIARY, border_radius=5))

    # 5. Organización del Layout Principal
    layout_principal = ft.Column(
        controls=[
            display,
            grid
        ],
        tight=True
    )

    # 6. Cargar elementos en la página
    page.add(layout_principal)
    page.update()
    # 7. Ejecución de la App
    ft.app(target=main)


Una vez tengas todo, deberías de tener algo como esto:

<img width="535" height="687" alt="Captura de pantalla 2026-02-14 212643" src="https://github.com/user-attachments/assets/e533866d-e458-40c9-8824-ce7b6e75370e" />
