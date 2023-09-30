"""The main Chat app."""

import reflex as rx

from therapy_bot import styles
from therapy_bot.components import login, signup, chat
from therapy_bot.state import State

def index() -> rx.Component:
    """The main app."""
    return login()


# Add state and page to the app.
app = rx.App(state=State, style=styles.base_style)
app.add_page(index, title="Login", description="Chat with Yumi")
app.add_page(signup, title="Signup", description="Chat with Yumi")
app.add_page(chat, title="Chat with Yumi", on_load=State.check_login())
app.compile()
