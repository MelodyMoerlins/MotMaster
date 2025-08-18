import pandas as pd

# from flask import Flask, render_template, request, jsonify
# from MAIN import translate  # your logic here

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/analyze', methods=['POST'])
# def analyze():
#     data = request.get_json()
#     text = data.get('text')
#     level = data.get('level')
#     result = translate(text, level)  # Your own logic here
#     return jsonify(result)

# if __name__ == '__main__':
#     app.run(debug=True)




lexique_df = pd.read_csv("Lexique383.tsv", sep="\t")
sorted_lexique = lexique_df.sort_values(by="freqfilms2", ascending=False)
all_words = sorted_lexique["ortho"].tolist()

a1_count = 500
a2_count = 1000
b1_count = 2000
b2_count = 4000
c1_count = 8000
c2_count = 16000

beginner = all_words[:a1_count]
a1_words = all_words[a1_count:a2_count]
a2_words = all_words[a2_count:b1_count]
b1_words = all_words[b1_count:b2_count]
b2_words = all_words[b2_count:c1_count]
c1_words = all_words[c1_count:c2_count]
c2_words = all_words[c2_count:]

def translate(texts):
    from transformers import MarianMTModel, MarianTokenizer    
    
    model_name = 'Helsinki-NLP/opus-mt-fr-en'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)

    batch = tokenizer(texts, return_tensors = "pt", padding = True)
    generated_ids = model.generate(input_ids=batch['input_ids'], attention_mask = batch['attention_mask'])
    translations = tokenizer.batch_decode(generated_ids, skip_special_tokens = True)
    return translations

french_text = input("copy paste your diaglogue here: ")
cefr_level = input("What is your CEFR level? We will give you vocabulary from the script currated to your level. If you know no words, please type 'beginner': ").lower()

match cefr_level:
    case "beginner":
        pass
    case "a1":
        pass
    case "a2":
        pass
    case "b1":
        pass
    case "b2":
        pass
    case "c1":
        pass
    case "c2":
        pass
    case _:
        cefr_level = input("please choose a CEFR standard level, such as A1 or B2: ").lower()

english_texts = translate(french_text)

#prints full translation
for fr, en in zip(french_text, english_texts):
    print("---")
    print(f"FR: {french_text}")
    print(f"EN: {en}")
    print("---")

#prints the vocab sheet and cefr levels
def vocab(text):
    global a1_words, a2_words, b1_words, b2_words, c1_words, c2_words
    for word in text.split():
        word.strip()
        if word in a1_words:
            level = "a1"
        elif word in a2_words:
            level = "a2"
        elif word in b1_words:
            level = "b1"
        elif word in b2_words:
            level = "b2"
        elif word in c1_words:
            level = "c1"
        elif word in c2_words:
            level = "c2"
        elif word in beginner:
            level = "beginner"
        else:
            level = "unknown"
        
        if level == cefr_level:
            definition = str(translate(word))
            definition = definition[2:-2]
            print(word + ": " + definition)

vocab(french_text)
print("---")