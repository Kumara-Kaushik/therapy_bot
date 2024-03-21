import reflex as rx
from therapy_bot import styles
from therapy_bot.state import AuthState

def terms_layout():
    """Layout for the Terms and Conditions page."""
    return rx.chakra.box(
        rx.chakra.heading(
            rx.chakra.span("Terms and Conditions"),
            display="flex",
            size="2xl",
            flex_direction="column",
            align_items="center",
            text_align="center",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
        ),
        rx.chakra.text(
            rx.html("""
                <p>Last updated: 28th September 2023</p></br>
                
                <p>Please read these <em>Terms of Service</em> ("Terms") carefully before using 
                <a href="http://yumisensei.online"><strong>yumisensei.online</strong></a> (the "Website") operated by Kai (Kumar Kaushik) ("I", "we," or "us").</p></br>
                
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
        rx.chakra.text(
            rx.html("""
                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Usage</h2>
                <p>1. The Service is designed to provide compassionate listening through our AI chatbot. It is intended for venting and casual conversation only.</p>
                <p>2. The Service is not a substitute for professional advice, diagnosis, or treatment. For critical issues or advice, please consult with a qualified professional.</p>
                <p>3. If you or someone you know is feeling suicidal, please call a national or international suicide prevention hotline immediately. A reputable international directory of crisis centers can be found at the International Association for Suicide Prevention (IASP) website: <a href="https://www.iasp.info/resources/Crisis_Centres/">IASP</a>.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">User Responsibilities</h2>
                <p>1. You must be at least 18 years old or have the necessary legal capacity in your jurisdiction to enter into these Terms and use the services.</p>
                <p>2. You agree to use the Service responsibly and at your own risk.</p>
                <p>3. Do not provide any personal identifying information while using the Service.</p>
                <p>4. You are responsible for any content you provide to the Service.</p>
                <p>5. You agree to provide accurate, current, and complete information if registering for an account and to keep your account information updated. You are responsible for maintaining the confidentiality of your account credentials and for all activities that occur under your account.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Data and Privacy</h2>
                <p>1. We value your privacy. We do not collect or store any of your chat data. All chat data is deleted after every session.</p>
                <p>2. You agree to avoid sharing any personal identifying information while using the Service.</p>
                <p>3. By using the Service, you acknowledge and agree that the Service may use the collected information for analytics, data training, and service improvement purposes.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Content Moderation</h2>
                <p>1. The chatbot's responses are moderated according to ChatGPT guidelines. However, we cannot guarantee the appropriateness or accuracy of every response.</p>
                <p>2. We encourage users to report any inappropriate or harmful content they encounter.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Intellectual Property</h2>
                <p>1. The Service and its original content, features, and functionality are owned by Kai (Kumar Kaushik) and are protected by international copyright, trademark, patent, trade secret, and other intellectual property or proprietary rights laws.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Limitation of Liability</h2>
                <p>1. Kai (Kumar Kaushik) is not liable for any harm, damages, or losses that may arise from using the Service. This includes, but is not limited to, emotional distress, misinformation, or technical issues. To the maximum extent permitted by applicable law, neither the Service nor its affiliates, officers, directors, employees, agents, suppliers, and licensors shall be liable for any indirect, incidental, special, consequential, or punitive damages, or any loss of profits or revenue, whether incurred directly or indirectly.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Changes to the Terms</h2>
                <p>1. We reserve the right to modify or replace these Terms at any time. Your continued use of the Service after the posting of any changes constitutes your acceptance of the modified Terms.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Termination</h2>
                <p>1. We reserve the right to terminate or suspend access to our Service, without prior notice, for conduct that we believe violates these Terms or is harmful to other users of the Service, us, or third parties, or for any other reason.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Refunds</h2>
                <p>1. The Service offers a refund policy for certain circumstances. You may be eligible for a refund if you encounter a technical issue with the services that prevents you from utilizing them as intended. Eligibility for a refund will be determined in its sole discretion.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;">Contact Us</h2>
                <p>1. If you have any questions about these Terms, please contact us at <a href="mailto:kumarakaushik@gmail.com">kumarakaushik@gmail.com</a>.</p></br>
                    
                <p>By using YumiSensei.Online, you acknowledge that you have read, understood, and agreed to the terms of this Terms and Conditions of use.</p>

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
        rx.chakra.button(
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


def privacy_layout():
    """Layout for the Privacy Policy page."""
    return rx.chakra.box(
        rx.chakra.heading(
            rx.chakra.span("Privacy Policy"),
            display="flex",
            size="2xl",
            flex_direction="column",
            align_items="center",
            text_align="center",
            background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
            background_clip="text",
        ),
        rx.chakra.text(
            rx.html("""
                <p>Last updated: 28th September 2023</p></br>
                
                <p>Please read these <em>Privacy Policy</em> ("Terms") carefully before using 
                <a href="http://yumisensei.online"><strong>yumisensei.online</strong></a> (the "Website") operated by Kai (Kumar Kaushik) ("I", "we," or "us").</p></br>
                
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
        rx.chakra.text(
            rx.html("""
                <h2 style="font-size: 1.5rem; margin-top: 1rem;"> Information We Collect</h3>
                <p>1 Personal Information: When you use YumiSensei.Online, we may collect personal information that you voluntarily provide to us, such as your name, email address, and any other information you choose to provide.</p>

                <p>2 Usage and Analytics Information: We use third-party analytics tools, including Google Analytics, Vercel Analytics, and Sentry, which collect information about your interactions with the Website. This may include your IP address, browser type, device type, operating system, and other usage details. Please refer to the respective privacy policies of these analytics providers for more information on their data practices.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;"> How We Use Your Information</h3>
                <p>1 Provision of Services: We use the information we collect to provide and improve our services, respond to user inquiries and support requests, personalize user experiences, and to communicate with users about their use of the Website and services.</p>

                <p>2 Analytics and Research: The usage and analytics information we collect helps us understand how users interact with the Website, analyze trends, and improve our services and user experiences.</p>

                <p>3 Communication: We may use your contact information to send you updates, newsletters, and promotional materials related to YumiSensei.Online. You may opt-out of receiving these communications by following the instructions provided in such communications or by contacting us directly.</p>

                <p>4 Legal Compliance: We may use your information to comply with applicable laws, regulations, legal processes, or enforceable governmental requests, or to protect our rights, privacy, safety, or property, as well as those of our users and the public.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;"> Information Sharing and Disclosure</h3>
                <p>1 Service Providers: We may engage third-party service providers who assist us in operating the Website and delivering our services. These service providers have access to your personal information only to perform specific tasks on our behalf and are obligated not to disclose or use it for any other purpose.</p>

                <p>2 Aggregate and Anonymized Information: We may aggregate and anonymize the information we collect to create statistical or research reports. These reports may be shared with third parties for analytical, research, or marketing purposes, but they will not contain any personally identifiable information.</p>

                <p>3 Legal Requirements: We may disclose your information if required to do so by law or in response to valid requests by public authorities (e.g., a court or government agency).</p>

                <p>4 Business Transfers: In the event of a merger, acquisition, reorganization, or sale of assets, your information may be transferred as part of the transaction. We will provide notice before your information is transferred and becomes subject to a different privacy policy.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;"> Data Security</h3>
                <p>1 We implement reasonable security measures to protect the confidentiality, integrity, and availability of your personal information. However, please note that no method of transmission or storage is completely secure, and we cannot guarantee the absolute security of your information.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;"> Third-Party Links and Services</h3>
                <p>1 The Website may contain links to third-party websites, applications, or services that are not owned or controlled by YumiSensei.Online. This Privacy Policy does not apply to such third-party platforms. We encourage you to review the privacy policies of those third parties before providing any personal information to them.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;"> Children's Privacy</h3>
                <p>1 YumiSensei.Online does not knowingly collect or solicit personal information from individuals under the age of 18. If you are under 18, please do not use the Website or provide any personal information to us. If we learn that we have collected personal information from a child under the age of 18, we will take steps to promptly delete the information.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;"> Changes to this Privacy Policy</h3>
                <p>1 YumiSensei.Online reserves the right to modify or update this Privacy Policy at any time. Any changes will be effective immediately upon posting the revised Privacy Policy on the Website. Your continued use of the Website following the posting of any changes constitutes your acceptance of such changes.</p>

                <h2 style="font-size: 1.5rem; margin-top: 1rem;"> Contact Us</h3>
                <p>1 If you have any questions or concerns about this Privacy Policy or our data practices, please contact us at kumarakaushik@gmail.com.</p></br>

                <p>By using YumiSensei.Online, you acknowledge that you have read, understood, and agreed to the terms of this Privacy Policy.</p>

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
        rx.chakra.button(
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

