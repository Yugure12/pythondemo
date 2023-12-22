# 测试工厂模式

class Benz:
    pass

class BMW:
    pass

class BYD:
    pass

class CarFactory:

    __benz = None
    __bmw = None
    __byd = None

    def __new__(cls, *args, **kwargs):
        if cls.__benz == None:
            cls.__benz = Benz()


    def create_car(self, brand):
        if brand == "Benz":
            return Benz()
        elif brand  == "BMW":
            return BMW()
        elif brand == "BYD":
            return BYD()
        else: return "未知品牌"


factory = CarFactory();
f1 = factory.create_car("Benz");
f2 = factory.create_car("BMW");
