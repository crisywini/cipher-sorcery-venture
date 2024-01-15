import os 

def analyze_java_version(path: str) -> str:
    """This function analyzes de java version of a gradle project"""

    if os.path.exists(path) ==  False:
        raise Exception("The provided path does not exists!")
        

    return "OK"