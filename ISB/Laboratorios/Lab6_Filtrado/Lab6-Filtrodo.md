# Uso de BITalino y Ultracortex para captura de EEG

## Laboratorio 5 - Equipo 6


## Tabla de contenido

- Introducción
- Materiales
- Métodos
- Resultados: Gráficas, imágenes y videos
- Discusión
- Referencias

#

### Introducción

Los filtros digitales son esenciales en el procesamiento de señales, ya que discriminan señales de manera virtual, ofrecen alta precisión y facilidad de diseño. En este laboratorio utilizaremos filtros FIR, IIR y Wavelet. Los filtros FIR (Respuesta finita al impulso) se caracterizan por tener una respuesta a una señal de impulso con un número limitado de términos no nulos. Sus ventajas incluyen la factible implementación utilizando la FFT, eficiencia en formas recursivas y no recursivas, estabilidad constante, y facilidad de diseño para filtros de fase lineal [1]. Los filtros IIR (Respuesta Infinita al Impulso) se caracterizan por tener una respuesta infinita al impulso y presentan retroalimentación de la señal de salida. Esto los hace ser recursivos, por lo que  su salida depende de la entrada actual, de las precedentes, sino también de las salidas anteriores, lo cual  implica una respuesta impulsional infinita en general [2]. Finalmente la transformada wavelet son señales con duración limitada y un valor promedio de cero. Estas están caracterizadas por su irregularidad y asimetría, lo que las hace más adecuadas para el análisis de señales en comparación con la transformada de Fourier. Al momento de utilizar estos principios en filtrado de señales se emplea la transformada wavelet discreta porque nos permite reconstruir la señal una vez que calculamos los coeficientes wavelet
 [3].



### Materiales

| Descripción | Modelo | Cantidad |
|---|---|---|
| Kit BITalino | (r)evolution Assembled Core BT | 1|
| Laptop | - | 1 | 
| Electrodos desechables adhesivos gelificados | 2230 RED DOT marca 3M | 3 | 
| Software 1 | Visual Studio Code | 1 |
| Software 2 | PyFDAx | 1 | 

### Metódos

El objetivo de esta metodología es filtrar las frecuencias altas de las señales de ECG, eliminando el ruido no deseado. Para lograr esto, se diseñarán dos tipos de filtros: uno IIR (Infinite Impulse Response) y otro FIR (Finite Impulse Response) [x], utilizando diferentes métodos y características específicas. El procedimiento ejecutado para el contraste de señales filtradas fue el siguiente:

1. Adquisición de datos:
   - Se utilizó el dataset de ECG generado en el laboratorio anterior como fuente de datos.

2. Selección de filtros:
   - Diseño un filtro IIR: Se seleccionó el tipo de filtro Butterworth porque es el que mejor se adapta a los requisitos de filtrado de estas señales [x].

   - Diseño un filtro FIR: Se seleccionó la ventana Hamming por su tipo de atenuación en la banda de transición y para preservar un bajo costo computacional [y].

3. Especificaciones del filtro:
     - Frecuencia de corte (Fc): 20 Hz.
     - Ancho de banda de paso (Wp): 94 rad/s.
     - Ancho de banda de rechazo (Ws): 157 rad/s.

4. Diseño de filtros:
   - Se utilizó la herramienta PyFDAx para la creación de los filtros IIR y FIR. 

5. Evaluación y optimización:
   - Se evaluó el rendimiento de los filtros en la eliminación de las frecuencias no deseadas.

   - Se realizaron ajustes para optimizar el rendimiento de los filtros, asegurando que se hubieran eliminado, eficazmente, las frecuencias altas no deseadas mientras se conservaba la información relevante de las señales de ECG.

6. Implementación y validación:
   - Se implementaron los filtros diseñados en el procesamiento de las señales de ECG.



### Discusión

- Respecto a la señal Delta en reposo podemos observar que cuenta con una amplitud más grande y una frecuencia más pequeña respecto a la señal delta después del ejercicio mental. Esta observación de una amplitud más grande y una frecuencia más pequeña en las ondas delta después del ejercicio mental sugiere que el cerebro está experimentando cambios en su actividad eléctrica en respuesta a la tarea cognitiva realizada.[7,8] Estos cambios pueden estar relacionados con la activación, la sincronización neuronal, la fatiga o el estado de relajación posterior al ejercicio mental.

- La señal Gamma tiene mayor actividad, mayor amplitud y mayor frecuencia en reposo respecto a la señal obtenida después del ejercicio mental. Este cambio refleja la dinámica de la actividad cerebral en respuesta a la tarea cognitiva realizada. Esta diferencia puede estar relacionada con la modulación de redes neuronales, la sincronización neuronal, la intensidad de la tarea, la fatiga cerebral y los cambios en el estado de alerta, entre otros factores.[8]

- La señal Alpha y Beta tienen mayor amplitud durante el reposo; mientras que después del ejercicio mental tienen menos amplitud.Esto puede estar relacionado con cambios en la atención, la sincronización neuronal, la inhibición cortical, la activación de otras frecuencias y la fatiga cerebral.[8]

- La señal Theta en ambas pruebas son parecidas. 
Las señales EEG son muy sensibles y pueden ser afectadas por la interferencia electromagnética, como la generada por otros dispositivos electrónicos cercanos. Esto podría provocar ruido en las señales EEG y afectar la calidad de los datos recopilados.

#

### Referencias

[1] “SEÑALES DE ENCEFALOGRAMA: Análisis y distinción de Canales Focales y No Focales.” Available: https://openaccess.uoc.edu/bitstream/10609/98326/6/atestapeTFM0619memoria.pdf

[2] “Electroencefalografía (EEG) - Mayo Clinic,” Mayoclinic.org, 2022. https://www.mayoclinic.org/es/tests-procedures/eeg/about/pac-20393875 (accessed Sep. 30, 2023).

[3] World, “Epilepsia,” Who.int, Feb. 09, 2023. https://www.who.int/es/news-room/fact-sheets/detail/epilepsy#:~:text=La%20proporci%C3%B3n%20de%20la%20poblaci%C3%B3n,millones%20de%20casos%20de%20epilepsia. (accessed Sep. 30, 2023).

[4] BITalino (r)evolution Lab Guide [Internet]. Available from: https://support.pluxbiosignals.com/wp-content/uploads/2022/04/HomeGuide3_EEG.pdf

[5] Río del, Miguel Ángel Guevara, Marisela Hernández González, María R, Manuel Aguilar Villagrán. EEG correlation during the solving of simple and complex logical–mathematical problems. Cognitive, Affective, & Behavioral Neuroscience [Internet]. 2019 Feb 21 [cited 2023 Oct 1];19(4):1036–46. Available from: https://link.springer.com/article/10.3758/s13415-019-00703-5/tables/1

[6] Ultracortex Mark IV | OpenBCI Documentation [Internet]. Openbci.com. 2022 [cited 2023 Oct 1]. Available from: https://docs.openbci.com/AddOns/Headwear/MarkIV/

[7] Carlos Ernesto Peña Goyas, Mauro Santoyo Mora, José Alfredo Padilla Medina.Metodología para el estudio de señales sinápticas mediante un sistema de EEG portátil.Vol. 42, Núm. 137 (2020). [cited 2023 Oct 1].Available: https://pistaseducativas.celaya.tecnm.mx/index.php/pistas/issue/view/74

[8]Chetan S. Nayak; Arayamparambil C. Anilkumar.EEG Normal.2023. [cited 2023 Oct 1].Available: https://www.ncbi.nlm.nih.gov/books/NBK539805/



