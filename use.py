from romanRekhta.preprocessing import Preprocessor
from romanRekhta.stopwords import StopwordHandler
from romanRekhta.tokenizer import word_tokenize, sentence_tokenize


# Default settings (lowercase, remove punctuation and emojis, normalize space)
p = Preprocessor()

text = "Apka service lajawab hai! 😍🔥"
print(p.process(text))  
# Output: "apka service lajawab hai"

# Replace emojis with text
p2 = Preprocessor(emoji_handling="replace")
print(p2.process(text))  
# Output: "apka service lajawab hai smiling_face_with_heart_eyes fire"

# Skip punctuation removal
p3 = Preprocessor(punctuation=False)
print(p3.process("Ye... boht~ acha!"))
# Output: "ye... boht~ acha"

stop_handler = StopwordHandler(filepath="stopwords.txt")

tokens = ["ye", "bohat", "acha", "kaam", "hai"]
filtered = stop_handler.remove_stopwords(tokens)

print(filtered)  # Output: ['ye', 'bohat', 'acha', 'kaam']

# Your custom list of Roman Urdu stopwords
custom_words = {"mera", "tumhara"}

# Create handler using only the custom set
stop_handler = StopwordHandler(custom_stopwords=custom_words)

tokens = ["ye", "mera", "bohat", "acha", "kaam", "nahi"]
filtered = stop_handler.remove_stopwords(tokens)

print(filtered)  
# Output: ['ye', 'bohat', 'acha', 'kaam']

stop_handler = StopwordHandler(
    filepath="stopwords.txt",
    custom_stopwords={"nahi", "kya"}
)
tokens = ["ye", "nahi", "kya", "acha", "kaam"]
filtered = stop_handler.remove_stopwords(tokens)

print(filtered)  
# Output: ['ye', 'acha', 'kaam']

text = "Yeh idea bohat acha hai. Shukriya!"

words = word_tokenize(text)
sentences = sentence_tokenize(text)

print(words)      # ['Yeh', 'idea', 'bohat', 'acha', 'hai', 'Shukriya']
print(sentences)  # ['Yeh idea bohat acha hai', ' Shukriya']
