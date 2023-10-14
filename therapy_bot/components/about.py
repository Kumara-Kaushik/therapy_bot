import reflex as rx
from therapy_bot import styles
from therapy_bot.state import AuthState

def about_layout():
    """Layout for the About us page."""
    return rx.box(
        rx.heading(
            rx.span("About us"),
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
            <p>Meet Team Yumi, a passionate collective of experts from various walks of life, driven by a common goal: to support and provide emotional solace through technology. At the heart of our team:</p></br>

            <ul>
                <li><strong>Kumar Kaushik:</strong> Our lead AI Engineer from Japan, who has personally witnessed the depth of mental health crises while volunteering at a mental-health hotline.</li></br>
                <li><strong>Kamal Muthiah:</strong> A Civil Engineer with invaluable venture capital experience, bringing a unique blend of technical know-how and business acumen to the table.</li></br>
                <li><strong>Aline Boanova:</strong> A seasoned Medical Doctor with extensive experience in the realm of mental health. Her insights provide the bridge between technology and the human psyche.</li></br>
                <li><strong>Hiral Arora:</strong> An Entrepreneur boasting a rich background in Product Marketing. She ensures that Yumi is not just effective but also widely accessible.</li></br>
                <li><strong>Leonhard Lukoschek:</strong> Another pivotal Medical Doctor in our team with deep expertise in health tech, helping us innovate and streamline our solutions.</li></br>
            </ul></br>

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