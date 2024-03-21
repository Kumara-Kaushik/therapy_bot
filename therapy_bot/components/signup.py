"""Sign up page. Uses auth_layout to render UI shared with the login page."""
import reflex as rx

from therapy_bot.auth import auth_layout
from therapy_bot.state import AuthState
from therapy_bot import styles

def signup():
    """The sign up page."""
    return auth_layout(
        rx.chakra.box(
            rx.chakra.input(placeholder="Username", 
                     color="white",
                     on_blur=AuthState.set_username, mb=4),
            rx.chakra.input(placeholder="Email ID", 
                     color="white",
                     on_blur=AuthState.set_email, mb=4),
            rx.chakra.input(
                type_="password",
                placeholder="Password",
                color="white",
                on_blur=AuthState.set_password,
                mb=4,
            ),
            rx.chakra.input(
                type_="password",
                placeholder="Confirm password",
                color="white",
                on_blur=AuthState.set_confirm_password,
                mb=4,
            ),
            rx.chakra.button(
                "Sign up",
                on_click=[AuthState.signup],
                bg="blue.500",
                color="white",
                _hover={"bg": "blue.600"},
                mb=2
            ),
            rx.chakra.box(rx.chakra.span("By signing up, you agree to our  ", 
                        rx.chakra.link("Terms of Use ", href="/terms", color="blue.500"),
                        "& ",
                        rx.chakra.link("Privacy Policy", href="/policy", color="blue.500"),
                        color="#A9A9A9",
                        font_size="12px",
                    )
            ),
            align_items="left",
            bg=styles.bg_medium_color,
            border=styles.border_color,
            p=4,
            max_width="400px",
            border_radius="lg",
        ),
        rx.chakra.text(
            "Already have an account? ",
            rx.chakra.link("Sign in here.", href="/", color="blue.500"),
            color="gray.600",
            text_align="center",
        ),
    )
