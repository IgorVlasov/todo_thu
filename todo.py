#импорт библиотек



TOKEN = ""

HELP = """
help  - вывод списка команд
add   - добавление задачи
show  - показать все задачи
done  - задача выполнена
"""
todo = {}

print("Привет! Введи команду help для вывода списка команд")

while True:
  userAnswer = input("Введите команду:\n")

  if userAnswer == "add":
    print("Работает!")
  elif userAnswer == "help":
    print("Работает!")
  elif userAnswer == "show":
    print("Работает!")
  elif userAnswer == "done":
    print("Работает!")
  elif userAnswer == "exit":
    print("Работает!")
  else:
    print("Error. Нет такой команды")
    print("Введиет help для вывода списка команд")