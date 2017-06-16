def SendEmail(data, type):
    import smtplib
    from email.mime.text import MIMEText



    msg = MIMEText("Test")

    me  = 'quntachi03@gmail.com'
    you = 'lyricia01@gmail.com'
    msg['Subject'] = 'The contents of test'  # 이메일 제목
    msg['From'] = me
    msg['To'] = you

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login("quntachi03@gmail.com", "asdiop120")
    s.sendmail(me, you, msg.as_string())
    s.quit()

    return True
