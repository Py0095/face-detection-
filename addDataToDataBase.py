import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://dgprojectfacedetection-default-rtdb.firebaseio.com/"
})


ref = db.reference('Targets')

data = {
    "123450":
    {
        'name': "Aliano CHARLES",
        'option': "Entrepreneur and Developer",
        'status':"Not Bandit",
        'infos': "Aliano is the creator of this Programs.",
        'register_at': "2023-16-08 5:43"
    },
    "963852":
    {
        'name': "Elon Musk",
        'option': "Entrepreneur",
        'status':"Not Bandit",
        'infos': "Musk is the founder, chairman, CEO and chief technology officer of SpaceX, angel investor, CEO and product architect of Tesla, Inc., owner, chairman and CTO of X Corp., founder of the Boring Company, a co-founder of Neuralink and OpenAI, and the president of the Musk Foundation.",
        'register_at': "2023-16-08 5:43"
    },
    "852741":
    {
        'name': "Emly Blunt",
        'option': "Entrepreneur",
        'status':"Not Bandit",
        'infos': "Blunt was born on February 23, 1983, in Roehampton, South West London, England, the second of four children in the family of Joanna Mackie, a former actress and teacher, and Oliver Simon Peter Blunt, a barrister. Her grandfather was Major General Peter Blunt, and her uncle is MP Crispin Blunt.",
        'register_at': "2023-16-08 5:43"
    },
    "321654":
    {
        'name': "Murtaza Hassan",
        'option': "Entrepreneur",
        'status':"Not Bandit",
        'infos': "Murtaza is a chemical biologist that joined the Gray Lab in July 2021 as a postdoctoral researcher. He developed his love for medicinal chemistry and chemical biology at the undergraduate level at the University of Toronto Mississauga which then motivated him to pursue an MSc (York University, Supervisor: Prof. Edward Lee-Ruff, 2017) and PhD (University of Toronto Mississauga, Supervisor: Patrick T. Gunning, 2021) in the field. His PhD work involved the development of some of the most potent and selective HDAC8 inhibitors known-to-date. It incorporated inhibitors with L-shaped conformational constraints to compliment the L-shaped HDAC8 pocket. His current work at the Gray Lab revolves around the development of first-in-class covalent inhibitors for recently discovered epigenetic targets that have been shown to synergize with anticancer immunotherapy. Additionally, he is interested in developing small-molecule chemoproteomic tools that can potentially expand our ability to target otherwise undruggable proteins, by using protein-protein interactions for cross-labelling/drugging interacting proteins.",
        'register_at': "2023-16-08 5:43"
    },
    "125640":
    {
        'name': "Vitelom",
        'option': "Criminal",
        'status': "Bandit",
        'infos': "Vitelom se youn nan bandi ki puissant kap simen la troublay nan divès komin nan peyi a",
        'register_at': "2023-16-08 5:43"
    },
    "125649":
    {
        'name': "Izo",
        'option': "Criminal",
        'status': "Bandit",
        'infos': "Izo chèf gang 5 sekond se youn nan bandi ki puissant kap simen la troublay nan divès komin nan peyi a",
        'register_at': "2023-16-08 5:43"
    }, "125643":
    {
        'name': "Lanmo san jou",
        'option': "Criminal",
        'status': "Bandit",
        'infos': "Lanmo san jou  chèf gang 400 marozo se youn nan bandi ki puissant kap simen la troublay nan divès komin nan peyi a",
        'register_at': "2023-16-08 5:43"
    }
}

for key, value in data.items():
    ref.child(key).set(value)

print("Data added successfully....")
