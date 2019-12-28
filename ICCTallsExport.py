# -----------------------------------------------------------------------------
# Name:      ICCTallsExport
# Purpose:   Generar arxius SHP amb tots els fulls que composen els talls ICC
#            descrits a l'article:
#
#            Macau, M., Colomina, I. 1987.
#            La generacio de talls geodesics en la cartografia de Catalunya
#            per a escales 1:50000 i mes grans
#            RCG n.5, juliol 1987, volum II. pp.16-31
#
# Author:      atermens
# Created:     31/05/2019
# Copyright:   (c) a.termens 2019
# License:     CC BY 4.0
# -----------------------------------------------------------------------------
#
# Estructura de dades d'un full:
#
#     "tall": kTall (key dt.TALLS) [string]
#     "IC":   columna absoluta full [integer]
#     "IF":   fila absoluta full [integer]
#     "epsg": 4230
#     "tp":   key dt.TALLS del tall pare = dt.TALLS[kTall][0]
#     "CTOT": particio total columnes del tall pare = dt.TALLS[kTall][1]
#     "FTOT": particio total files del tall pare = dt.TALLS[kTall][2]
#     "ICtp": columna full pare
#     "IFtp": fila full pare
#     "IDtp": identificador sequencial full pare
#     "CR":   columna relativa
#     "FR":   fila relativa
#     "NW":   [x, y] cantonada NW
#     "NE":   [x, y] cantonada NE
#     "SE":   [x, y] cantonada SE
#     "SW":   [x, y] cantonada SW
#     "polyline": [[xNW, yNW], [xNE, yNE], [xSE, ySE], [xSW, SNW], [xNW, yNW]]
#                 poligon que defineix el full a partir de les cantonades.
#
# -----------------------------------------------------------------------------
# !/usr/bin/env python

import ICCTallsExportData as dt
import ICCTallsExportTools as tt


# -----------------------------------------------------------------------------
# carreguem la informacio associada al diccionari MTN50.
#
# d >> [ID50, IC50, IF50,
#       glonNW, mlonNW, slonNW, glatNW, mlatNW, slatNW,
#       glonNE, mlonNE, slonNE, glatNE, mlatNE, slatNE,
#       glonSE, mlonSE, slonSE, glatSE, mlatSE, slatSE,
#       glonSW, mlonSW, slonSW, glatSW, mlatSW, slatSW]
# -----------------------------------------------------------------------------

def load_mtn50():
    kTall = "Tall50K"

    tp_code = dt.TALLS[kTall][0]
    ctot = dt.TALLS[kTall][1]
    ftot = dt.TALLS[kTall][2]
    epsg_code = dt.TALLS[kTall][5]

    tbase = {}
    for k50 in dt.MTN50.keys():
        # --- obtenim cantonades ---
        d = dt.MTN50[k50]
        nw = [tt.de2dd(d[3], d[4], d[5]), tt.de2dd(d[6], d[7], d[8])]
        ne = [tt.de2dd(d[9], d[10], d[11]), tt.de2dd(d[12], d[13], d[14])]
        se = [tt.de2dd(d[15], d[16], d[17]), tt.de2dd(d[18], d[19], d[20])]
        sw = [tt.de2dd(d[21], d[22], d[23]), tt.de2dd(d[24], d[25], d[26])]
        # --- farcim estructura dades ---
        full = {}
        full["tall"] = kTall
        full["IC"] = d[1]
        full["IF"] = d[2]
        full["epsg"] = epsg_code
        full["tp"] = tp_code
        full["CTOT"] = ctot
        full["FTOT"] = ftot
        full["ICtp"] = full["IC"]
        full["IFtp"] = full["IF"]
        full["IDtp"] = d[0]
        full["CR"] = 1
        full["FR"] = 1
        full["NW"] = nw
        full["NE"] = ne
        full["SE"] = se
        full["SW"] = sw
        full["polyline"] = [nw, ne, se, sw, nw]
        tbase[k50] = full

    return tbase


# -----------------------------------------------------------------------------
# carreguem la informacio associada al diccionari T100.
#
# d >> [IC100, IF100, xNW, yNW, xNE, yNE, xSE, ySE, xNW, yNW]
# -----------------------------------------------------------------------------

