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

La Electroencefalografía (EEG) posibilita la captura de señales originadas en el cerebro al registrar la actividad eléctrica de este órgano durante un lapso temporal. Estas señales se originan debido a la actividad eléctrica producida por miles de neuronas y se registran mediante múltiples electrodos, cuya ubicación en el paciente puede variar en cuanto a su invasividad [1]. Es utilizado para el diagnóstico de trastornos cerebrales, con un mayor enfoque en la epilepsia y otros trastornos convulsivos. Sin embargo, su versatilidad va más allá de estos trastornos específicos y se extiende a una amplia gama de aplicaciones médicas. Un electroencefalograma también puede ser sumamente útil en la identificación o tratamiento de condiciones como tumores cerebrales, lesiones cerebrales debidas a traumatismos craneoencefálicos, disfunciones cerebrales de origen diverso, trastornos del sueño, inflamación cerebral como la encefalitis herpética, accidentes cerebrovasculares y la enfermedad de Creutzfeldt-Jakob, así como otros trastornos relacionados con el sueño [2].
La proporción de la población general con epilepsia activa en un momento dado se estima entre 4 y 10 personas cada 1000. Según las estimaciones, en todo el mundo se diagnostican anualmente unos cinco millones de casos de epilepsia. En los países de ingresos altos, se estima que 49 de cada 100 000 personas son diagnosticadas de epilepsia cada año. En los países de ingresos bajos y medianos, la cifra puede ser de hasta 139 cada 100 000 personas [3].


#### Materiales

| Descripción | Modelo | Cantidad |
|---|---|---|
| Kit BITalino | (r)evolution Assembled Core BT | 1|
| Laptop | - | 1 | 
| Electrodos desechables adhesivos gelificados | 2230 RED DOT marca 3M | 3 | 
| Software 1 | OpenSignals | 1 |
| Software 2 | OpenBCI | 1 | 
| Headset | Ultracortex Mark IV | 1|

#### Metódos

En primer lugar, se realizó el emparejamiento entre el módulo BITalino y la laptop vía Bluetooth. Luego, se preparó la piel adecuadamente antes de pegar los electrodos en ella. Para medir la actividad cerebral desde el cuero cabelludo, se empleó la técnica de configuración bipolar que consistía en dos electrodos de medición (IN + e IN-). Asimismo, fue necesario conectar un electrodo de referencia adicional y colocarlo en una zona ósea.

| Referencia de posicionamiento de eléctrodos BITalino | Colocación electrodos en sujeto de prueba vista frontal | Colocación electrodos en sujeto de prueba vista lateral |
|---|---|---|
| ![Figura 1: Posicionamiento del electrodo para medir EEG. Clavijas de medición IN+/- (izquierda) y referencia (derecha) [4].](Imagenes_videos_EEG/Referencia_electrodos.png)| ![](Imagenes_videos_EEG/SujetoPrueba.jpg)|![](Imagenes_videos_EEG/Colocacion_Electrodos_BITalino.jpg)|

Una vez iniciada la adquisición de señales a través del software OpenSignals, el sujeto de prueba debía suprimir cualquier activación muscular, especialmente en el área facial (movimientos oculares y parpadeos) y los movimientos del cuello y la mandíbula (apretar/masticar) [4]. Seguidamente se realizaron las siguientes preguntas a modo ejercicio mental:

![Tabla 1: Ejemplos de problemas planteados de lógica y matemáticas utilizados en el estudio [5].](Imagenes_videos_EEG/Preguntas_ref.png)

#### Conexión BITalino

|Sujeto 1 | Sujeto 2 |
|---|---|
| ![](Img_videosECG/ConexionBITalino_Sujeto1.jpg)|![](Img_videosECG/ECG_Sujeto2.jpg) | 

#### Gráficas en reposo OpenSignals

|Sujeto 1 | Sujeto 2 |
|---|---|
| ![](Img_videosECG/ECG_Reposo_Sujeto1.jpg)|![](Img_videosECG/ECG_Reposo_Sujeto2.jpg) | 

Aquí se pueden visualizar ciertas diferencias entre los sujetos. En el segundo se puede observar mayor ruido en la señal, mayor amplitud en la onda S y una onda T más ancha y también con mayor amplitud. En el apartado de discusión se abordarán las posibles causas de lo anteriormente descrito.

