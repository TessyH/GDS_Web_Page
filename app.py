from flask import Flask
from flask import render_template, request, jsonify, url_for, redirect
from flask_mail import Mail, Message
import csv

app = Flask(__name__)

# TODO: find cheap smtp server
# configuration of mail
app.config['MAIL_SERVER'] = 'find a cheep one'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USERNAME'] = 'teasdssyasdetzelasd.gasds@gmail.com'
app.config['MAIL_PASSWORD'] = '456559sd456gfdfh9W456i456r'
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route("/home")
def index():
    return render_template("index.html", gds="Glider Development Services")


@app.route("/about")
def about():
    return render_template("About.html")


@app.route("/glider")
def glider():
    return render_template("Glider.html")


@app.route("/services")
def services():
    return render_template("Services.html")


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        print(request.form)
        First = request.form['First']
        Last = request.form['Last']
        Company = request.form['Company']
        fieldnames = ['First', 'Last', 'Company']
        with open('NewClients.csv', 'w') as inFile:
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)
            writer.writerow({'First': First, 'Last': Last, 'Company': Company})
        return render_template("Thanks.html")
    else:
        return render_template('Contact.html')


@app.route("/thanks")
def thanks():
    return render_template("Thanks.html", title="Thanks")


@app.route("/json")
def get_json():
    return jsonify({})  # python dictionary calls


@app.route("/data")
def get_data():
    data = request.json
    return jsonify(data)


def sendContactForm(result):
    msg = Message("This is test",
                  sender="tessyhetzel.gds@gmail.com",
                  recipients=["tessyhetzel.gds@gmail.com"]
                  )

    msg.body = """
    Hello there,
    You just received a contact form.
    Name: {}
    Email: {}
    Message: {}
    regards,
    Webmaster
    """.format(result['name'], result['email'], result['message'])

    mail.send(message=msg)


if __name__ == '__main__':
    app.run(port=5000)  # allows site updates in real time
