import os

import openai
import reflex as rx
import re
import bcrypt
import time


## Add login:
from typing import Optional

from sqlmodel import Field

openai.api_key = os.environ["OPENAI_KEY"]
openai.api_base = os.getenv("OPENAI_API_BASE","https://api.openai.com/v1")

master_prompt = """
                ChatGPT adopts the role of Yumi [YOU=Yumi|USER=USER] and addresses the user. A kind, patient, and introspective therapist with a gentle demeanor.
                Specializes in a wide variety of therapy techniques to cater to individual needs. Committed to helping clients navigate life's challenges and fostering 
                personal growth. Skilled in creating a safe, non-judgmental space for clients to explore their emotions and experiences.
                MOST IMPORTANT POINT: SHE NEVER STARTS ANY MESSAGE WITH "I'M SORRY TO HEAR THAT..." OR ANY VARIATION OF THAT.

                Yumi🌙, late 30s, empathetic🌸. Specializes in various therapy techniques🔧. Committed to client growth🌱, understanding🤗, and self-discovery🔍.
                Fosters safe space🏠 and open communication💬.

                PersRubric:
                O2E: 20, I: 90, AI: 70, E: 95, Adv: 50, Int: 80, Lib: 70
                C: 90, SE: 90, Ord: 80, Dt: 50, AS: 80, SD: 50, Cau: 60
                E: 95, W: 85, G: 90, A: 95, AL: 95, ES: 90, Ch: 70
                A: 85, Tr: 90, SF: 70, Alt: 60, Comp: 50, Mod: 80, TM: 80
                N: 20, Anx: 30, Ang: 15, Dep: 20, SC: 10, Immod: 20, V: 15

                Ask about user needs. Nod START, follow the process. ITERATE WHEN DONE. EVERY ITERATION, REMIND YOURSELF WHO YOU ARE AND WHAT YOU'RE DOING AND ALWAYS BE YOURSELF,
                AND DON'T TALK ABOUT TECHNIQUES UNLESS THEY BRING IT UP FIRST. IT'S RUDE.

                [START]-1AssessNeeds-2BuildRapport-3IdentifyIssues-4ExploreEmotions-5SetGoals-6DevelopCopingStrategies-7SelfReflection-8MonitorProgress-9AdjustApproach-10EvaluateOutcome
                -11Closure->1EstablishTrust-2ActiveListening-3Empathy-4ProbingQuestions-5IdentifyStrengthsWeaknesses-6AlignValues-7EmotionalRegulation-8CommunicationSkills-9Mindfulness-
                10CognitiveReframing->[END]

                The final workflow product must be presented to the user at the end of the workflow cycle. One page at a time, pausing for confirmation. If the process cannot construct it, 
                say so before beginning.

                YUMI ALWAYS REMINDS HERSELF OF THE SAFE AND CALM SPACE SHE SEEKS TO CREATE AND KEEPS HER RESPONSES VERY CONCISE. SHE ALWAYS REMINDS HERSELF
                NEVER TO START ANY MESSAGE WITH "I'M SORRY TO HEAR THAT..." OR ANY VARIATION OF THAT. 
                """
                # [THERAPY_TECHNIQUES]:1-CognitiveBehavioralTherapy(1a-CognitiveReframing->1b-BehavioralActivation->1c-ExposureTherapy->1d-GoalSetting->1e-ProblemSolving->1f-SkillsTraining)
                # ->2-PsychodynamicTherapy(2a-FreeAssociation->2b-DreamAnalysis->2c-Transference->2d-WorkingThrough->2e-Insight->2f-Interpretation)->3-HumanisticTherapy(3a-ClientCentered->3b
                # -ActiveListening->3c-UnconditionalPositiveRegard->3d-Genuineness->3e-Empathy->3f-SelfActualization)->4-SolutionFocusedBriefTherapy(4a-MiracleQuestion->4b-ExceptionFinding->
                # 4c-ScalingQuestions->4d-GoalSetting->4e-CopingQuestions->4f-Compliments)->5-MindfulnessBasedTherapies(5a-Meditation->5b-BodyScan->5c-MindfulBreathing->5d-LovingKindnessMeditation
                # ->5e-NonjudgmentalAwareness->5f-EmotionRegulation)->6-DialecticalBehaviorTherapy(6a-Mindfulness->6b-DistressTolerance->6c-EmotionRegulation->6d-InterpersonalEffectiveness->6e-
                # Validation->6f-SkillsGeneralization)


class QA(rx.Base):
    """A question and answer pair."""

    question: str
    answer: str


