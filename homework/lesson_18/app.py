from flask import Flask
from sqlalchemy.orm import joinedload
from sqlalchemy import func
from config import config

from io import BytesIO
from flask import send_file

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from flask import render_template, request, redirect
from models import db, User, Room, Booking, Equipment
from sqlalchemy import func

import time
from datetime import datetime, timedelta

app = Flask(__name__)
app.config.from_object(config["development"])

db.init_app(app)


@app.route("/")
def index():
    return "Flask + PostgreSQL działa! 🎉"


@app.route("/test-db")
def test_db():
    try:
        db.session.execute(db.text("SELECT 1"))
        return "✅ Połączenie z PostgreSQL OK!"
    except Exception as e:
        return f"❌ Błąd połączenia: {str(e)}"


@app.route("/seed")
def seed():

    if User.query.first():
        return "Dane testowe już istnieją."

    user1 = User(
        name="Jan Kowalski",
        email="jan@example.com",
        department="IT"
    )

    user2 = User(
        name="Anna Nowak",
        email="anna@example.com",
        department="HR"
    )

    room1 = Room(
        name="Sala A1",
        capacity=10
    )

    room2 = Room(
        name="Sala B2",
        capacity=20
    )

    booking1 = Booking(
        title="Spotkanie zespołu",
        user=user1,
        room=room1
    )

    booking2 = Booking(
        title="Prezentacja projektu",
        user=user2,
        room=room2
    )

    projector = Equipment(
        name="Projektor"
    )

    tv = Equipment(
        name="Telewizor"
    )

    microphone = Equipment(
        name="Mikrofon"
    )

    room1.equipment.append(projector)
    room1.equipment.append(tv)

    room2.equipment.append(tv)
    room2.equipment.append(microphone)

    db.session.add_all([
        user1,
        user2,
        room1,
        room2,
        booking1,
        booking2,
        projector,
        tv,
        microphone,
    ])

    db.session.commit()

    return "Dodano przykładowe dane."


@app.route("/bookings")
def bookings():

    all_bookings = Booking.query.all()

    result = "<h1>Rezerwacje</h1>"

    for booking in all_bookings:
        result += (
            f"<p>"
            f"{booking.title} | "
            f"Sala: {booking.room.name} | "
            f"Użytkownik: {booking.user.name}"
            f"</p>"
        )

    return result


@app.route("/debug/n-plus-1")
def debug_n_plus_1():

    start = time.time()

    bookings = Booking.query.all()

    for booking in bookings:
        room_name = booking.room.name
        user_name = booking.user.name

    bad_time = time.time() - start

    start = time.time()

    bookings = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).all()

    for booking in bookings:
        room_name = booking.room.name
        user_name = booking.user.name

    good_time = time.time() - start

    return f"""
    <h1>Porównanie N+1</h1>

    <p>Bez joinedload: {bad_time:.6f} s</p>
    <p>Z joinedload: {good_time:.6f} s</p>
    """


@app.route("/debug/n-plus-1-fixed")
def debug_n_plus_1_fixed():

    bookings = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).all()

    result = "<h1>Problem N+1 - naprawiony</h1>"

    for booking in bookings:
        result += (
            f"<p>"
            f"{booking.title} | "
            f"{booking.room.name} | "
            f"{booking.user.name}"
            f"</p>"
        )

    return result


