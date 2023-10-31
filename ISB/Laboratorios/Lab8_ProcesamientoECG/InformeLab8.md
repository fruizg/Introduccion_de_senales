# Procesamiento de ECG

## Laboratorio 8 - Equipo 6

## Tabla de contenido

- Introducción
- Materiales
- Métodos
- Resultados: Gráficas e imágenes   
- Discusión
- Referencias



## Introducción

El Electrocardiograma (ECG) es una herramienta fundamental en la práctica médica, que ha revolucionado la comprensión y diagnóstico de enfermedades cardíacas desde su invención a principios del siglo XX. Esta técnica no invasiva permite registrar la actividad eléctrica del corazón y proporciona información valiosa sobre su función, ritmo y salud en general.El corazón es un órgano muscular que se contrae rítmicamente para bombear sangre a todo el cuerpo. Esta actividad está regulada por un sistema eléctrico intrínseco. El ECG detecta estas señales eléctricas y las representa gráficamente en un electrocardiograma. Las principales ondas del ECG incluyen la onda P (representando la despolarización de las aurículas), el complejo QRS (marcando la despolarización de los ventrículos) y la onda T (indicando la repolarización ventricular) [1].

El ECG es una herramienta esencial para el diagnóstico de trastornos cardíacos. Puede identificar arritmias, como la fibrilación auricular o ventricular, así como el infarto de miocardio, insuficiencia cardíaca, y otros problemas cardíacos [2]. 

En la medicina moderna, el ECG se utiliza para una amplia gama de propósitos. Además de su papel en el diagnóstico, es fundamental en la evaluación preoperatoria, seguimiento de pacientes con enfermedades cardíacas, control de tratamientos y monitoreo a largo plazo [3]. Los avances tecnológicos han permitido la miniaturización de los dispositivos, lo que ha llevado a la creación de dispositivos portátiles, como los monitores Holter, que permiten un seguimiento continuo.

Asimismo, en el presente informe tuvo como objetivo la extracción de características de las señales de ECG, lo cual es fundamental por las razones como:

1. Diagnóstico médico: Para el monitoreo de enfermedades cardiovasculares, como arritmias, infartos de miocardio y trastornos de la conducción. La extracción de características permite a los médicos identificar patrones anormales en la señal, lo que facilita el diagnóstico preciso y el tratamiento oportuno [4].

2. Monitorización continua: En entornos de cuidados intensivos y unidades de monitoreo, se utiliza la extracción de características para rastrear la actividad eléctrica del corazón de los pacientes de forma continua. Esto permite una supervisión constante y una respuesta rápida en caso de emergencia [5].

3. Reducción de ruido: Las características extraídas también pueden utilizarse para eliminar ruido o artefactos de las señales de ECG, mejorando la calidad de los datos y facilitando el análisis posterior [6].

4. Automatización: La extracción automática de características es fundamental para la automatización de procesos, lo que agiliza el análisis de grandes volúmenes de datos de ECG y reduce la carga de trabajo de los profesionales de la salud [7].

## Metodología 

La presente metodología de análisis de señales de ECG permite procesar y caracterizar eficazmente las señales cardíacas, mejorando la capacidad de detección de patrones y contribuyendo a la toma de decisiones clínicas.


1. Lectura del DataSet:
   - Se inició el proceso leyendo el conjunto de datos que contenía las señales de ECG que habían sido obtenidas anteriormente.

2. Análisis en frecuencia:
   - Se realizó un análisis de la señal ECG en el dominio de frecuencia para detectar componentes de ruido a 50 Hz y 150 Hz.

3. Filtro pasabanda:
   - La señal se filtró con un paso banda para resaltar las componentes de interés en el rango de frecuencias deseado.

4. Filtro paso alto:
   - Se aplicó un filtro paso alto para eliminar componentes de frecuencia no deseadas y realzar las variaciones rápidas en la señal.

5. Filtrado derivativo:
   - Se realizó un filtrado derivativo para acentuar las transiciones de la señal y resaltar las pendientes.

6. Elevación al cuadrado:
   - La señal fue elevada al cuadrado para enfatizar las áreas con mayor cambio y destacar las ondas QRS.

7. Operador moving window integration:
   - Se aplicó el operador Moving Window Integration para suavizar la señal y reducir el ruido.

8. Marcado de picos:
   - Se identificaron y marcaron los picos en la señal, destacando los puntos de mayor amplitud que correspondían a los complejos QRS.

9. Análisis de threshold:
    - Se aproximó el umbral de referencia para identificar los picos R y ruidos en la señal ECG.

10. Obtención de complejos QRS:
    - Finalmente, se determinaron y obtuvieron los complejos QRS en la señal ECG, proporcionando información relevante para el diagnóstico clínico y la evaluación de la actividad cardíaca.


## Resultados


![](Images/ECGyFFT_crudo.png)

<p align="center">
 Figura 1: Señal ECG sin preprocesamiento y FFT de la misma
