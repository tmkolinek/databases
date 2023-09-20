"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy import MetaData
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
  pass
# db = SQLAlchemy()
db = SQLAlchemy(model_class=Base)


class Playlist(db.Model):
    # __tablename__ = 'playlist'
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(db.String(140), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(db.text)

# class Playlist(db.Model):
#     """Playlist."""
#     __tablename__ = 'playlist'

#     id = db.Column(db.Integer, primary_key=True)

#     name = db.Column(db.String(140),
#         nullable=False,
#     )

    # description = db.Column(
    #     db.Text,
    # )



    # ADD THE NECESSARY CODE HERE


# class Song(db.Model):
#     """Song."""

#     __tablename__ = 'song'

#     id = db.Column(
#         db.Integer,
#         primary_key=True,
#     )

#     title = db.Column(
#         db.String(140),
#         nullable=False,
#     )

#     artist = db.Columm(
#         db.String(140),
#         nullable=False,
#     )





#     # ADD THE NECESSARY CODE HERE


# class PlaylistSong(db.Model):
#     """Mapping of a playlist to a song."""

#     # ADD THE NECESSARY CODE HERE

#     __tablename__ = 'playlistsong'

#     id = db.Column(
#         db.Integer,
#         primary_key=True,
#     )

#     playlist_id = db.Column(
#         db.Integer,
#         db.ForeignKey('playlist.id', ondelete='cascade'),
#         primary_key=True,
#     )

#     song_id = db.Column(
#         db.Integer,
#         db.ForeignKey('song.id', ondelete='cascade'),
#         primary_key=True,
#     )


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
