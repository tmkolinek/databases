"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Playlist(db.Model):
    """Playlist."""
    __tablename__ = 'playlist'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(140),
                     nullable=False,
                     )

    description = db.Column(
        db.String(500),
    )

    songs = db.Column(
        db.String(500),
    )



# class Playlist2(db.Model):
#     """Playlist2."""
#     __tablename__ = 'playlist2'

#     id = db.Column(db.Integer, primary_key=True)

#     name = db.Column(db.String(140),
#                      nullable=False,
#                      )

#     description = db.Column(
#         db.String(500),
#     )

#     songs = db.Column(
#         db.String(500),
#     )

    # ADD THE NECESSARY CODE HERE
class Song(db.Model):
    """Song."""

    __tablename__ = 'song'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(140), nullable=False)

    artist = db.Column(db.String(20), nullable=False)


    # ADD THE NECESSARY CODE HERE
class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE

    __tablename__ = 'playlistsong'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    playlist_id = db.Column(
        db.Integer,
        db.ForeignKey('playlist.id', ondelete='cascade'),
        primary_key=True,
    )

    song_id = db.Column(
        db.Integer,
        db.ForeignKey('song.id', ondelete='cascade'),
        primary_key=True,
    )
# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)