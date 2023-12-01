# Evaluación de sEMG en busqueda de fátiga en grupos musculares específicos de conductores de vehículos durante largos periodos de conducción

### Assessment of sEMG for the detection of muscle fatigue in specific muscle groups of vehicle drivers during extended periods of driving.

#
#### Keywords: Electromiografía, fatiga muscular , análisis estadístico, movimiento dinámico

#
## [Sobre nosotros](ISB/Laboratorios/Lab1_AboutUs/README.md)


## Tabla de contenido
- [Resumen](#Resumen)
- [Motivación](#Motivación)
- [Principales hallazgos](#Principales-hallazgos)
- [Referencias](#Referencias)


## Resumen 

El presente estudio tiene como finalidad evaluar la fatiga muscular de diversos grupos musculares en conductores de auto. Lo anterior con la finalidad de encontrar los grupos musculares que más se fatigan que presentan fátiga después de una conducción prolongada sin descanso. Los resultados podrían ser utilizados por personal de la salud para desarrollar ejercicios específicos para cada área afectada con el objetivo de fortalecer los músculos que allí se encuentran. El estudio utilizará electromiografía de superficie comoo técnica de obtenición de las señales musculares, la cual consiste técnica en la medición de biopotenciles que se basa en la acción eléctrica de los potenciales de acción enviados desde el sistema nervioso hacia los músculos para causar la despolarización de las miofibrillas y así lograr el moviento. El hardware que se utilizará para llevar a cabo lo anterior tiene como nombre BITalino, que corresponde a un producto desarrollado por BioSignals PluX. Se conducirá durante un tiempo y una distancia determinada, y se evaluará la actividad elécttrica de los grupos musculares seleccionados antes y después de la conducción, realizando movimientos específicos y propios de esa acción. Posteriormente se aplicarán técnicas de preprocesado y procesado de señales, entre las cuales se destaca el filtrado y la extracción de características (RMS,MDF), las cuales serán útiles para realizar un análisis estadístico que servirá para determinar si existe o no diferencia entre las señales antes y después de la conducción.

## Motivación

La electromiografía (EMG) registra la actividad eléctrica en nervios y músculos mediante el uso de electrodos, proporcionando información valiosa
sobre la fisiología y los patrones de activación muscular. Para capturar la actividad eléctrica, se colocan pequeños electrodos en la piel sobre el músculo
o se introducen agujas delgadas directamente en el músculo. La fatiga muscular, que se caracteriza por la incapacidad de un músculo para mantener la
fuerza de contracción después de una actividad prolongada, puede detectarse mediante la evaluación de las señales mioeléctricas generadas por la
contracción muscular [1]. Además, la fatiga muscular está vinculada a la fatiga corporal, siendo uno de los factores contribuyentes a los accidentes de
carretera [2]. Los efectos adversos de la fatiga corporal incluyen respuestas más lentas en situaciones de emergencia, pérdida de concentración,
alteración en el campo de visión y el riesgo de somnolencia al volante, factores críticos que pueden desencadenar accidentes [3][4][5][6].
Los músculos superficiales relacionados con la conducción prolongada incluyen los cervicales, el tibial anterior, el erector espinal y el bíceps. En este
contexto, se empleó la electromiografía de superficie, una técnica no invasiva que, a pesar de su facilidad de uso, presenta limitaciones como la
susceptibilidad a alteraciones por movimiento y ruido. Se seleccionaron músculos superficiales asociados a la fatiga muscular en la conducción
prolongada para el análisis de las señales EMG, evitando así la necesidad de supervisión profesional requerida por técnicas más invasivas [7]. Este
enfoque tiene como objetivo comprender y prevenir la fatiga muscular en contextos relevantes para la seguridad vial.

## Principales hallazgos

Aunque se observa falta de normalidad y variabilidad significativa en
las varianzas en algunos casos, las pruebas estadísticas, indican en
general la ausencia de diferencias estadísticamente significativas entre
las muestras de los diferentes grupos musculares antes y después de conducir; además también de demarca ausencia de diferencia estadísticamente significativa en las pruebas realizadas a las características extraídas de las señales.

|Resultados |
|----|
|![TibialAnteriorYErectores](https://github.com/fruizg/Introduccion_de_senales/assets/142452596/4aa03b3a-eece-47a5-a659-f9e1af460373) <p align="center">Figura 1: Medianas del tibial anterior derecho y los erectores espinales</p>|
|![BicepsYcervicales](https://github.com/fruizg/Introduccion_de_senales/assets/142452596/edaa4b9a-9006-4f07-813f-4bd51300b9f3) <p align="center">Figura 2: Medianas del biceps derecho y los músculos cervicales</p>|


## Referencias

[1] Defensoria del pueblo, “Defensor´ıa del Pueblo: cifra de
accidentes de transito en 2022 alcanza niveles registrados ´
antes de la pandemia,” Defensoria del Pueblo - Peru, 2023. ´
https://www.defensoria.gob.pe/defensoria-del-pueblo-cifra-de-accidentesde-transito-en-2022-alcanza-niveles-registrados-antes-de-la-pandemia/
(accessed Sep. 01, 2023).

[2] Andina, “¡Alerta! Reportan 303 fallecidos por accidentes de
transito en Lima en lo que va del a ´ no,” Andina.pe, Aug. 28, ˜
2023.https://andina.pe/agencia/noticia-alerta-reportan-303-fallecidosaccidentes-transito-lima-lo-va-del-ano-952368.aspx (accessed Sep. 01,
2023).

[3] MAPFRE, ”Sueno y fatiga, y su influencia al volante“, Feb. 09, 2021. ˜
https://www.fundacionmapfre.org/educacion-divulgacion/seguridadvial/movilidad-segura-salud/temas-conduccion-segura/enfermedadesneurologicas/sueno-fatiga/ (accessed Sep. 01,2023).
[4] Bryan Derrickson Gerard J. Tortora, Principios de Anatom´ıa y Fisiolog´ıa.
Editorial MedicaPanamericana, 2018. ´

[5] Muhammad, M. Mustafa, Rafiuddin Abdubrani, A. Hadi, Ahmad, and
Zarith Liyana Zahari,“Electromyograph (EMG) Signal Analysis to Predict
Muscle Fatigue During Driving,” Lecturenotes in electrical engineering,
Jan. 2019, doi: https://doi.org/10.1007/978-981-13-3708-6-35.

[6] H. M. Abd-Elfattah, Faten Abdelazeim, and Shorouk Elshennawy,
“Physical and cognitiveconsequences of fatigue: A review,” Journal
of Advanced Research, vol. 6, no. 3, pp.351–358, May 2015, doi:
https://doi.org/10.1016/j.jare.2015.01.011.

[7] “Truck driver fatigue risk assessment and management: a multinational survey,”Ergonomics,2023.
https://www.tandfonline.com/doi/abs/10.1080/0014013021000056980
(accessed Sep. 01, 2023).

[8] X. Hu and G. Lodewijks, “Exploration of the effects of taskrelated fatigue on eye-motion features and its value in improving driver fatigue-related technology,” TransportationResearch Part Ftraffic Psychology and Behaviour, vol. 80, pp. 150–171, Jul. 2021,
doi:https://doi.org/10.1016/j.trf.2021.03.014

[9] S. M. Jimenez, “ EVALUACION DEL DESEMPE ´ NO˜
MUSCULAR.” Accessed: Nov. 26, 2023. [Online]. Available:
http://5.161.118.10:8080/bitstream/123456789/5228/3/EVALUACI

[10] S. Gao, J. Gong, B. Zhang, F. Luo, M. Yerabakan, Y. Pan, y B. Hu, ”Use
of Advanced Materials and Artificial Intelligence in Electromyography
Signal Detection and Interpretation,” Advanced Intelligent Systems, vol.
4, p. 2200063, 2022, doi: 10.1002/aisy.202200063.

[11] “Electromiograf´ıa - Mayo Clinic,” Mayoclinic.org, 2019.
https://www.mayoclinic.org/es/tests-procedures/emg/about/pac-20393913
(accessed Nov. 19, 2023).

[12] M. Mahmoodi, “Driver drowsiness detection based on classification
of surface electromyography features in a driving simulator - Mohammad Mahmoodi, Ali Nahvi, 2019,” Proceedings of the Institution of
Mechanical Engineers, Part H: Journal of Engineering in Medicine,
2019. https://journals.sagepub.com/doi/10.1177/0954411919831313 (accessed Nov. 26, 2023).

[13] M. Lecocq et al., “Neuromuscular fatigue profiles depends on seat
feature during long duration driving on a static simulator,” Applied Ergonomics, vol. 87, pp. 103118–103118, Sep. 2020, doi:
https://doi.org/10.1016/j.apergo.2020.103118.

[14] Z. Gao, Z. Li, H. Hu, and F. Gao, “Experimental and Numerical Study of
Cervical Muscle Contraction in Frontal Impact,” Automotive Innovation,
vol. 2, no. 2, pp. 93–101, May 2019, doi: https://doi.org/10.1007/s42154-
019-00060-6. []

[15] Cl´ınica Rozalen. ”How to Use TENS at Home”, [Online]. Available: ´
clinicarozalen.com/como-usar-el-tens-en-casa. [Accessed: November 25,
2023].

[16] J. A. Cortes G ´ omez, D. S. Acebes Moreno, L. M. Pe ´ nuela Calder ˜ on, y ´
A. Velasco Vivas, Deteccion de fuerza y posici ´ on para los movimientos ´
de flexion-extensi ´ on de codo a partir de se ´ nales de EMG, reveia, vol. 20, ˜
n.º 39, pp. 3924 pp. 1–20, feb. 2023.

[17] N. T. Mahmood, M. H. Al-Muifraje, T. R. Saeed y A. H. Kaittan, “Upper Prosthetic Design based on EMG: A Systematic Review”,
IOP Conf. Ser.: Mater. Sci. Eng., vol. 978, p. 012025, diciembre de
2020. Accedido el 24 de noviembre de 2023. [En l´ınea]. Disponible:
https://doi.org/10.1088/1757-899x/978/1/012025

[18] Zhang S, Kui H, Liu X, Zhang Z. Analysis of Musculoskeletal Biomechanics of Lower Limbs of Drivers in Pedal-Operation States. Sensors
[Internet]. 2023 Nov 1 [cited 2023 Nov 18];23(21):8897–7. Available
from: https://www.mdpi.com/1424-8220/23/21/8897

[19] Rosalie SM, Malone JM. Women in motorsport: A case report of driving
posture and performance after double mastectomy. Physical Therapy in
Sport [Internet]. 2019 Mar 1 [cited 2023 Nov 18]; Available from: https:
//www.sciencedirect.com/science/article/pii/S1466853X18303250?casatoken=LFZIXzDACpAAAAAA:bFgY6XJ9Q11auc2V8WudfMJF
3BhTuhdoQsRzbAYwin7Edt3Xkbpmpgmz4ON-hkNV7PmVGrg

[20] Mahmoodi M. Driver drowsiness detection based on classification of surface electromyography features in a driving simulator -
Mohammad Mahmoodi, Ali Nahvi, 2019 [Internet]. Proceedings of
the Institution of Mechanical Engineers, Part H: Journal of Engineering in Medicine. 2019 [cited 2023 Nov 18]. Available from:
https://journals.sagepub.com/doi/abs/10.1177/0954411919831313

[21] Schneider L, Sogemeier D, Jaitner T, Buchner A, Stutzig N.
Adaptions in back muscle activity in long-haul truck drivers
during prolonged driving with and without seat-integrated
stimulation. International Journal of Industrial Ergonomics [Internet].
2023 Jul 1 [cited 2023 Nov 18];96:103475–5. Available from:
https://www.sciencedirect.com/science/article/pii/S0169814123000677?
casa-token=AG-RJYW-b6kAAAAA:AKp-SoJBCXPGDzDIDCk8qZFiDy7hJgh8xPrNtw6VW2unHjV4qHUWCatDTUIJrTLQiIzLvc
