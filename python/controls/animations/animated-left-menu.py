import flet as ft


def main(page: ft.Page):
    def show_menu(e):
        c.offset = ft.Offset(0, 0)
        c.update()

    def hide_menu(e):
        c.offset = ft.Offset(-2, 0)
        c.update()

    c = ft.Container(
        content=ft.Column(
            [
                ft.Row(
                    [ft.IconButton(icon=ft.Icons.CLOSE, on_click=hide_menu)],
                    alignment=ft.MainAxisAlignment.END,
                ),
                ft.ListTile(
                    title=ft.Text("Menu A"),
                    on_click=lambda _: print("Menu A clicked"),
                ),
                ft.ListTile(
                    title=ft.Text("Menu B"),
                    on_click=lambda _: print("Menu B clicked"),
                ),
            ]
        ),
        left=10,
        top=10,
        width=200,
        height=300,
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
        border_radius=5,
        offset=ft.Offset(-2, 0),
        animate_offset=ft.Animation(300, ft.AnimationCurve.EASE_IN),
    )

    page.overlay.append(c)
    page.add(
        ft.ElevatedButton("Show menu", on_click=show_menu),
    )


ft.app(main)
