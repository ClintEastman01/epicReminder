from requests_html import HTMLSession
session = HTMLSession()

# This is just a simple webscraper that grabs the free games currently available in the epic store

url = 'https://www.epicgames.com/store/en-US/free-games'

r = session.get(url)
r.html.render(sleep=1, keep_page=True)

def GetFreeGames():
    bothFreeGames = r.html.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div')
    # freeNow = r.html.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div/div[1]/div/div/a/div/div/div[3]/span[1]/div')
    # freeNowEndDate = r.html.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div/div[1]/div/div/a/div/div/div[3]/span[2]/div')
    # comingSoon = r.html.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div/div[2]/div/div/a/div/div/div[3]/span[1]/div')
    # comingSoonDate = r.html.xpath('//*[@id="dieselReactWrapper"]/div/div[4]/main/div[3]/div/div/div/div/div[2]/span/div/div/section/div/div[2]/div/div/a/div/div/div[3]/span[2]/div')
    # print(freeNow[0].text)
    # print(freeNowEndDate[0].text)
    # print()
    # print(comingSoon[0].text)
    # print(comingSoonDate[0].text)

# Prints the same output just in a loop
    for item in bothFreeGames:
        print(item.text)

GetFreeGames()