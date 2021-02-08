class Hero:

    def __init__(self, name):
        self.health_pool = [0, 100, 200, 300, 400, 500]
        self.attPower_pool = [0, 10, 20, 30, 40, 50]
        self.armor_pool = [0, 1, 2, 3, 4, 5]
        self._name = name
        self._exp = 0
        self._level = 0

    def showInfo(self):
        print('{} \n\tlevel: {}\n\thealth: {} \n\tattPower: \n\tArmor: {}'.format(
                self._name,
                self._level,
                self._health,
                self._attPower,
                self._armor
            )
        )