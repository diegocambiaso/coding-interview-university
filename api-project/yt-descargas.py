from pytube import Search

s = Search("Pixelco")
print(len(s.results))
print(s.results)
