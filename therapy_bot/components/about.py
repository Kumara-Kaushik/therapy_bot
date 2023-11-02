import reflex as rx
from therapy_bot import styles
from therapy_bot.state import AuthState

def about_layout():
    """Layout for the About us page."""
    return rx.box(
        rx.heading(
            rx.span("About Me"),
            display="flex",
            size="2xl",
            flex_direction="column",
            align_items="center",
            text_align="center",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
        ),
        rx.text(
            rx.html("""
            <p>Hey there!</br></br> I'm Kai, The tech enthusiast behind Yumi. For the past five years, I've been immersed in AI work here in Japan, and it's where Yumi came to life. The idea was born out of real conversations from a mental health hotline, showing me the power of a listening ear.

I wear many hats – coder, designer, and your go-to support. My aim? To make Yumi a helpful, easy-to-use app for anyone needing a bit of mental space. It's about straightforward, honest support, one tap at a time.</p></br>

            """),
            display="flex",
            size="sm",
            color=styles.text_light_color,
            flex_direction="column",
            align_items="center",
            text_align="left",
            width=["100%", "100%", "60%"],
            max_height="auto",   # Adjust as necessary
            padding="1em",
        ),
        rx.heading(
            rx.span("Why Yumi"),
            display="flex",
            size="2xl",
            flex_direction="column",
            align_items="center",
            text_align="center",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
        ),
        rx.text(
            rx.html("""
            <p>Mental health faces a daunting predicament in Japan. With an estimated 30 million individuals suffering from mental health issues, a staggering 70% of them go 
                    untreated. Alarmingly, half of the junior-high and high school students experience mild to severe depression. In a society where mental illness is misconstrued as a sign 
                    of weakness or low will power, and where therapy is not covered under the national health insurance, the barriers to seeking help are monumental. This cultural perspective 
                    combined with practical concerns makes the need for accessible, relatable, and culturally-sensitive support paramount.</p></br>

            """),
            display="flex",
            size="sm",
            color=styles.text_light_color,
            flex_direction="column",
            align_items="center",
            text_align="left",
            width=["100%", "100%", "60%"],
            max_height="auto",   # Adjust as necessary
            padding="1em",
        ),
        rx.heading(
            rx.span("The Yumi Difference"),
            display="flex",
            size="2xl",
            flex_direction="column",
            align_items="center",
            text_align="center",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
        ),
        rx.text(
            rx.html("""
            <p>While the barriers to seeking mental health support in Japan are multifaceted, Yumi is here to provide an empathetic ear without judgment. People feel the need to not burden their parents, 
                    and therapy's high costs make it inaccessible for many. Concerns about judgment from friends or the workplace often silence those in need. Existing online chatbots feel artificial and 
                    culturally disjointed, while helplines grapple with long wait times.</p></br>

            <p><strong>Enter Yumi: A beacon of hope.</strong></p></br>

            <p>Designed with a relatable Japanese persona, Yumi offers human-like, compassionate conversations, always ready to listen and provide solace. Key features include:</p></br>

            <ul>
                <li><strong>Cultural Sensitivity:</strong> Yumi is designed with Japanese sensibilities at its core, ensuring every interaction feels genuine and culturally resonant.</li></br>
                <li><strong>Multilingual Capabilities:</strong> Catering to an international audience, Yumi is proficient in Japanese, English, Korean, and French.</li></br>
                <li><strong>Diverse Conversational Styles:</strong> Whether you wish to vent or seek advice, Yumi adapts to your needs.</li></br>
                <li><strong>24/7 Availability:</strong> With Yumi, support is just a click away, anytime, anywhere.</li></br>
            </ul></br>

            <p>Join us on this journey to revolutionize mental health support in Japan. Together, let's make mental well-being accessible to all.</p></br>

            """),
            display="flex",
            size="sm",
            color=styles.text_light_color,
            flex_direction="column",
            align_items="center",
            text_align="left",
            width=["100%", "100%", "60%"],
            max_height="auto",   # Adjust as necessary
            padding="1em",
        ),
        rx.button(
            "Return to Signup",
            bg="#5535d4",
            box_shadow="md",
            px="4",
            py="2",
            on_click=[rx.redirect("/signup")],  # Adjust the redirect link accordingly
            mt=4
        ),
        border_top_radius="lg",
        display="flex",
        flex_direction="column",
        align_items="center",
        py=12,
        gap=4,
        width="100%",
        bg=styles.bg_dark_color,
        px=[4, 12],
        margin="0 auto",
        position="relative",
        overflow="auto",
        h="100vh",
        pt=16,
        padding_bottom="5em"
    )