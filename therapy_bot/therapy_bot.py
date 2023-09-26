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
app.add_page(index, title="Login")
app.add_page(signup, title="Signup")
app.add_page(chat, title="Chat with Dr.Yumi")
app.compile()
