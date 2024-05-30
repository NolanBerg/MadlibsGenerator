with open("story.txt", "r") as f:
    story = f.read()

words = set()
start = -1

for i, char in enumerate(story):
    if char == "<":
        start = i

    if char == ">" and start != -1:
        word = story[start: i + 1]
        words.add(word)
        start = -1

answers = {}
print("\n")

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(f"\n{story}")