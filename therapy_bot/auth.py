import reflex as rx
from therapy_bot import styles

def auth_layout(*args):
    """The shared layout for the login and sign up pages."""
    return rx.box(
        rx.image(
            src="/yumi.png",  # Replace with the path to your image
            border_radius="full",  # Makes the image circular
            width="150px",  # Optional: Adjust the size as needed
            height="150px",  # Optional: Adjust the size as needed
            mb=4,  # Optional: Margin-bottom for spacing between the image and the heading
        ),
        rx.heading(
            rx.span("Hi! I'm Dr. Yumi!"),
            display="flex",
            size="2xl",
            # color=styles.text_light_color,
            flex_direction="column",
            align_items="center",
            text_align="center",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
        ),
        rx.text(
            rx.span("An compassionate AI therapist, made with ❤️ by Kai - An AI Architect and \
                     passionate suicide hotline volunteer."),
            display="flex",
            size="sm",
            color=styles.text_light_color,
            flex_direction="column",
            align_items="center",
            text_align="center",
            width=["100%", "100%", "60%"],
        ), 
        rx.text(
            "Sign in or sign up to get started!",
            # font_weight="medium",
            color="#A9A9A9",
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
        # max_width="960px",
        bg=styles.bg_dark_color,  # Set the background to dark color
        px=[4, 12],
        margin="0 auto",
        position="relative",
        overflow="auto",
        h="100vh",
        pt=16,
        # background="url(bg.svg)",  # Comment this out if you don't want any other background
        background_repeat="no-repeat",
        background_size="cover",
    )