def load_T100():
    kTall = "Tall100K"

    tp_code = dt.TALLS[kTall][0]
    ctot = dt.TALLS[kTall][1]
    ftot = dt.TALLS[kTall][2]
    epsg_code = dt.TALLS[kTall][5]

    tbase = {}
    for k100 in dt.T100.keys():
        # --- obtenim cantonades ---
        d = dt.T100[k100]
        nw = [d[2], d[3]]
        ne = [d[4], d[5]]
        se = [d[6], d[7]]
        sw = [d[8], d[9]]
        # --- farcim estructura dades ---
        full = {}
        full["tall"] = kTall
        full["IC"] = d[0]
        full["IF"] = d[1]
        full["epsg"] = epsg_code
        full["tp"] = tp_code
        full["CTOT"] = ctot
        full["FTOT"] = ftot
        full["ICtp"] = full["IC"]
        full["IFtp"] = full["IF"]
        full["IDtp"] = "-"
        full["CR"] = 1
        full["FR"] = 1
        full["NW"] = nw
        full["NE"] = ne
        full["SE"] = se
        full["SW"] = sw
        full["polyline"] = [nw, ne, se, sw, nw]
        tbase[k100] = full

    return tbase


# -----------------------------------------------------------------------------
# CONVERSIO DE SEQUENCIAL A COLUMNA-FILA I VICEVERSA
# -----------------------------------------------------------------------------
def cf2seq(col, row):
    k50 = col*100 + row
    if k50 in dt.IDTALLBASE.keys():
        return dt.IDTALLBASE[k50]["IDVISREL"]
    else:
        return " "


def seq2cf(seq):
    for k50 in dt.IDTALLBASE.keys():
        if dt.IDTALLBASE[k50]["IDVISREL"] == seq:
            col = dt.IDTALLBASE[k50]["COLABS"]
            row = dt.IDTALLBASE[k50]["FILABS"]
            return [col, row]
    return []


# -----------------------------------------------------------------------------
# Retorn de tots els fulls que composen un tall donat
# -----------------------------------------------------------------------------
def setKey(iC, iF):
    return str(iC)+"_"+str(iF)


def getTall50K():
    print ' '
    print '     processing getTall50K ...'
    mtn50 = load_mtn50()

    tall = {}
    for k50 in dt.IDTALLBASE.keys():
        if k50 in mtn50.keys():
            ic50 = mtn50[k50]["IC"]
            if50 = mtn50[k50]["IF"]
            kk = setKey(ic50, if50)
            tall[kk] = mtn50[k50]
        else:
            print "Full sense coordenades: ", k50

    print '     num. fulls: ', len(tall)
    return tall


def getTall100K():
    print ' '
    print '     processing getTall100K ...'
    t100 = load_T100()

    tall = {}
    for i in range(len(dt.IC100)):
        ic100 = dt.IC100[i]
        if100 = dt.IF100[i]
        k100 = 100*ic100 + if100
        if k100 in t100.keys():
            kk = setKey(ic100, if100)
            tall[kk] = t100[k100]
        else:
            print "Full sense coordenades: ", k100

    print '     num. fulls: ', len(tall)
    return tall


