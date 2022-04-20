def email_list(domains):
    emails = []
    for domain,users in domains.items():
        for user in users:
          new_mail = user + "@" + domain
          emails.append(new_mail)
	
    return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))