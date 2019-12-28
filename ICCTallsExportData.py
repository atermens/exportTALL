# -----------------------------------------------------------------------------
# Name:        ICCTallsExportData
# Purpose:     Variables globals associades a ICCTallsExport.py
#
# Author:      atermens
# Created:     31/05/2019
# Copyright:   (c) a.termens 2019
# License:     CC BY 4.0
# -----------------------------------------------------------------------------
# !/usr/bin/env python


# -----------------------------------------------------------------------------
# OBSERVACIONS
#
# els punts son llistes: [x,y]
# un poligon o un segment es defineix com una llista de punts:
# [ [x0,y0], [x1,y1], ... , [xN,yN] ]
#
# -----------------------------------------------------------------------------
#        0      1     2     3    4      5
# key: [tpare, ctot, ftot, nom, codis, epsg]
TALLS = {
    "Tall50K":    ["Tall50K",   1,  1, "Tall base 1:50 000",
                   " ", "EPSG::4230"],
    "Tall25K":    ["Tall50K",   2,  2, "Tall 1:25 000 (IGN)",
                   "IC25-IF25", "EPSG::4230"],
    "Tall10K":    ["Tall50K",   4,  4, "Tall 1:10 000",
                   "IC10-IF10", "EPSG::4230"],
    "Tall5K":     ["Tall50K",   8,  8, "Tall 1:5 000 (IGN)",
                   "IC5-IF5", "EPSG::4230"],
    "Tall2K":     ["Tall50K",  20, 20, "Tall 1:2 000",
                   "IC2-IF2", "EPSG::4230"],
    "Tall1K":     ["Tall50K",  40, 40, "Tall 1:1 000",
                   "IC1-IF1", "EPSG::4230"],
    "Tall25Kicc": ["Tall50K",   3,  2, "Tall 1:25 000 (ICC)",
                   "ID50-c-f", "EPSG::4230"],
    "Tall5Kicc":  ["Tall50K",  12,  8, "Tall 1:5 000 (ICC)",
                   "ID50-c-f", "EPSG::4230"],
    "Tall2Kicc":  ["Tall10K",   5,  5, "Tall 1:2 000 (20x20)",
                   "IC10-IF10-C-F", "EPSG::4230"],
    "Tall5Ccmb":  ["Tall2Kicc", 4,  2, "Tall 1:500 CMB",
                   "IC10-IF10-C-F-S", "EPSG::4230"],
    "Tall100K":   ["Tall100K",  1,  1, "Tall 1:100000",
                   "IC100-IF100", "EPSG::23031"]
    }


IC100 = [16, 17, 16, 17, 18, 19, 20, 16, 17, 18, 19, 20, 16, 17, 18, 19, 20,
         16, 17, 18, 19, 16, 17, 18, 19, 16, 17, 16, 17]
IF100 = [4,  4,  5,  5,  5,  5,  5,  6,  6,  6,  6,  6,  7,  7,  7,  7,  7,
         8,  8,  8,  8,  9,  9,  9,  9,  10, 10, 11, 11]

# epsg: 23031
# key: [ic100, if100, xNW, yNW, xNE, yNE,
#       xSE, ySE, xSW, ySW]

T100 = {
    1604: [16,  4, 26740467.0, 476487368.0, 32179440.0, 476334701.0,
           32083427.0, 472632875.0, 26617214.0, 472785285.0],
    1704: [17,  4, 32179440.0, 476334701.0, 37613428.0, 476204014.0,
           37546963.0, 472512928.0, 32083427.0, 472632875.0],
    1605: [16,  5, 26617214.0, 472785285.0, 32083427.0, 472632875.0,
           31987958.0, 468931330.0, 26493977.0, 469083669.0],
    1705: [17,  5, 32083427.0, 472632875.0, 37546963.0, 472512928.0,
           37480672.0, 468811598.0, 31987958.0, 468931330.0],
    1805: [18,  5, 37546963.0, 472512928.0, 43010194.0, 472425297.0,
           42973134.0, 468734788.0, 37480672.0, 468811598.0],
    1905: [19,  5, 43010194.0, 472425297.0, 48473692.0, 472402347.0,
           48465578.0, 468701120.0, 42973134.0, 468734788.0],
    2005: [20,  5, 48473692.0, 472402347.0, 53937069.0, 472411760.0,
           53958003.0, 468710554.0, 48465578.0, 468701120.0],
    1606: [16,  6, 26493977.0, 469083669.0, 31987958.0, 468931330.0,
           31893056.0, 465230033.0, 26371098.0, 465392814.0],
    1706: [17,  6, 31987958.0, 468931330.0, 37480672.0, 468811598.0,
           37414690.0, 465110349.0, 31893056.0, 465230033.0],
    1806: [18,  6, 37480672.0, 468811598.0, 42973134.0, 468734788.0,
           42936145.0, 465033688.0, 37414690.0, 465110349.0],
    1906: [19,  6, 42973134.0, 468734788.0, 48465578.0, 468701120.0,
           48457547.0, 465000059.0, 42936145.0, 465033688.0],
    2006: [20,  6, 48465578.0, 468701120.0, 53958003.0, 468710554.0,
           53978767.0, 465009513.0, 48457547.0, 465000059.0],
    1607: [16,  7, 26371100.0, 465392800.0, 31893056.0, 465230033.0,
           31798793.0, 461528891.0, 26248068.0, 461691398.0],
    1707: [17,  7, 31893056.0, 465230033.0, 37414690.0, 465110349.0,
           37349158.0, 461409269.0, 31798793.0, 461528891.0],
    1807: [18,  7, 37414690.0, 465110349.0, 42936145.0, 465033688.0,
           42899374.0, 461332738.0, 37349158.0, 461409269.0],
    1907: [19,  7, 42936145.0, 465033688.0, 48457547.0, 465000059.0,
           48449500.0, 461299184.0, 42899374.0, 461332738.0],
    2007: [20,  7, 48457547.0, 465000059.0, 53978767.0, 465009513.0,
           53999559.0, 461297864.0, 48449500.0, 461299184.0],
    1608: [16,  8, 26248068.0, 461691398.0, 31798793.0, 461528891.0,
           31705145.0, 457827840.0, 26125775.0, 457990116.0],
    1708: [17,  8, 31798793.0, 461528891.0, 37349158.0, 461409269.0,
           37283962.0, 457708330.0, 31705145.0, 457827840.0],
    1808: [18,  8, 37349158.0, 461409269.0, 42899374.0, 461332738.0,
           42862819.0, 457631940.0, 37283962.0, 457708330.0],
    1908: [19,  8, 42899374.0, 461332738.0, 48449500.0, 461299184.0,
           48441401.0, 457587747.0, 42862819.0, 457631940.0],
    1609: [16,  9, 26125775.0, 457990116.0, 31705145.0, 457827840.0,
           31611675.0, 454126955.0, 26004283.0, 454288750.0],
    1709: [17,  9, 31705145.0, 457827840.0, 37283962.0, 457708330.0,
           37219060.0, 454007781.0, 31611675.0, 454126955.0],
    1809: [18,  9, 37283962.0, 457708330.0, 42862819.0, 457631940.0,
           42826445.0, 453931058.0, 37219060.0, 454007781.0],
    1909: [19,  9, 42862819.0, 457631940.0, 48441401.0, 457587747.0,
           48433277.0, 453865122.0, 42826445.0, 453931058.0],
    1610: [16, 10, 26004283.0, 454288750.0, 31611675.0, 454126955.0,
           31519228.0, 450426429.0, 25883488.0, 450588230.0],
    1710: [17, 10, 31611675.0, 454126955.0, 37219060.0, 454007781.0,
           37154082.0, 450296812.0, 31519228.0, 450426429.0],
    1611: [16, 11, 25883488.0, 450588230.0, 31519228.0, 450426429.0,
           31427235.0, 446726304.0, 25763139.0, 446877646.0],
    1711: [17, 11, 31519228.0, 450426429.0, 37154082.0, 450296812.0,
           37089292.0, 446596504.0, 31427235.0, 446726304.0]
        }
