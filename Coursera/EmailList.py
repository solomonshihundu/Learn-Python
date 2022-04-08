def full_mails(people):
    result = []
    for email,name in people:
        result.append("{} <{}>".format(name,email))
    return result

print(full_mails([("s@gmail.com","Solomon"),("jk@gmail.com","Jonny Kage")]))
