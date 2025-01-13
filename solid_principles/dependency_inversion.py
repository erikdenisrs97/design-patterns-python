class EmailService:
    def send_email(self, message, receiver):
        print(f"Email sent to {receiver} with message: {message}")

class SmsService:
    def send_sms(self, message, receiver):
        print(f"SMS sent to {receiver} with message: {message}")

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()

    def send_notification(self, message, receiver, method):
        if method == "email":
            self.email_service.send_email(message, receiver)
        if method == "sms":
            self.sms_service.send_sms(message, receiver)

# Solution

from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass

class EmailService(IMessageService):
    def send(self, message, receiver):
        print(f"Email sent to {receiver} with message: {message}")

class SmsService(IMessageService):
    def send(self, message, receiver):
        print(f"SMS sent to {receiver} with message: {message}")

class NotificationService:
    def __init__(self, message_service: IMessageService):
        self.message_service = message_service

    def send_notification(self, message, receiver):
        self.message_service.send(message, receiver)