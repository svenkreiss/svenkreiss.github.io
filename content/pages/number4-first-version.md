Title: number4 - First Version
Date: 2013-03-22
Slug: number4-first-version



## Technische Daten

* Höhe: 51 cm
* Masse: 1.2 kg
* Freiheitsgrade: 11
* Abstandssensoren: 2
* Drucksensoren: 8
* Lagesensoren: noch keine


## Bilder

{% img /images/number4/first-version/Foto_fuesse.jpg 350 number4 %}
{% img /images/number4/first-version/Foto_huefte.jpg 350 number4 %}
{% img /images/number4/first-version/Foto_totale.jpg 350 number4 %}
{% img /images/number4/first-version/Foto_unterkoerper.jpg 350 number4 %}
{% img /images/number4/first-version/Nummer4_050502_1.jpg 350 number4 %}
{% img /images/number4/first-version/Nummer4_050502_2.jpg 350 number4 %}
{% img /images/number4/first-version/Nummer4_050502_3.jpg 350 number4 %}
{% img /images/number4/first-version/Nummer4_050502_4.jpg 350 number4 %}




## Aufbau von Nummer4

### Mechanik
Basismaterial sind speziell zugefräste Plastestückchen. Diese stammen aus alten Fleischerbrettchen. Sie bilden die Halterung sowie die Verbindung zwischen den Servomotoren. Jedes Gelenk besteht aus zwei Lagern. Das eine Lager ist das Kugellager im Motor selbst und das andere Lager ist ein Reiblager bestehend aus einem Messingbolzen und zwei Löchern in den Plastikstückchen.

### Aktuatoren
Digitale Servomotoren von der Firma Robbe treiben den Roboter an. Sie sind besonders durch ihr hohes Haltemoment und ihre hohe Präzision geeignet. Derzeit verwende ich den Typ FS-250T. Das Verhalten der Servomotoren lässt sich mit der Software CAMI 2000 programmieren. Ein neuer Digitalservo, der FS-280T, ist sicherlich eine noch bessere Alternative, für die mir derzeit das Geld fehlt. In diesem Zusammenhang möchte ich mich bei der Firma robbe - Modellsport GmbH für ihre bisherige Unterstützung bedanken.

### PC-Software
Die Software in einem PC berechnet derzeit die Bewegung. Es ist eine C Applikation, die ich bisher auf einem SuSE-Linux- und auf einem Debian-Linux-System laufen hatte. Eingaben erfolgen über die Tastatur. Dadurch werden Routinen für bestimmte Bewegungsabläufe aufgerufen oder Variablen wie die Schrittweite modifiziert. Die Bewegung wird zum einen als Echtzeitanimation mit OpenGL auf dem Bildschirm ausgegeben und zum anderen mit der seriellen Schnittstelle übertragen. Die Ausgangsdaten an der seriellen Schnittstelle sind schon die Pulsweiten für die Generierung des PWM-Signals im Controller. Über die serielle Schnittstelle werden auch Sensorinformationen zurückgesendet. Derzeit nur die beiden Werte der Abstandssensoren. Eine Übertragung von mehr Sensorinformationen ist ohne Probleme möglich (Nummer3 hatte schon an jedem Fuß vier Taster, deren Zustände übertragen wurden).

### Sensorik
Nummer4 verfügt derzeit nur über zwei Abstandssensoren. Diese sind nach vorn gerichtet. Er kann somit auf größere Gegenstände reagieren und seine Schrittweite auf Null verringern.
Sensoren, welche die Belastungen der Füße messen und Unebenheiten im Boden erkennen fehlen noch. Nummer 1,2 und 3 besaßen bereits pro Fuß vier Taster mit denen zumindest eine Erkennung von Hindernissen möglich war.
Die neue Elektronik (Fertigstellung geplant für 03-06/2005), die bereits als Schaltungslayout existiert, wird auch in der Lage sein, die Ströme an jedem einzelnen Servo zu messen. Dadurch wird zum ersten Mal in diesem Projekt eine Bewertung des Energieverbrauchs mit experimentell bestimmten Zahlen möglich.

### Elektronik
Die Elektronik erhält über die serielle Schnittstelle die Pulsweiten für jedes einzelne Servosignal. Der Controller hat dann die Aufgabe simultan 11 PWM-Signale zu erzeugen. Kern der Elektronik ist ein mit 16 MHz betriebener ATMega128 von Atmel. Dieser 8-Bit-Controller ist besonders gut durch seine zahlreichen Ports und die Kommunikationsschnittstellen (2x USART, TWI, SPI, ...) geeignet.

Noch vor kurzem programmierte ich diesen Controller mit BASCOM (Basic). Nun bin ich auch hier auf Linux und gleichzeitig auf C umgestiegen. Es wird noch etwas dauern bis ich mit C dieselben Sachen anstellen kann wie mit BASCOM.

Die neue Elektronik (geplant für 03-06/2005) soll dann den Roboter autonom vom PC werden lassen. Ein verteiltes System aus mehreren ATMega128 wird die Bewegung berechnen und in die PWM-Signale umwandeln. Zusätzlich soll der Strom an jedem Motor einzeln gemessen werden können und jeder Motor soll einzeln abschaltbar sein. Vorstellbar sind dann auch weitere Module für Sensorauswertungen usw.

Die Kommunikation zwischen den Controllern sollen die implementierten UARTs übernehmen. Master erzeugt einen Datenblock, der dann von allen gelesen wird. Durch eine externe Beschaltung kann auch ein Slave zum Master senden, jedoch nur nach Aufforderung durch den Master.

Die PWM-Signale sollen in der neuen Elektronik nicht mehr durch Softwarealgorithmen erzeugt werden, sondern durch die beiden 16-Bit-Timer. Jeder dieser beiden Timer kann drei PWM-Signale erzeugen.

Soweit die Theorie, ich habe das noch nie probiert.
