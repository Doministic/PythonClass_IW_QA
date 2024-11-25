QA_Folks = {
    "UI_Embedded" : "A QA tester that focus' primarily on all aspects of UI",
    "DMZ_Embedded" : "A QA tester that focuses on DMZ based content",
    "Red_Team_Embedded" : "A QA tester that helps the Red Team with DMZ and other content",
    "VFX_Embedded" : "A QA tester that focuses on primarily VFX content"
}

print(QA_Folks["VFX_Embedded"])
print(QA_Folks["DMZ_Embedded"])
print(QA_Folks["UI_Embedded"])
print(QA_Folks["Red_Team_Embedded"])


QA_Folks["UI_Embedded"] = 0
print(QA_Folks["UI_Embedded"])
