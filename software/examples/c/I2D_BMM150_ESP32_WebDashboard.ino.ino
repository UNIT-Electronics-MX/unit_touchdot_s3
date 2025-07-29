/*
  ============================================================================
  Nombre del archivo:   UNIT_BMM150_WebAJAX.ino
  Proyecto:             Monitor Web AJAX para Magnetómetro BMM150 en ESP32
  Autor:                Adrian Rabadan
  Área:                 I2D Electrónica – UNIT Electronics
  Fecha:                2025-07-29
  ============================================================================

  Descripción:
    Este programa permite leer los valores del sensor magnetómetro BMM150 y
    mostrarlos en una página web accesible desde cualquier dispositivo en la
    misma red WiFi, utilizando actualización dinámica (AJAX) sin recargar la página.
    También despliega los datos en una pantalla OLED y un NeoPixel cambia de
    color si hay cambios magnéticos.

  ----------------------------------------------------------------------------
  **Conexión de Hardware**
  ----------------------------------------------------------------------------
  - ESP32 (modelo con WiFi y soporte I2C, por ejemplo, ESP32-WROOM-32).
  - Sensor BMM150 (por I2C, breakout DFRobot u otro compatible).
  - Pantalla OLED SSD1306 128x64 (I2C).
  - 1 LED NeoPixel (WS2812 o compatible) conectado a pin 25 del ESP32.

  **Pines sugeridos para conexión:**

  *ESP32         ->    Componente        ->   Descripción*
  ----------------------------------------------------------
   3V3           ->    VCC OLED, VCC BMM150
   GND           ->    GND OLED, GND BMM150, GND NeoPixel
   5 (SDA)      ->    SDA OLED, SDA BMM150
   6 (SCL)      ->    SCL OLED, SCL BMM150
   D25            ->    DIN NeoPixel
   3V3           ->    VCC NeoPixel (si solo usas 1-2 leds)

  - Los pines SDA/SCL pueden variar según tu placa, revisa la documentación del ESP32 que uses.
  - El OLED y el BMM150 pueden compartir bus I2C.

  ----------------------------------------------------------------------------
  **Acceso a la página web de monitoreo**
  ----------------------------------------------------------------------------
  1. Conecta el ESP32 a la PC y sube el código.
  2. El ESP32 se conectará a la red WiFi configurada en las variables `ssid` y `password`.
  3. Cuando veas en el monitor serial el mensaje `IP: xxx.xxx.xxx.xxx`, anota esa dirección IP.
  4. Desde cualquier PC, teléfono o tablet conectado a la **misma red WiFi**, abre tu navegador
     y entra a la dirección IP mostrada. Ejemplo:  
         http://192.168.1.120
  5. Verás una página con los datos actualizándose automáticamente cada segundo.
  6. Si la página no carga, revisa que el ESP32 y el dispositivo estén en la **misma red**.

  ----------------------------------------------------------------------------
  **Solución de problemas**
  ----------------------------------------------------------------------------
  - Si ves pantalla en blanco o el sitio no carga, reinicia el ESP32 o espera unos segundos.
  - Si se satura la página al abrir muchas veces, cierra todas las pestañas y prueba de nuevo.
  - Si la página muestra datos pero no cambian, revisa la conexión física del sensor.

  ———————————————————————————————————————
  Desarrollado para UNIT Electronics / I2D Electrónica / 
  ———————————————————————————————————————

*/

// ====== LIBRERÍAS ======
#include <Wire.h>
#include <WiFi.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_NeoPixel.h>
#include "DFRobot_BMM150.h"

// ====== CONFIGURACIÓN DE HARDWARE ======
#define NEOPIXEL_PIN 25          // Pin para el NeoPixel
#define NEOPIXEL_COUNT 1         // Número de LEDs NeoPixel

#define SCREEN_WIDTH 128         // Ancho de pantalla OLED
#define SCREEN_HEIGHT 64         // Alto de pantalla OLED
#define OLED_RESET -1            // Reset de OLED (-1 si no se usa)

// ====== CONFIGURACIÓN DE WIFI ======
const char* ssid = "your_SSID";         // Nombre de la red WiFi
const char* password = "your_password";   // Contraseña de la red WiFi

// ====== INICIALIZACIÓN DE OBJETOS ======
DFRobot_BMM150_I2C bmm150(&Wire, I2C_ADDRESS_4);              // Sensor BMM150 por I2C
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET); // Pantalla OLED
Adafruit_NeoPixel strip(NEOPIXEL_COUNT, NEOPIXEL_PIN, NEO_GRB + NEO_KHZ800); // NeoPixel