</p> 
SNR de la señal sin preprocesamiento: 19


![](Images/ECGyFFT_filtrada.png)

<p align="center">
 Figura 2: Señal ECG filtrada y FFT de la misma
</p> 
 SNR en decibeles de la señal filtrada: 30


![](Images/ECG_SignalsPeaks.png)

<p align="center">
 Figura 3: Onda R ECG
</p> 

![](Images/ECGINFO.png)

<p align="center">
 Figura 4: ECG informacion
</p> 

![](Images/ECGForm.png)

<p align="center">
 Figura 5: EC forma promedio
</p> 



## Discusión

1. Se destaca la importancia del Electrocardiograma (ECG) como una herramienta esencial en la práctica médica para el diagnóstico y monitoreo de enfermedades cardíacas. El ECG proporciona información vital sobre su funcionamiento y salud en general. Esto se logra a través de la representación gráfica de las ondas del ECG, como la onda P, el complejo QRS y la onda T, lo cual se puede observar en el procesamiento de los datos adquiridos. 

2. La metodología que empleamos nos facilita la extracción de características de las señales de ECG y esto relacionado con el diagnóstico médico.

3. Respecto a la imagen sin procesar y procesada obtenemos gráficas, el análisis será en la señal filtrada. Las cuales son: 

      - Señal ECG filtrada: El gráfico superior muestra la señal ECG filtrada en función del tiempo. La línea azul representa la señal ECG y parece tener un patrón regular respecto a la señal sin procesar, lo cual es típico en las señales ECG normales.

      - Análisis espectral de la señal ECG después del filtro: El gráfico inferior muestra el espectro de frecuencias de la señal ECG. La línea azul representa el análisis espectral y hay un pico prominente alrededor de los 30 Hz, lo que podría indicar la frecuencia cardíaca dominante.

   La imagen muestra la señal ECG después de haber sido filtrada para eliminar el ruido y mejorar la calidad de la señal. Al comparar ambas imágenes, podemos observar que el filtrado de la señal ECG puede ayudar a resaltar características importantes y eliminar ruido no deseado. También podemos observar que la onda P precede a cada complejo QRS.

4. En la Figura 3, se muestra una línea roja que representa la señal ECG y una línea amarilla que representa los picos. Los picos en la señal ECG, etiquetados como “R-peaks”, son características importantes en un ECG ya que representan la contracción ventricular, podemos observar que tenemos valores más allá de 0.4, lo cual son picos normales de la onda y positivos, además de claramente visibles. Se puede identificar también que la señal ha sido procesada para mejorar su calidad, con los 30 decibelios.

5. En la Figura 4, se puede apreciar la representación gráfica de la señal ECG sin procesar, la cual se muestra como una línea azul en la parte superior del gráfico. Asimismo, se observa la señal ECG después de someterse a un proceso de procesamiento que tiene como objetivo eliminar el ruido y mejorar la calidad de la señal, lo que se representa con una línea roja. Además, se destacan los picos R en ambas señales. En cuanto a la gráfica inferior, se encuentra la línea naranja, que representa la frecuencia cardíaca. Esta frecuencia cardíaca se calcula a partir de la detección de los picos R en la señal ECG. Además, en el centro de la parte inferior del gráfico, se muestra la línea que representa la frecuencia cardíaca media, la cual corresponde al promedio de la frecuencia cardíaca a lo largo del tiempo.

6. En la figura 5 el gráfico muestra una línea roja que representa la señal ECG. Cada pico en la señal representa un latido cardíaco individual. Las líneas verticales punteadas marcan el pico de cada latido, que es el punto más alto de la onda R en el complejo QRS de la señal. La frecuencia cardíaca promedio es de 65.5 latidos por minuto. Esto está dentro del rango normal para un adulto en reposo, que generalmente es de 60 a 100 latidos por minuto.
Respecto a los valores obtenidos [8][9]: 

      - MaxRR: El valor máximo de los intervalos RR (intervalos entre los picos R del ECG) es de aproximadamente 1.005 segundos. Esto indica el tiempo máximo entre dos latidos cardíacos sucesivos.

      - MinRR: El valor mínimo de los intervalos RR es de aproximadamente 0.788 segundos. Esto indica el tiempo mínimo entre dos latidos cardíacos sucesivos.

      - AvgRR: El promedio de los intervalos RR es de aproximadamente 0.917 segundos. Representa el ritmo cardíaco promedio.

      - MaxBPM: La frecuencia cardíaca máxima en latidos por minuto (BPM) es de alrededor de 76.14.

      - MinBPM: La frecuencia cardíaca mínima en BPM es de alrededor de 59.70.

   Estos valores reflejan medidas relacionadas con la variabilidad de la frecuencia cardíaca (HRV) y la frecuencia cardíaca promedio.

      - SDNN: La desviación estándar de los intervalos RR es de aproximadamente 0.0515 segundos. Representa la variabilidad absoluta de la frecuencia cardíaca.

      - SD1/SD2: La relación entre las variabilidades de la frecuencia (SD1 y SD2) es de aproximadamente 0.6617. Esto puede proporcionar información sobre la simetría y el equilibrio de la variabilidad cardíaca.

      - NN20: Hay 35 pares de intervalos RR sucesivos con una diferencia de más de 20 ms.

      - NN50: Hay 19 pares de intervalos RR sucesivos con una diferencia de más de 50 ms.

      - pNN50: El porcentaje de pares de intervalos RR sucesivos con una diferencia de más de 50 ms es del 43%.

      - LF_Power: La potencia en la banda de frecuencia "Baja Frecuencia" es de 0.00064. Esta banda está relacionada con la modulación simpática y parasimpática de la frecuencia cardíaca.

      - HF_Power: La potencia en la banda de frecuencia "Alta Frecuencia" es de 0.00115. Esta banda está relacionada con la modulación del sistema parasimpático.

      - LF_HF_Ratio: La relación entre la potencia en las bandas de baja y alta frecuencia es de aproximadamente 0.5565. Esta relación puede proporcionar información sobre el equilibrio entre el sistema simpático y parasimpático.


