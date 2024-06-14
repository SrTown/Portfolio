import time
import lcdlibreria as LCD
import brazo_V3 as brazo
import comparacion
import Detector_V5 as detector
import venoso_p as venas
import RPi.GPIO as GPIO

GPIO.setup(11,GPIO.OUT)
GPIO.output(11, GPIO.LOW)
            
LCD.lcd_init()
vartime=.2
def animation():
     
     for i in range(1, 10):
            if (i == 1):
                LCD.lcd_texto("  C          ",LCD.LINE_1)
                time.sleep(vartime)
                
            if (i == 2):
                LCD.lcd_texto("   A         ",LCD.LINE_1)
                time.sleep(vartime)
                
            if (i == 3):
                LCD.lcd_texto("    R        ",LCD.LINE_1)
                time.sleep(vartime)
                
            if (i == 4):
                LCD.lcd_texto("     G       ",LCD.LINE_1)
                time.sleep(vartime)
                
            if (i == 5):
                LCD.lcd_texto("      A      ",LCD.LINE_1)
                time.sleep(vartime)
                
            if (i == 6):
                LCD.lcd_texto("       N     ",LCD.LINE_1)
                time.sleep(vartime)
                
            if (i == 7):
                LCD.lcd_texto("        D    ",LCD.LINE_1)
                time.sleep(vartime)
                
            if (i == 8):
                LCD.lcd_texto("         O   ",LCD.LINE_1)
                time.sleep(vartime)
            if (i == 9):
                LCD.lcd_texto("    CARGANDO    ",LCD.LINE_1)
                time.sleep(vartime)

animation()
# variable que va a recibir la de la voz
voz=comparacion.main()
# voz="cubo"
nombre=""
print("hpñ")
print(voz)

# cubo = 1
# esfera = 2


h=detector.pachon()
# h=[2,1]

# h[0]=Lo que se encuentra en la posicion 1
# h[1]=Lo que se encuentra en la posicion 2
if h[0] == 1 and voz == 'cubo':
        
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    LCD.lcd_texto("   SE DETECTO   ",LCD.LINE_1)
    LCD.lcd_texto("      CUBO      " ,LCD.LINE_2)
    LCD.GPIO.cleanup()
    brazo.init()
    brazo.set_initial_positions()
    brazo.set_primera_posicion()
    nombre=venas.pachon()
#     nombre="Kevin Pachon"
    
        
if h[0] == 2 and voz == 'esfera':
    
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    LCD.lcd_texto("  SE DETECTO  ",LCD.LINE_1)
    LCD.lcd_texto("     ESFERA  " ,LCD.LINE_2)
#     LCD.GPIO.cleanup()
    
    brazo.init()
    brazo.set_initial_positions()
    brazo.set_primera_posicion()
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    GPIO.output(11, GPIO.HIGH)
    LCD.lcd_texto("     MOTOR    ",LCD.LINE_1)
    LCD.lcd_texto("   ENCENDIDO  " ,LCD.LINE_2)
    print("Motor ENCENDIDO")
#     time.sleep(5)
#     GPIO.output(11, GPIO.LOW)
    
if h[1] == 1 and voz == 'cubo':
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    LCD.lcd_texto("   SE DETECTO   ",LCD.LINE_1)
    LCD.lcd_texto("      CUBO      " ,LCD.LINE_2)
#     LCD.GPIO.cleanup()
    brazo.init()
    brazo.set_initial_positions()
    brazo.set_segunda_posicion()
    nombre=venas.pachon()
#     nombre="Kevin Pachon"
        
if h[1] == 2 and voz == 'esfera':
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    LCD.lcd_texto("  SE DETECTO  ",LCD.LINE_1)
    LCD.lcd_texto("     ESFERA  " ,LCD.LINE_2)
#     LCD.GPIO.cleanup()
    brazo.init()
    brazo.set_initial_positions()
    brazo.set_segunda_posicion()
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    LCD.lcd_texto("     MOTOR    ",LCD.LINE_1)
    LCD.lcd_texto("   ENCENDIDO  " ,LCD.LINE_2)
    GPIO.output(11, GPIO.HIGH)
#     time.sleep(5)
#     GPIO.output(11, GPIO.LOW)
    
if(nombre=="Maria Paula"):
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    LCD.lcd_texto("   BIENVENIDA   ",LCD.LINE_1)
    LCD.lcd_texto("  MARIA PAULA   " ,LCD.LINE_2)
#     LCD.GPIO.cleanup()
if(nombre=="Kevin Pachon"):
#     LCD.lcd_init()
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    LCD.lcd_texto("   BIENVENIDO   ",LCD.LINE_1)
    LCD.lcd_texto("  KEVIN PACHON  " ,LCD.LINE_2)
#     LCD.GPIO.cleanup()
if(nombre=="Jefferson Perez"):
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    LCD.lcd_texto("   BIENVENIDO   ",LCD.LINE_1)
    LCD.lcd_texto(" JEFFERSON PEREZ" ,LCD.LINE_2)
#     LCD.GPIO.cleanup()
if(nombre=="Carlos Villa"):
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    LCD.lcd_texto("   BIENVENIDO   ",LCD.LINE_1)
    LCD.lcd_texto("  CARLOS VILLA  " ,LCD.LINE_2)
#     LCD.GPIO.cleanup()
if(nombre=="Ludving Beltran"):
    LCD.lcd_write(0x01, LCD.LCD_CMD)
    LCD.lcd_texto("   BIENVENIDO   ",LCD.LINE_1)
    LCD.lcd_texto("Ludving Beltran" ,LCD.LINE_2)
#     LCD.GPIO.cleanup()
# else:
#     print("nadie dijo nada")