class User(rx.Model, table=True):
    """A table of Users."""

    username: str = Field()
    email: str = Field()
    password: str = Field()
    message_count: int = Field(default=0)
    is_password_hashed: bool = Field(default=False)

class State(rx.State):
    """The app state."""

    master_answer = f"Hi there! I'm here to chat. Are you in the mood to vent, seek some advice, or indulge in a bit of banter?"

    # A dict from the chat name to the list of questions and answers.
    chats: dict[str, list[QA]] = {
        "Consultation with Yumi": [QA(question=master_prompt, answer=master_answer)],
    }

    # The current chat name.
    current_chat = "Consultation with Yumi"

    # The currrent question.
    question: str

    # Whether we are processing the question.
    processing: bool = False

    # The name of the new chat.
    new_chat_name: str = "Consultation with Yumi"

    # Whether the drawer is open.
    drawer_open: bool = False

    # Whether the modal is open.
    modal_open: bool = False

    # User
    user: Optional[User] = None

    # Alert
    show: bool = False

    # accept terms
    accept_terms: bool = False

    # accept terms
    accept_terms_2: bool = False

    # input_text state
    text: str = ""

    # signup model state
    # signup_show: bool = False

    def create_chat(self):
        """Create a new chat."""
        # Insert a default question.
        del self.chats[self.current_chat]
        self.chats[self.new_chat_name] = [
            QA(question=master_prompt, answer=self.master_answer)
        ]
        self.current_chat = self.new_chat_name

    def english_chat(self):
        self.new_chat_name = "Chat with Yumi"
        self.master_answer = f"Hi {self.user.username}! I'm here to chat. Are you in the mood to vent, seek some advice, or indulge in a bit of banter?"      
        self.create_chat()

    def japanese_chat(self):
        self.new_chat_name = "ユミとのチャット"
        self.master_answer = f"こんにちは {self.user.username}さん！話をするためにここにいます。愚痴を言いたい、アドバイスを求めたい、またはちょっとしたおしゃべりをしたいですか？"       
        self.create_chat()

        
    def french_chat(self):
        self.new_chat_name = "Chat avec Yumi"
        self.master_answer = f"Bonjour {self.user.username}! Je suis là pour discuter. Envie de te défouler, chercher quelques conseils ou simplement échanger quelques mots?"
        self.create_chat()

    def toggle_modal(self):
        """Toggle the new chat modal."""
        self.modal_open = not self.modal_open

    # def signup_change(self):
    #     self.signup_show = not (self.signup_show)

    def toggle_drawer(self):
        """Toggle the drawer."""
        self.drawer_open = not self.drawer_open

    def set_chat(self, chat_name: str):
        """Set the name of the current chat.

        Args:
            chat_name: The name of the chat.
        """
        self.current_chat = chat_name
        self.toggle_drawer()

    @rx.var
    def chat_titles(self) -> list[str]:
        """Get the list of chat titles.

        Returns:
            The list of chat names.
        """
        return list(self.chats.keys())
    
    
    def convert_links_to_html(self, text: str) -> str:
        import re
        if not isinstance(text, str):
            return text

        # Regular expression to match markdown-style links: [text](url)
        pattern = r'\[(?P<text>[^\]]+)\]\((?P<url>https?://[^\)]+)\)'
        
        converted_text = re.sub(pattern, r"<a href='\2' target='_blank'>\1</a>", text)
        return converted_text
    

    async def process_question(self, form_data: dict[str, str]):
        self.question = form_data["question"]
        
        # Check if the user has already asked the same question or if the question is empty
        if (
            self.chats[self.current_chat][-1].question == self.question
            or self.question == ""
        ):
            return

        # Step 1: Immediately add the user's question to the chat
        qa = QA(question=self.question, answer="...")  # ... as a placeholder indicating the bot is "typing"
        self.chats[self.current_chat].append(qa)
        yield  # Yield to update the UI

        # Step 2: Simulate a brief typing delay
        time.sleep(1)  # Adjust this value to increase or decrease the "typing" delay

        # Step 3: Fetch bot's reply (non-streamed)
        self.processing = True
        session = openai.ChatCompletion.create(
            model=os.getenv("OPENAI_MODEL", "gpt-3.5-turbo"),
            messages=self.api_message(),
            temperature=0.7,
            stream=False,  # Ensure it's not streamed
        )

        # print(session)
        answer_text = session['choices'][0]['message']['content'].replace("\n", "<br/>")
        self.chats[self.current_chat][-1].answer = answer_text
        self.processing = False
        yield  # Yield to update the UI with the bot's reply

        # The remaining logic for updating user's message count and other operations
        self.user.message_count += 1

        if (self.user.message_count in [5, 50, 100]) or (self.user.message_count % 100 == 0):
            self.show = True
        else:
            self.show = False

        # Add the message count to the database every 5 messages
        if self.user.message_count % 1 == 0:  # Adjusted from 1 to 5 as per the comment
            self.enter_user_msg_number()


    def toggle_change(self):
        self.show = not (self.show)

    def toggle_terms(self):
        self.accept_terms = not (self.accept_terms)

    def toggle_terms_2(self):
        self.accept_terms_2 = not (self.accept_terms_2)

    def get_user_message(self, msg):
        return {"role": "user", "content": msg}
    
    def get_assistant_message(self, msg):
        return {"role": "assistant", "content": msg}

    def api_message(self):
        '''
        This function, will constact a Openai API message to pass to Openai everytime a user asks a question.
        The first 2 and latest 3 question-answer pairs from the chat along with the latest question is sent to
        the openai API, to give it more context of the chat.
        '''
        message_list = []
        for item in self.chats[self.current_chat][:2]:
            message_list.append(self.get_user_message(item.question))
            message_list.append(self.get_assistant_message(item.answer))
        for item in self.chats[self.current_chat][-3:]:
            message_list.append(self.get_user_message(item.question))
            message_list.append(self.get_assistant_message(item.answer))
        message_list.append(self.get_user_message(self.question))
        return message_list

    def logout(self):
        """Log out a user."""
        self.english_chat()
        return rx.redirect("/")

    def check_login(self):
        """Check if a user is logged in."""
        if not self.logged_in:
            return rx.redirect("/")

    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user is not None
    
    def enter_user_msg_number(self):
        """Use this function to register the total number of messages sent by user when session ends."""
        with rx.session() as session:
            user = session.exec(
                User.select.where(User.username == self.user.username)
            ).first()
            user.message_count = self.user.message_count
            session.add(user)
            session.commit()
            return rx.redirect("/")


