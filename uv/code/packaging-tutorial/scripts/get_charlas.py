import packaging_tutorial.pycon as pycon

try:
    from rich import print
except ImportError:
    pass


sessions = pycon.get_sessions()
charlas = (session for session in sessions if session.kind == "charla")
print("Charlas:")
print("========\n")
for charla in charlas:
    print(charla.name, charla.start)
