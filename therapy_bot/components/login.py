"""Login page. Uses auth_layout to render UI shared with the sign up page."""
import reflex as rx
from therapy_bot.auth import auth_layout
from therapy_bot.state import AuthState 
from therapy_bot import styles


def login():
    """The login page."""
    return auth_layout(
        rx.chakra.box(
            rx.chakra.input(placeholder="Username or Email ID", 
                     color="white",
                     on_blur=AuthState.set_username, mb=4),
            rx.chakra.input(
                type_="password",
                placeholder="Password",
                color="white",
                on_blur=AuthState.set_password,
                mb=4,
            ),
            rx.chakra.button(
                "Log in",
                on_click=[AuthState.login],
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
        rx.chakra.text(
            "Don't have an account yet? ",
            rx.chakra.link("Sign up here.", href="/signup", color="blue.500"),
            color="#A9A9A9",
            text_align="center",
        ),
        # bg=styles.bg_dark_color,
        # color=styles.text_light_color,
    )
