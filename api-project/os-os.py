import os

print(os.getcwd())
# os.mkdir("DJCs")
os.chdir("DJCs")
print(os.getcwd())
os.chdir("..")
print(os.getcwd())
print(os.listdir())