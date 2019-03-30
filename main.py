from flask import Flask, render_template, request

from lib import wallpapers_calc


def main():

    app = Flask(__name__)

    @app.route('/')
    def myfunc():
        width_room = request.args.get('width_room')
        length_room = request.args.get('length_room')
        height_room = request.args.get('height_room')
        width_wallpapers = request.args.get('width_wallpapers')
        length_wallpapers = request.args.get('lenght_wallpapers')
        if width_room and length_room and height_room and width_wallpapers and length_wallpapers:
            calculate = wallpapers_calc(float(width_room), float(length_room), float(height_room), float(width_wallpapers), float(length_wallpapers))
            return render_template('index.html', title='Калькулятор обоев', calculate=calculate, width_room=width_room, length_room=length_room, height_room=height_room, width_wallpapers=width_wallpapers, length_wallpapers=length_wallpapers)
        return render_template('index.html', title='Калькулятор обоев')

    app.run(port=9877, debug=True)

if __name__ == '__main__':
    main()