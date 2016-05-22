import webbrowser
import time


numberOfBreaks = 1
while numberOfBreaks <=3:
    time.sleep(5)
    webbrowser.open('http://www.google.com')
    numberOfBreaks+=1
