from nlp_object.text_loader import TextLoader

# Hello World
print("Hello world")

print("Hello c'est Solene")
print("Hello, c'est Olivier !")

# NLP Tasks
my_text_loader = TextLoader(name="Titi")
print(my_text_loader.name)
print(my_text_loader.load_txt("data/my_first_file.txt"))
print(my_text_loader.load_csv("data/text_light.csv").head())

