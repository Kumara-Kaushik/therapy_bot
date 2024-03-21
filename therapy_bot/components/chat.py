import reflex as rx

from therapy_bot import styles
from therapy_bot.components import loading_icon, navbar, modal, modal_alert
from therapy_bot.state import QA, State

loading_effect = rx.html('''
<div class="three-dots-loading">
    <div class="dot"></div>
    <div class="dot"></div>
    <div class="dot"></div>
</div>
''')

def full_message(qa: QA) -> rx.Component:
    """A single question/answer message."""
    
    user_icon = "/yumi.png"
    bot_icon = "/yumi.png"

    return rx.chakra.box(
        # User's message (question)
        rx.chakra.box(
            rx.chakra.hstack(
                rx.chakra.box(
                    rx.chakra.text(
                        rx.html(qa.question),
                        bg=styles.border_color,
                        shadow=styles.shadow_light,
                        **styles.message_style,
                    ),
                    margin_top="1em",
                ),
                rx.chakra.avatar(name="User", border_radius="full", 
                          width="40px", height="40px",
                          shadow= styles.shadow,
                          color= styles.text_light_color,
                          bg=  styles.border_color,),
                align_items="flex-end",
                justify_content="flex-end",
            ),
            ml="5%",  # Left margin for user's message
        ),
        # Bot's message (answer)
        rx.chakra.box(
            rx.chakra.hstack(
                rx.chakra.image(src=bot_icon, border_radius="full", width="40px", height="40px", padding_top="0em"),
                rx.chakra.box(
                    rx.cond(
                    qa.answer == "...",
                    rx.chakra.box(
                        loading_effect,
                        bg=styles.accent_color,
                        shadow=styles.shadow_light,
                        **styles.message_style,
                    ),
                    rx.chakra.text(
                        rx.html(qa.answer),
                        bg=styles.accent_color,
                        shadow=styles.shadow_light,
                        **styles.message_style,
                    )
                ),
                    text_align="left",
                    padding_top="1em",
                ),
                align_items="flex-end",
            ),
            mr="5%",  # Right margin for bot's message
        ),
        width="100%",
    )



def message(qa: QA) -> rx.Component:
    """A single question/answer message.

    Args:
        qa: The question/answer pair.

    Returns:
        A component displaying the answer.
    """
    bot_icon = "/yumi.png"
    return rx.chakra.box(
            rx.chakra.hstack(
                rx.chakra.image(src=bot_icon, border_radius="full", width="40px", height="40px", padding_top="0em"),
                rx.chakra.box(
                    rx.cond(
                    qa.answer == "...",
                    rx.chakra.box(
                        loading_effect,
                        bg=styles.accent_color,
                        shadow=styles.shadow_light,
                        **styles.message_style,
                    ),
                    rx.chakra.text(
                        rx.html(qa.answer),
                        bg=styles.accent_color,
                        shadow=styles.shadow_light,
                        **styles.message_style,
                    )
                ),
                    text_align="left",
                    padding_top="1em",
                ),
                align_items="flex-end",
            ),
            mr="5%",  # Right margin for bot's message
        )

def chat_layout() -> rx.Component:
    """List all the messages in a single conversation."""
    return rx.chakra.vstack(
        # rx.chakra.box(message(State.chats[State.current_chat][0])),
        rx.chakra.box(rx.foreach(State.chats[State.current_chat][:1], message)),
        rx.chakra.box(rx.foreach(State.chats[State.current_chat][1:], full_message)),
        py="8",
        flex="1",
        width="100%",
        max_w="3xl",
        padding_x="4",
        align_self="center",
        overflow="auto",
        padding_bottom="5em"

    )

def chat():
    return rx.chakra.vstack(
                navbar(),
                chat_layout(),
                action_bar(),
                # sidebar(),
                modal(),
                modal_alert(),
                bg=styles.bg_dark_color,
                color=styles.text_light_color,
                min_h="100vh",
                align_items="stretch",
                spacing="0",
        )

def action_bar() -> rx.Component:
    """The action bar to send a new message."""
    return rx.chakra.box(
        rx.chakra.vstack(
            rx.chakra.form(
                rx.chakra.form_control(
                    rx.chakra.hstack(
                        rx.chakra.text_area(
                            placeholder="Type something...",
                            id="question",
                            _placeholder={"color": "#fffa"},
                            _hover={"border_color": styles.accent_color},
                            style={**styles.input_style, "padding": "0.5em"},
                            overflow="scroll",
                            min_height="1em",
                        ),
                        # rx.chakra.input(
                        #     placeholder="Type something...",
                        #     id="question",
                        #     _placeholder={"color": "#fffa"},
                        #     _hover={"border_color": styles.accent_color},
                        #     style=styles.input_style,
                        #     overflow="scroll",
                        # ),
                        rx.chakra.button(
                            rx.cond(
                                State.processing,
                                loading_icon(height="1em"),
                                rx.chakra.text("Send"),
                            ),
                            type_="submit",
                            _hover={"bg": styles.accent_color},
                            style=styles.input_style,
                        ),
                        align_items="center"
                    ),
                    is_disabled=State.processing,
                ),
                on_submit=[rx.set_value("question", ""), State.process_question],
                width="100%",
            ),
            rx.chakra.text(
                "Yumi is not a certified medical professional and may sometimes return factually incorrect responses. Use discretion.",
                font_size="xs",
                color="#fff6",
                text_align="center",
            ),
            width="100%",
            max_w="3xl",
            mx="auto",
        ),
        position="sticky",
        bottom="0",
        left="0",
        py="4",
        backdrop_filter="auto",
        backdrop_blur="lg",
        border_top=f"1px solid {styles.border_color}",
        align_items="stretch",
        width="100%",
        padding_left="1em",
        padding_right="1em"
    )