@app.route("/dashboard")
def dashboard():

    total_users = User.query.count()
    total_rooms = Room.query.count()
    total_bookings = Booking.query.count()

    most_popular_room = (
        db.session.query(
            Room.name,
            func.count(Booking.id).label("bookings_count")
        )
        .join(Booking)
        .group_by(Room.id)
        .order_by(func.count(Booking.id).desc())
        .first()
    )

    room_info = "Brak danych"

    if most_popular_room:
        room_info = (
            f"{most_popular_room.name} "
            f"({most_popular_room.bookings_count} rezerwacji)"
        )

    all_bookings = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).all()
    rooms = Room.query.options(
        joinedload(Room.equipment)
    ).all()

    room_stats = (
        db.session.query(
            Room.name,
            func.count(Booking.id).label("bookings_count")
        )
        .outerjoin(Booking)
        .group_by(Room.id)
        .order_by(Room.name)
        .all()
    )

    daily_trend = (
        db.session.query(
            func.date(Booking.start_time).label("day"),
            func.count(Booking.id).label("count")
        )
        .group_by(func.date(Booking.start_time))
        .order_by(func.date(Booking.start_time))
        .all()
    )

    department_stats = (
        db.session.query(
            User.department,
            func.count(Booking.id).label("count")
        )
        .join(Booking)
        .group_by(User.department)
        .order_by(func.count(Booking.id).desc())
        .all()
    )

    heatmap_data = (
        db.session.query(
            func.extract("dow", Booking.start_time).label("day"),
            func.extract("hour", Booking.start_time).label("hour"),
            func.count(Booking.id).label("count")
        )
        .group_by(
            func.extract("dow", Booking.start_time),
            func.extract("hour", Booking.start_time)
        )
        .order_by(
            func.extract("dow", Booking.start_time),
            func.extract("hour", Booking.start_time)
        )
        .all()
    )

    days_map = {
        0: "Niedziela",
        1: "Poniedziałek",
        2: "Wtorek",
        3: "Środa",
        4: "Czwartek",
        5: "Piątek",
        6: "Sobota"
    }

    formatted_heatmap = []

    for row in heatmap_data:
        formatted_heatmap.append({
            "day": days_map[int(row.day)],
            "hour": int(row.hour),
            "count": row.count
        })

    return render_template(
        "dashboard.html",
        total_users=total_users,
        total_rooms=total_rooms,
        total_bookings=total_bookings,
        room_info=room_info,
        bookings=all_bookings,
        room_stats=room_stats,
        rooms=rooms,
        daily_trend=daily_trend,
        department_stats=department_stats,
        heatmap_data=formatted_heatmap
    )

@app.route("/add-booking", methods=["GET", "POST"])
def add_booking():

    if request.method == "POST":

        title = request.form["title"]
        user_id = request.form["user_id"]
        room_id = request.form["room_id"]

        start_time = datetime.fromisoformat(
            request.form["start_time"]
        )

        end_time = datetime.fromisoformat(
            request.form["end_time"]
        )

        if start_time >= end_time:
            return "❌ Data rozpoczęcia musi być wcześniejsza niż data zakończenia."

        existing_booking = Booking.query.filter(
            Booking.room_id == room_id,
            Booking.start_time < end_time,
            Booking.end_time > start_time
        ).first()

        if existing_booking:
            return "❌ Sala jest już zajęta w tym terminie!"

        booking = Booking(
            title=title,
            user_id=user_id,
            room_id=room_id,
            start_time=start_time,
            end_time=end_time
        )

        db.session.add(booking)
        db.session.commit()

        return redirect("/dashboard")

    users = User.query.all()
    rooms = Room.query.all()

    return render_template(
        "add_booking.html",
        users=users,
        rooms=rooms
    )

@app.route("/report")
def report():

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    pdfmetrics.registerFont(
    TTFont(
        "DejaVuSans",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    )
)

    styles = getSampleStyleSheet()

    styles["Title"].fontName = "DejaVuSans"
    styles["BodyText"].fontName = "DejaVuSans"

    elements = []

    elements.append(
        Paragraph(
            "Raport rezerwacji",
            styles["Title"]
        )
    )

    elements.append(Spacer(1, 20))

    bookings = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).all()

    for booking in bookings:

        text = (
            f"{booking.title} | "
            f"Użytkownik: {booking.user.name} | "
            f"Sala: {booking.room.name} | "
            f"Status: {booking.status}"
        )

        elements.append(
            Paragraph(
                text,
                styles["BodyText"]
            )
        )

    doc.build(elements)

    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="rezerwacje.pdf",
        mimetype="application/pdf"
    )

@app.route("/reminders")
def reminders():

    now = datetime.now()
    next_24h = now + timedelta(hours=24)

    upcoming_bookings = Booking.query.options(
        joinedload(Booking.room),
        joinedload(Booking.user)
    ).filter(
        Booking.start_time >= now,
        Booking.start_time <= next_24h,
        Booking.status == "confirmed"
    ).order_by(
        Booking.start_time
    ).all()

    result = "<h1>Przypomnienia o rezerwacjach</h1>"

    if not upcoming_bookings:
        result += "<p>Brak rezerwacji w ciągu najbliższych 24 godzin.</p>"

    for booking in upcoming_bookings:
        result += (
            f"<p>"
            f"{booking.start_time} | "
            f"{booking.title} | "
            f"Sala: {booking.room.name} | "
            f"Użytkownik: {booking.user.name}"
            f"</p>"
        )

    return result

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        print("Tabele utworzone!")

    app.run(debug=True)