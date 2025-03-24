import smtplib


sender='pythonanytime@gmail.com'
recipient='mlathkar@gmail.com'
header='To:'+recipient+'\n'+'From:'+sender+'\n'+'subject:testmail\n'
content="Hello World"

whole_email = header+content
print(whole_email)
print("\n\n\n")

mail=smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('pythonanytime@gmail.com','m15v5l61')
mail.sendmail(sender, recipient, whole_email)
mail.close()

#Before running above script, sender's gmail account must be configured to allow 'less secure apps'. Visit following link.

#https://myaccount.google.com/lesssecureapps
