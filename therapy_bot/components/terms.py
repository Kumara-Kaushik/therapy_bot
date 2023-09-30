import reflex as rx
from therapy_bot import styles
from therapy_bot.state import AuthState

def terms_layout():
    """Layout for the Terms and Conditions page."""
    return rx.box(
        rx.heading(
            rx.span("Terms and Conditions"),
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
                <p>Last updated: 28th September 2023</p></br>
                
                <p>Please read these <em>Terms of Service</em> carefully before using 
                <a href="http://yumisensei.online"><strong>yumisensei.online</strong></a> operated by Kai (Kumar Kaushik).</p></br>
                
                <p>By accessing or using the Service, you agree to be bound by these Terms. If you disagree with any part of the terms, then you may not access the Service.</p>
            """),
            display="flex",
            size="sm",
            color=styles.text_light_color,
            flex_direction="column",
            align_items="center",
            text_align="left",
            width=["100%", "100%", "60%"],
            max_height="500px",   # Adjust as necessary
            padding="1em",
        ),
        rx.text(
            rx.html("""
                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Usage</h2>
                <p> 1. The Service is designed to provide compassionate listening through our AI chatbot. It is intended for venting and casual conversation only.</p>
                <p> 2. The Service is not a substitute for professional advice, diagnosis, or treatment. For critical issues or advice, please consult with a qualified professional.</p>
                <p> 3. If you or someone you know is feeling suicidal, please call a national or international suicide prevention hotline immediately. [You can insert a list of hotlines for different countries here].</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">User Responsibilities</h2>
                <p> 1. You agree to use the Service responsibly and at your own risk.</p>
                <p> 2. Do not provide any personal identifying information while using the Service.</p>
                <p> 3. You are responsible for any content you provide to the Service.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Data and Privacy</h2>
                <p> 1. We value your privacy. We do not collect or store any of your chat data. All chat data is deleted after every session.</p>
                <p> 2. You agree to avoid sharing any personal identifying information while using the Service.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Content Moderation</h2>
                <p> 1. The chatbot's responses are moderated according to ChatGPT guidelines. However, we cannot guarantee the appropriateness or accuracy of every response.</p>
                <p> 2. We encourage users to report any inappropriate or harmful content they encounter.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Limitation of Liability</h2>
                <p> 1. Kai (Kumar Kaushik) is not liable for any harm, damages, or losses that may arise from using the Service. This includes, but is not limited to, emotional distress, misinformation, or technical issues.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Intellectual Property</h2>
                <p> 2. The Service and its original content, features, and functionality are owned by Kai (Kumar Kaushik) and are protected by international copyright, trademark, patent, trade secret, and other intellectual property or proprietary rights laws.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Changes to the Terms</h2>
                <p> 1. We reserve the right to modify or replace these Terms at any time. We will make an effort to provide at least 30 days' notice prior to any new terms taking effect.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Termination</h2>
                <p> 1. We reserve the right to terminate or suspend access to our Service, without prior notice, for conduct that we believe violates these Terms or is harmful to other users of the Service, us, or third parties, or for any other reason.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Contact Us</h2>
                <p> 1. If you have any questions about these Terms, please contact us at <a href="mailto:kumarakaushik@gmail.com">kumarakaushik@gmail.com</a>.</p>
            """),  # Include your actual terms here.
            display="flex",
            size="sm",
            color=styles.text_light_color,
            flex_direction="column",
            align_items="center",
            text_align="left",
            width=["100%", "100%", "60%"],
            overflow_y="scroll",  # Allows the terms text to be scrollable
            max_height="500px",   # Adjust as necessary
            padding="1em",
            background_color="rgba(236, 236, 236, 0.05)",
        ),
        rx.checkbox(
            "I agree to the Terms and Conditions.",
            color=styles.text_light_color,
            mt=4,
            on_change=AuthState.set_accept_terms_2,
        ),
        rx.cond(
            AuthState.accept_terms_2,
            rx.button(
            "Return to Signup",
            bg="#5535d4",
            box_shadow="md",
            px="4",
            py="2",
            on_click=[rx.redirect("/signup"), AuthState.toggle_terms_2],  # Adjust the redirect link accordingly
            mt=4),
            rx.button(
            "Return to Signup",
            bg="#5535d4",
            box_shadow="md",
            px="4",
            py="2",
            on_click=[rx.window_alert("Please check the terms and conditions declaration box.")],  # Adjust the redirect link accordingly
            mt=4)
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

