from flask import Flask, redirect, render_template,url_for
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist,  PlaylistSong, Song
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlist-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)
# db.create_all()

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

debug = DebugToolbarExtension(app)


@app.route("/")
def root():
    """Homepage: redirect to /playlists."""

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)

    return render_template('playlist.html', playlist=playlist)

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """
    form = PlaylistForm()
    playlist = Playlist()

    if form.validate_on_submit():
        playlist.name = form.name.data
        playlist.description = form.description.data
        db.session.add(playlist)
        db.session.commit()
        # return redirect(url_for('playlists', add_playlist=form))
        return render_template('new_playlist.html',form=form)#redirect("playlists.html")

    else:
        return render_template('new_playlist.html',form=form)#redirect('new_playlist.html', form=form)

@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)

@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """
    form = SongForm()
    song = Song()

    if form.validate_on_submit():
        song.title = form.title.data
        song.artist = form.artist.data
        db.session.add(song)
        db.session.commit()
        return render_template('new_song.html', form=form)
        # return redirect(url_for("songs", add_song=form))
    else:
        return render_template('new_song.html', form=form)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""

    song = Song.query.get_or_404(song_id)
    return render_template('song.html', song=song)

@app.route("/playlists/<int:playlist_id>/add-song", methods=["GET", "POST"])
def add_song_to_playlist(playlist_id):
    """Add a playlist and redirect to list."""

    # BONUS - ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK

    playlist = Playlist.query.get_or_404(playlist_id)
    form = NewSongForPlaylistForm()
    # playlist = [id,'joe','kay']
    # Restrict form to songs not already on this playlist

    curr_on_playlist = [s.id for s in playlist.songs]
    form.song.choices = (db.session.query(Song.id, Song.title)
                      .filter(Song.id.notin_(curr_on_playlist))
                      .all())

    if form.validate_on_submit():

        # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
        playlist_song = PlaylistSong(song_id=form.song.data,playlist_id=playlist_id)
        db.session.add(playlist_song)

        db.session.commit()

        return redirect(f"/playlists/{playlist_id}")


    return render_template("add_song_to_playlist.html",
                             playlist=playlist,
                             form=form)


if __name__ == '__main__':
    try:
        debug = False
        with app.app_context():
            db.create_all()
            app.run(debug=debug, port=4000, threaded=True)
    except Exception as e:
        raise e