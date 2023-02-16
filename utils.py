from chatgpt_wrapper import ChatGPT

def main():
    bot = ChatGPT()
    response = bot.ask("Hello")
    print(response)

if __name__ == "__main__":
    main()