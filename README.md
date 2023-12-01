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

|Resultado 1 | Resultado2 |
|----|----|
|![TibialAnteriorYErectores](https://github.com/fruizg/Introduccion_de_senales/assets/142452596/4aa03b3a-eece-47a5-a659-f9e1af460373)
<p align="center">Figura 1: Medianas del tibial anterior derecho y los erectores espinales</p>||![BicepsYcervicales](https://github.com/fruizg/Introduccion_de_senales/assets/142452596/edaa4b9a-9006-4f07-813f-4bd51300b9f3)
<p align="center">Figura 2: Medianas del biceps derecho y los músculos cervicales</p>|

## Referencias

[1] Bryan Derrickson Gerard J. Tortora, Principios de Anatomía y Fisiología. Editorial MédicaPanamericana, 2018

[2] Muhammad, M. Mustafa, Rafiuddin Abdubrani, A. Hadi, Ahmad, and Zarith Liyana Zahari,“Electromyograph (EMG) Signal Analysis to Predict Muscle Fatigue During Driving,” Lecturenotes in electrical engineering, Jan. 2019, doi: https://doi.org/10.1007/978-981-13-3708-6_35.

[3] Muhammad, M. Mustafa, Rafiuddin Abdubrani, A. Hadi, Ahmad, and Zarith Liyana Zahari,“Electromyograph (EMG) Signal Analysis to Predict Muscle Fatigue During Driving,” Lecturenotes in electrical engineering, Jan. 2019, doi: https://doi.org/10.1007/978-981-13-3708-6_35.

[4] H. M. Abd-Elfattah, Faten Abdelazeim, and Shorouk Elshennawy, “Physical and cognitiveconsequences of fatigue: A review,” Journal of Advanced Research, vol. 6, no. 3, pp.351–358, May 2015, doi: https://doi.org/10.1016/j.jare.2015.01.011.

[5] “Truck driver fatigue risk assessment and management: a multinational survey,”Ergonomics,2023.https://www.tandfonline.com/doi/abs/10.1080/0014013021000056980(accessed Sep. 01, 2023).

[6] X. Hu and G. Lodewijks, “Exploration of the effects of task-related fatigue on eye-motion features and its value in improving driver fatigue-related technology,” TransportationResearch Part F-traffic Psychology and Behaviour, vol. 80, pp. 150–171, Jul. 2021,
doi:https://doi.org/10.1016/j.trf.2021.03.014

[7] S. Gao, J. Gong, B. Zhang, F. Luo, M. Yerabakan, Y. Pan, y B. Hu, "Use of Advanced Materials and Artificial Intelligence in Electromyography Signal Detection and Interpretation," Advanced Intelligent Systems, vol. 4, p. 2200063, 2022, doi: 10.1002/aisy.202200063.

[8] Defensoria del pueblo, “Defensoría del Pueblo: cifra de accidentes de tránsito en 2022 alcanza niveles registrados antes de la pandemia,” Defensoria del Pueblo - Perú, 2023. https://www.defensoria.gob.pe/defensoria-del-pueblo-cifra-de-accidentes-de-transito-en-2022-alcanza-nivelesregistrados-antes-de-la-pandemia/ (accessed Sep. 01, 2023)