def getTallFill50(kTall, tpare):
    print ' '
    print '     processing getTallFill50 ' + kTall + ' ...'
    tp_code = dt.TALLS[kTall][0]
    ctot = dt.TALLS[kTall][1]
    ftot = dt.TALLS[kTall][2]
    epsg_code = dt.TALLS[kTall][5]

    if tp_code != "Tall50K":
        return {}

    tall = {}
    for k50 in tpare.keys():
        ic50 = tpare[k50]["IC"]
        if50 = tpare[k50]["IF"]
        pN = tt.segment(ctot, tpare[k50]["NW"], tpare[k50]["NE"])
        pS = tt.segment(ctot, tpare[k50]["SW"], tpare[k50]["SE"])
        pE = tt.segment(ftot, tpare[k50]["NE"], tpare[k50]["SE"])
        pW = tt.segment(ftot, tpare[k50]["NW"], tpare[k50]["SW"])
        # el full cr-fr esta definit per aquests costats
        #  nord -- pW(fr-1) pE(fr-1)
        #  sud  -- pW(fr)   pE(fr)
        #  oest -- pN(cr-1) pS(cr-1)
        #  est  -- pN(cr)   pS(cr)
        for fr in range(1, ftot+1):
            iffill = ftot*(if50-1) + fr
            for cr in range(1, ctot+1):
                icfill = ctot*(ic50-1) + cr
                nw = tt.intersecta(pN[cr-1], pS[cr-1], pW[fr-1], pE[fr-1])
                ne = tt.intersecta(pN[cr], pS[cr], pW[fr-1], pE[fr-1])
                se = tt.intersecta(pN[cr], pS[cr], pW[fr], pE[fr])
                sw = tt.intersecta(pN[cr-1], pS[cr-1], pW[fr], pE[fr])
                kk = setKey(icfill, iffill)
                full = {}
                full["tall"] = kTall
                full["IC"] = icfill
                full["IF"] = iffill
                full["epsg"] = epsg_code
                full["tp"] = tp_code
                full["CTOT"] = ctot
                full["FTOT"] = ftot
                full["ICtp"] = ic50
                full["IFtp"] = if50
                full["IDtp"] = tpare[k50]["IDtp"]
                full["CR"] = cr
                full["FR"] = fr
                full["NW"] = nw
                full["NE"] = ne
                full["SE"] = se
                full["SW"] = sw
                full["polyline"] = [nw, ne, se, sw, nw]
                tall[kk] = full
    print '     num. fulls: ', len(tall)
    return tall


def getTall2Kicc(tpare):
    print ' '
    print '     processing getTall2Kicc ...'
    kTall = "Tall2Kicc"

    tp_code = dt.TALLS[kTall][0]
    ctot = dt.TALLS[kTall][1]
    ftot = dt.TALLS[kTall][2]
    epsg_code = dt.TALLS[kTall][5]

    cc = ['A', 'B', 'C', 'D', 'E']

    tall = {}
    for k10 in tpare.keys():
        ic10 = tpare[k10]["IC"]
        if10 = tpare[k10]["IF"]
        pN = tt.segment(ctot, tpare[k10]["NW"], tpare[k10]["NE"])
        pS = tt.segment(ctot, tpare[k10]["SW"], tpare[k10]["SE"])
        pE = tt.segment(ftot, tpare[k10]["NE"], tpare[k10]["SE"])
        pW = tt.segment(ftot, tpare[k10]["NW"], tpare[k10]["SW"])
        # el full cr-fr esta definit per aquests costats
        #  nord -- pW(fr-1) pE(fr-1)
        #  sud  -- pW(fr)   pE(fr)
        #  oest -- pN(cr-1) pS(cr-1)
        #  est  -- pN(cr)   pS(cr)
        for fr in range(1, ftot+1):
            if2 = ftot*(if10-1) + fr
            for cr in range(1, ctot+1):
                ic2 = ctot*(ic10-1) + cr
                nw = tt.intersecta(pN[cr-1], pS[cr-1], pW[fr-1], pE[fr-1])
                ne = tt.intersecta(pN[cr], pS[cr], pW[fr-1], pE[fr-1])
                se = tt.intersecta(pN[cr], pS[cr], pW[fr], pE[fr])
                sw = tt.intersecta(pN[cr-1], pS[cr-1], pW[fr], pE[fr])
                kk = setKey(ic2, if2)
                full = {}
                full["tall"] = kTall
                full["IC"] = ic2
                full["IF"] = if2
                full["epsg"] = epsg_code
                full["tp"] = tp_code
                full["CTOT"] = ctot
                full["FTOT"] = ftot
                full["ICtp"] = ic10
                full["IFtp"] = if10
                full["IDtp"] = setKey(ic10, if10)
                full["CR"] = cc[cr-1]
                full["FR"] = fr
                full["NW"] = nw
                full["NE"] = ne
                full["SE"] = se
                full["SW"] = sw
                full["polyline"] = [nw, ne, se, sw, nw]
                tall[kk] = full

    print '     num. fulls: ', len(tall)
    return tall


