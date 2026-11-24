#завдання 2. інкапсуляція, property та контроль доступу

class BankAccount:
    def __init__(self, owner, initial_balance):
        self._owner = owner  # захищений атрибут
        self.__balance = initial_balance  # приватний атрибут
        self._currency = "uah"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        #перевірка на тип даних
        if not isinstance(value, (int, float)):
            raise TypeError("баланс має бути числом")
        #перевірка на додатне значення
        if value < 0:
            raise ValueError("баланс не може бути від'ємним")
        self.__balance = value

    @property
    def account_info(self):
        #обчислювана властивість (read-only)
        return f"власник: {self._owner}, поточний стан: {self.__balance} {self._currency}"


def main():
    #коректне створення екземпляра
    account = BankAccount("володимир", 1000)
    print("створено рахунок:")
    print(account.account_info)

    #зміна через setter (коректна)
    account.balance = 1500
    print(f"новий баланс: {account.balance}")

    #спроба встановити від'ємне значення
    print("\nспроба встановити від'ємний баланс:")
    try:
        account.balance = -500
    except ValueError as e:
        print(f"помилка: {e}")

    #спроба встановити текст замість числа
    print("\nспроба встановити текст замість числа:")
    try:
        account.balance = "багато"
    except TypeError as e:
        print(f"помилка: {e}")

    #спроба прямого доступу до приватного атрибута
    print("\nспроба прямого доступу до __balance:")
    try:
        print(account.__balance)
    except AttributeError as e:
        print(f"помилка доступу: {e}")

    #доступ через name mangling
    print("\nдоступ через name mangling:")
    print(f"прихований баланс: {account._BankAccount__balance}")


if __name__ == "__main__":
    main()