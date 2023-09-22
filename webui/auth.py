import reflex as rx

def auth_layout(*args):
    """The shared layout for the login and sign up pages."""
    return rx.box(
        rx.heading(
                rx.span("Hi! I'm Dr. Yumi!"),
                rx.text("A person you can confide in. :)"),
                display="flex",
                flex_direction="column",
                align_items="center",
                text_align="center",
            ),
            rx.text(
                "Sign in or sign up to get started!",
                # color="gray.500",
                # font_weight="medium",
            ),
            *args,
            border_top_radius="lg",
            # box_shadow="0 4px 60px 0 rgba(0, 0, 0, 0.08), 0 4px 16px 0 rgba(0, 0, 0, 0.08)",
            display="flex",
            flex_direction="column",
            align_items="center",
            py=12,
            gap=4,
            # container props:
            width="100%",
            max_width="960px",
            # bg="white",
            px=[4, 12],
            margin="0 auto",
            position="relative",
            h="100vh",
            pt=16,
            # background="url(bg.svg)",
            background_repeat="no-repeat",
            background_size="cover",
        )