import random

def magic_8_ball():
    """A fun Magic 8-Ball fortune teller!"""

    responses = [
        "Yes, definitely!",
        "It is certain.",
        "Without a doubt.",
        "Most likely.",
        "Ask again later.",
        "Cannot predict now.",
        "Don't count on it.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
    ]

    print("=" * 40)
    print("  Welcome to the Magic 8-Ball!")
    print("=" * 40)
    print()

    question = input("Ask me a yes/no question: ")

    if question:
        answer = random.choice(responses)
        print()
        print(f"The Magic 8-Ball says: {answer}")
    else:
        print("You didn't ask anything!")

if __name__ == "__main__":
    magic_8_ball()
