# Procesamiento de EMG

## Laboratorio 7 - Equipo 6

## Tabla de contenido

- Introducción
- Materiales
- Métodos
- Resultados: Gráficas e imágenes   
- Discusión
- Referencias

#

### Introducción

Las señales electromiográficas, ampliamente conocidas como EMG, representan una herramienta fundamental en el ámbito de la medicina, la ingeniería y la investigación biomédica. Estas señales ofrecen una ventana única a la actividad eléctrica de nuestros músculos esqueléticos, revelando una riqueza de información que revoluciona el diagnóstico, la rehabilitación y la comprensión de diversos aspectos del sistema muscular humano [1]. Asimismo, el proceso de obtención de señales EMG implica la colocación estratégica de electrodos en la superficie de la piel, directamente sobre los músculos de interés. Estos electrodos capturan y registran la actividad eléctrica generada por las células musculares durante sus contracciones y relajaciones. Posteriormente, esta actividad eléctrica se convierte en una señal eléctrica que puede ser meticulosamente registrada y analizada, proporcionando una visión detallada de la función muscular [2]. Por otro lado, las ventajas de las señales EMG son múltiples y notables, lo que las convierte en una herramienta indispensable en diversos campos. Entre sus principales beneficios se incluyen:
Diagnóstico Médico: Las señales EMG son esenciales para el diagnóstico preciso de trastornos neuromusculares. Estas señales permiten a los profesionales de la salud evaluar la función muscular y detectar irregularidades, facilitando el tratamiento y la gestión de enfermedades como la miastenia gravis, la esclerosis lateral amiotrófica y entre otras afecciones [1][3].
Rehabilitación: Proporcionan información en tiempo real sobre el progreso terapéutico y permiten diseñar programas de ejercicios específicos para fortalecer los músculos afectados, contribuyendo así a la recuperación [2].
Control de prótesis y dispositivos médicos: Posibilitan que personas con discapacidades controlen prótesis, sillas de ruedas eléctricas y otros dispositivos mediante la activación de los músculos, mejorando la calidad de vida y la independencia [4].
Ergonomía y rendimiento deportivo: Las señales EMG son un recurso valioso en la evaluación de la fatiga muscular, la optimización del diseño de equipos y el análisis del rendimiento deportivo. Esto puede ayudar a perfeccionar técnicas, prevenir lesiones y mejorar el desempeño atlético [5].
Por otro lado, el bloque de características espectrales se encarga de extraer información sobre la frecuencia, potencia y otras propiedades de una señal. Asimismo, es capaz de aplicar filtros de paso bajo y paso alto para eliminar aquellas frecuencias no deseadas. Este proceso resulta especialmente útil para analizar patrones que se repiten en una señal EMG. Por último, en el presente informe, se ejecutó la descomposición discreta de Wavelet, además de la extracción de características y reducción de dimensionalidad. Después de la descomposición, se calcularon algunas características en cada nivel, que podían incluir la entropía, la mediana, la media, la desviación estándar, la varianza y la raíz cuadrada de la media cuadrática (RMS). Estas características proporcionan una visión detallada y útil de la información contenida en la señal para la toma de decisiones [6]. 

#

### Materiales

| Descripción | Modelo | Cantidad |
|---|---|---|
| Kit BITalino | (r)evolution Assembled Core BT | 1|
| Laptop | - | 1 | 
| Electrodos desechables adhesivos gelificados | 2230 RED DOT marca 3M | 3 | 
| Software 1 | Visual Studio Code | 1 |

### Metodología

1. Adquisición de señales EMG:
   - Se contaba con señales EMG de buena calidad adquiridas mediante electrodos colocados en los músculos de interés.

2. Preprocesamiento:
   - Se realizó un preprocesamiento inicial para eliminar ruido, filtrar la señal y asegurar que esté en un formato adecuado para su procesamiento posterior.

3. Descomposición Wavelet:
   - Se utilizó una función de descomposición wavelet en el software. Esta función dividió la señal EMG en sus componentes de diferentes escalas en función de una wavelet seleccionada.

4. Selección del nivel de descomposición:
   - Se determinó el número de niveles de descomposición apropiados para el análisis. Esto depende de la resolución requerida y la información que deseas extraer.

5. Extracción de características:
   - Tras la descomposición, se generaron coeficientes en cada nivel. Con ello, se pudo extraer diversas características, como la energía, la entropía, la media, la desviación estándar, entre otras. Más tarde, para fines del presente trabajo, se enfatizó en la entropía de la señal.

#

### Resultados

Se presenta una señal sEMG del bicep braquial derecho de un adulto varón, sano, de 20 años de edad, sin lesiones musculares presentes. En ella se visualiza la actividad basal (o en reposo) del mismo y contracciones musculares donde el sujeto hace una contracción del músculo en cuestión, donde una persona externa ejercia una palanca para maximizar el esfuerzo y poder apreciar mejor la contracción.

