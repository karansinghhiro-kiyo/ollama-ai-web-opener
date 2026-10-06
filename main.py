import ollama 
import webbrowser

while True:

    user_input = input("Hello sir which website do you want to open (type 'exit' to quit): ")


    if user_input.lower() == "exit":
        user_input = "exit"
        print("Exiting the program. Goodbye!")
        break


    if user_input.lower() == "open youtube":
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif user_input.lower() == "open google":
        print("Opening Google...")
        webbrowser.open("https://www.google.com")   

    elif user_input.lower() == "open facebook":
        print("Opening Facebook...")    
        webbrowser.open("https://www.facebook.com") 

    elif user_input.lower() == "open kick":
        print("Opening Kick...")
        webbrowser.open("https://www.kick.com") 

    elif user_input.lower() == "open twitter":
        print("Opening Twitter...")
        webbrowser.open("https://www.twitter.com") 

    elif user_input.lower() == "open instagram":
        print("Opening Instagram...")
        webbrowser.open("https://www.instagram.com") 

    else:
        print("Sorry, I don't recognize that website.")

response = ollama.chat(
    model="gemma3:1b",
    messages=[
        {
            "role": "user",
            "content": user_input
        }
    ]
)