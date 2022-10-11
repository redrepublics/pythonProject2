#мпорn класса из Feline
from Feline import Pet

#карточки для вывода
pet_1 = Pet("собака", "Феликс", "мальчик", 2)
pet_2 = Pet("собака", "Мухтар", "мальчик", 1)
pet_3 = Pet("кот", "Сэм", "мальчик", 2)
pet_4 = Pet("попугай", "Гоша", "мальчик", 1)

#шаблоны по функциям, соединенные с краточками
print("Питомец 1: ", pet_1.getSpecies(), pet_1.getName(), pet_1.getGender(), pet_1.getAge())
print("Питомец 2: ", pet_2.getSpecies(), pet_2.getName(), pet_2.getGender(), pet_2.getAge())
print("Питомец 3: ", pet_3.getSpecies(), pet_3.getName(), pet_3.getGender(), pet_3.getAge())

