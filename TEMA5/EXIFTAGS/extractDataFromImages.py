# -*- encoding: utf-8 -*-

from PIL.ExifTags import TAGS, GPSTAGS
from PIL import Image
import os

def decode_gps_info(exif):
    gpsinfo = {}
    if 'GPSInfo' in exif:
        '''
        Raw Geo-references
        for key in exif['GPSInfo'].keys():
            decode = GPSTAGS.get(key,key)
            gpsinfo[decode] = exif['GPSInfo'][key]
        exif['GPSInfo'] = gpsinfo
        '''
        
        #Parse geo references.
        Nsec = exif['GPSInfo'][2][2][0] / float(exif['GPSInfo'][2][2][1])
        Nmin = exif['GPSInfo'][2][1][0] / float(exif['GPSInfo'][2][1][1])
        Ndeg = exif['GPSInfo'][2][0][0] / float(exif['GPSInfo'][2][0][1])
        Wsec = exif['GPSInfo'][4][2][0] / float(exif['GPSInfo'][4][2][1])
        Wmin = exif['GPSInfo'][4][1][0] / float(exif['GPSInfo'][4][1][1])
        Wdeg = exif['GPSInfo'][4][0][0] / float(exif['GPSInfo'][4][0][1])
        if exif['GPSInfo'][1] == 'N':
            Nmult = 1
        else:
            Nmult = -1
        if exif['GPSInfo'][1] == 'E':
            Wmult = 1
        else:
            Wmult = -1
        Lat = Nmult * (Ndeg + (Nmin + Nsec/60.0)/60.0)
        Lng = Wmult * (Wdeg + (Wmin + Wsec/60.0)/60.0)
        exif['GPSInfo'] = {"Lat" : Lat, "Lng" : Lng}

 
def get_exif_metadata(image_path):
    ret = {}
    image = Image.open(image_path)
    if hasattr(image, '_getexif'):
        exifinfo = image._getexif()
        if exifinfo is not None:
            for tag, value in exifinfo.items():
                decoded = TAGS.get(tag, tag)
                ret[decoded] = value
    decode_gps_info(ret)
    return ret
    
def printMeta():
    for dirpath, dirnames, files in os.walk("images"):
        for name in files:
            print "[+] Metadata for file: %s " %(dirpath+os.path.sep+name)
            try:
                exifData = {}
                exif = get_exif_metadata(dirpath+os.path.sep+name)
                for metadata in exif:
                    print "Metadata: %s - Value: %s " %(metadata, exif[metadata])
                print "\n"
            except:
                import sys, traceback
                traceback.print_exc(file=sys.stdout)
printMeta()


