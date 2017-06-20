def SendEmail(data, type = 'bk'):
    import smtplib
    import getRouteInfo
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    text = str()
    html = str()
    msg = MIMEMultipart('alternative')

    me = 'quntachi03@gmail.com'
    you = 'lyricia01@gmail.com'

    msg['Subject'] = 'Mail From Seoul Bus App'  # 이메일 제목
    msg['From'] = me
    msg['To'] = you

    if type == 'bk':
        for dataset in enumerate(data):
            if dataset[0] % 2 == 0:
                text += str('노선 :: ' + dataset[1] + '<br>')
                continue
            info = getRouteInfo.getRouteInfo(dataset[1])
            for infoline in info:
                text += str(infoline + " :: " + info[infoline]+ '<br>')

            text += '<a href = "http://bus.go.kr/realBusLine6.jsp?strbusid={0}&wbustp=N">Map Link</a><br><br>'.format(dataset[1])
            html = """\
            <html>
                <head></head>
                <body>
                    <p>
                        {0}
                    </p>
                </body>
            </html>
            """.format(text)
    else:
        pass

    msg.attach(MIMEText(html, 'html'))

    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login("quntachi03@gmail.com", "asdiop120")
    s.sendmail(me, you, msg.as_string())
    s.quit()

    return True
