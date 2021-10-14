

#creates an html file
f = open("webpagegenerator.html", "x")
f.write("Stay tuned for our amazing summer sale!")
f.close()

import webbrowser
url = 'webpagegenerator.html'
webbrowser.open(url, new=2) #open in a new tab

