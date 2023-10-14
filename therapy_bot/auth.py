import reflex as rx
from therapy_bot import styles


def social_icon(src, link):
    return rx.link(
            rx.image(src=src, width="24px", height="24px", ml=2, mr=2),
            href=link
        )


def auth_layout(*args):
    """The shared layout for the login and sign up pages."""

    linkedin_icon = social_icon("/linkedin_icon.png", "https://www.linkedin.com/in/kumar-kaushik/")
    email_icon = social_icon("/email_icon.png", "mailto:kumarakaushik@gmail.com")
    twitter_icon = social_icon("/twitter_icon.png", "https://twitter.com/i_am_kingkai")

    github_icon = social_icon("/github_icon.png", "https://github.com/Kumara-Kaushik")
    # medium_icon = social_icon("/medium_icon.png", "https://medium.com/@your-medium-username")
    # youtube_icon = social_icon("/youtube_icon.png", "https://www.youtube.com/channel/your-channel-id")


    return rx.box(
        rx.image(
            src="/yumi.png",  # Replace with the path to your image
            border_radius="full",  # Makes the image circular
            width="150px",  # Optional: Adjust the size as needed
            height="150px",  # Optional: Adjust the size as needed
            mb=4,  # Optional: Margin-bottom for spacing between the image and the heading
        ),
        rx.heading(
            rx.span("Hi! I'm Yumi!"),
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
            rx.span("An compassionate AI emotional support companion, made with ❤️ by Team Yumi. ",
                    rx.link("Learn more. ", href="/about", color="blue.500")),
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
        # rx.box(
        #     linkedin_icon,
        #     email_icon,
        #     twitter_icon,
        #     github_icon,
        #     display="flex",
        #     justify_content="center",
        #     mb=4
        # ),
        rx.html("""<a href='https://ko-fi.com/U7U2N7KRS' target='_blank'><img height='36' style='border:0px;font-size:14px;height:36px;' 
                             src='https://storage.ko-fi.com/cdn/kofi3.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>""",
                position="fixed",
                left="1em",
                bottom="1em"),
        rx.button(
                    "Give Feedback",
                    bg="#5535d4",
                    box_shadow="md",
                    px="4",
                    py="2",
                    h="40px",
                    font_size="12px",
                    on_click=[lambda: rx.redirect("https://discord.gg/aKyQEuRT")],
                    right="1em",
                    position="fixed",
                    bottom="1.2em",
                    rounded="full",          
                    ),
        # rx.html("""<script type="text/javascript" 
        #                     src="https://platform-api.sharethis.com/js/sharethis.js#property=651552f9dbc58b001ae436bb&product=inline-share-buttons&source=platform" 
        #                     async="async"></script>"""),
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
        padding_bottom = "5em"
    )
