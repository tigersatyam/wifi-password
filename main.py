import subprocess


data = subprocess.check_output(['ntesh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')

pfofiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]


for i in profiles:

    results = subprocess.check_output(['ntesh','wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

    try:
        print ("{:<30}| {:<}".format(i, results[0]))
    except IndexError:
        print ("{:<30}| {:<}".format(i, ""))