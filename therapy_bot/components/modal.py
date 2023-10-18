import reflex as rx
from therapy_bot.state import State


def modal() -> rx.Component:
    """A modal to create a new chat."""
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header(
                    rx.hstack(
                        rx.vstack(
                            rx.text("Are you sure you want to delete this Chat?"),
                            rx.text("All your data will be lost.")
                        ),
                        rx.icon(
                            tag="close",
                            font_size="sm",
                            on_click=State.toggle_modal,
                            color="#fff8",
                            _hover={"color": "#fff"},
                            cursor="pointer",
                        ),
                        align_items="center",
                        justify_content="space-between",
                    )
                ),
                # rx.modal_body(
                #     rx.input(
                #         placeholder="Type something...",
                #         on_blur=State.set_new_chat_name,
                #         bg="#222",
                #         border_color="#fff3",
                #         _placeholder={"color": "#fffa"},
                #     ),
                # ),
                rx.modal_footer(
                    rx.hstack(
                    rx.button(
                            "Yes",
                            bg="#5535d4",
                            box_shadow="md",
                            px="4",
                            py="2",
                            h="auto",
                            _hover={"bg": "#4c2db3"},
                            on_click=[State.create_chat, State.toggle_modal],
                        ),
                        rx.button(
                            "No",
                            bg="#5535d4",
                            box_shadow="md",
                            px="4",
                            py="2",
                            h="auto",
                            _hover={"bg": "#4c2db3"},
                            on_click=[State.toggle_modal],
                        )),
                ),
                bg="#222",
                color="#fff",
            ),
        ),
        is_open=State.modal_open,
    )


def modal_alert() -> rx.Component:
    return rx.modal(
        rx.modal_overlay(
            rx.modal_content(
                rx.modal_header(
                    rx.hstack(
                        rx.vstack(
                            rx.text("Engagement Alert"),
                        ),
                        rx.icon(
                            tag="close",
                            font_size="sm",
                            on_click=State.toggle_change,
                            color="#fff8",
                            _hover={"color": "#fff"},
                            cursor="pointer",
                        ),
                        align_items="center",
                        justify_content="space-between",
                    )
                ),
                rx.modal_body(
                    rx.html("Hey! Is the conversation helping? I'd like to make this app accessible to \
                         everyone who needs support, which unfortunately isn't cheap. </br></br>Please Support me on this mission \
                         and take some time to leave some feedback on the Discord Server for any suggestions or improvements! :) \
                         </br></br>If you have already done so, Please ignore this message. ")
                ),
                rx.modal_footer(
                    rx.hstack(
                        rx.html("""<a href='https://ko-fi.com/U7U2N7KRS' target='_blank'><img height='36' style='border:0px;height:36px;' 
                             src='https://storage.ko-fi.com/cdn/kofi3.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>"""),
                        rx.button(
                            "Join Discord",
                            bg="#5535d4",
                            box_shadow="md",
                            px="4",
                            py="2",
                            h="auto",
                            _hover={"bg": "#4c2db3"},
                            on_click=[lambda: rx.redirect("https://discord.com/invite/9Z32E3BmZB")],
                        ),
                    ),
                    align_items="center",
                    justify_content="space-between",

                ),
                bg="#222",
                color="#fff",
            ),
        ),
        is_open=State.show,
    )


# def modal_signup_alert() -> rx.Component:
#     return rx.modal(
#             rx.modal_overlay(
#                 rx.modal_content(
#                     rx.modal_header(
#                         rx.text("Congratulations!")
#                     ),
#                     rx.modal_body(
#                         rx.html("You have successfully signed up!</br></br>Login to chat with Yumi")
#                     ),
#                     rx.modal_footer(
#                         rx.button(
#                             "Close", 
#                             bg="#5535d4",
#                             box_shadow="md",
#                             px="4",
#                             py="2",
#                             h="auto",
#                             _hover={"bg": "#4c2db3"},
#                             on_click=State.signup_change
#                         )
#                     ),
#                     bg="#222",
#                     color="#fff",
#                 ),
#             ),
#             is_open=State.signup_show,
#         )