![](img/EMGyFFT_crudo.png)

<p align="center">
 Figura 1: Señal EMG sin preprocesamiento y FFT de la misma
</p> 

Asimismo, se visualiza la respuesta en frecuencia de la señal, teniendo un espectro caracterizado por la presencia de frecuencias en todo su espectro, sobretodo en las altas. 

#### Filtrado

![](img/EMGyFFT_filtrada.png)

<p align="center">
 Figura 2: Señal EMG después de la aplicación de filtros
</p>

En la figura 2 se aprecia la señal filtrada y atenuada. Se realizó un filtro IIR pasabandas entre 65-150 Hz de orden 6. Las frecuencias fueron elegidas con base en la literatura consultada en el laboratorio 2, donde se específica que el espectro de las señales EMG oscilan entre 50 y 150 Hz; sin embargo, se decidió la frecuencia de corte baja en 65 Hz para eliminar la frecuencia producida por la alimentación (60 Hz). 


#
![](img/Comparison_crudoVfiltro.jpg)

<p align="center">
 Figura 3: Comparación entre la señal cruda y la señal filtrada
</p>

En la figura 3 se logra apreciar no sólo la acción del filtro sino también del suavizado realizado a la señal. Se logra apreciar disminución en la amplitud de la señal, la cual se atribuye entonces a las frecuencias altas, y también se nota diferencia en la actividad basal de la señal antes y después del preprocesado.

#### Extracción de características

![](img/MuscularBurst.jpg)

<p align="center">
 Figura 4: Detección de contracciones musculares
</p>



- Number of Muscular Activations: 2
- Maximum Muscular Activation Duration: 0.8332670727797371
 - Minimum Muscular Activation Duration: 0.7952548893876243
 - Average Muscular Activation Duration: 0.8142609810836807
 - Standard Deviation of Muscular Activation Duration: 0.019006091696056382
 - Maximum Sample Value: 32.73623388284635
 - Minimum Sample Value: -35.17329652137063
 - Average Sample Value: 0.00012926668896625452
 - Standard Deviation Sample Value: 6.440104564094373
 - RMS: 6.440104565391703
 - Area: 0.3260373983423782
 - Total Power Spect: 40.286267198789844
 - Median Frequency: 101.5625
 - Maximum Power Frequency: 89.84375
 - curtosis: 5.221198383861978
 - oblicuidad: -0.0384668965964368
 #

### Discusión 


- El uso de un filtro pasabandas es una herramienta valiosa en el análisis de señales, ya que permite seleccionar y retener un rango específico de frecuencias mientras atenúa las que se encuentran fuera de este intervalo. El orden del filtro, en este caso, un orden 6, desempeña un papel esencial en la precisión y capacidad de selectividad del filtro. Cuanto mayor sea el orden del filtro, mayor será su capacidad para atenuar de manera más pronunciada las frecuencias que se encuentran fuera del rango deseado, en este caso, 65-150 Hz.

- Las pruebas realizadas con un filtro de orden 6 han demostrado una notoria eficacia en la atenuación del ruido y las frecuencias no deseadas en nuestras señales. Esto es particularmente evidente al observar la señal de electromiografía (EMG) después de la filtración. El ruido ha sido reducido significativamente, y las frecuencias que se encuentran fuera del rango de interés, es decir, aquellas que no se sitúan entre 65-150 Hz, han sido atenuadas de manera efectiva. Este proceso de filtrado ha mejorado considerablemente la calidad de la señal y ha resaltado las frecuencias de interés, lo que facilita su posterior análisis y procesamiento.

#### Análisis de los obtenido: 

- Number of Muscular Activations:  El hecho de que haya 2 activaciones musculares sugiere la presencia de dos eventos distintos de activación en el análisis de la señal: Esto podría ser relevante para identificar patrones específicos en la actividad muscular. 

- Maximum Muscular Activation Duration:  el valor de 0.833 segundos indica la duración más larga de una activación muscular. Esto podría ser relevante para determinar la fatiga muscular o la sostenibilidad de la actividad.

- Minimum Muscular Activation Duration: La duración más corta de 0.795 segundos podría representar una activación muscular rápida o intermitente. Esto podría relacionarse con movimientos rápidos o contracciones musculares instantáneas.

- Average Muscular Activation Duration: El promedio de 0.814 segundos proporciona una idea general de la duración típica de las activaciones musculares en la señal.

- Standard Deviation of Muscular Activation Duration: La baja desviación estándar de 0.019 sugiere que las duraciones de las activaciones musculares son consistentes y tienden a agruparse alrededor de la media [7].

