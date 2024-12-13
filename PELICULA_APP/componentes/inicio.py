import reflex as rx

def inicio() -> rx.Component:
    return rx.center(
        rx.box(
            rx.vstack(
                # Encabezado Principal
                rx.heading(
                    "Acerca de PELICULAS YAA",
                    size="8",  # Tamaño del texto
                    weight="bold",
                    color="white",
                ),
                # Breve Descripción
                rx.text(
                    "Paga solo por la pelicula que desees ver .",
                    size="4",
                    color="lightgray",
                    margin="1em 0",
                ),
                # Secciones Informativas
                rx.box(
                    rx.heading(
                        "Funciones Clave",
                        size="6",
                        weight="bold",
                        color="white",
                        margin="1em 0",
                    ),
                    rx.text(
                        "pagos de manera facil y rapido.",
                        size="4",
                        color="lightgray",
                        margin="0.5em 0",
                    ),
                    rx.text(
                        "algunas peliculas con 50%  de descuento",
                        size="4",
                        color="lightgray",
                        margin="0.5em 0",
                    ),
                    rx.text(
                        "elije una pelicula premiun.",
                        size="4",
                        color="lightgray",
                        margin="0.5em 0",
                    ),
                    rx.text(
                        "Historial de vistas",
                        size="4",
                        color="lightgray",
                        margin="0.5em 0",
                    ),
                    spacing="4",
                    align="start",
                ),
                spacing="6",
                align="center",  # Alinear el contenido del vstack en el centro
            ),
            padding="2em",
            background="black",  # Fondo con gradiente en tonos cálidos
            border_radius="1em",  # Bordes redondeados
            box_shadow="0 8px 16px rgba(0, 0, 0, 0.2)",  # Sombra pronunciada
            align_items="center",  # Centrar el contenido dentro del box
            max_width="800px",  # Ancho máximo del cuadro
        ),
        height="100vh",
        background="url('https://www.teknofilo.com/wp-content/uploads/2021/06/Netflix-1280x720.jpg')",  # Fondo de la página con gradiente
        justify="center",
        align_items="center",
    )

