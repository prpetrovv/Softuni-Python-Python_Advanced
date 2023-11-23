class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class NameTooShortError(Exception):
    pass


possible_domains = ['com', 'bg', 'net', 'org']

while True:
    email = input()
    if '@' not in email:
        raise MustContainAtSymbolError('Email must contain @')
    if email.split('.')[-1] not in possible_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if len(email.split('@')[0]) < 5:
        raise NameTooShortError("Name must be more than 4 characters")
    print('Email is valid')
