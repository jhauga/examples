import flet as ft


def main(page: ft.Page):

    c1 = ft.ShaderMask(
        content=ft.Image(
            src="https://picsum.photos/140/100?1",
            width=140,
            height=100,
            fit=ft.ImageFit.FILL,
        ),
        blend_mode=ft.BlendMode.COLOR_BURN,
        shader=ft.RadialGradient(
            center=ft.alignment.top_left,
            radius=1.0,
            colors=[ft.Colors.YELLOW, ft.Colors.DEEP_ORANGE_900],
            tile_mode=ft.GradientTileMode.CLAMP,
        ),
        border_radius=5,
        animate_rotation=300,
        animate_scale=ft.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
    )

    def animate(e):
        c1.rotate = 1
        c1.scale = 3
        page.update()

    page.add(
        ft.Stack([c1], width=500, height=300),
        ft.ElevatedButton("Animate!", on_click=animate),
    )


ft.app(target=main)
