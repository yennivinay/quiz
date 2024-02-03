

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        # print(self.q)
        self.score = 0

    def display_question(self, question_num):
        
        question = self.questions[question_num]['question']
        options = self.questions[question_num]['options']
        print(f"\n Question {question_num+1} : {question}")
        for i in range(len(options)):
            print(f"{i+1} : {options[i]}")

    def get_user_answer(self):
        while True:
            self.user_input = input("\nEnter your answer (1-4): ")
            if self.user_input.isdigit() and 1 <= int(self.user_input) <= 4:
                return int(self.user_input)
            else:
                print("Invalid input. Please enter a number between 1 and 4.")

    def check_answer(self, question_num, user_answer):
        correct_answer = self.questions[question_num]['correct']
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}: {self.questions[question_num]['options'][correct_answer - 1]}")

    def run_quiz(self):
        for i in range(len(self.questions)):
            k=self.questions[i]
            self.display_question(i)
            user_answer = self.get_user_answer()
            self.check_answer(i, user_answer)

        print(f"\nQuiz completed. Your final score: {self.score}/{len(self.questions)}")

# Example quiz

questions = [
    {
        'question': 'What is the capital of India?',
        'options': ['Berlin', 'Madrid', 'New Delhi', 'Rome'],
        'correct': 3
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Jupiter', 'Venus', 'Saturn'],
        'correct': 1
    },
    {
        'question': 'Who invented the first bulb?',
        'options': ['Thomas Edison', 'Jane Austen', 'Charles Dickens', 'Mark Twain'],
        'correct': 1
    }
]

# Create a quiz instance

quiz = Quiz(questions)

# Run the quiz
quiz.run_quiz()
