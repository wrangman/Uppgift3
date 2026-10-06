import subprocess


def truncate(text):
    if len(text) > 15:
        return text[:15] + "..."
    else:
        return text



subprocess.run("cls", shell=True)





subject = "Till"

#[visa från höger till vänster:visa från vänster till höger]




print(truncate(subject))


