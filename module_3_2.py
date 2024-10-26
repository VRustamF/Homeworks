def send_email(message, recipient, sender = "university.help@gmail.com"):
    if ("@" in sender) and ("@" in recipient):
            if ((".com" in sender or ".ru" in sender or ".net" in sender)
                    and (".com" in recipient or ".ru" in recipient or ".net" in recipient)):
                if sender == recipient:
                    print("Нельзя отправить письмо самому себе!")
                    return None
                if sender != "university.help@gmail.com":
                    print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", sender, "на адрес", recipient + ".")
                    return None
                print("Письмо успешно отправлено с адреса", sender, "на адрес", recipient + ".")
                return None
    print("Невозможно отправить письмо с адреса", sender, "на адрес", recipient + ".")
    return None
