while True:
    aclNum = int(input("What is IPv4 ACL Number?"))
    if aclNum >= 1 and aclNum <= 99:
        print("This is a standard IPv4 ACL.")
    elif aclNum >= 100 and aclNum <= 199:
        print("This is a extended IPv4 ACL.")
    else:
        print("This is neither a standard nor extended IPv4 ACL5")