WiFiServer server(80);           // Servidor web en puerto 80

// ====== VARIABLES DE SENSOR ======
sBmm150MagData_t prevMagData = {0,0,0};    // Últimos datos para comparar cambios
float prevCompassDegree = -1;

// ====== SETUP ======
void setup() {
  Serial.begin(115200);
  Wire.begin();

  // Inicializa el sensor BMM150
  while(bmm150.begin()){
    Serial.println("bmm150 init failed, retrying...");
    delay(1000);
  }
  Serial.println("bmm150 init success!");
  bmm150.setOperationMode(BMM150_POWERMODE_NORMAL);
  bmm150.setPresetMode(BMM150_PRESETMODE_HIGHACCURACY);
  bmm150.setRate(BMM150_DATA_RATE_10HZ);
  bmm150.setMeasurementXYZ();

  // Inicializa la pantalla OLED
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) {
    Serial.println("Error iniciando pantalla OLED");
    while(true); // Detiene el programa si falla la pantalla
  }
  display.clearDisplay();
  display.setTextColor(SSD1306_WHITE);

  // Inicializa NeoPixel
  strip.begin();
  strip.show(); // Apaga el LED al inicio

  // Conexión a red WiFi
  Serial.printf("Conectando a %s\n", ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado");
  Serial.print("IP: "); Serial.println(WiFi.localIP());

  server.begin(); // Inicia el servidor web
}

// ====== LOOP PRINCIPAL ======
void loop() {
  // Lectura de datos del sensor BMM150
  sBmm150MagData_t magData = bmm150.getGeomagneticData();
  float compassDegree = bmm150.getCompassDegree();

  // Muestra los datos por Serial (debug)
  Serial.printf("mag x=%d y=%d z=%d | compass=%.2f\n", magData.x, magData.y, magData.z, compassDegree);

  // Muestra los datos en pantalla OLED
  display.clearDisplay();
  display.setCursor(0,0);
  display.printf("Magnetic Data:\nX: %d\nY: %d\nZ: %d\n", magData.x, magData.y, magData.z);
  display.printf("Compass: %.2f\n", compassDegree);
  display.display();

  // Cambia el color del NeoPixel si hay un cambio importante en los datos
  if (abs(magData.x - prevMagData.x) > 5 || abs(magData.y - prevMagData.y) > 5 || abs(magData.z - prevMagData.z) > 5) {
    uint32_t color = Wheel((millis() / 100) % 256);
    strip.setPixelColor(0, color);
    strip.show();
    prevMagData = magData;
  }
  prevCompassDegree = compassDegree;

  // ====== ATIENDE CLIENTES WEB ======
  WiFiClient client = server.available();
  if (client) {
    String req = client.readStringUntil('\r'); // Lee la solicitud HTTP
    client.flush();

    // Si el navegador solicita la raíz "/", sirve la página HTML
    if (req.indexOf("GET / ") != -1 || req.indexOf("GET /HTTP") != -1) {
      enviarPaginaWeb(client);
    }
    // Si el navegador solicita "/data", responde con JSON (lo pide el AJAX)
    else if (req.indexOf("GET /data") != -1) {
      enviarDatosJSON(client, magData, compassDegree);
    }
    // Espera corto y cierra la conexión
    delay(10);
    client.stop();
  }

  delay(100);
}

// ====== FUNCIÓN: Envía la página web principal con AJAX ======
void enviarPaginaWeb(WiFiClient& client) {
  String html = 
    "<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>"
    "<meta name='viewport' content='width=device-width, initial-scale=1'>"
    "<title>BMM150 ESP32 S3</title>"
    "<style>body{font-family:Arial; text-align:center; padding:30px;} h1{color:#333;} .data{font-size:2em;margin:10px;}</style>"
    "</head><body>"
    "<h1>Sensor BMM150</h1>"
    "<div class='data'><b>Magnetic X:</b> <span id='x'>-</span></div>"
    "<div class='data'><b>Magnetic Y:</b> <span id='y'>-</span></div>"
    "<div class='data'><b>Magnetic Z:</b> <span id='z'>-</span></div>"
    "<div class='data'><b>Compass Angle:</b> <span id='c'>-</span>°</div>"
    "<div class='data'>Actualizado: <span id='t'>-</span>s</div>"
    // Firma UNI
