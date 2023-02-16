class User:
   def __init__(self, mail, idd):
      self.mail = mail
      self.__id = idd

   def wyswietl_id(self):
      print(self.__id)

   def zmien_id(self, nowe_id):
      print('Sprawdzam, czy nowe ID dostepne')
      self.__id = nowe_id


class Date:
   def __init__(self, dzien, miesiac, rok):
      self.__dzien = dzien
      self.__miesiac = miesiac
      self.__rok = rok
      self.__dzien_tygodnia = None

   def zmien_date(self, nowy_dzien, nowy_miesiac, nowy_rok):
      print('sprawdza, czy data poprawna')
      self.__dzien = nowy_dzien
      self.__miesiac = nowy_miesiac
      self.__dzien = nowy_rok

   def __str__(self):
      return f'Dzien to {self.__dzien}.....'