# 이메일을 보내기 위한 smtplib 모듈을 import 한다
import smtplib

# 이메일을 보내기 위한 email 모듈을 import 한다
# MIME (Multipurpose Internet Mail Extensions) 는 전자우편을 위한 인터넷 표준이라고 한다.
from email.mime.text import MIMEText

# 텍스트 문서로 구성되어 있는 파일을 읽는다.
# 여기서는 텍스트 파일이 ASCII  문자로만 구성되어 있다고 가정한다.
#fp = open(textfile, 'rb')

# utf-8로 인코딩 된 파일을 읽고자 하는 경우
# import codecs
# fp = codecs.open(textfile, 'rb', 'utf-8')
# 로 읽어들이면 될 듯 하다.

# 읽어들인 파일의 텍스트를 MIME 형식으로 바꾼다.
msg = MIMEText("Test")

me  = 'quntachi03@gmail.com'
you = 'lyricia01@gmail.com'
msg['Subject'] = 'The contents of test'  # 이메일 제목
msg['From'] = me
msg['To'] = you

# 로컬 SMTP 서버를 사용해서 메세지를 보낸다.
# 이 예제에서는 Header 는 추가하지 않는다.


# 로컬 SMTP 서버가 없을 경우 계정이 있는 다른 서버를 사용하면 된다.
s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
s.login("quntachi03@gmail.com", "asdiop120")
s.sendmail(me, you, msg.as_string())
s.quit()