# -----------------------------------------------------------------------------
# 500 CMB
# -----------------------------------------------------------------------------
def getTall5Ccmb(tpare):
    print ' '
    print '     processing getTall5Ccmb ...'
    kTall = "Tall5Ccmb"

    tp_code = dt.TALLS[kTall][0]
    ctot = dt.TALLS[kTall][1]
    ftot = dt.TALLS[kTall][2]
    epsg_code = dt.TALLS[kTall][5]

    tall = {}
    for k2 in tpare.keys():
        ic2 = tpare[k2]["IC"]
        if2 = tpare[k2]["IF"]
        pN = tt.segment(ctot, tpare[k2]["NW"], tpare[k2]["NE"])
        pS = tt.segment(ctot, tpare[k2]["SW"], tpare[k2]["SE"])
        pE = tt.segment(ftot, tpare[k2]["NE"], tpare[k2]["SE"])
        pW = tt.segment(ftot, tpare[k2]["NW"], tpare[k2]["SW"])
        # el full cr-fr esta definit per aquests costats
        #  nord -- pW(fr-1) pE(fr-1)
        #  sud  -- pW(fr)   pE(fr)
        #  oest -- pN(cr-1) pS(cr-1)
        #  est  -- pN(cr)   pS(cr)
        for fr in range(1, ftot+1):
            if5c = ftot*(if2-1) + fr
            for cr in range(1, ctot+1):
                ic5c = ctot*(ic2-1) + cr
                nw = tt.intersecta(pN[cr-1], pS[cr-1], pW[fr-1], pE[fr-1])
                ne = tt.intersecta(pN[cr], pS[cr], pW[fr-1], pE[fr-1])
                se = tt.intersecta(pN[cr], pS[cr], pW[fr], pE[fr])
                sw = tt.intersecta(pN[cr-1], pS[cr-1], pW[fr], pE[fr])
                kk = setKey(ic5c, if5c)
                full = {}
                full["tall"] = kTall
                full["IC"] = ic5c
                full["IF"] = if5c
                full["epsg"] = epsg_code
                full["tp"] = tp_code
                full["CTOT"] = ctot
                full["FTOT"] = ftot
                full["ICtp"] = ic2
                full["IFtp"] = if2
                full["IDtp"] = "none"
                full["CR"] = cr
                full["FR"] = fr
                full["NW"] = nw
                full["NE"] = ne
                full["SE"] = se
                full["SW"] = sw
                full["polyline"] = [nw, ne, se, sw, nw]
                tall[kk] = full

    print '     num. fulls: ', len(tall)
    return tall


