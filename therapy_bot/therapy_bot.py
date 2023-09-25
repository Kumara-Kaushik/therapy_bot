"""The main Chat app."""

import reflex as rx

from therapy_bot import styles
from therapy_bot.components import chat, modal, navbar, sidebar, login, signup
from therapy_bot.state import State


def index() -> rx.Component:
    """The main app."""
    return rx.vstack(
        navbar(),
        chat.chat(),
        chat.action_bar(),
        # sidebar(),
        modal(),
        bg=styles.bg_dark_color,
        color=styles.text_light_color,
        min_h="100vh",
        align_items="stretch",
        spacing="0",
    )


# Add state and page to the app.
app = rx.App(state=State, style=styles.base_style)
app.add_page(login)
app.add_page(signup)
app.add_page(index, route="/", on_load=State.check_login())
app.compile()