class AuthState(State):
    """The authentication state for sign up and login page."""

    username: str
    email: str
    password: str
    confirm_password: str

    def signup(self):
        """Sign up a user."""
        with rx.session() as session:
            if session.exec(User.select.where(User.username == self.username)).first():
                return rx.window_alert("Username already exists.")

            # Email validation using regex
            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if not re.match(email_pattern, self.email):
                return rx.window_alert("Please enter a valid email address.")
            
            if self.password != self.confirm_password:
                return rx.window_alert("Passwords do not match.")
            
            # if not self.accept_terms:
            #     return rx.window_alert("Please read and accept the terms and conditions.")
            
            # Hash the password before storing it
            hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())

            self.user = User(
                username=self.username, 
                email=self.email, 
                password=hashed_password.decode('utf-8'), 
                is_password_hashed=True
            )
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            self.english_chat()
            # self.toggle_terms()
            return[rx.window_alert("Congratulations! You have successfully signed up! Login to chat with Yumi."), rx.redirect("/")]
            # return rx.redirect("/")

    def login(self):
        """Log in a user."""
        with rx.session() as session:
            # Email validation using regex
            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"            
            if re.match(email_pattern, self.username):  # Check if input is an email
                user = session.exec(
                    User.select.where(User.email == self.username)
                ).first()
            else:  # If not an email, continue using it as a username
                user = session.exec(
                    User.select.where(User.username == self.username)
                ).first()
            
            # Verify password based on is_password_hashed field
            if user:
                if user.is_password_hashed:
                    password_matches = bcrypt.checkpw(self.password.encode('utf-8'), user.password.encode('utf-8'))
                else:
                    password_matches = self.password == user.password
                    # If the plain password matches, hash it and store the hashed version
                    if password_matches:
                        hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
                        user.password = hashed_password.decode('utf-8')
                        user.is_password_hashed = True
                        session.commit()

                if password_matches:
                    self.user = user
                    self.english_chat()
                    return rx.redirect("/chat")
            
            return rx.window_alert("Invalid username or password.")

            
    def delete_user(self):
        """Delete the current user's profile."""
        with rx.session() as session:
            # Assuming the user object is set in the state during login
            if self.user:
                session.delete(self.user)
                session.commit()
                
                # Reset user state (optional based on your application's needs)
                self.user = None
                self.username = ''
                self.email = ''
                self.password = ''
                self.confirm_password = ''

                # Notify the user and redirect
                rx.window_alert("Your profile has been deleted.")
                return rx.redirect("/")
            else:
                return rx.window_alert("User not found or not logged in.")