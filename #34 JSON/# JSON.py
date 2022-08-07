from contextlib import nullcontext
import json

x = 10
x_json = json.dumps(x)

ism = "anvar"
ism_json = json.dumps(ism)

sonlar = [12, 45, 23, 67]
sonlar_json = json.dumps(sonlar)
print(type(sonlar_json))

bemor = {
  "ism": "Alijon Valiyev",
  "yosh": 30,
  "oila": True,
  "farzandlar": ("Ahmad","Bonu"),
  "allergiya": None,
  "dorilar": [
    {"nomi": "Analgin", "miqdori": 0.5},
    {"nomi": "Panadol", "miqdori": 1.2}
  ]
}

bemor_json = json.dumps(bemor)
print(bemor_json)

bemor_json = json.dumps(bemor, indent=4)
print(bemor_json)
{
    "ism": "Alijon Valiyev",
    "yosh": 30,
    "oila":True,
    "farzandlar": [
        "Ahmad",
        "Bonu"
    ],
    "allergiya": nullcontext,
    "dorilar": [
        {
            "nomi": "Analgin",
            "miqdori": 0.5
        },
        {
            "nomi": "Panadol",
            "miqdori": 1.2
        }
    ]
}
sonlar = json.loads(sonlar_json)
bemor = json.loads(bemor_json)
print(bemor)



