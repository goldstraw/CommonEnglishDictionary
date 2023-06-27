if __name__ == "__main__":
    with open("words.txt", "r") as f:
        words = f.readlines()
    
    words = [word.strip() for word in words]

    print("Please enter a word to add to the list. Enter \"quit\" to quit.")

    count = 0
    while (word := input("Word: ")) != "quit":
        w = word.lower()
        if w in words:
            print(f"{w} is already in the list.")
        else:
            words.append(w)
            print(f"Added {w} to the list.")
            count += 1

    with open("words.txt", "w") as f:
        f.write("\n".join(words))

    print(f"Successfully added {count} words to the list.")
    print("Please remember to commit and push your changes to GitHub.")
