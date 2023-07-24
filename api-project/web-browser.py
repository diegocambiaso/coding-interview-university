import webbrowser

url = "https://pixelcoblog.com/"

try:
    webbrowser.open("https://pixelcoblog.com")
except webbrowser.Error:
    print("Error open the URL")