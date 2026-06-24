from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

room_equipment = db.Table(
    "room_equipment",

    db.Column(
        "room_id",
        db.Integer,
        db.ForeignKey("rooms.id"),
        primary_key=True
    ),

    db.Column(
        "equipment_id",
        db.Integer,
        db.ForeignKey("equipment.id"),
        primary_key=True
    )
)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    bookings = db.relationship(
        "Booking",
        backref="user",
        lazy=True
    )
    department = db.Column(
        db.String(100),
        nullable=False,
        default="IT"
    )
    
    def __repr__(self):
        return f"<User {self.name}>"


class Room(db.Model):
    __tablename__ = "rooms"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)

    bookings = db.relationship(
        "Booking",
        backref="room",
        lazy=True
    )

    equipment = db.relationship(
        "Equipment",
        secondary=room_equipment,
        back_populates="rooms"
    )

    def __repr__(self):
        return f"<Room {self.name}>"

class Equipment(db.Model):
    __tablename__ = "equipment"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    rooms = db.relationship(
        "Room",
        secondary=room_equipment,
        back_populates="equipment"
    )

    def __repr__(self):
        return f"<Equipment {self.name}>"


class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    start_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    end_time = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    status = db.Column(
        db.String(20),
        default="confirmed"
    )

    attendees_count = db.Column(
        db.Integer,
        default=1
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    room_id = db.Column(
        db.Integer,
        db.ForeignKey("rooms.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Booking {self.title}>"