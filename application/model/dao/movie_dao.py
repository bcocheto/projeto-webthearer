from application.model.entity.movie_entity import Movie


class Movie_DAO:
    def __init__(self):
        self._movies = []
        self._movies.append(
            Movie(
                1,
                "Video 1",
                "https://www.youtube.com/watch?v=5okLnZB4QNY",
                1,
                "legal",
                "/thumbnails/BG.jpg",
                1,
            )
        )
        self._movies.append(
            Movie(
                2,
                "Video 2",
                "https://www.youtube.com/watch?v=5okLnZB4QNY",
                2,
                "legal ou não",
                "/thumbnails/BG.jpg",
                1,
            )
        )
        self._movies.append(
            Movie(
                3,
                "Video 3",
                "https://www.youtube.com/watch?v=5okLnZB4QNY",
                3,
                "legal ou sim",
                "/thumbnails/BG.jpg",
                1,
            )
        )
        self._movies.append(
            Movie(
                4,
                "Video 1",
                "https://www.youtube.com/watch?v=B8y3SSmz4sg",
                2,
                "gostei não",
                "/thumbnails/BG.jpg",
                2,
            )
        )
        self._movies.append(
            Movie(
                5,
                "Video 2",
                "https://www.youtube.com/watch?v=B8y3SSmz4sg",
                2,
                "gostei",
                "/thumbnails/BG.jpg",
                2,
            )
        )

        self._movies.append(
            Movie(
                6,
                "Video 3",
                "https://www.youtube.com/watch?v=B8y3SSmz4sg",
                2,
                "gostei ou não",
                "/thumbnails/BG.jpg",
                2,
            )
        )

        self._movies.append(
            Movie(
                7,
                "Video 1",
                "https://www.youtube.com/watch?v=2eXCKFMzg2w",
                3,
                "aushaushaush 1",
                "/thumbnails/BG.jpg",
                3,
            )
        )
        self._movies.append(
            Movie(
                8,
                "Video 2",
                "https://www.youtube.com/watch?v=2eXCKFMzg2w",
                3,
                "aushaushaush 2 ",
                "/thumbnails/BG.jpg",
                3,
            )
        )
        self._movies.append(
            Movie(
                9,
                "Video 3",
                "https://www.youtube.com/watch?v=2eXCKFMzg2w",
                3,
                "aushaushaush 3",
                "/thumbnails/BG.jpg",
                3,
            )
        )

    def getMovies(self):
        return self._movies
