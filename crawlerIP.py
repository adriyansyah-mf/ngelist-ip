from shodan import Shodan
import requests
api = Shodan('API KEY SHODAN')
keyword = input("Masukan List : ")
output = open("ip.txt","a")

with open(keyword, "r") as list_file:
    for line in list_file:
        word = line.strip()
        results = api.search(word)
        for result in results['matches']:
                ip = format(result['ip_str'])+'\n'
                
                print(ip)
                output.write(ip)
