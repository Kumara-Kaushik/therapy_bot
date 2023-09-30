"""Sign up page. Uses auth_layout to render UI shared with the login page."""
import reflex as rx

from therapy_bot.auth import auth_layout
from therapy_bot.state import AuthState
from therapy_bot import styles

def signup():
    """The sign up page."""
    return auth_layout(
        rx.box(
            rx.input(placeholder="Username", 
                     color="white",
                     on_blur=AuthState.set_username, mb=4),
            rx.input(placeholder="Email ID", 
                     color="white",
                     on_blur=AuthState.set_email, mb=4),
            rx.input(
                type_="password",
                placeholder="Password",
                color="white",
                on_blur=AuthState.set_password,
                mb=4,
            ),
            rx.input(
                type_="password",
                placeholder="Confirm password",
                color="white",
                on_blur=AuthState.set_confirm_password,
                mb=4,
            ),
            rx.button(
                "Sign up",
                on_click=[AuthState.signup],
                bg="blue.500",
                color="white",
                _hover={"bg": "blue.600"},
                mb=2
            ),
            rx.box(rx.span("By signing up, you agree to our  ", 
                        rx.link("Terms of Use ", href="/terms", color="blue.500"),
                        "& ",
                        rx.link("Privacy Policy", href="/policy", color="blue.500"),
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
        rx.text(
            "Already have an account? ",
            rx.link("Sign in here.", href="/", color="blue.500"),
            color="gray.600",
            text_align="center",
        ),
    )