- Maximum Sample Value: El valor máximo de 32.74 indica una amplitud máxima en la señal muscular. Esto podría representar momentos de máxima fuerza muscular.

- Minimum Sample Value: El valor mínimo de -35.17 señala la amplitud mínima en la señal, que podría ser una representación de relajación muscular o momentos de baja actividad.

- Average Sample Value: El valor promedio cercano a cero (0.0001) sugiere que la señal se encuentra centrada alrededor de cero, lo que es común en señales eléctricas.

- RMS: El valor RMS de 6.44 podría estar relacionado con la magnitud total de la señal, lo que indica la fuerza general de la actividad muscular.

- Area: El área de 0.326 sugiere la cantidad total de energía en la señal muscular.

- Median Frequency: La frecuencia mediana de 101.56 Hz es importante en el análisis de la señal y podría estar relacionada con la frecuencia dominante de la señal muscular [7].

Estos valores ofrecen información valiosa sobre la señal muscular y pueden ser fundamentales para evaluar y entender la actividad muscular, la fatiga, la fuerza y otros aspectos relacionados con la salud y el rendimiento.

Respecto a la oblicuidad, se puede decir que es una medida que describe la asimetría de la distribución de datos. Un valor negativo de oblicuidad, como la que se obtuvo (-0.0385), indica que la distribución de los datos se inclina hacia la izquierda o tiene una cola más larga en el lado izquierdo del pico principal. Esto significa que hay una tendencia hacia valores más bajos en la distribución, lo que resulta en una asimetría negativa. En otras palabras, la mayoría de los valores se encuentran en el lado derecho del promedio, y hay valores atípicamente bajos en el lado izquierdo. Mientras que la curtosis mide  la forma de la distribución. Un valor de curtosis de 5.2212 indica una curtosis positiva. Una curtosis positiva significa que la distribución tiene colas más pesadas y es más puntiaguda en comparación con una distribución normal estándar. En este caso, los datos tienden a estar más concentrados alrededor de la media y tienen valores extremos más pronunciados (tanto positivos como negativos) en comparación con una distribución normal.

Se puede observar que este tipo de filtro se puede aplicar en el procesamiento de señales EMG. Este se puede configurar cómo es que se quiera obtener de la señal a filtrar y que datos se quiera obtener para un analisis.


### Referencias

[1] Bernabé Rodríguez-Tapia, Soto I, Marinez DM, Norma Candolfi Arballo. Myoelectric Interfaces and Related Applications: Current State of EMG Signal Processing–A Systematic Review. IEEE Access [Internet]. 2020 Jan 1;8:7792–805. Available from: https://ieeexplore.ieee.org/abstract/document/8949764
	
[2] Fang C, He B, Wang Y, Cao J, Gao S. EMG-Centered Multisensory Based Technologies for Pattern Recognition in Rehabilitation: State of the Art and Challenges. Biosensors [Internet]. 2020 Jul 26;10(8):85–5. Available from: https://www.mdpi.com/2079-6374/10/8/85

[3] Dubey R, Kumar M, Upadhyay A, Ram Bilas Pachori. Automated diagnosis of muscle diseases from EMG signals using empirical mode decomposition based method. Biomedical Signal Processing and Control [Internet]. 2022 Jan 1;71:103098–8. Available from: https://www.sciencedirect.com/science/article/abs/pii/S1746809421006959

‌[4] Jarque-Bou NJ, Sancho-BruJL, Vergara M. A Systematic Review of EMG Applications for the Characterization of Forearm and Hand Muscle Activity during Activities of Daily Living: Results, Challenges, and Open Issues. Sensors [Internet]. 2021 Apr 26 ;21(9):3035–5. Available from: https://www.mdpi.com/1424-8220/21/9/3035
‌

[5] Campanini I, Dißelhorst-Klug C, Rymer WZ, Merletti R. Surface EMG in Clinical Assessment and Neurorehabilitation: Barriers Limiting Its Use. Frontiers in Neurology [Internet]. 2020 Sep 2;11. Available from: https://www.frontiersin.org/articles/10.3389/fneur.2020.00934/full?&utm_source=Email_to_authors_&utm_medium=Email&utm_content=T1_11.5e1_author&utm_campaign=Email_publication&field=&journalName=Frontiers_in_Neurology&id=556522

[6] Spectral features - Edge Impulse Documentation [Internet]. Edgeimpulse.com. 2023 . Available from: https://docs.edgeimpulse.com/docs/edge-impulse-studio/processing-blocks/spectral-features

[7] L. Gila1, A. Malanda, I. Rodríguez Carreño, J. Rodríguez Falces, J. Navallas. Electromyographic signal processing and analysis methods.[Internet]. 2009, Vol. 32. Available from: https://scielo.isciii.es/pdf/asisna/v32s3/original3.pdf.