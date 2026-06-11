
import webbrowser
import os

file_path = os.path.abspath("car.html")
webbrowser.open("file://" + file_path)

print("Calculator opened in browser.")
