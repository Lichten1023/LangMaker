from Module.SoftwareName import SoftwareInfo
from Module.LoadLibrary import LoadLibrary, RefreshGrammarDictionaly

def Boot():
    print("Welcome to " + str(SoftwareInfo()) + ".")
    LoadLibrary()
    print("Boot completed.")