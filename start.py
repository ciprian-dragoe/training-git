from flask import Flask, render_template
import csv

app = Flask('app')


@app.route('/')
def index():
    products = get_products("products_cars.csv") + get_products("products_home_appliances.csv") + get_products("products_smartphones.csv")
    return render_template('index.html', products=products)


def get_products(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return [element.replace("\n", "").split('______') for element in lines]


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
