import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora TAP"
    page.window_width = 250
    page.window_height = 400
    page.padding = 20

    display = ft.Container(
        content=ft.Text("0", size=30),
        bgcolor=ft.Colors.BLACK12,
        border_radius=5,
        alignment=ft.alignment.Alignment(1, 0),
        padding=10,
        width=250, # Forzamos el ancho manualmente
        height=70,
    )

    grid = ft.GridView(
        runs_count=2,
        spacing=10,
        run_spacing=10,
        width=250, # Ancho fijo igual al display
        height=200, # Alto fijo para que no crezca
        expand=False
    )

    # Botones de ejemplo agregados al grid
    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.PRIMARY, border_radius=5))
    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.SECONDARY, border_radius=5))
    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.TERTIARY, border_radius=5))
    grid.controls.append(ft.Container(height=50, bgcolor=ft.Colors.AMBER, border_radius=5))

    layout_principal = ft.Column(
        controls=[
            display,
            grid
        ],
        tight=True
    )

    page.add(layout_principal)
    page.update()

ft.app(target=main)
