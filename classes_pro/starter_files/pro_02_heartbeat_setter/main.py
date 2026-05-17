from heart import Heart

def main():
    heart = Heart(70)
    print(heart.heartbeat)
    heart.heartbeat = 85
    print(heart.heartbeat)
    # heart.heartbeat = -10

if __name__ == "__main__":
    main()
