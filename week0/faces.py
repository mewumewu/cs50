def convert(message: str):
    message = message.replace(":)", "🙂")
    message = message.replace(":(", "🙁")
    return message

def main():
    print(convert(input("Message: ")))

if __name__ == "__main__":
    main()