# -----------------------------------------------------------------------------
# generem arxiu geojson amb tots els fulls del tall que el composen
#
# Format de sortida geoJSON:
#
# {
#   "type": "FeatureCollection",
#   "crs": { "type": "name",
#            "properties": { "name": "urn:ogc:def:crs:EPSG::25831" } },
# ...
#   "features": [
#       { "type": "Feature",
#          "properties": { "ID100MABS": "16-4",
#                          "SHAPE_Leng": 183097.266814,
#                          "SHAPE_Area": 2018900429.760000 },
#          "geometry": { "type": "Polygon",
#                        "coordinates": [ [
#                            [ 320795.9775, 4728433.126299999654 ],
#                            [ 320736.073800000362098, 4726119.6117 ],
#                            [ 317321.381299999542534, 4726208.85339999944 ],
#                            [ 313906.680800000205636, 4726299.780899999663 ],
#                            [ 320795.9775, 4728433.126299999654 ]
#                            ] ] }
#       },
#       ...
#       { "type": "Feature",
#         "properties": {
#                         "ID100MABS": "16-4",
#                         "SHAPE_Leng": 183097.266814,
#                         "SHAPE_Area": 2018900429.760000
#                       },
#         "geometry": { "type": "Polygon",
#                       "coordinates": [
#                         [
#                           [ 320795.9775, 4728433.126299999654 ],
#                           [ 320736.073800000362098, 4726119.6117 ],
#                           [ 317321.381299999542534, 4726208.85339999944 ],
#                           [ 313906.680800000205636, 4726299.780899999663 ],
#                           [ 320795.9775, 4728433.126299999654 ]
#                         ]
#                       ]
#                     }
#        } ]
# }
#
# -----------------------------------------------------------------------------
def exportGeoJSON(kTall, tall):
    print '     processing ' + kTall + '.geojson ...'
    epsg_code = dt.TALLS[kTall][5]

    # agafem el nom de l'arxiu del camp "tall" associat a tots els fulls
    fout = open(kTall+".geojson", "w")

    fout.write('{ \n')
    fout.write(' "type": "FeatureCollection", \n')

    msgCRS = ' "crs": { "type": "name",'
    msgCRS += ' "properties": { "name": "urn:ogc:def:crs:'
    msgCRS += epsg_code
    msgCRS += '" } }, \n'
    fout.write(msgCRS)

    fout.write(' "features": [ \n')
    iP = 0
    for kk in tall.keys():
        full = tall[kk]
        msgFULL = ' { "type": "Feature", '
        msgFULL += ' "properties": {'
        msgFULL += ' "tall": "' + full["tall"] + '",'
        msgFULL += ' "IC": ' + str(full["IC"]) + ','
        msgFULL += ' "IF": ' + str(full["IF"]) + ','
        msgFULL += ' "tp": "' + full["tp"] + '",'
        msgFULL += ' "CTOT": ' + str(full["CTOT"]) + ','
        msgFULL += ' "FTOT": ' + str(full["FTOT"]) + ','
        msgFULL += ' "ICtp": ' + str(full["ICtp"]) + ','
        msgFULL += ' "IFtp": ' + str(full["IFtp"]) + ','
        msgFULL += ' "IDtp": "' + full["IDtp"] + '",'
        msgFULL += ' "CR": ' + str(full["CR"]) + ','
        msgFULL += ' "FR": ' + str(full["FR"]) + ' },'
        msgFULL += ' "geometry": { "type": "Polygon", "coordinates": [ ['
        iQ = 0
        for punt in full["polyline"]:
            msgFULL += ' [ ' + str(punt[0]) + ', ' + str(punt[1]) + ' ]'
            if iQ < len(full["polyline"])-1:
                msgFULL += ','
            iQ += 1
        msgFULL += ' ] ] } }'
        if iP < len(tall.keys())-1:
            msgFULL += ','
        msgFULL += ' \n'
        fout.write(msgFULL)
        iP += 1
    fout.write(' ] \n')
    fout.write('} \n')
    fout.close()


if __name__ == '__main__':
    # "Tall100K" - "Tall 1:100000"
    tall100k = getTall100K()
    exportGeoJSON("Tall100K", tall100k)

    # "Tall50K" - "Tall base 1:50 000"
    tall50k = getTall50K()
    exportGeoJSON("Tall50K", tall50k)

    # "Tall25K" - "Tall 1:25 000 (IGN)"
    tall25k = getTallFill50("Tall25K", tall50k)
    exportGeoJSON("Tall25K", tall25k)

    # "Tall25Kicc" - "Tall 1:25 000 (ICC)"
    tall25kicc = getTallFill50("Tall25Kicc", tall50k)
    exportGeoJSON("Tall25Kicc", tall25kicc)

    # "Tall10K" - "Tall 1:10 000"
    tall10k = getTallFill50("Tall10K", tall50k)
    exportGeoJSON("Tall10K", tall10k)

    # "Tall5K" - "Tall 1:5 000 (IGN)"
    tall5k = getTallFill50("Tall5K", tall50k)
    exportGeoJSON("Tall5K", tall5k)

    # "Tall5Kicc" - "Tall 1:5 000 (ICC)"
    tall5kicc = getTallFill50("Tall5Kicc", tall50k)
    exportGeoJSON("Tall5Kicc", tall5kicc)

    # "Tall2K" - "Tall 1:2 000"
    tall2k = getTallFill50("Tall2K", tall50k)
    exportGeoJSON("Tall2K", tall2k)

    # "Tall2Kicc" - "Tall 1:2 000 (20x20)"
    tall2kicc = getTall2Kicc(tall10k)
    exportGeoJSON("Tall2Kicc", tall2kicc)

    # "Tall1K" - "Tall 1:1 000"
    tall1k = getTallFill50("Tall1K", tall50k)
    exportGeoJSON("Tall1K", tall1k)

    # "Tall5Ccmb" - "Tall 1:500 CMB"
    tall5cmb = getTall5Ccmb(tall2kicc)
    exportGeoJSON("Tall5Ccmb", tall5cmb)

    print ' ----------------------------------------------------'
    print '    END ICCTallsExport  '
    print ' ----------------------------------------------------'
