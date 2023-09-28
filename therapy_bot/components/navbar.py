import reflex as rx

from therapy_bot import styles
from therapy_bot.state import State


def navbar():
    bot_icon = "/yumi.png"
    return rx.box(
        rx.hstack(
            rx.hstack(
                # rx.icon(
                #     tag="hamburger",
                #     mr=4,
                #     on_click=State.toggle_drawer,
                #     cursor="pointer",
                # ),
                rx.link(
                    rx.image(src=bot_icon, border_radius="full", width="40px", height="40px", padding_top="0em"),
                    href="/chat",
                ),
                rx.breadcrumb(
                    # rx.breadcrumb_item(
                    #     rx.heading("ReflexGPT", size="sm"),
                    # ),
                    rx.breadcrumb_item(
                        rx.text(State.current_chat, size="sm", font_weight="normal"),
                    ),
                ),
            ),
            rx.hstack(
                # rx.button(
                #     "+ New chat",
                #     bg=styles.accent_color,
                #     px="4",
                #     py="2",
                #     h="auto",
                #     on_click=State.toggle_modal,
                # ),
                rx.menu(
                    rx.menu_button(
                        "Language",
                            bg=styles.accent_color,
                            px="4",
                            py="2",
                            h="auto",
                            rounded="lg"
                    ),
                    rx.menu_list(
                        rx.menu_item("English",
                                     on_click=[State.english_chat]),
                        rx.menu_divider(),
                        rx.menu_item("Japanese",
                                     on_click=[State.japanese_chat]),
                        rx.menu_divider(),
                        rx.menu_item("French",
                                     on_click=[State.french_chat]),
                    ),
                ),
                rx.menu(
                    rx.menu_button(
                        rx.avatar(name="User", size="md"),
                        rx.box(),
                    ),
                    rx.menu_list(
                        rx.menu_item("Delete Chat",
                                     on_click=State.toggle_modal),
                        rx.menu_divider(),
                        rx.menu_item("Logout",
                                     on_click=[State.enter_user_msg_number, State.logout]),
                    ),
                ),
                spacing="3",
            ),
            justify="space-between",
        ),
        bg=styles.bg_dark_color,
        backdrop_filter="auto",
        backdrop_blur="lg",
        p="4",
        border_bottom=f"1px solid {styles.border_color}",
        position="sticky",
        top="0",
        z_index="100",
    )
