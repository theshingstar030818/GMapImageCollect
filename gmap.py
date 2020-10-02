#!/usr/bin/python
# GoogleMapDownloader.py
# Created by Hayden Eskriett [http://eskriett.com]
#
# A script which when given a longitude, latitude and zoom level downloads a
# high resolution google map
# Find the associated blog post at: http://blog.eskriett.com/2013/07/19/downloading-google-maps/

#import urllib
import urllib.request

#import Image
from PIL import Image
#import them
import math
import os

class GoogleMapDownloader:
    """
        A class which generates high resolution google maps images given
        a longitude, latitude and zoom level
    """

    def __init__(self, lat, lng, zoom=12):
        self._lat = lat
        self._lng = lng
        self._zoom = zoom


    def getXY(self):
        """
            Generates an X,Y tile coordinate based on the latitude, longitude
            and zoom level

            Returns:    An X,Y tile coordinate
        """

        tile_size = 256

        # Use a left shift to get the power of 2
        # i.e. a zoom level of 2 will have 2^2 = 4 tiles
        numTiles = 1 << self._zoom

        # Find the x_point given the longitude
        point_x = (tile_size / 2 + self._lng * tile_size / 360.0) * numTiles // tile_size

        # Convert the latitude to radians and take the sine
        sin_y = math.sin(self._lat * (math.pi / 180.0))

        # Calulate the y coorindate
        point_y = ((tile_size / 2) + 0.5 * math.log((1 + sin_y) / (1 - sin_y)) * -(
                    tile_size / (2 * math.pi))) * numTiles // tile_size

        return int(point_x), int(point_y)


    def generateImage(self, **kwargs):
        """
            Generates an image by stitching a number of google map tiles together.

            Args:
                start_x:        The top-left x-tile coordinate
                start_y:        The top-left y-tile coordinate
                tile_width:     The number of tiles wide the image should be -
                                defaults to 5
                tile_height:    The number of tiles high the image should be -
                                defaults to 5
            Returns:
                A high-resolution Goole Map image.
        """

        start_x = kwargs.get('start_x', None)
        start_y = kwargs.get('start_y', None)
        tile_width = kwargs.get('tile_width', 5)
        tile_height = kwargs.get('tile_height', 5)

        # Check that we have x and y tile coordinates
        if start_x == None or start_y == None:
            start_x, start_y = self.getXY()

        # Determine the size of the image
        width, height = 256 * tile_width, 256 * tile_height

        # Create a new image of the size require
        map_img = Image.new('RGB', (width, height))

        for x in range(0, tile_width):
            for y in range(0, tile_height):
                url = 'https://mt0.google.com/vt?x=' + str(start_x + x) + '&y=' + str(start_y + y) + '&z=' + str(self._zoom) + '&s=Galile&lyrs=y&hl=ko'
                current_tile = str(x) + '-' + str(y)
                #urllib.urlretrieve(url, current_tile)
                urllib.request.urlretrieve(url, current_tile)

                im = Image.open(current_tile)
                map_img.paste(im, (x * 256, y * 256))

                os.remove(current_tile)
            print(x)
        return map_img


def main():
    # Create a new instance of GoogleMap Downloader
    # 37.5092557,126.6167708
    # gmd = GoogleMapDownloader(51.5171, 0.1062, 18)
    # gmd = GoogleMapDownloader(37.5092557,126.6167708, 18)
    # gmd = GoogleMapDownloader(35.6002465, 126.2458603, 18)  # WiDo
    # gmd = GoogleMapDownloader(35.6002465, 126.2458603, 18)  # WiDo
    #35.6046594, 126.1931834
    gmd = GoogleMapDownloader(35.6046594, 126.1931834, 18)  # WiDo


    print("The tile coorindates are {}".format(gmd.getXY()))

    try:
        # Get the high resolution image
        img = gmd.generateImage(tile_width=50, tile_height=50)
    except IOError:
        print("Could not generate the image - try adjusting the zoom level and checking your coordinates")
    else:
        # Save the image to disk
        img.save("high_resolution_image.png")
        print("The map has successfully been created")


if __name__ == '__main__':  main()