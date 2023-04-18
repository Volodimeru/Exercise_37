from jar import Jar
def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(4)
    assert jar.capacity == 4


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(20)
    jar.deposit(10)
    assert jar.size == 10
    jar.deposit(5)
    assert jar.size == 15


def test_withdraw():
    jar = Jar(30)
    jar.deposit(30)
    jar.withdraw(15)
    assert jar.size == 15