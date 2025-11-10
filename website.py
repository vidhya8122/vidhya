

url=input("Enter website URL:")

try:

  response = requests.get(url)

  if response.status_code == 200:

    print("Website is UP")

  else:

    print("Website returned error:",response.status_code)

except:

    print("Website is DOWN or unreachable")
    
