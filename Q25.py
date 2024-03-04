import random

class QuizQuestion:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

class QuizCategory:
    def __init__(self, name, questions):
        self.name = name
        self.questions = questions

class QuizGame:
    def __init__(self, categories):
        self.categories = categories
        self.score = 0

    def display_categories(self):
        print("Categories:")
        for i, category in enumerate(self.categories, 1):
            print(f"{i}. {category.name}")

    def start_game(self):
        print("Quiz Game!")
        self.display_categories()
        category_choice = int(input("Choose category (1-3): ")) - 1

        if 0 <= category_choice < len(self.categories):
            selected_category = self.categories[category_choice]
            self.play_quiz(selected_category)
        else:
            print("Invalid category choice. Exiting the game.")

    def play_quiz(self, category):
        print(f"\n{category.name} Quiz:")
        for i, question in enumerate(category.questions, 1):
            print(f"\nQuestion {i}: {question.question}")
            for j, option in enumerate(question.options, 1):
                print(f"{j}. {option}")

            user_answer = int(input("Your answer (1-4): "))
            if user_answer == question.correct_option:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question.correct_option}.")

        print(f"\nQuiz completed! Your final score is {self.score}/{len(category.questions)}.")

questions_category1 = [
    QuizQuestion("On which continent is the Sahara Desert located?", ["Asia", "South America", "Africa", "Europe"], 3),
    QuizQuestion("How tall is Mount Everest?", ["6,849 m", "7,849 m", "8,849 m", "9,849 m"], 3),
    QuizQuestion("What is the largest mammal?", ["Elephant", "Blue Whale", "Giraffe", "Lion"], 2),
]

questions_category2 = [
    QuizQuestion("What is the main ingredient in guacamole?", ["Tomato", "Avocado", "Onion", "Cheese"], 2),
    QuizQuestion("Who among the following wrote Sanskrit grammar?'?", ["Kalidasa", "Charak", "Panini", "Aryabhatt"], 3),
    QuizQuestion(" The metal whose salts are sensitive to light is??", ["Zinc", "Silver", "Copper", " Aluminum"], 2),
]

questions_category3 = [
    QuizQuestion("What programming language is this quiz written in?", ["Java", "Python", "C++", "JavaScript"], 2),
    QuizQuestion("Which company developed the Python programming language?", ["Microsoft", "Apple", "Google", "Facebook"], 3),
    QuizQuestion("What does HTML stand for?", ["HyperText Markup Language", "High-Level Text Language", "Home Tool Markup Language", "Hyperlink and Text Markup Language"], 1),
]

category1 = QuizCategory("Geography", questions_category1)
category2 = QuizCategory("General Knowledge", questions_category2)
category3 = QuizCategory("Programming", questions_category3)

quiz_game = QuizGame([category1, category2, category3])

quiz_game.start_game()