# -----------------------------------------------------------------------------
# Identificadors fulls MTN50 a Catalunya:
#
# key = IC50*100 + IF50
#
# Exemple:
#         3207: { "COLABS": 32,
#                 "FILABS":  7,
#                 "ID50M": "0118B",
#                 "IDVISABS": "32-7",
#                 "IDVISREL": "118B" }
# -----------------------------------------------------------------------------
IDTALLBASE = {
    3207: {"COLABS": 32, "FILABS":  7, "ID50M": "0118B",
           "IDVISABS": "32-7",  "IDVISREL": "118B"},
    3307: {"COLABS": 33, "FILABS":  7, "ID50M": "0149B",
           "IDVISABS": "33-7",  "IDVISREL": "149B"},
    3208: {"COLABS": 32, "FILABS":  8, "ID50M": "0148A",
           "IDVISABS": "32-8",  "IDVISREL": "148"},
    3308: {"COLABS": 33, "FILABS":  8, "ID50M": "0149A",
           "IDVISABS": "33-8",  "IDVISREL": "149"},
    3408: {"COLABS": 34, "FILABS":  8, "ID50M": "0150A",
           "IDVISABS": "34-8",  "IDVISREL": "150"},
    3209: {"COLABS": 32, "FILABS":  9, "ID50M": "0180A",
           "IDVISABS": "32-9",  "IDVISREL": "180"},
    3309: {"COLABS": 33, "FILABS":  9, "ID50M": "0181A",
           "IDVISABS": "33-9",  "IDVISREL": "181"},
    3409: {"COLABS": 34, "FILABS":  9, "ID50M": "0182A",
           "IDVISABS": "34-9",  "IDVISREL": "182"},
    3509: {"COLABS": 35, "FILABS":  9, "ID50M": "0183A",
           "IDVISABS": "35-9",  "IDVISREL": "183"},
    3210: {"COLABS": 32, "FILABS": 10, "ID50M": "0213A",
           "IDVISABS": "32-10", "IDVISREL": "213"},
    3310: {"COLABS": 33, "FILABS": 10, "ID50M": "0214A",
           "IDVISABS": "33-10", "IDVISREL": "214"},
    3410: {"COLABS": 34, "FILABS": 10, "ID50M": "0215A",
           "IDVISABS": "34-10", "IDVISREL": "215"},
    3510: {"COLABS": 35, "FILABS": 10, "ID50M": "0216A",
           "IDVISABS": "35-10", "IDVISREL": "216"},
    3610: {"COLABS": 36, "FILABS": 10, "ID50M": "0217A",
           "IDVISABS": "36-10", "IDVISREL": "217"},
    3710: {"COLABS": 37, "FILABS": 10, "ID50M": "0218A",
           "IDVISABS": "37-10", "IDVISREL": "218"},
    3810: {"COLABS": 38, "FILABS": 10, "ID50M": "0219A",
           "IDVISABS": "38-10", "IDVISREL": "219"},
    3910: {"COLABS": 39, "FILABS": 10, "ID50M": "0220A",
           "IDVISABS": "39-10", "IDVISREL": "220"},
    4010: {"COLABS": 40, "FILABS": 10, "ID50M": "0221A",
           "IDVISABS": "40-10", "IDVISREL": "221"},
    3211: {"COLABS": 32, "FILABS": 11, "ID50M": "0251A",
           "IDVISABS": "32-11", "IDVISREL": "251"},
    3311: {"COLABS": 33, "FILABS": 11, "ID50M": "0252A",
           "IDVISABS": "33-11", "IDVISREL": "252"},
    3411: {"COLABS": 34, "FILABS": 11, "ID50M": "0253A",
           "IDVISABS": "34-11", "IDVISREL": "253"},
    3511: {"COLABS": 35, "FILABS": 11, "ID50M": "0254A",
           "IDVISABS": "35-11", "IDVISREL": "254"},
    3611: {"COLABS": 36, "FILABS": 11, "ID50M": "0255A",
           "IDVISABS": "36-11", "IDVISREL": "255"},
    3711: {"COLABS": 37, "FILABS": 11, "ID50M": "0256A",
           "IDVISABS": "37-11", "IDVISREL": "256"},
    3811: {"COLABS": 38, "FILABS": 11, "ID50M": "0257A",
           "IDVISABS": "38-11", "IDVISREL": "257"},
    3911: {"COLABS": 39, "FILABS": 11, "ID50M": "0258A",
           "IDVISABS": "39-11", "IDVISREL": "258"},
    4011: {"COLABS": 40, "FILABS": 11, "ID50M": "0259A",
           "IDVISABS": "40-11", "IDVISREL": "259"},
    3212: {"COLABS": 32, "FILABS": 12, "ID50M": "0289A",
           "IDVISABS": "32-12", "IDVISREL": "289"},
    3312: {"COLABS": 33, "FILABS": 12, "ID50M": "0290A",
           "IDVISABS": "33-12", "IDVISREL": "290"},
    3412: {"COLABS": 34, "FILABS": 12, "ID50M": "0291A",
           "IDVISABS": "34-12", "IDVISREL": "291"},
    3512: {"COLABS": 35, "FILABS": 12, "ID50M": "0292A",
           "IDVISABS": "35-12", "IDVISREL": "292"},
    3612: {"COLABS": 36, "FILABS": 12, "ID50M": "0293A",
           "IDVISABS": "36-12", "IDVISREL": "293"},
    3712: {"COLABS": 37, "FILABS": 12, "ID50M": "0294A",
           "IDVISABS": "37-12", "IDVISREL": "294"},
    3812: {"COLABS": 38, "FILABS": 12, "ID50M": "0295A",
           "IDVISABS": "38-12", "IDVISREL": "295"},
    3912: {"COLABS": 39, "FILABS": 12, "ID50M": "0296A",
           "IDVISABS": "39-12", "IDVISREL": "296"},
    4012: {"COLABS": 40, "FILABS": 12, "ID50M": "0297A",
           "IDVISABS": "40-12", "IDVISREL": "297"},
    3213: {"COLABS": 32, "FILABS": 13, "ID50M": "0327A",
           "IDVISABS": "32-13", "IDVISREL": "327"},
    3313: {"COLABS": 33, "FILABS": 13, "ID50M": "0328A",
           "IDVISABS": "33-13", "IDVISREL": "328"},
    3413: {"COLABS": 34, "FILABS": 13, "ID50M": "0329A",
           "IDVISABS": "34-13", "IDVISREL": "329"},
    3513: {"COLABS": 35, "FILABS": 13, "ID50M": "0330A",
           "IDVISABS": "35-13", "IDVISREL": "330"},
    3613: {"COLABS": 36, "FILABS": 13, "ID50M": "0331A",
           "IDVISABS": "36-13", "IDVISREL": "331"},
    3713: {"COLABS": 37, "FILABS": 13, "ID50M": "0332A",
           "IDVISABS": "37-13", "IDVISREL": "332"},
    3813: {"COLABS": 38, "FILABS": 13, "ID50M": "0333A",
           "IDVISABS": "38-13", "IDVISREL": "333"},
    3913: {"COLABS": 39, "FILABS": 13, "ID50M": "0334A",
           "IDVISABS": "39-13", "IDVISREL": "334"},
    4013: {"COLABS": 40, "FILABS": 13, "ID50M": "0335A",
           "IDVISABS": "40-13", "IDVISREL": "335"},
    3114: {"COLABS": 31, "FILABS": 14, "ID50M": "0358A",
           "IDVISABS": "31-14", "IDVISREL": "358"},
    3214: {"COLABS": 32, "FILABS": 14, "ID50M": "0359A",
           "IDVISABS": "32-14", "IDVISREL": "359"},
    3314: {"COLABS": 33, "FILABS": 14, "ID50M": "0360A",
           "IDVISABS": "33-14", "IDVISREL": "360"},
    3414: {"COLABS": 34, "FILABS": 14, "ID50M": "0361A",
           "IDVISABS": "34-14", "IDVISREL": "361"},
    3514: {"COLABS": 35, "FILABS": 14, "ID50M": "0362A",
           "IDVISABS": "35-14", "IDVISREL": "362"},
    3614: {"COLABS": 36, "FILABS": 14, "ID50M": "0363A",
           "IDVISABS": "36-14", "IDVISREL": "363"},
    3714: {"COLABS": 37, "FILABS": 14, "ID50M": "0364A",
           "IDVISABS": "37-14", "IDVISREL": "364"},
    3814: {"COLABS": 38, "FILABS": 14, "ID50M": "0365A",
           "IDVISABS": "38-14", "IDVISREL": "365"},
    3914: {"COLABS": 39, "FILABS": 14, "ID50M": "0366A",
           "IDVISABS": "39-14", "IDVISREL": "366"},
    3115: {"COLABS": 31, "FILABS": 15, "ID50M": "0387A",
           "IDVISABS": "31-15", "IDVISREL": "387"},
    3215: {"COLABS": 32, "FILABS": 15, "ID50M": "0388A",
           "IDVISABS": "32-15", "IDVISREL": "388"},
    3315: {"COLABS": 33, "FILABS": 15, "ID50M": "0389A",
           "IDVISABS": "33-15", "IDVISREL": "389"},
    3415: {"COLABS": 34, "FILABS": 15, "ID50M": "0390A",
           "IDVISABS": "34-15", "IDVISREL": "390"},
    3515: {"COLABS": 35, "FILABS": 15, "ID50M": "0391A",
           "IDVISABS": "35-15", "IDVISREL": "391"},
    3615: {"COLABS": 36, "FILABS": 15, "ID50M": "0392A",
           "IDVISABS": "36-15", "IDVISREL": "392"},
    3715: {"COLABS": 37, "FILABS": 15, "ID50M": "0393A",
           "IDVISABS": "37-15", "IDVISREL": "393"},
    3815: {"COLABS": 38, "FILABS": 15, "ID50M": "0394A",
           "IDVISABS": "38-15", "IDVISREL": "394"},
    3116: {"COLABS": 31, "FILABS": 16, "ID50M": "0415A",
           "IDVISABS": "31-16", "IDVISREL": "415"},
    3216: {"COLABS": 32, "FILABS": 16, "ID50M": "0416A",
           "IDVISABS": "32-16", "IDVISREL": "416"},
    3316: {"COLABS": 33, "FILABS": 16, "ID50M": "0417A",
           "IDVISABS": "33-16", "IDVISREL": "417"},
    3416: {"COLABS": 34, "FILABS": 16, "ID50M": "0418A",
           "IDVISABS": "34-16", "IDVISREL": "418"},
    3516: {"COLABS": 35, "FILABS": 16, "ID50M": "0419A",
           "IDVISABS": "35-16", "IDVISREL": "419"},
    3616: {"COLABS": 36, "FILABS": 16, "ID50M": "0420A",
           "IDVISABS": "36-16", "IDVISREL": "420"},
    3716: {"COLABS": 37, "FILABS": 16, "ID50M": "0421A",
           "IDVISABS": "37-16", "IDVISREL": "421"},
    3117: {"COLABS": 31, "FILABS": 17, "ID50M": "0443A",
           "IDVISABS": "31-17", "IDVISREL": "443"},
    3217: {"COLABS": 32, "FILABS": 17, "ID50M": "0444A",
           "IDVISABS": "32-17", "IDVISREL": "444"},
    3317: {"COLABS": 33, "FILABS": 17, "ID50M": "0445A",
           "IDVISABS": "33-17", "IDVISREL": "445"},
    3417: {"COLABS": 34, "FILABS": 17, "ID50M": "0446A",
           "IDVISABS": "34-17", "IDVISREL": "446"},
    3517: {"COLABS": 35, "FILABS": 17, "ID50M": "0447A",
           "IDVISABS": "35-17", "IDVISREL": "447"},
    3617: {"COLABS": 36, "FILABS": 17, "ID50M": "0448A",
           "IDVISABS": "36-17", "IDVISREL": "448"},
    3717: {"COLABS": 37, "FILABS": 17, "ID50M": "0448C",
           "IDVISABS": "37-17", "IDVISREL": "448C"},
    3118: {"COLABS": 31, "FILABS": 18, "ID50M": "0470A",
           "IDVISABS": "31-18", "IDVISREL": "470"},
    3218: {"COLABS": 32, "FILABS": 18, "ID50M": "0471A",
           "IDVISABS": "32-18", "IDVISREL": "471"},
    3318: {"COLABS": 33, "FILABS": 18, "ID50M": "0472A",
           "IDVISABS": "33-18", "IDVISREL": "472"},
    3418: {"COLABS": 34, "FILABS": 18, "ID50M": "0473A",
           "IDVISABS": "34-18", "IDVISREL": "473"},
    3518: {"COLABS": 35, "FILABS": 18, "ID50M": "0473B",
           "IDVISABS": "35-18", "IDVISREL": "473B"},
    3119: {"COLABS": 31, "FILABS": 19, "ID50M": "0496A",
           "IDVISABS": "31-19", "IDVISREL": "496"},
    3219: {"COLABS": 32, "FILABS": 19, "ID50M": "0497A",
           "IDVISABS": "32-19", "IDVISREL": "497"},
    3319: {"COLABS": 33, "FILABS": 19, "ID50M": "0498A",
           "IDVISABS": "33-19", "IDVISREL": "498"},
    3120: {"COLABS": 31, "FILABS": 20, "ID50M": "0521A",
           "IDVISABS": "31-20", "IDVISREL": "521"},
    3220: {"COLABS": 32, "FILABS": 20, "ID50M": "0522A",
           "IDVISABS": "32-20", "IDVISREL": "522"},
    3320: {"COLABS": 33, "FILABS": 20, "ID50M": "0523A",
           "IDVISABS": "33-20", "IDVISREL": "523"},
    3121: {"COLABS": 31, "FILABS": 21, "ID50M": "0546A",
           "IDVISABS": "31-21", "IDVISREL": "546"},
    3221: {"COLABS": 32, "FILABS": 21, "ID50M": "0547A",
           "IDVISABS": "32-21", "IDVISREL": "547"},
    3321: {"COLABS": 33, "FILABS": 21, "ID50M": "0548A",
           "IDVISABS": "33-21", "IDVISREL": "548"}
}


