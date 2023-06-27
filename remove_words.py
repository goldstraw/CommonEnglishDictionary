if __name__ == "__main__":
    with open("words.txt", "r") as f:
        words = f.readlines()
    
    words = [word.strip() for word in words]

    print("Please enter a word to remove from the list. Enter \"quit\" to quit.")

    count = 0
    while (word := input("Word: ")) != "quit":
        w = word.lower()
        if w in words:
            words.remove(w)
            print(f"Removed {w} from the list.")
            count += 1
        else:
            print(f"{w} is not in the list.")

    with open("words.txt", "w") as f:
        f.write("\n".join(words))

    print(f"Successfully removed {count} words from the list.")
    print("Please remember to commit and push your changes to GitHub.")
