"""Login page. Uses auth_layout to render UI shared with the sign up page."""
import reflex as rx
from webui.auth import auth_layout
from webui.state import AuthState
from webui import styles


def login():
    """The login page."""
    return auth_layout(
        rx.box(
            rx.input(placeholder="Username", on_blur=AuthState.set_username, mb=4),
            rx.input(
                type_="password",
                placeholder="Password",
                on_blur=AuthState.set_password,
                mb=4,
            ),
            rx.button(
                "Log in",
                on_click=AuthState.login,
                bg="blue.500",
                color="white",
                _hover={"bg": "blue.600"},
            ),
            align_items="left",
            bg=styles.bg_medium_color,
            border=styles.border_color,
            p=4,
            max_width="400px",
            border_radius="lg",
        ),
        rx.text(
            "Don't have an account yet? ",
            rx.link("Sign up here.", href="/signup", color="blue.500"),
            color="gray.600",
        ),
        # bg=styles.bg_dark_color,
        # color=styles.text_light_color,
    )
