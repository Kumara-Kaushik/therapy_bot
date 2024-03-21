import reflex as rx

from therapy_bot import styles
from therapy_bot.state import State


def navbar():
    bot_icon = "/yumi.png"
    return rx.chakra.box(
        rx.chakra.hstack(
            rx.chakra.hstack(
                # rx.chakra.icon(
                #     tag="hamburger",
                #     mr=4,
                #     on_click=State.toggle_drawer,
                #     cursor="pointer",
                # ),
                rx.chakra.link(
                    rx.chakra.image(src=bot_icon, border_radius="full", width="40px", height="40px", padding_top="0em"),
                    href="/chat",
                ),
                rx.chakra.breadcrumb(
                    # rx.chakra.breadcrumb_item(
                    #     rx.chakra.heading("ReflexGPT", size="sm"),
                    # ),
                    rx.chakra.breadcrumb_item(
                        rx.chakra.text(State.current_chat, size="sm", font_weight="normal"),
                    ),
                ),
            ),
            rx.chakra.hstack(
                # rx.chakra.button(
                #     "+ New chat",
                #     bg=styles.accent_color,
                #     px="4",
                #     py="2",
                #     h="auto",
                #     on_click=State.toggle_modal,
                # ),
                rx.chakra.menu(
                    rx.chakra.menu_button(
                        "Language",
                            bg=styles.accent_color,
                            px="4",
                            py="2",
                            h="auto",
                            rounded="lg"
                    ),
                    rx.chakra.menu_list(
                        rx.chakra.menu_item("English",
                                     on_click=[State.english_chat]),
                        rx.chakra.menu_divider(),
                        rx.chakra.menu_item("Japanese",
                                     on_click=[State.japanese_chat]),
                        rx.chakra.menu_divider(),
                        rx.chakra.menu_item("French",
                                     on_click=[State.french_chat]),
                    ),
                ),
                rx.chakra.menu(
                    rx.chakra.menu_button(
                        rx.chakra.avatar(name="User", size="md"),
                        rx.chakra.box(),
                    ),
                    rx.chakra.menu_list(
                        rx.chakra.menu_item("Delete Chat",
                                     on_click=State.toggle_modal),
                        rx.chakra.menu_divider(),
                        rx.chakra.menu_item("Logout",
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
