def main():
    pass

def print_news(di, formatter):
    counter = 1
    for i in di.items():
        print(f"{counter}. {i[0]}: {i[1]}", end=formatter)
        counter += 1

if __name__ == "__main__":
    main()