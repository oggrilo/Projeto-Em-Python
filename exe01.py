import this
this.a = 10
this.b = 20
this.c = 0

def trocar():
    this.c = this.a
    this.a = this.b
    this.b = this.c
    print("A = " + str(this.a) + "\n B = " + str(this.b))