## Referencias
[1] What is an electrocardiogram (ECG)? [Internet]. Nih.gov. Institute for Quality and Efficiency in Health Care (IQWiG); 2019 [cited 2023 Oct 30]. Available from: https://www.ncbi.nlm.nih.gov/books/NBK536878/

‌[2] Samol A, Bischof K, Blerim Luani, Pascut D, Wiemer M, Sven Kaese. Single-Lead ECG Recordings Including Einthoven and Wilson Leads by a Smartwatch: A New Era of Patient Directed Early ECG Differential Diagnosis of Cardiac Diseases? Sensors [Internet]. 2019 Oct 10 [cited 2023 Oct 30];19(20):4377–7. Available from: https://www.mdpi.com/1424-8220/19/20/4377

[3] Flores N, Reyna MA, Avitia RL, José Antonio Cárdenas-Haro, Conrado García. Non-Invasive Systems and Methods Patents Review Based on Electrocardiogram for Diagnosis of Cardiovascular Diseases. Algorithms [Internet]. 2022 Feb 28 [cited 2023 Oct 30];15(3):82–2. Available from: https://www.mdpi.com/1999-4893/15/3/82

‌[4] Anuoluwapo Ajibade, Younas H, Pullan M, Amer Harky. Telemedicine in cardiovascular surgery during COVID‐19 pandemic: A systematic review and our experience. Journal of Cardiac Surgery [Internet]. 2020 Aug 16 [cited 2023 Oct 30];35(10):2773–84. Available from: https://onlinelibrary.wiley.com/doi/full/10.1111/jocs.14933

[5] Pezawas T. ECG Smart Monitoring versus Implantable Loop Recorders for Atrial Fibrillation Detection after Cryptogenic Stroke—An Overview for Decision Making. Journal of Cardiovascular Development and Disease [Internet]. 2023 Jul 18 [cited 2023 Oct 30];10(7):306–6. Available from: https://www.mdpi.com/2308-3425/10/7/306

[6] Chiang HT, Hsieh YY, Fu SW, Hung KH, Tsao Y, Chien SY. Noise Reduction in ECG Signals Using Fully Convolutional Denoising Autoencoders. IEEE Access [Internet]. 2019 Jan 1 [cited 2023 Oct 30];7:60806–13. Available from: https://ieeexplore.ieee.org/abstract/document/8693790

‌[7] An JM, Gregg RE, Soheil Borhani. Effective Data Augmentation, Filters, and Automation Techniques for Automatic 12-Lead ECG Classification Using Deep Residual Neural Networks. 2022 44th Annual International Conference of the IEEE Engineering in Medicine & Biology Society (EMBC) [Internet]. 2022 Jul 11 [cited 2023 Oct 30]; Available from: https://ieeexplore.ieee.org/abstract/document/9871654

‌[8] O. Gawron, N. González, F. Lage. Análisis de métodos para el reconocimiento de patrones en ECG. VIII Workshop de Tecnologia Adaptativa. [Internet]. [cited 2023 Oct 30]; Available from: https://www.researchgate.net/profile/Nahuel-Gonzalez/publication/334495515_Analisis_de_metodos_para_el_reconocimiento_de_patrones_en_ECG/links/5d2e555c92851cf4408a731c/Analisis-de-metodos-para-el-reconocimiento-de-patrones-en-ECG.pdf

[9] Jose Rodrigo González, Ricardo López y Álvaro Jaramillo. Wavelets in the analysis of EKG. Scientia et Technica Año Año XXI, Vol. 20, No. 3, septiembre de 2016. Universidad Tecnológica de Pereira.  [Internet]. [cited 2023 Oct 30]; Available from: https://www.redalyc.org/pdf/849/84950585011.pdf
