Title: number123
Date: 2014-03-22
Slug: number123



Auf dieser Seite möchte ich nicht speziell über einen Prototypen, sondern über das Projekt an sich sprechen. Was ist schon geschafft? Was fehlt? Was kann verändert werden?


## Projektstatus - Stand: 01. Januar 2006

* Fertig:
** lauffähige Prototypen: Nummer3, Nummer4 und Nummer4punkt1
** klassisches dynamisches Gehen realisiert
** Standardalgorithmus des dynamischen Gehens verbessert
** Nummer4punkt1 trägt zwei Akkupacks und zwei Platinen mit Elektronik (wichtige Algorithmen sind bereits auf die Controller ausgelagert)
** Nummer4punkt1 hat an jedem Fuß vier Kraftsensoren
** Umstellung der Programmiersprachen: Mikrocontroller mit C, Computer mit C++
** Verteilung der Rechenprozesse auf mehrere Controller

* In Arbeit:
** Messung der Ströme an jedem Servomotor
** Experimente zur wissenschaftlichen Auswertung des Energieverbrauchs mit unterschiedlichen Bewegungsalgorithmen

* To Do:
** Zwei weitere Freiheitsgrade den Hüftgelenken hinzufügen
** Längen von Ober- und Unterschenkel vergrößern
** Abstandsmessverfahren optimieren
** Lagesensorik entwerfen


## Ideen, die mir im Kopf rumschwirren...

### Lagesensorik
In Planung ist eine Lagesensorik. Sie steht derzeit noch etwas hinten an, aber sie soll kommen. Sie soll die simpel klingende Aufgabe übernehmen, zu bestimmen wo "unten" ist. Def.: Unten ist da wo alles hin fällt.

Basis dieser Sensorik sollen ein oder mehrere Beschleunigungssensoren von Analog Devices sein. Diese müssen natürlich mit anderen Sensoren gekoppelt sein. Hier bieten sich Gyroskope an.

Hat jemand Erfahrungen? Bitte E-Mail schreiben: sk@svenkreiss.com
Für hilfen wäre ich wirklich dankbar.


### Geräuschpeilung
Mit der "Geräuschpeilung" möchte ich die Richtung des lautesten Geräusches in der Umgebung ermitteln. Wenn er eine schwenkbare Kamera besitzt, dann könnte er immer in diese Richtung "sehen". Das könnte eine nette Spielerei werden.

### Fernsteuerung
Wenn einmal die Elektronik für ein autonomes Gehen fertig ist und funktioniert, dann stelle ich es mir nicht besonders schwer vor, den Roboter mit einer Funkfernsteuerung aus dem Modellbau zu bedienen. Es müsste nur ein Controller die erzeugten PWM-Signale ausmessen und z.B. mit der Schrittweite der Laufbewegung koppeln.

### Kamera
Wenn er autonom gehen kann und fernsteuerbar ist, dann wäre eine Erweiterung mit einer Kamera sicherlich interessant. Durch diese kann man den Roboter dann auch ohne direkten Sichtkontakt fernsteuern. Eine Einblendung z.B. mit Informationen aus welcher Richtung im Moment das lauteste Geräsch kommt wäre eine weitere Idee.



## History

### Nummer1
Der erste Prototyp bestand aus zwei sehr schweren Füßen. Wie bei allen Gelenken wurde auch zu den Füßen die Kraft von den Servos per Seilzug übertragen. Diesen Prototyp baute ich in der siebenten und achten Klasse. Aus Mangel an Erfahrung habe ich keine Teile selber "geformt". Der Roboter bestand nur aus zugesägten und gebohrten Aluminiumprofilen, Hartpapierplatten, M3-Schrauben, etc.
Durch das Spiel der Seilzüge, durch die Gelenke aus M3-Schrauben und Alu-Profilen, durch eine viel zu schwere Konstruktion und durch einen fehlenden Oberkörper konnte dieser Roboter nicht einmal ansatzweise gehen. Jedoch waren schon bei Nummer1 in jedem Fuß vier Mikroschalter. Bei Kontakt mit dem Boden konnten die Füße schon nach dem Boden ausgerichtet werden.

### Nummer2
Für Nummer2 habe ich dann schon selber verzinkte Stahlplatten entworfen, zugesägt, gebohrt und geknickt. Damit habe ich mir für jeden Servo einen Stahlrahmen für jeden einzelnen Servo gebaut. Die Stahlrahmen konnte man dann modular aneinander schrauben.
Analoge Servos besitzen ein sehr großes Spiel. Durch die gleichen Module ist der Roboter sehr hoch geworden, so dass die Auswirkung des Spiels sehr groß war.

### Nummer3
In der elften Klasse sollte jeder ein Jahresarbeit schreiben. Meine Arbeit schrieb ich über Nummer3. Nummer3 hatte viele Ähnlichkeiten zu Nummer2. Die Metallrahmen waren hier jedoch nicht mehr aus Stahl sondern aus Aluminium. Besonders hervorzuheben ist der Oberschenkel. Zwei um 45° gedrehte Servomotoren wurden an der langen Seite miteinander verbunden. Dadurch konnte die Länge des Oberschenkels von über 8 cm auf 3.25 cm verringert werden. Die Jahresarbeit habe ich dann in der zwölften Klasse zur Besonderen Lernleistung ausgebaut.

Auch bei JugendForscht habe ich eine gekürzte Fassung meine Besonderen Lernleistung eingereicht. Nach dem ersten Platz beim Landeswettbewerb begann ich mit der Planung von Nummer4. Zum Bundeswettbewerb bin ich dann schon mit Nummer3 und Nummer4 angetreten.


## Bilder

{% img /images/number4/number123/Nummer3_1.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_2.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_3.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_4.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_5.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_6.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_7.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_Bildschirmphoto1.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_Bildschirmphoto2.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_Bildschirmphoto4.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_Bildschirmphoto5.jpg 350 number3 %}
{% img /images/number4/number123/Nummer3_Bildschirmphoto8.jpg 350 number3 %}

