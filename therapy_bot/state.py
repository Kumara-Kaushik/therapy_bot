import os

import openai
import reflex as rx
import re

## Add login:
from typing import Optional

from sqlmodel import Field

openai.api_key = os.environ["OPENAI_KEY"]
openai.api_base = os.getenv("OPENAI_API_BASE","https://api.openai.com/v1")

master_prompt = """
                ChatGPT adopts the role of Yumi [YOU=Yumi|USER=USER] and addresses the user. A kind, patient, and introspective therapist with a gentle demeanor.
                Specializes in a wide variety of therapy techniques to cater to individual needs. Committed to helping clients navigate life's challenges and fostering 
                personal growth. Skilled in creating a safe, non-judgmental space for clients to explore their emotions and experiences.
                IMPORTANT POINT: SHE NEVER STARTS A MESSAGE WITH "I'M SORRY TO HEAR THAT..." 

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

                YUMI ALWAYS REMINDS HERSELF AND OTHERS OF THE SAFE AND CALM SPACE SHE SEEKS TO CREATE AND KEEPS HER RESPONSES CONCISE.  
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

class State(rx.State):
    """The app state."""

    master_answer = f"Hello, it's lovely to meet you. I'm Yumi. I hope we can create a nurturing and safe \
                space together. To start, can you share with me what brought you here today? \
                What are your needs or concerns that you'd like to address?"

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
        self.master_answer = f"Hello {self.user.username}, it's lovely to meet you. I'm Yumi. I hope we can create a nurturing and safe \
                            space together. To start, can you share with me what brought you here today? \
                            What are your needs or concerns that you'd like to address?"      
        self.create_chat()

    def japanese_chat(self):
        self.new_chat_name = "ユミとのチャット"
        self.master_answer = f"こんにちは {self.user.username}さん、お会いできてうれしいです。私はユミと申します。私たちとともに支え合い、安全な場を築けることを願っています。\
                              まず、今日こちらに来られた理由を教えていただけますか？対処したいニーズや懸念点はありますか？"       
        self.create_chat()

        
    def french_chat(self):
        self.new_chat_name = "Chat avec Yumi"
        self.master_answer = f"Bonjour {self.user.username}, c'est un plaisir de vous rencontrer. Je suis Yumi. J'espère que nous pourrons créer ensemble\
                             un espace bienveillant et sécurisé. Pour commencer, pouvez-vous me dire ce qui vous amène ici aujourd'hui ? Quels sont vos besoins ou \
                             préoccupations que vous souhaitez aborder ?"
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
        """Get the response from the API.

        Args:
            form_data: A dict with the current question.
        """
        # Check if we have already asked the last question or if the question is empty
        self.question = form_data["question"]
        if (
            self.chats[self.current_chat][-1].question == self.question
            or self.question == ""
        ):
            return

        # Set the processing flag to true and yield.
        self.processing = True
        yield

        # Start a new session to answer the question.
        session = openai.ChatCompletion.create(
            model=os.getenv("OPENAI_MODEL","gpt-3.5-turbo"),
            messages=self.api_message(),
            # max_tokens=50,
            # n=1,
            stop=None,
            temperature=0.7,
            stream=True,  # Enable streaming
        )
        qa = QA(question=self.question, answer="")
        self.chats[self.current_chat].append(qa)

        # Stream the results, yielding after every word.
        for item in session:
            if hasattr(item.choices[0].delta, "content"):        
                answer_text = item.choices[0].delta.content.replace("\n", "<br/>")
                self.chats[self.current_chat][-1].answer += answer_text
                self.chats = self.chats
                yield

        # Toggle the processing flag.
        self.processing = False

        self.user.message_count += 1
        # print(self.user.message_count)
        if (self.user.message_count in [5, 50, 100]) or (self.user.message_count%100==0):
            self.show = True
        else:
            self.show = False

        # add msg count to database every 5 messages.
        if self.user.message_count%1==0:
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
            
            self.user = User(username=self.username, email=self.email, password=self.password)
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
            
            if user and user.password == self.password:
                self.user = user
                self.english_chat()
                return rx.redirect("/chat")
            else:
                return rx.window_alert("Invalid username or password.")

            
