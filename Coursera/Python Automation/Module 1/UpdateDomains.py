def replace_domain(email,old_domain,new_domain):
    
    if "@" + old_domain in email: #checks wether email has @ and old domian name
        index = email.index("@" + old_domain) #get the index of the old domin 
        new_email = email[:index] + "@" + new_domain #create new string with username and new domin
        return new_email

    return email