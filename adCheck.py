import http.client
print("ଲ(ⓛ ω ⓛ)ଲ W33BC@T TECHNOLOGIES PRESENTS")
target = input('Type URI of a target: ')
attempts = ['/admin', '/administrator', '/login', '/enter', '/panel',
 '/admin.php', '/administrator.php', '/login.php', 'enter.php',
 '/wp-login.php', '/wp-admin']
successful = []
i = 0
for i in attempts:
 conn = http.client.HTTPConnection(target)
 conn.request("GET", i)
 send = conn.getresponse()
 status = send.status
 print("Trying " + i + ": " + str(status))
 data1 = send.read()
 if status == 200:
  print('Successful attempt. Possible admin page location: ' + target + i)
  successful.append(target + i)
print('Successfull attempts: ' + successful[0])