#### Gráficas comparando reposo y actividad física

|Sujeto 1 | Sujeto 2 |
|---|---|
| ![](Img_videosECG/ECG_Sujeto1_comparison.png)|![](Img_videosECG/ECG_Sujeto2_comparison.png) | 

De acuerdo con el algoritmo creado, la frecuencia cardiaca del sujeto 1 en reposo fue de 62 lpm y, luego de realizar actividad física, fue de 118 lpm.

Por su parte, la frecuencia cardiaca del sujeto 2 en reposo fue de 83 y, luego de la actividad física fue de 149. En el sujeto 2 después de la realización de la actividad física, se aprecia que la onda T tiene mayor amplitud que el mismo complejo QRS.

#### Gráficas arrojadas por PromSim 

![](Img_videosECG/ECG_Prosim_comparison.png)

En la imagen anterior se observa 4 diferentes ritmos cardiacos arrojados por el dispositivo ProSim, el cual simula ECG. 

La gráfica de la sección superior izquierda corresponde a un ritmo normal de 150 lpm. El que le sigue a la derecha es un ritmo normal también pero que sus lpm corresponden a 180. Por su parte, los 2 ritmos de la sección inferior corresponden a ritmos de paro, más especificamente a taquicardia ventricular y fibrilación ventricular. 

![g](Img_videosECG/RitmosAnormalesECG.png) [g]

#### Análisis espectral de las señales

|FFT Sujeto 1 | FFT Sujeto 2 | FFT ProSim|
|---|---|---|
| ![](Img_videosECG/FFT_Sujeto1.png)|![](Img_videosECG/FFT_Sujeto2.png) | ![](Img_videosECG/FFT_ProSim.png)

Las imágenes son consistentes con la teoría, las bajas frecuencias son dominantes en la toma de ECG. Asímismo, se evidencian algunas frecuencias que podrían corresponder a artefactos o ruidos, tales como la que corresponde a 60 Hz (de la fuente de alimentación), 2.4 Hz (interferencia electromagnética por dispositivos móviles que utilicen WiFi o Bluetooth). Las frecuencias más altas podrían estar relacionas con actividad muscular superficial (EMG).
#### Videos de la actividad Física

##### Sujeto 1

https://github.com/fruizg/Introduccion_de_senales/assets/142452596/0e924114-f470-4f22-be13-9bd9091df8f8


##### Sujeto 2


https://github.com/fruizg/Introduccion_de_senales/assets/142452596/59177078-1aa7-40b4-b1aa-ba847f332dee


#### Videos de la toma del ECG

##### Sujeto 1


https://github.com/fruizg/Introduccion_de_senales/assets/142452596/bd73a6bf-7043-42ce-8076-9b4162d9a5c1

#### Sujeto 2


https://github.com/fruizg/Introduccion_de_senales/assets/142452596/22558447-69d8-4dd6-b632-9ee29f13c25b


#### Videos ProSim

Se visualiza la captura de la señal arrojada por el Prosim

https://github.com/fruizg/Introduccion_de_senales/assets/142452596/09ea4fb0-1cc1-4018-ab54-e796300efb32


### Discusión

•	Para la toma de datos con el BITalino se debe establecer un protocolo cuando la toma de datos sea con actividad física y sin, para poder obtener datos que se puedan analizar.

•	Se identifica que la onda S se destaca más en la segunda toma del sujeto 2, lo cual resalta la importancia de comprender cómo ciertos factores, como la ubicación incorrecta de los electrodos o una conexión deficiente entre los electrodos y la piel, pueden resultar en una apariencia inusual en el registro del BITalino. La ubicación de los electrodos en el cuerpo puede impactar en la amplitud de las ondas en el ECG, especialmente si se orientan de manera que registren el flujo de corriente eléctrica en una dirección específica. Además, se debe considerar cómo la anatomía del corazón, las condiciones cardíacas, la edad y el género pueden influir en las mediciones obtenidas, pero no se puede llegar a un diagnóstico con la toma del BITalino. Si se analiza el tema fisiológico, se debe considerar que la onda S es más prominente en un electrocardiograma (ECG) cuando hay una hipertrofia ventricular izquierda (HVI) o un bloqueo de rama derecha (BRD). Estas condiciones hacen que la despolarización del ventrículo izquierdo se retrase y se prolongue, lo que produce una onda S más profunda y ancha en las derivaciones precordiales derechas (V1-V2) y en las derivaciones periféricas izquierdas (I, aVL) [H][I]. En resumen, en este caso no se puede llegar a una conclusión definitiva, ya que mientras un ECG tradicional se especializa en la medición precisa de señales cardíacas, el BITalino es una plataforma más versátil que puede capturar señales cardíacas, aunque su enfoque principal es brindar flexibilidad para diversas aplicaciones de adquisición de señales fisiológicas.

