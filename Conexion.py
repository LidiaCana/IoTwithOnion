from firebase import firebase
import threading
import time

class Conexion(threading.Thread):

    def __init__(self, cb):
        threading.Thread.__init__(self)
        self.callback = cb
        self.fire = firebase.FirebaseApplication('https://prueba1-aed02.firebaseio.com/', None)
        self.ultimo_estado0 = self.fire.get('/led', None)
        self.callback(self.ultimo_estado0)

    def run(self):
        try:
                E = []
                E.append(self.ultimo_estado0)
                i = 0
                print "hola"
                while True:
                        self.r= run()
                        estado_actual0 = self.fire.get('/led', None)
                        E.append(estado_actual0)
                        print "esta en el while"
                        if E[i] != E[-1]:
                                self.callback(estado_actual0)

                        del E[0]
                        i = i+i
                        time.sleep(0.3)

        except:
                print "error"
