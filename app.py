from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


# --------------------------------------------------------------
# 👉 THIS is where your existing command-line program's logic goes.
# Take whatever you currently do with input()/print() and turn it
# into a plain function that takes arguments and RETURNS a result
# instead of printing it.
#
# Example placeholder below — replace with your real logic.
# --------------------------------------------------------------
def run_my_program():#user_text: str) -> str:
    
    #if not user_text.strip():
        #return "Would you want to see your fortune? ✨"
    
    fortune = ["Something Big is coming your way!", "look out for a blue butterfly!", "Everything you want is right around the corner!",
               "A surprise is waiting for you", "You will meet someone important today", "Your next random decision will change something!",
              "A little surprise is looking for you.", "The answer will arrive unexpectedly.", "Trust the strange little feeling."
              , "A small yes will lead somewhere interesting.", "The moon knows. You'll find out.", "The person you least expect knows more than they say.",
              "Look around. Maybe they're already there.", "Almost there.", "Choose differently.", "The answer is hiding in plain sight.",
              "Someone's heart has already noticed yours.", "The thing you're waiting for is moving.", "Follow the tiny coincidence.",
              "Trust the strange little feeling", "Take the long way this time.", "Love may arrive disguised as coincidence.", "Keep wondering.", "It begins.",
              "Something unexpected begins on an ordinary day.", "A door you forgot about is still open.", "A small yes will lead somewhere interesting.",
              "Someone is secretly rooting for you.", "The person you least expect knows more than they say.", "Take the long way this time."]
    return random.choice(fortune)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/run", methods=["POST"])
def run():
    #data = request.get_json()
    #user_text = data.get("text", "")
    result = run_my_program()
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
