def zhuangshiqi(efunc):
    def caozuoyuan(*args, **kwargs):
        print("function is going to run")
        return  efunc(*args, **kwargs)
    return caozuoyuan

@zhuangshiqi
def helloworld():
    print("Hello world")
if __name__ == '__main__':
    helloworld()
    print("My name is ", helloworld.__name__)
