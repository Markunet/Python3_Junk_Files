import dns.resolver

result = dns.resolver.query('google.com', 'A')

print(type(result))

for ipval in result:
    print('IP', ipval.to_text())

