import mysql.connector as MySql
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
Dbms = MySql.connect(host="localhost", user="root", passwd="shetty", database="flaskapp")
cursor = Dbms.cursor()
cursor.execute("Use flaskapp")


# payment
@app.route('/payment_enter', methods=['GET', 'POST'])
def index_payment():
    if request.method == 'POST':
        # fetch form data
        userDetails = request.form
        pid = userDetails['pid']
        amt = userDetails['amt']
        date = userDetails['date']
        time = userDetails['time']
        ppid = userDetails['ppid']
        cursor.execute("INSERT INTO payment(pid, amt, date,time,ppid) VALUES(%s,%s,%s,%s,%s)",
                       (pid, amt, date, time, ppid))
        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('payment.html')


# fuel
@app.route('/fuel_enter', methods=['GET', 'POST'])
def index_ppd():
    if request.method == 'POST':
        userDetails = request.form
        fid = userDetails['fid']
        fuel = userDetails['fuel']
        ppid = userDetails['ppid']
        cursor.execute("INSERT INTO fuel(fid,fuel,ppid) VALUES(%s,%s,%s)", (fid, fuel, ppid))
        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('fuel.html')


# tax
@app.route('/tax_enter', methods=['GET', 'POST'])
def index_ppg():

    if request.method == 'GET':
        return render_template('tax.html')

    if request.method == 'POST':
        fid = request.form.get("fid")
        tax = request.form.get("tax")
        cursor.execute("INSERT INTO tax(fid, tax) VALUES(%s,%s)", (fid,tax))

        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('tax.html',fid=fid)


#crud_delete_tax
@app.route('/tax_button_enter', methods=['POST'])
def delete_tax():
    fid = request.form.get("fid")

    cursor.execute("""
            DELETE FROM tax WHERE fid=%s
            """,(fid,))
    Dbms.commit()
    return "tax deleted Successfully"




# updates
@app.route('/updates_enter', methods=['GET', 'POST'])
def index_updates():
    if request.method == 'POST':
        userDetails = request.form
        uid = userDetails['uid']
        date = userDetails['date']
        fid = userDetails['fid']
        amt_day = userDetails['amt_day']
        amt_remaining = userDetails['amt_remaining']
        ppid = userDetails['ppid']
        cursor.execute("INSERT INTO updates(uid, date, fid, amt_day, amt_remaining,ppid) VALUES(%s,%s,%s,%s,%s,%s)",
                       (uid, date, fid, amt_day, amt_remaining, ppid))
        # cursor.execute("select * from updates")
        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('updates.html')


# @app.route('/users')
# def users():
# cursor=mysql.connection.cursor()
# resultValue = cursor.execute("SELECT * FROM updates")
# if resultValue>0:
# userDetails = cursor.fetchall()
# return render_template('users.html', userDetails=userDetails)


# register
@app.route('/register_enter', methods=['GET', 'POST'])
def index_register():
    if request.method == 'POST':
        userDetails = request.form
        rid = userDetails['rid']
        date = userDetails['date']
        fid = userDetails['fid']
        number = userDetails['number']
        qty = userDetails['qty']
        amt = userDetails['amt']
        pid = userDetails['pid']
        ppid = userDetails['ppid']
        cursor.execute("INSERT INTO registration(rid, date,fid,number,qty,amt,pid,ppid) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                       (rid, date, fid, number, qty, amt, pid, ppid))
        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('registration.html')

#crud_update_updates



# petrol_pump
@app.route('/petrol_pump_enter', methods=['GET', 'POST'])
def index_petrol_pump():
    if request.method == 'POST':
        userDetails = request.form
        ppid = userDetails['ppid']
        branch = userDetails['branch']
        cursor.execute("INSERT INTO petrol_pump(ppid, branch) VALUES(%s,%s)", (ppid, branch))
        Dbms.commit()
        cursor.close()
        return 'success'
    return render_template('petrol_pump.html')


@app.route('/')
def home():
    return render_template('petrolpump1.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route("/fuel")
def fuel():
    return render_template('fuel.html')


@app.route('/tax')
def tax():
    return render_template('tax.html')


@app.route('/payment')
def payment():
    return render_template('payment.html')


@app.route('/updates')
def updates():
    return render_template('updates.html')


@app.route('/petrol_pump')
def petrol_pump():
    return render_template('petrol_pump.html')


if __name__ == '__main__':
    app.run(debug=True)
