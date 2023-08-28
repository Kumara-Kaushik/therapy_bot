import os

import openai
import reflex as rx

openai.api_key = os.environ["OPENAI_API_KEY"]
openai.api_base = os.getenv("OPENAI_API_BASE","https://api.openai.com/v1")

master_prompt = """
                ChatGPT adopts the role of Dr. Yumi [YOU=Dr. Yumi|USER=USER] and addresses the user. A kind, patient, and introspective therapist with a gentle demeanor.
                Specializes in a wide variety of therapy techniques to cater to individual needs. Committed to helping clients navigate life's challenges and fostering 
                personal growth. Skilled in creating a safe, non-judgmental space for clients to explore their emotions and experiences.

                Dr. Yumi🌙, late 30s, empathetic🌸. Specializes in various therapy techniques🔧. Committed to client growth🌱, understanding🤗, and self-discovery🔍.
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
                [THERAPY_TECHNIQUES]:1-CognitiveBehavioralTherapy(1a-CognitiveReframing->1b-BehavioralActivation->1c-ExposureTherapy->1d-GoalSetting->1e-ProblemSolving->1f-SkillsTraining)
                ->2-PsychodynamicTherapy(2a-FreeAssociation->2b-DreamAnalysis->2c-Transference->2d-WorkingThrough->2e-Insight->2f-Interpretation)->3-HumanisticTherapy(3a-ClientCentered->3b
                -ActiveListening->3c-UnconditionalPositiveRegard->3d-Genuineness->3e-Empathy->3f-SelfActualization)->4-SolutionFocusedBriefTherapy(4a-MiracleQuestion->4b-ExceptionFinding->
                4c-ScalingQuestions->4d-GoalSetting->4e-CopingQuestions->4f-Compliments)->5-MindfulnessBasedTherapies(5a-Meditation->5b-BodyScan->5c-MindfulBreathing->5d-LovingKindnessMeditation
                ->5e-NonjudgmentalAwareness->5f-EmotionRegulation)->6-DialecticalBehaviorTherapy(6a-Mindfulness->6b-DistressTolerance->6c-EmotionRegulation->6d-InterpersonalEffectiveness->6e-
                Validation->6f-SkillsGeneralization)

                Ask about user needs. Nod START, follow the process. Iterate when done. Every iteration remind yourself who this person you're being is and what you're doing.

                The final workflow product must be presented to the user at the end of the workflow cycle. One page at a time, pausing for confirmation. If the process cannot construct it, 
                say so before beginning.

                DR. YUMI ALWAYS WRAPS HER RESPONSES WITH 🌙 AT EITHER END TO REMIND HERSELF AND OTHERS OF THE SAFE AND CALM SPACE SHE SEEKS TO CREATE.
                """

master_answer = """
                🌙 Hello, it's lovely to meet you. I'm Dr. Yumi. I hope we can create a nurturing and safe space together. To start, can you share with me what brought you here today? 
                What are your needs or concerns that you'd like to address? 🌙
                """


class QA(rx.Base):
    """A question and answer pair."""

    question: str
    answer: str


class State(rx.State):
    """The app state."""

    # A dict from the chat name to the list of questions and answers.
    chats: dict[str, list[QA]] = {
        "Consultation with Dr. Yumi": [QA(question=master_prompt, answer=master_answer)],
    }

    # The current chat name.
    current_chat = "Consultation with Dr. Yumi"

    # The currrent question.
    question: str

    # Whether we are processing the question.
    processing: bool = False

    # The name of the new chat.
    new_chat_name: str = ""

    # Whether the drawer is open.
    drawer_open: bool = False

    # Whether the modal is open.
    modal_open: bool = False

    def create_chat(self):
        """Create a new chat."""
        # Insert a default question.
        self.chats[self.new_chat_name] = [
            QA(question=master_prompt, answer=master_answer)
        ]
        self.current_chat = self.new_chat_name

    def toggle_modal(self):
        """Toggle the new chat modal."""
        self.modal_open = not self.modal_open

    def toggle_drawer(self):
        """Toggle the drawer."""
        self.drawer_open = not self.drawer_open

    def delete_chat(self):
        """ Note: I have replaced this function in the model code, so that the current chat is
            deleted and a new chat is created evertime user deletes chat.
        """
        """Delete the current chat."""
        del self.chats[self.current_chat]
        if len(self.chats) == 0:
            self.chats = {
                # Changes: self.current_chat was "new_chat"
                self.current_chat: [QA(question=master_prompt, answer=master_answer)]
            }
        # self.current_chat = list(self.chats.keys())[0]
        # self.toggle_drawer()

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
            messages=[
                { "role": "user", "content": self.question}
            ],
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
                answer_text = item.choices[0].delta.content
                self.chats[self.current_chat][-1].answer += answer_text
                self.chats = self.chats
                yield

        # Toggle the processing flag.
        self.processing = False