# -----------------------------------------------------------------------------
# ---- coordenades fulls MTN50 (epsg:4230) NW, NE, SE, SW ----
# epgs: 4230
#
# key = IC50*100 + IF50
#
# Format:
#        key: [ID50, IC50, IF50,
#              glonNW, mlonNW, slonNW, glatNW, mlatNW, slatNW,
#              glonNE, mlonNE, slonNE, glatNE, mlatNE, slatNE,
#              glonSE, mlonSE, slonSE, glatSE, mlatSE, slatSE,
#              glonSW, mlonSW, slonSW, glatSW, mlatSW, slatSW]
# -----------------------------------------------------------------------------
MTN50 = {
    3107: ["118R", 31,  7,
           0,  8, 49.48, 43,  0, 4.16, 0, 28, 49.48, 43,  0, 4.16,
           0, 28, 49.51, 42, 50, 4.14, 0,  8, 49.48, 42, 50, 4.18],
    3207: ["118B", 32,  7,
           0, 28, 49.48, 43,  0, 4.16, 0, 48, 49.50, 43,  0, 4.12,
           0, 48, 49.53, 42, 50, 4.10, 0, 28, 49.51, 42, 50, 4.14],
    3307: ["118C", 33,  7,
           0, 48, 49.50, 43,  0, 4.12, 1,  8, 49.52, 43,  0, 4.12,
           1,  8, 49.52, 42, 50, 4.08, 0, 48, 49.53, 42, 50, 4.10],
    3108: ["147 ", 31,  8,
           0,  8, 49.48, 42, 50, 4.18, 0, 28, 49.51, 42, 50, 4.14,
           0, 28, 49.53, 42, 40, 4.15, 0,  8, 49.51, 42, 40, 4.20],
    3208: ["148 ", 32,  8,
           0, 28, 49.51, 42, 50, 4.14, 0, 48, 49.53, 42, 50, 4.10,
           0, 48, 49.53, 42, 40, 4.12, 0, 28, 49.53, 42, 40, 4.15],
    3308: ["149 ", 33,  8,
           0, 48, 49.53, 42, 50, 4.10, 1,  8, 49.52, 42, 50, 4.08,
           1,  8, 49.55, 42, 40, 4.11, 0, 48, 49.53, 42, 40, 4.12],
    3408: ["150 ", 34,  8,
           1,  8, 49.52, 42, 50, 4.08, 1, 28, 49.52, 42, 50, 4.05,
           1, 28, 49.52, 42, 40, 4.07, 1,  8, 49.55, 42, 40, 4.11],
    3508: ["150B", 35,  8,
           1, 28, 49.52, 42, 50, 4.05, 1, 48, 49.51, 42, 50, 4.02,
           1, 48, 49.51, 42, 40, 4.04, 1, 28, 49.52, 42, 40, 4.07],
    3109: ["179 ", 31,  9,
           0,  8, 49.51, 42, 40, 4.20, 0, 28, 49.53, 42, 40, 4.15,
           0, 28, 49.53, 42, 30, 4.20, 0,  8, 49.52, 42, 30, 4.24],
    3209: ["180 ", 32,  9,
           0, 28, 49.53, 42, 40, 4.15, 0, 48, 49.53, 42, 40, 4.12,
           0, 48, 49.53, 42, 30, 4.14, 0, 28, 49.53, 42, 30, 4.20],
    3309: ["181 ", 33,  9,
           0, 48, 49.53, 42, 40, 4.12, 1,  8, 49.55, 42, 40, 4.11,
           1,  8, 49.55, 42, 30, 4.10, 0, 48, 49.53, 42, 30, 4.14],
    3409: ["182 ", 34,  9,
           1,  8, 49.55, 42, 40, 4.11, 1, 28, 49.52, 42, 40, 4.07,
           1, 28, 49.56, 42, 30, 4.12, 1,  8, 49.55, 42, 30, 4.10],
    3509: ["183 ", 35,  9,
           1, 28, 49.52, 42, 40, 4.07, 1, 48, 49.51, 42, 40, 4.04,
           1, 48, 49.53, 42, 30, 4.07, 1, 28, 49.56, 42, 30, 4.12],
    3609: ["183B", 36,  9,
           1, 48, 49.51, 42, 40, 4.04, 2,  8, 49.49, 42, 40, 4.01,
           2,  8, 49.51, 42, 30, 4.04, 1, 48, 49.53, 42, 30, 4.07],
    3110: ["212 ", 31, 10,
           0,  8, 49.52, 42, 30, 4.24, 0, 28, 49.53, 42, 30, 4.20,
           0, 28, 49.51, 42, 20, 4.20, 0,  8, 49.51, 42, 20, 4.25],
    3210: ["213 ", 32, 10,
           0, 28, 49.53, 42, 30, 4.20, 0, 48, 49.53, 42, 30, 4.14,
           0, 48, 49.53, 42, 20, 4.15, 0, 28, 49.51, 42, 20, 4.20],
    3310: ["214 ", 33, 10,
           0, 48, 49.53, 42, 30, 4.14, 1,  8, 49.55, 42, 30, 4.10,
           1,  8, 49.54, 42, 20, 4.12, 0, 48, 49.53, 42, 20, 4.15],
    3410: ["215 ", 34, 10,
           1,  8, 49.55, 42, 30, 4.10, 1, 28, 49.56, 42, 30, 4.12,
           1, 28, 49.54, 42, 20, 4.13, 1,  8, 49.54, 42, 20, 4.12],
    3510: ["216 ", 35, 10,
           1, 28, 49.56, 42, 30, 4.12, 1, 48, 49.53, 42, 30, 4.07,
           1, 48, 49.53, 42, 20, 4.09, 1, 28, 49.54, 42, 20, 4.13],
    3610: ["217 ", 36, 10,
           1, 48, 49.53, 42, 30, 4.07, 2,  8, 49.51, 42, 30, 4.04,
           2,  8, 49.51, 42, 20, 4.06, 1, 48, 49.53, 42, 20, 4.09],
    3710: ["218 ", 37, 10,
           2,  8, 49.51, 42, 30, 4.04, 2, 28, 49.50, 42, 30, 4.02,
           2, 28, 49.51, 42, 20, 4.05, 2,  8, 49.51, 42, 20, 4.06],
    3810: ["219 ", 38, 10,
           2, 28, 49.50, 42, 30, 4.02, 2, 48, 49.51, 42, 30, 4.00,
           2, 48, 49.51, 42, 20, 4.02, 2, 28, 49.51, 42, 20, 4.05],
    3910: ["220 ", 39, 10,
           2, 48, 49.51, 42, 30, 4.00, 3,  8, 49.51, 42, 30, 3.99,
           3,  8, 49.51, 42, 20, 4.01, 2, 48, 49.51, 42, 20, 4.02],
    4010: ["221 ", 40, 10,
           3,  8, 49.51, 42, 30, 3.99, 3, 28, 49.51, 42, 30, 3.98,
           3, 28, 49.51, 42, 20, 4.00, 3,  8, 49.51, 42, 20, 4.01],
    3111: ["250 ", 31, 11,
           0,  8, 49.51, 42, 20, 4.25, 0, 28, 49.51, 42, 20, 4.20,
           0, 28, 49.49, 42, 10, 4.21, 0,  8, 49.49, 42, 10, 4.25],
    3211: ["251 ", 32, 11,
           0, 28, 49.51, 42, 20, 4.20, 0, 48, 49.53, 42, 20, 4.15,
           0, 48, 49.52, 42, 10, 4.17, 0, 28, 49.49, 42, 10, 4.21],
    3311: ["252 ", 33, 11,
           0, 48, 49.53, 42, 20, 4.15, 1,  8, 49.54, 42, 20, 4.12,
           1,  8, 49.51, 42, 10, 4.15, 0, 48, 49.52, 42, 10, 4.17],
    3411: ["253 ", 34, 11,
           1,  8, 49.54, 42, 20, 4.12, 1, 28, 49.54, 42, 20, 4.13,
           1, 28, 49.51, 42, 10, 4.13, 1,  8, 49.51, 42, 10, 4.15],
    3511: ["254 ", 35, 11,
           1, 28, 49.54, 42, 20, 4.13, 1, 48, 49.53, 42, 20, 4.09,
           1, 48, 49.51, 42, 10, 4.10, 1, 28, 49.51, 42, 10, 4.13],
    3611: ["255 ", 36, 11,
           1, 48, 49.53, 42, 20, 4.09, 2,  8, 49.51, 42, 20, 4.06,
           2,  8, 49.51, 42, 10, 4.09, 1, 48, 49.51, 42, 10, 4.10],
    3711: ["256 ", 37, 11,
           2,  8, 49.51, 42, 20, 4.06, 2, 28, 49.51, 42, 20, 4.05,
           2, 28, 49.51, 42, 10, 4.08, 2,  8, 49.51, 42, 10, 4.09],
    3811: ["257 ", 38, 11,
           2, 28, 49.51, 42, 20, 4.05, 2, 48, 49.51, 42, 20, 4.02,
           2, 48, 49.52, 42, 10, 4.04, 2, 28, 49.51, 42, 10, 4.08],
    3911: ["258 ", 39, 11,
           2, 48, 49.51, 42, 20, 4.02, 3,  8, 49.51, 42, 20, 4.01,
           3,  8, 49.51, 42, 10, 4.03, 2, 48, 49.52, 42, 10, 4.04],
    4011: ["259 ", 40, 11,
           3,  8, 49.51, 42, 20, 4.01, 3, 28, 49.51, 42, 20, 4.00,
           3, 28, 49.51, 42, 10, 4.02, 3,  8, 49.51, 42, 10, 4.03],
    3112: ["288 ", 31, 12,
           0,  8, 49.49, 42, 10, 4.25, 0, 28, 49.49, 42, 10, 4.21,
           0, 28, 49.49, 42,  0, 4.23, 0,  8, 49.48, 42,  0, 4.26],
    3212: ["289 ", 32, 12,
           0, 28, 49.49, 42, 10, 4.21, 0, 48, 49.52, 42, 10, 4.17,
           0, 48, 49.51, 42,  0, 4.20, 0, 28, 49.49, 42,  0, 4.23],
    3312: ["290 ", 33, 12,
           0, 48, 49.52, 42, 10, 4.17, 1,  8, 49.51, 42, 10, 4.15,
           1,  8, 49.51, 42,  0, 4.17, 0, 48, 49.51, 42,  0, 4.20],
    3412: ["291 ", 34, 12,
           1,  8, 49.51, 42, 10, 4.15, 1, 28, 49.51, 42, 10, 4.13,
           1, 28, 49.51, 42,  0, 4.15, 1,  8, 49.51, 42,  0, 4.17],
    3512: ["292 ", 35, 12,
           1, 28, 49.51, 42, 10, 4.13, 1, 48, 49.51, 42, 10, 4.10,
           1, 48, 49.51, 42,  0, 4.12, 1, 28, 49.51, 42,  0, 4.15],
    3612: ["293 ", 36, 12,
           1, 48, 49.51, 42, 10, 4.10, 2,  8, 49.51, 42, 10, 4.09,
           2,  8, 49.51, 42,  0, 4.10, 1, 48, 49.51, 42,  0, 4.12],
    3712: ["294 ", 37, 12,
           2,  8, 49.51, 42, 10, 4.09, 2, 28, 49.51, 42, 10, 4.08,
           2, 28, 49.51, 42,  0, 4.09, 2,  8, 49.51, 42,  0, 4.10],
    3812: ["295 ", 38, 12,
           2, 28, 49.51, 42, 10, 4.08, 2, 48, 49.52, 42, 10, 4.04,
           2, 48, 49.53, 42,  0, 4.06, 2, 28, 49.51, 42,  0, 4.09],
    3912: ["296 ", 39, 12,
           2, 48, 49.52, 42, 10, 4.04, 3,  8, 49.51, 42, 10, 4.03,
           3,  8, 49.51, 42,  0, 4.05, 2, 48, 49.53, 42,  0, 4.06],
    4012: ["297 ", 40, 12,
           3,  8, 49.51, 42, 10, 4.03, 3, 28, 49.51, 42, 10, 4.02,
           3, 28, 49.48, 42,  0, 4.05, 3,  8, 49.51, 42,  0, 4.05],
    3113: ["326 ", 31, 13,
           0,   8, 49.48, 42,  0, 4.26, 0, 28, 49.49, 42,  0, 4.23,
           0, 28, 49.49, 41, 50, 4.25, 0,   8, 49.48, 41, 50, 4.27],
    3213: ["327 ", 32, 13,
           0,  28, 49.49, 42,  0, 4.23, 0, 48, 49.51, 42,  0, 4.20,
           0, 48, 49.51, 41, 50, 4.22, 0,  28, 49.49, 41, 50, 4.25],
    3313: ["328 ", 33, 13,
           0,  48, 49.51, 42,  0, 4.20, 1,  8, 49.51, 42,  0, 4.17,
           1,  8, 49.51, 41, 50, 4.20, 0,  48, 49.51, 41, 50, 4.22],
    3413: ["329 ", 34, 13,
           1,   8, 49.51, 42,  0, 4.17, 1, 28, 49.51, 42,  0, 4.15,
           1, 28, 49.51, 41, 50, 4.17, 1,   8, 49.51, 41, 50, 4.20],
    3513: ["330 ", 35, 13,
           1,  28, 49.51, 42,  0, 4.15, 1, 48, 49.51, 42,  0, 4.12,
           1, 48, 49.51, 41, 50, 4.15, 1,  28, 49.51, 41, 50, 4.17],
    3613: ["331 ", 36, 13,
           1,  48, 49.51, 42,  0, 4.12, 2,  8, 49.51, 42,  0, 4.10,
           2,  8, 49.51, 41, 50, 4.12, 1,  48, 49.51, 41, 50, 4.15],
    3713: ["332 ", 37, 13,
           2,   8, 49.51, 42,  0, 4.10, 2, 28, 49.51, 42,  0, 4.09,
           2, 28, 49.51, 41, 50, 4.10, 2,   8, 49.51, 41, 50, 4.12],
    3813: ["333 ", 38, 13,
           2,  28, 49.51, 42,  0, 4.09, 2, 48, 49.53, 42,  0, 4.06,
           2, 48, 49.52, 41, 50, 4.08, 2,  28, 49.51, 41, 50, 4.10],
    3913: ["334 ", 39, 13,
           2,  48, 49.53, 42,  0, 4.06, 3,  8, 49.51, 42,  0, 4.05,
           3,  8, 49.51, 41, 50, 4.08, 2,  48, 49.52, 41, 50, 4.08],
    4013: ["335 ", 40, 13,
           3,   8, 49.51, 42,  0, 4.05, 3, 28, 49.48, 42,  0, 4.05,
           3, 28, 49.48, 41, 50, 4.07, 3,   8, 49.51, 41, 50, 4.08],
    3114: ["358 ", 31, 14,
           0,   8, 49.48, 41, 50, 4.27, 0, 28, 49.49, 41, 50, 4.25,
           0, 28, 49.49, 41, 40, 4.27, 0,   8, 49.48, 41, 40, 4.28],
    3214: ["359 ", 32, 14,
           0,  28, 49.49, 41, 50, 4.25, 0, 48, 49.51, 41, 50, 4.22,
           0, 48, 49.50, 41, 40, 4.24, 0,  28, 49.49, 41, 40, 4.27],
    3314: ["360 ", 33, 14,
           0,  48, 49.51, 41, 50, 4.22, 1,  8, 49.51, 41, 50, 4.20,
           1,  8, 49.50, 41, 40, 4.20, 0,  48, 49.50, 41, 40, 4.24],
    3414: ["361 ", 34, 14,
           1,   8, 49.51, 41, 50, 4.20, 1, 28, 49.51, 41, 50, 4.17,
           1, 28, 49.49, 41, 40, 4.16, 1,   8, 49.50, 41, 40, 4.20],
    3514: ["362 ", 35, 14,
           1,  28, 49.51, 41, 50, 4.17, 1, 48, 49.51, 41, 50, 4.15,
           1, 48, 49.49, 41, 40, 4.14, 1,  28, 49.49, 41, 40, 4.16],
    3614: ["363 ", 36, 14,
           1,  48, 49.51, 41, 50, 4.15, 2,  8, 49.51, 41, 50, 4.12,
           2,  8, 49.50, 41, 40, 4.12, 1,  48, 49.49, 41, 40, 4.14],
    3714: ["364 ", 37, 14,
           2,   8, 49.51, 41, 50, 4.12, 2, 28, 49.51, 41, 50, 4.10,
           2, 28, 49.51, 41, 40, 4.11, 2,   8, 49.50, 41, 40, 4.12],
    3814: ["365 ", 38, 14,
           2,  28, 49.51, 41, 50, 4.10, 2, 48, 49.52, 41, 50, 4.08,
           2, 48, 49.52, 41, 40, 4.09, 2,  28, 49.51, 41, 40, 4.11],
    3914: ["366 ", 39, 14,
           2,  48, 49.52, 41, 50, 4.08, 3,  8, 49.51, 41, 50, 4.08,
           3,  8, 49.52, 41, 40, 4.08, 2,  48, 49.52, 41, 40, 4.09],
    3115: ["387 ", 31, 15,
           0,   8, 49.48, 41, 40, 4.28, 0, 28, 49.49, 41, 40, 4.27,
           0, 28, 49.48, 41, 30, 4.28, 0,   8, 49.47, 41, 30, 4.29],
    3215: ["388 ", 32, 15,
           0,  28, 49.49, 41, 40, 4.27, 0, 48, 49.50, 41, 40, 4.24,
           0, 48, 49.50, 41, 30, 4.24, 0,  28, 49.48, 41, 30, 4.28],
    3315: ["389 ", 33, 15,
           0,  48, 49.50, 41, 40, 4.24, 1,  8, 49.50, 41, 40, 4.20,
           1,  8, 49.47, 41, 30, 4.18, 0,  48, 49.50, 41, 30, 4.24],
    3415: ["390 ", 34, 15,
           1,   8, 49.50, 41, 40, 4.20, 1, 28, 49.49, 41, 40, 4.16,
           1, 28, 49.47, 41, 30, 4.14, 1,   8, 49.47, 41, 30, 4.18],
    3515: ["391 ", 35, 15,
           1,  28, 49.49, 41, 40, 4.16, 1, 48, 49.49, 41, 40, 4.14,
           1, 48, 49.47, 41, 30, 4.13, 1,  28, 49.47, 41, 30, 4.14],
    3615: ["392 ", 36, 15,
           1,  48, 49.49, 41, 40, 4.14, 2,  8, 49.50, 41, 40, 4.12,
           2,  8, 49.49, 41, 30, 4.12, 1,  48, 49.47, 41, 30, 4.13],
    3715: ["393 ", 37, 15,
           2,   8, 49.50, 41, 40, 4.12, 2, 28, 49.51, 41, 40, 4.11,
           2, 28, 49.50, 41, 30, 4.11, 2,   8, 49.49, 41, 30, 4.12],
    3815: ["394 ", 38, 15,
           2,  28, 49.51, 41, 40, 4.11, 2, 48, 49.52, 41, 40, 4.09,
           2, 48, 49.50, 41, 30, 4.10, 2,  28, 49.50, 41, 30, 4.11],
    3116: ["415 ", 31, 16,
           0,   8, 49.47, 41, 30, 4.29, 0, 28, 49.48, 41, 30, 4.28,
           0, 28, 49.44, 41, 20, 4.28, 0,   8, 49.45, 41, 20, 4.29],
    3216: ["416 ", 32, 16,
           0,  28, 49.48, 41, 30, 4.28, 0, 48, 49.50, 41, 30, 4.24,
           0, 48, 49.49, 41, 20, 4.25, 0,  28, 49.44, 41, 20, 4.28],
    3316: ["417 ", 33, 16,
           0,  48, 49.50, 41, 30, 4.24, 1,  8, 49.47, 41, 30, 4.18,
           1,  8, 49.48, 41, 20, 4.20, 0,  48, 49.49, 41, 20, 4.25],
    3416: ["418 ", 34, 16,
           1,   8, 49.47, 41, 30, 4.18, 1, 28, 49.47, 41, 30, 4.14,
           1, 28, 49.43, 41, 20, 4.15, 1,   8, 49.48, 41, 20, 4.20],
    3516: ["419 ", 35, 16,
           1,  28, 49.47, 41, 30, 4.14, 1, 48, 49.47, 41, 30, 4.13,
           1, 48, 49.46, 41, 20, 4.12, 1,  28, 49.43, 41, 20, 4.15],
    3616: ["420 ", 36, 16,
           1,  48, 49.47, 41, 30, 4.13, 2,  8, 49.49, 41, 30, 4.12,
           2,  8, 49.48, 41, 20, 4.12, 1,  48, 49.46, 41, 20, 4.12],
    3716: ["421 ", 37, 16,
           2,   8, 49.49, 41, 30, 4.12, 2, 28, 49.50, 41, 30, 4.11,
           2, 28, 49.49, 41, 20, 4.11, 2,   8, 49.48, 41, 20, 4.12],
    3117: ["443 ", 31, 17,
           0,   8, 49.45, 41, 20, 4.29, 0, 28, 49.44, 41, 20, 4.28,
           0, 28, 49.37, 41, 10, 4.28, 0,   8, 49.47, 41, 10, 4.18],
    3217: ["444 ", 32, 17,
           0,  28, 49.44, 41, 20, 4.28, 0, 48, 49.49, 41, 20, 4.25,
           0, 48, 49.35, 41, 10, 4.24, 0,  28, 49.37, 41, 10, 4.28],
    3317: ["445 ", 33, 17,
           0,  48, 49.49, 41, 20, 4.25, 1,  8, 49.48, 41, 20, 4.20,
           1,  8, 49.38, 41, 10, 4.21, 0,  48, 49.35, 41, 10, 4.24],
    3417: ["446 ", 34, 17,
           1,   8, 49.48, 41, 20, 4.20, 1, 28, 49.43, 41, 20, 4.15,
           1, 28, 49.37, 41, 10, 4.17, 1,   8, 49.38, 41, 10, 4.21],
    3517: ["447 ", 35, 17,
           1,  28, 49.43, 41, 20, 4.15, 1, 48, 49.46, 41, 20, 4.12,
           1, 48, 49.41, 41, 10, 4.15, 1,  28, 49.37, 41, 10, 4.17],
    3617: ["448 ", 36, 17,
           1,  48, 49.46, 41, 20, 4.12, 2,  8, 49.48, 41, 20, 4.12,
           2,  8, 49.47, 41, 10, 4.11, 1,  48, 49.41, 41, 10, 4.15],
    3717: ["448C", 37, 17,
           2,   8, 49.48, 41, 20, 4.12, 2, 28, 49.49, 41, 20, 4.11,
           2, 28, 49.47, 41, 10, 4.12, 2,   8, 49.47, 41, 10, 4.11],
    3118: ["470 ", 31, 18,
           0,   8, 49.47, 41, 10, 4.18, 0, 28, 49.37, 41, 10, 4.28,
           0, 28, 49.33, 41,  0, 4.28, 0,   8, 49.42, 41,  0, 4.22],
    3218: ["471 ", 32, 18,
           0,  28, 49.37, 41, 10, 4.28, 0, 48, 49.35, 41, 10, 4.24,
           0, 48, 49.29, 41,  0, 4.25, 0,  28, 49.33, 41,  0, 4.28],
    3318: ["472 ", 33, 18,
           0,  48, 49.35, 41, 10, 4.24, 1,  8, 49.38, 41, 10, 4.21,
           1,  8, 49.30, 41,  0, 4.23, 0,  48, 49.29, 41,  0, 4.25],
    3418: ["473 ", 34, 18,
           1,   8, 49.38, 41, 10, 4.21, 1, 28, 49.37, 41, 10, 4.17,
           1, 28, 49.31, 41,  0, 4.20, 1,   8, 49.30, 41,  0, 4.23],
    3518: ["473B", 35, 18,
           1,  28, 49.37, 41, 10, 4.17, 1, 48, 49.41, 41, 10, 4.15,
           1, 48, 49.41, 41,  0, 4.18, 1,  28, 49.31, 41,  0, 4.20],
    3119: ["496 ", 31, 19,
           0,   8, 49.42, 41,  0, 4.22, 0, 28, 49.33, 41,  0, 4.28,
           0, 28, 49.30, 40, 50, 4.30, 0,   8, 49.37, 40, 50, 4.30],
    3219: ["497 ", 32, 19,
           0,  28, 49.33, 41,  0, 4.28, 0, 48, 49.29, 41,  0, 4.25,
           0, 48, 49.28, 40, 50, 4.28, 0,  28, 49.30, 40, 50, 4.30],
    3319: ["498 ", 33, 19,
           0,  48, 49.29, 41,  0, 4.25, 1,  8, 49.30, 41,  0, 4.23,
           1,  8, 49.29, 40, 50, 4.26, 0,  48, 49.28, 40, 50, 4.28],
    3120: ["521 ", 31, 20,
           0,   8, 49.37, 40, 50, 4.30, 0, 28, 49.30, 40, 50, 4.30,
           0, 28, 49.28, 40, 40, 4.33, 0,   8, 49.33, 40, 40, 4.37],
    3220: ["522 ", 32, 20,
           0,  28, 49.30, 40, 50, 4.30, 0, 48, 49.28, 40, 50, 4.28,
           0, 48, 49.26, 40, 40, 4.31, 0,  28, 49.28, 40, 40, 4.33],
    3320: ["523 ", 33, 20,
           0,  48, 49.28, 40, 50, 4.28, 1,  8, 49.29, 40, 50, 4.26,
           1,  8, 49.28, 40, 40, 4.29, 0,  48, 49.26, 40, 40, 4.31],
    3121: ["546 ", 31, 21,
           0,   8, 49.33, 40, 40, 4.37, 0, 28, 49.28, 40, 40, 4.33,
           0, 28, 49.27, 40, 30, 4.37, 0,   8, 49.32, 40, 30, 4.41],
    3221: ["547 ", 32, 21,
           0,  28, 49.28, 40, 40, 4.33, 0, 48, 49.26, 40, 40, 4.31,
           0, 48, 49.24, 40, 30, 4.34, 0,  28, 49.27, 40, 30, 4.37],
    3321: ["547C", 33, 21,
           0,  48, 49.26, 40, 40, 4.31, 1,  8, 49.28, 40, 40, 4.29,
           1,  8, 49.26, 40, 30, 4.32, 0,  48, 49.24, 40, 30, 4.34],
    3122: ["571 ", 31, 22,
           0,   8, 49.32, 40, 30, 4.41, 0, 28, 49.27, 40, 30, 4.37,
           0, 28, 49.26, 40, 20, 4.42, 0,   8, 49.30, 40, 20, 4.46],
    3222: ["571B", 32, 22,
           0,  28, 49.27, 40, 30, 4.37, 0, 48, 49.24, 40, 30, 4.34,
           0, 48, 49.21, 40, 20, 4.38, 0,  28, 49.26, 40, 20, 4.42]
        }
