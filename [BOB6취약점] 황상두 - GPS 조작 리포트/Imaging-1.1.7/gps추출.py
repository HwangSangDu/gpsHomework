
from PIL import Image
from PIL.ExifTags import TAGS
filename = "hsd.jpg"
extension = filename.split('.')[-1]
if (extension == 'jpg') | (extension == 'JPG') | (extension == 'jpeg') | (extension == 'JPEG'):
    try:
        
        img = Image.open(filename)
        
        info = img._getexif()
        exif = {}
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            exif[decoded] = value
        # from the exif data, extract gps
        exifGPS = exif['GPSInfo']

        latData = exifGPS[2]
        lonData = exifGPS[4]
        
        x = 37.4087310
        y = 127.1324040


        Counterfeit_latDeg = int(x)
        Counterfeit_latMin = (x - int(x))*60
        Counterfeit_latSec = 60*int(Counterfeit_latMin - int(Counterfeit_latMin))
        
        Counterfeit_lonDeg = int(y)
        Counterfeit_lonMin = (y - int(y))*60
        Counterfeit_lonSec = 60*int(Counterfeit_lonMin - int(Counterfeit_lonMin))
        
        # calculae the lat / long
        latDeg = Counterfeit_latDeg
        latMin = Counterfeit_latMin
        latSec = Counterfeit_latSec
        
        lonDeg = Counterfeit_lonDeg
        lonMin = Counterfeit_lonMin
        lonSec = Counterfeit_lonSec
        '''
        latDeg = latData[0][0] / float(latData[0][1])
        latMin = latData[1][0] / float(latData[1][1])
        latSec = latData[2][0] / float(latData[2][1])
        
        lonDeg = lonData[0][0] / float(lonData[0][1])
        lonMin = lonData[1][0] / float(lonData[1][1])
        lonSec = lonData[2][0] / float(lonData[2][1])
        '''

        # correct the lat/lon based on N/E/W/S
        Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
        if exifGPS[1] == 'S': Lat = Lat * -1
        Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
        if exifGPS[3] == 'W': Lon = Lon * -1
        # print file
        msg = "There is GPS info in this picture located at " + str(Lat) + "," + str(Lon)
        print msg
        kmlheader = '<?xml version="1.0" encoding="UTF-8"?>' + '<kml xmlns="http://www.opengis.net/kml/2.2">'
        kml = ('<Placemark><name>%s</name><Point><coordinates>%6f,%6f</coordinates></Point></Placemark></kml>') % (
        filename, Lon, Lat)
        with open(filename + '.kml', "w") as f:
            f.write(kmlheader + kml)
        print 'kml file created'
    except:
        print 'There is no GPS info in this picture'
        pass