Recomendaciones: 

•	Respecto a la toma de datos con el BITalino se debe considerar la idoneidad de la tecnología para el propósito específico. Si la precisión es de suma importancia, como en el diagnóstico de afecciones cardíacas críticas, un ECG tradicional podría ser la mejor opción. Sin embargo, si se necesita flexibilidad en la adquisición de señales para aplicaciones más diversas, BITalino puede ser adecuado.

•	Se debe verificar bien la ubicación de electrodos, además que cuando se haga la toma no haya interferencias ya que la señal se puede alterar. 

•	Si bien el BITalino aplica filtros específicos para cada una de las señales, se debe filtrar aún más la señal para obtener mejores resultados. Se podrían aplicar algunas técnicas de filtros digitales como FIR e IIR. 


#### Referencias

[a]
Clínica Anglo Americana, “Enfermedades Cardiovasculares: la tercera causa de muerte en el país - Clínica Anglo Americana,” Clínica Anglo Americana, Mar. 12, 2021. https://clinicaangloamericana.pe/enfermedades-cardiovasculares-la-tercera-causa-de-muerte-en-el-pais/#:~:text=En%20Per%C3%BA%2C%20las%20enfermedades%20cardiovasculares,a%C3%B1os%20padece%20alguna%20complicaci%C3%B3n%20cardiaca. (accessed Sep. 17, 2023).

‌[b]
“La Carga de Enfermedades Cardiovasculares - OPS/OMS | Organización Panamericana de la Salud,” Paho.org, 2018. https://www.paho.org/es/enlace/carga-enfermedades-cardiovasculares#:~:text=En%202019%2C%202.0%20millones%20de,000%20habitantes%20en%20el%202019. (accessed Sep. 17, 2023).
‌
[c]
S. Trejo, “Revisión bibliográfica : Interpretación del electrocardiograma, una herramienta para la detección de cardiopatías,” Xoc.uam.mx, 2021, doi: https://repositorio.xoc.uam.mx/jspui/handle/123456789/26548.

[d]
BITalino (r)evolution Board Kit - DEV-14022 - SparkFun Electronics [Internet]. Sparkfun.com. 2023 [cited 2023 Sep 17]. Available from: https://www.sparkfun.com/products/retired/14022

[e]
López Núñez, Álvaro, Monroy M, Molinares C. EFECTOS DEL USO DE ESCALERAS EN LA SALUD FÍSICA. Biosalud [Internet]. 2014 [cited 2023 Sep 17];13(2):36–47. Available from: http://www.scielo.org.co/scielo.php?pid=S1657-95502014000200004&script=sci_arttext

[f]
Valentino SE, Dunford EC, Dubberley J, Lonn E, Gibala MJ, Phillips SM, et al. Cardiovascular responses to high‐intensity stair climbing in individuals with coronary artery disease. Physiological Reports [Internet]. 2022 May 1 [cited 2023 Sep 17];10(10). Available from: https://physoc.onlinelibrary.wiley.com/doi/full/10.14814/phy2.15308

[g]
Bryan Derrickson Gerard J. Tortora, Principios de Anatomía y Fisiología. Ed. Medica Panam., 2018.

[H]
Universidad Autónoma de México. FUNDAMENTOS ELECTROFISIOLÓGICOS DEL ELECTROCARDIOGRAMA. Unidad temática II.

[I]
Biopac Student Lab. Lección 6. ELECTROCARDIOGRAFÍA (ECG) II. 


