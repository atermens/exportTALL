# -----------------------------------------------------------------------------
# Name:       ICCTallsExport
# Purpose:    Generar arxius SHP amb tots els fulls que composen els talls ICC
#             descrits a l'article:
#
#             Macau, M., Colomina, I. 1987.
#             La generacio de talls geodesics en la cartografia de Catalunya
#             per a escales 1:50000 i mes grans
#             RCG n.5, juliol 1987, volum II. pp.16-31
#
# Author:      atermens
# Created:     31/05/2019
# Copyright:   (c) a.termens 2019
# License:     CC BY 4.0
# -----------------------------------------------------------------------------
# !/usr/bin/env python

import math
import numpy as np


def sgn(graus, minuts, segons):
    if graus < 0 or minuts < 0 or segons < 0.0:
        return -1.0
    else:
        return 1.0


def de2ss(graus, minuts, segons):
    wrk1 = sgn(graus, minuts, segons)
    wrk2 = math.fabs(graus)*3600.0+math.fabs(minuts)*60.0+math.fabs(segons)
    return wrk1*wrk2


def de2dd(graus, minuts, segons):
    return de2ss(graus, minuts, segons)/3600.0


# -----------------------------------------------------------------------------
# esDins
# funcio que ens diu si un punt esta dins d'un poligon regular
# es considera que el poligon esta ordenat segons les agulles del rellotge
# len(xpol) = len(ypol) = npol
# -----------------------------------------------------------------------------
def esDins(punt, pol):
    npol = len(pol)
    recht = 0
    for i in range(npol-1):
        if dreta(pol[i], pol[i+1], punt) != 1:
            recht += 1
    if dreta(pol[npol-1], pol[0], punt) != -1:
        recht += 1
    if recht == npol:
        return True
    else:
        return False


# -----------------------------------------------------------------------------
# dreta
# purpose: tests if point C is to the right of the edge from A to B
# usage: intval = dreta(A,B,C)
#   +1 when C is to the right
#   -1 when C is to the left
#    0 when A, B and C are colinear
# -----------------------------------------------------------------------------
def dreta(a, b, c):
    tol = 1.e-15
    prod = (c[0]-a[0])*(b[1]-a[1]) - (b[0]-a[0])*(c[1]-a[1])
    if prod > tol:
        return 1
    elif prod < tol:
        return -1
    else:
        return 0


# -----------------------------------------------------------------------------
# General Form of Equation of a Line defined by points p0 and p1
#
#  A*x + B*y + C = 0
#
# where:
#           p0=(x0,y0) and p1=(x1,y1)
#
#            x-x0      y-y0          x-x0     y-y0
#          ------- = -------        ------ = ------
#           x1-x0     y1-y0           v0       v1
#
#           v1*(x-x0) = v0*(y-y0)
#           v1*x - v1*x0 = v0*y - v0*y0
#           v1*x - v0*y + v0*y0-v1*x0 = 0
#
#           A = v1
#           B = -v0
#           C = v0*y0-v1*x0
# -----------------------------------------------------------------------------
def recta(p0, p1):
    v = [p1[0]-p0[0], p1[1]-p0[1]]
    return [v[1], -v[0], v[0]*p0[1]-v[1]*p0[0]]


# -----------------------------------------------------------------------------
#  Proposit
# -----------------------------------------------------------------------------
#  Calcula el punt interseccio de R1 i R2,a on:
#
#     R1 es la recta que passa pels punts p01 i p11
#
#          x-p01[0]          y-p01[1]
#    --------------- = ---------------
#     p11[0]-p01[0]     p11[1]-p01[1]
#
#    (p11[1]-p01[1])*x - (p11[0]-p01[0])*y =
#                      (p11[1]-p01[1])*p01[0] - (p11[0]-p01[0])*p01[1]
#
#  De manera similar R2 es la recta que passa pels punts p02 i p12:
#
#    (p12[1]-p02[1])*x - (p12[0]-p02[0])*y =
#                      (p12[1]-p02[1])*p02[0] - (p12[0]-p02[0])*p02[1]
#
#  El punt de interseccio es la resultant de resoldre el sistema:
#
#    (p11[1]-p01[1])*x - (p11[0]-p01[0])*y =
#                      (p11[1]-p01[1])*p01[0] - (p11[0]-p01[0])*p01[1]
#    (p12[1]-p02[1])*x - (p12[0]-p02[0])*y =
#                      (p12[1]-p02[1])*p02[0] - (p12[0]-p02[0])*p02[1]
#
#  S'utilizara la llibreria NumPy per a resoldre el sistema A*p = B,
#  on p = inv(A)*B
#  En el nostre cas,
#  A => [[p11[1]-p01[1], -(p11[0]-p01[0])], [p12[1]-p02[1], -(p12[0]-p02[0])]]
#  B => [[(p11[1]-p01[1])*p01[0]-(p11[0]-p01[0])*p01[1]],
#        [p12[1]-p02[1])*p02[0]-(p12[0]-p02[0])*p02[1]]]
#  Totes les dades son reals per vuit.El resultat es retornat en les
#  variables X,Y (punt interseccio (X,Y) ).
# -----------------------------------------------------------------------------
def intersecta(p01, p11, p02, p12):
    r1 = recta(p01, p11)  # r1[0]*x + r1[1]*y = -r1[2]
    r2 = recta(p02, p12)
    a = np.array([[r1[0], r1[1]], [r2[0], r2[1]]])
    b = np.array([[-r1[2]], [-r2[2]]])
    p = np.linalg.inv(a).dot(b)  # p es un np.array
    punt = p.tolist()  # [[x], [y]]
    x = punt[0][0]
    y = punt[1][0]
    return [x, y]


# -----------------------------------------------------------------------------
# Discretitzacio del segment definit per p0 i p1 amb np elements
# -----------------------------------------------------------------------------
def segment(nP, p0, pN):
    punt_list = []
    for i in range(nP+1):
        kk = float(i)/float(nP)
        punt = []
        for j in range(2):
            punt.append(p0[j] + kk*(pN[j]-p0[j]))
        punt_list.append(punt)
    return punt_list
