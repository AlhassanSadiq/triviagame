# trivia_game.py
import requests
import html

def display_question(question):
    print(html.unescape(question["question"]))  # Unescape HTML entities
    for i, option in enumerate(question["incorrect_answers"], 1):
        print(f"{i}. {html.unescape(option)}")
    print(f"{len(question['incorrect_answers']) + 1}. {html.unescape(question['correct_answer'])}")

def get_trivia_questions(amount):
    base_url = "https://opentdb.com/api.php"
    params = {
        'amount': amount,
        'type': 'multiple'  # Multiple-choice questions
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        trivia_data = response.json()
        return trivia_data['results']
    else:
        print(f"Error fetching trivia questions. Status Code: {response.status_code}")
        return None

def quiz_game():
    amount = 3  # Number of questions

    trivia_questions = get_trivia_questions(amount)

    if not trivia_questions:
        print("Exiting Quiz Game.")
        return

    score = 0

    print("Welcome to the Trivia Quiz Game!\n")

    for question in trivia_questions:
        display_question(question)

        user_answer = input("Your answer (enter the option number): ")

        if user_answer.isdigit() and 1 <= int(user_answer) <= len(question["incorrect_answers"]) + 1:
            user_answer = html.unescape(question["incorrect_answers"][int(user_answer) - 1])

            if user_answer.lower() == html.unescape(question["correct_answer"]).lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {html.unescape(question['correct_answer'])}.")
        else:
            print("Invalid input. Skipping this question.")

    print(f"\nQuiz completed! Your final score is: {score}/{amount}")

if __name__ == "__main__":
    quiz_game()
