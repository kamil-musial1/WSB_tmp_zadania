class KontoBankowe:
    def __init__(self):
        self.__stan = 0
        self.plec = 'k'

    def __del__(self):
        pass

    def __str__(self):
        return 'info powitalne'

    def __eq__(self, other):
        return self.plec == other.plec and self.__stan > other.__stan + 1

    def __add__(self, other):
        if self.plec == other.plec:
            return self.__stan + other.__stan
        else:
            return max(self.__stan, other.__stan)

    @property
    def stan_konta(self):
        return self.__stan

    @stan_konta.getter
    def stan_konta(self):
        return 'stan konta: '+ str(self.__stan) + 'zl'

    @stan_konta.setter
    def stan_konta(self, value):
        self.__stan += value

    @stan_konta.deleter
    def stan_konta(self):
        del self.__stan

konto = KontoBankowe()
print(konto.stan_konta)
konto.stan_konta = 50
print(konto.stan_konta)

konto2 = KontoBankowe()
konto2.stan_konta = 80
konto2.plec = 'm'
print(konto + konto2)