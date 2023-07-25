from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'PASSWORD'
app.config['MYSQL_DB'] = 'car_database'

mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/cars')
def show_cars():
    try:
        cursor = mysql.cursor()
        cursor.execute('SELECT * FROM cars')
        cars_data = cursor.fetchall()
        return render_template('cars.html', cars=cars_data)
    except Exception as e:
        return f'Error fetching data from the database: {str(e)}'
    finally:
        cursor.close()

@app.route('/cars/add', methods=['GET', 'POST'])
def add_car():
    if request.method == 'POST':
        color = request.form['color']
        model = request.form['model']
        year = request.form['year']

        try:
            cursor = mysql.cursor()
            cursor.execute('INSERT INTO cars (color, model, year) VALUES (%s, %s, %s)', (color, model, year))
            mysql.commit()
            return redirect(url_for('show_cars'))
        except Exception as e:
            return f'Error adding car to the database: {str(e)}'
        finally:
            cursor.close()

    return render_template('car_form.html', title='Add', action=url_for('add_car'), button_text='Add Car', car=None)

@app.route('/cars/edit/<int:car_id>', methods=['GET', 'POST'])
def edit_car(car_id):
    try:
        cursor = mysql.cursor()
        cursor.execute('SELECT * FROM cars WHERE id = %s', (car_id,))
        car_data = cursor.fetchone()
        if car_data is None:
            return 'Car not found'

        if request.method == 'POST':
            color = request.form['color']
            model = request.form['model']
            year = request.form['year']

            cursor.execute('UPDATE cars SET color = %s, model = %s, year = %s WHERE id = %s',
                           (color, model, year, car_id))
            mysql.commit()
            return redirect(url_for('show_cars'))

        return render_template('car_form.html', title='Edit', action=url_for('edit_car', car_id=car_id),
                               button_text='Update Car', car={'color': car_data[1], 'model': car_data[2], 'year': car_data[3]})

    except Exception as e:
        return f'Error editing car data: {str(e)}'
    finally:
        cursor.close()

@app.route('/cars/delete/<int:car_id>')
def delete_car(car_id):
    try:
        cursor = mysql.cursor()
        cursor.execute('DELETE FROM cars WHERE id = %s', (car_id,))
        mysql.commit()
        return redirect(url_for('show_cars'))
    except Exception as e:
        return f'Error deleting car from the database: {str(e)}'
    finally:
        cursor.close()

if __name__ == '__main__':
    app.run()
