# URL1 = "https://www.cricbuzz.com/"
# URL2 = "https://www.cricbuzz.com/live-cricket-scores/38276/1st-match-icc-cricket-world-cup-league-two-2019-22"
# URL3 = "https://www.cricbuzz.com/live-cricket-scores/38276/1st-match-icc-cricket-world-cup-league-two-2019-22"
# URL = "https://www.naukri.com/spring-boot-developer-java-developer-jobs-in-gurgaon-gurugram?k=spring%20boot%20developer%2C%20java%20developer&l=gurgaon%2Fgurugram%2C%20bangalore%2Fbengaluru%2C%20noida"
# page = requests.get(URL)
# html_doc = """<html><head><title>Welcome  to geeksforgeeks</title></head>
# <body>
# <p class="title"><b>Geeks</b></p>
#
#
# <p class="body">geeksforgeeks a computer science portal for geeks
# </body>
# """
# headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OSX 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko)"
#                          "Chrome/71.0.3578.98 Safari/537.36",
#            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
# soup = BeautifulSoup(page.content, "html.parser")
# print(page.text)
# result = soup.find(class_="list").getText();
# print(result)