from flask import Flask, jsonify

app = Flask(__name__)


data = [
  {
    "id": 1,
    "first_name": "Rosita",
    "last_name": "Bilt",
    "email": "rbilt0@example.com",
    "gender": "Female"
  },
  {
    "id": 2,
    "first_name": "Henrieta",
    "last_name": "Fasson",
    "email": "hfasson1@chicagotribune.com",
    "gender": "Female"
  },
  {
    "id": 3,
    "first_name": "Merry",
    "last_name": "Cammidge",
    "email": "mcammidge2@pinterest.com",
    "gender": "Female"
  },
  {
    "id": 4,
    "first_name": "Taryn",
    "last_name": "Cockton",
    "email": "tcockton3@desdev.cn",
    "gender": "Female"
  },
  {
    "id": 5,
    "first_name": "Leone",
    "last_name": "Smallwood",
    "email": "lsmallwood4@ucoz.ru",
    "gender": "Female"
  },
  {
    "id": 6,
    "first_name": "Ethe",
    "last_name": "Glisane",
    "email": "eglisane5@google.cn",
    "gender": "Male"
  },
  {
    "id": 7,
    "first_name": "Stevana",
    "last_name": "Cobden",
    "email": "scobden6@omniture.com",
    "gender": "Female"
  },
  {
    "id": 8,
    "first_name": "Emery",
    "last_name": "Slaght",
    "email": "eslaght7@sbwire.com",
    "gender": "Male"
  },
  {
    "id": 9,
    "first_name": "Anissa",
    "last_name": "Cornelisse",
    "email": "acornelisse8@bbb.org",
    "gender": "Female"
  },
  {
    "id": 10,
    "first_name": "Wyn",
    "last_name": "Stoppe",
    "email": "wstoppe9@sina.com.cn",
    "gender": "Male"
  },
  {
    "id": 11,
    "first_name": "Tammie",
    "last_name": "Smee",
    "email": "tsmeea@mapy.cz",
    "gender": "Female"
  },
  {
    "id": 12,
    "first_name": "Antonin",
    "last_name": "Baston",
    "email": "abastonb@apple.com",
    "gender": "Male"
  },
  {
    "id": 13,
    "first_name": "Fidelio",
    "last_name": "Khristoforov",
    "email": "fkhristoforovc@senate.gov",
    "gender": "Male"
  },
  {
    "id": 14,
    "first_name": "Markos",
    "last_name": "Godlonton",
    "email": "mgodlontond@friendfeed.com",
    "gender": "Male"
  },
  {
    "id": 15,
    "first_name": "Nestor",
    "last_name": "Minifie",
    "email": "nminifiee@washingtonpost.com",
    "gender": "Male"
  },
  {
    "id": 16,
    "first_name": "Tamma",
    "last_name": "Okroy",
    "email": "tokroyf@qq.com",
    "gender": "Female"
  },
  {
    "id": 17,
    "first_name": "Delmer",
    "last_name": "Bearne",
    "email": "dbearneg@xing.com",
    "gender": "Male"
  },
  {
    "id": 18,
    "first_name": "Rob",
    "last_name": "Farny",
    "email": "rfarnyh@de.vu",
    "gender": "Male"
  },
  {
    "id": 19,
    "first_name": "Betsy",
    "last_name": "Sharland",
    "email": "bsharlandi@w3.org",
    "gender": "Female"
  },
  {
    "id": 20,
    "first_name": "Auroora",
    "last_name": "Henrys",
    "email": "ahenrysj@shareasale.com",
    "gender": "Female"
  }
]

@ app.route('/mockaroo')
def mockaroo_list():
    return jsonify("Did this on my own!")

@app.route('/fname')
def get_all_users():
    return jsonify(data), 202

@app.route("/the_users/<id>")
def get_user_by_id(id):
    for user in data:
        if user["id"] == id:
            return jsonify(user),200
    return jsonify("User does not exist."),404

if __name__ == "__main__":
    app.run(port="8086", host= "0.0.0.0")

