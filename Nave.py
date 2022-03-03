#La nomenclatura indica que la primera letra del nombre de una clase va en mayusculas
from OpenGL.GL import *
from glew_wish import *
import glfw
import math

class Nave:
    posicion_x = 0.0
    posicion_y = 0.0
    posicion_z = 0.0
    velocidad = 1.2
    angulo = 0.0
    velocidad_rotacion = 270.0
    fase = 90.0

    def dibujar(self):
        glPushMatrix()
        glTranslatef(self.posicion_x, self.posicion_y, self.posicion_z)
        glRotatef(self.angulo, 0.0, 0.0, 1.0)
        glBegin(GL_TRIANGLES)
        glColor3f(0.3, 0.0, 1.0)
        glVertex3f(-0.05,-0.05,0)
        glVertex3f(0.0,0.05,0)
        glVertex3f(0.05,-0.05,0)

        glEnd()

        glBegin(GL_LINE_LOOP)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f(-0.05, -0.05, 0)
        glVertex3f(-0.05,0.05,0.0)
        glVertex3f(0.05, 0.05,0.0)
        glVertex3f(0.05,-0.05,0.0)
        glEnd()

        glPopMatrix()

        def actualizar(self, tiempo_delta):   
            global disparando
            global angulo_bala
            global estado_anterior_espacio
            #Leer los estados de las teclas que queremos
            estado_tecla_arriba = glfw.get_key(window, glfw.KEY_UP)
            estado_tecla_derecha = glfw.get_key(window, glfw.KEY_RIGHT)
            estado_tecla_izquierda = glfw.get_key(window, glfw.KEY_LEFT)
            estado_tecla_espacio = glfw.get_key(window, glfw.KEY_SPACE)

            # if (estado_tecla_espacio == glfw.PRESS and 
            #     estado_anterior_espacio == glfw.RELEASE):
            #     for i in range(3):
            #         if not disparando[i]:
            #             disparando[i] = True
            #             posiciones_bala[i][0] = nave.posicion_x
            #             posiciones_bala[i][1] = nave.posicion_y
            #             angulo_bala[i] = nave.angulo + nave.fase
            #             break

            #Revisamos estados y realizamos acciones
            cantidad_movimiento = self.velocidad * tiempo_delta
            if estado_tecla_arriba == glfw.PRESS:
                self.posicion_x = self.posicion_x + (
                    math.cos((self.angulo + self.fase) * math.pi / 180.0) * cantidad_movimiento
                )
                self.posicion_y = self.posicion_y + (
                    math.sin((self.angulo + self.fase) * math.pi / 180.0) * cantidad_movimiento
                )

            cantidad_rotacion = self.velocidad_rotacion * tiempo_delta
            if estado_tecla_izquierda == glfw.PRESS:
                self.angulo = self.angulo + cantidad_rotacion
                if self.angulo > 360.0:
                    self.angulo = self.angulo - 360.0 
            if estado_tecla_derecha == glfw.PRESS:
                self.angulo = self.angulo - cantidad_rotacion
                if self.angulo < 0.0:
                    self.angulo = self.angulo + 360.0
            estado_anterior_espacio = estado_tecla_espacio

            if self.posicion_x > 1.05: 
                self.posicion_x = -1.0
            if self.posicion_x < -1.05: 
                self.posicion_x = 1.0
                
            if self.posicion_y > 1.05: 
                self.posicion_y = -1.0   
            if self.posicion_y < -1.05: 
                self.posicion_y = 1.0  