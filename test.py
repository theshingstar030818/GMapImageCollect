"""Tests to make some huge Gmaps. See README.md for more info."""

from hugegmaps import create_map


def test_calibration():
    """Quick single screenshot of Philly Art Museum for calibration.
    Takes about 10 seconds to run.
    """
    create_map(
        lat_start=39.9644273,
        long_start=-75.1801129,
        number_rows=1,
        number_cols=1,
        scale=0.5,
        sleep_time=0,
        offset_left=0,  # My value: 0.05
        offset_top=0,  # My value: 0.17
        offset_right=0,  # My value: 0.03
        offset_bottom=0,  # My value: 0.09
        outfile='huge_gmap_calibration.png',
    )


def test_small_area():
    """Small 3x3 grid of images to test combining images.
    Takes about 60 seconds to run.
    """
    create_map(
        lat_start=39.9644273,
        long_start=-75.1801129,
        number_rows=3,
        number_cols=3,
        scale=0.2,
        sleep_time=3,
        offset_left=0.05,
        offset_top=0.17,
        offset_right=0.03,
        offset_bottom=0.09,
        outfile='huge_gmap_small_area.png',
    )


def test_philly_high_res():
    """High-res map of Philly. Creates the final version I hung on my wall.
    Takes about 20 minutes to run.
    """
    # 37.027491,126.8389479 // pyong taek
    # 37.0410402,126.9306334
    # 37.0770916,126.8154896
    create_map(
        lat_start=37.0770916,
        long_start=126.8154896,
        number_rows=5,
        number_cols=5,
        scale=1,
        sleep_time=3,
        offset_left=0.3,
        offset_top=0.17,
        offset_right=0.1,
        offset_bottom=0.09,
        outfile='huge_gmap_high_res_pyongtaek.png',
    )


def main():
    test_philly_high_res()


if __name__ == '__main__':  main()