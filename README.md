# exportTALL

Generar arxius SHP o geojson amb tots els fulls que composen els talls ICC descrits a l'article: 
  Macau, M., Colomina, I. 1987. 
  La generació de talls geodèsics en la cartografia de Catalunya per a escales 1:50000 i mes grans. 
  RCG n.5, juliol 1987, volum II. pp.16-31

Tota la informació de coordenades estan en el sistema EPSG:4230.

L'estructura de les dades d'un full qualsevol és:
+ **tall** = kTall, acrònim que defineix el tall) [string] : **Tall50K**, **Tall25K**, **Tall10K**, **Tall5K**, **Tall2K**, **Tall1K**, **Tall25Kicc**, **Tall5Kicc**, **Tall2Kicc**, **Tall5Ccmb** i **Tall100K**.
+ **IC**, columna absoluta full [integer]
+ **IF**, fila absoluta full [integer]
+ **epsg** = 4230 [integer]
+ **tp**, kTall del tall pare. La majoria de talls són fills del MTN 1:50000 (**Tall50K**) [string]
+ **CTOT**, partició total de columnes del tall pare [integer]
+ **FTOT**, partició total files del tall pare [integer]
+ **ICtp**, columna del full pare [integer]
+ **IFtp**, fila del full pare [integer]
+ **IDtp**, identificador sequencial del full pare [string]
+ **CR**, columna relativa del full respecte el full pare. És un valor entre 1 i **CTOT**.
+ **FR**, fila relativa del full respecte el full pare. És un valor entre 1 i **FTOT**.
+ **NW**, [x, y] cantonada NW. Si EPSG=4230, [longitud, latitud]
+ **NE**, [x, y] cantonada NE
+ **SE**, [x, y] cantonada SE
+ **SW**, [x, y] cantonada SW
+ **polyline** = [[xNW, yNW], [xNE, yNE], [xSE, ySE], [xSW, SNW], [xNW, yNW]], polígon que defineix el full a partir de les cantonades.
