from abc import ABC, abstractmethod

# 1. Interfaz
class INotificador(ABC):
    
    @abstractmethod
    def enviar(self, mensaje: str):
        pass


# 2. Implementaciones concretas
class NotificadorEmail(INotificador):
    
    def enviar(self, mensaje: str):
        print(f"Enviando Email: {mensaje}")


class NotificadorSMS(INotificador):
    
    def enviar(self, mensaje: str):
        print(f"Enviando SMS: {mensaje}")


# 3. Nueva funcionalidad
class NotificadorWhatsApp(INotificador):
    
    def enviar(self, mensaje: str):
        print(f"Enviando WhatsApp: {mensaje}")


# Clase que usa la interfaz
class GestorNotificaciones:
    
    def __init__(self, notificador: INotificador):
        self.notificador = notificador

    def notificar_usuario(self, mensaje: str):
        self.notificador.enviar(mensaje)


# Uso
gestor = GestorNotificaciones(NotificadorWhatsApp())
gestor.notificar_usuario("Hola, tu pedido ha sido enviado.")