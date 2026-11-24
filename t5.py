#завдання 5. паттерн проектування (observer / спостерігач)

from abc import ABC, abstractmethod


#абстрактний спостерігач (інтерфейс підписника)
class Subscriber(ABC):
    @abstractmethod
    def update(self, news_headline):
        pass


#конкретний спостерігач 1
class EmailSubscriber(Subscriber):
    def __init__(self, email):
        self.email = email

    def update(self, news_headline):
        print(f"лист на {self.email}: свіжа новина - {news_headline}")


#конкретний спостерігач 2
class TelegramSubscriber(Subscriber):
    def __init__(self, username):
        self.username = username

    def update(self, news_headline):
        print(f"повідомлення в tg {self.username}: {news_headline}")


#видавець (subject), який розсилає новини
class NewsPortal:
    def __init__(self):
        #список усіх підписників
        self._subscribers = []
        self._latest_news = ""

    def subscribe(self, subscriber):
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def notify_all(self):
        #сповіщаємо всіх підписників
        for sub in self._subscribers:
            sub.update(self._latest_news)

    def publish_news(self, news_headline):
        self._latest_news = news_headline
        self.notify_all()


#розширення: додаємо нового спостерігача (sms) без зміни існуючого коду порталу чи інших класів
class SmsSubscriber(Subscriber):
    def __init__(self, phone):
        self.phone = phone

    def update(self, news_headline):
        print(f"sms на {self.phone}: {news_headline}")


def main():
    portal = NewsPortal()

    sub1 = EmailSubscriber("test@mail.com")
    sub2 = TelegramSubscriber("@user123")

    print("1. базова взаємодія:")
    portal.subscribe(sub1)
    portal.subscribe(sub2)
    portal.publish_news("вийшов новий реліз python")

    print("\n2. демонстрація розширюваності:")
    #додаємо нового підписника взагалі не чіпаючи код самого порталу
    sub3 = SmsSubscriber("+380991234567")
    portal.subscribe(sub3)
    portal.publish_news("додано підтримку нових типів даних")


if __name__ == "__main__":
    main()