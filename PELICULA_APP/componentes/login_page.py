import reflex as rx

def login_page() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.flex(
                rx.image(
                    width="2.5em",
                    height="auto",
                    border_radius="25%",
                ),
                rx.heading(
                    "Inicia secion en tu cuenta",
                    size="6",
                    as_="h2",
                    width="100%",
                ),
                rx.hstack(
                    rx.text(
                        "Nuevo aqui?",
                        size="3",
                        text_align="left",
                    ),
                    rx.link("inscribirse", href="#", size="3"),
                    spacing="2",
                    opacity="0.8",
                    width="100%",
                ),
                justify="start",
                direction="column",
                spacing="4",
                width="100%",
            ),
            rx.vstack(
                rx.text(
                    "correo electronico",
                    size="3",
                    weight="medium",
                    text_align="left",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("user")),
                    placeholder="correo@gmail.com",
                    type="email",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                justify="start",
                width="100%",
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "contraseña ",
                        size="3",
                        weight="medium",
                    ),
                    rx.link(
                        "has olvidado tu contraseña ?",
                        href="#",
                        size="3",
                    ),
                    justify="between",
                    width="100%",
                ),
                rx.input(
                    rx.input.slot(rx.icon("lock")),
                    placeholder="contraseña",
                    type="password",
                    size="3",
                    width="100%",
                ),
                spacing="2",
                width="100%",
            ),
            rx.button("INICIAR SESION", size="3",bg="red",width="100%",on_click=lambda:rx.redirect("/home")),
            rx.hstack(
                rx.divider(margin="0",),
                rx.text(
                    "O continuar con",
                    white_space="nowrap",
                    weight="medium",
                ),
                rx.divider(margin="0"),
                align="center",
                width="100%",
            ),
            rx.center(
                rx.icon_button(
                    rx.icon(tag="github"),
                    variant="soft",
                    size="3",
                    color="red"
                ),
                rx.icon_button(
                    rx.icon(tag="facebook"),
                    variant="soft",
                    size="3",
                    color="red"
                ),
                rx.icon_button(
                    rx.icon(tag="instagram"),
                    variant="soft",
                    size="3",
                    color="red"
                ),
                spacing="4",
                direction="row",
                width="100%",
            ),
            spacing="6",
            width="100%",
        ),
        size="4",
        max_width="28em",
        width="100%",
        aling_items="center",
        justify_contens="center",
        align="center",
        background="black"
    )
bg="black"

