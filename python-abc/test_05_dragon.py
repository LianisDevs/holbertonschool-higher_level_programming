import pytest
from task_05_dragon import SwimMixin, FlyMixin, Dragon

class BaseClass(SwimMixin, FlyMixin):
        pass


class TestSwimMixin():
    base_class = BaseClass()

    def test_SwimMixin_adds_swim_functionality(self, capfd):
        self.base_class.swim()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The creature swims!"

class TestFlyMixin():
    base_class = BaseClass()

    def test_SwimMixin_adds_fly_functionality(self, capfd):
        self.base_class.fly()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The creature flies!"


class TestDragonClass():
    dragon = Dragon()

    def test_dragon_exists(self):
        assert isinstance(self.dragon, (SwimMixin, FlyMixin))

    def test_dragon_has_roar(self, capfd):
        self.dragon.roar()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The dragon roars!"

    def test_dragon_has_swim(self, capfd):
        self.dragon.swim()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The creature swims!"

    def test_dragon_has_fly(self, capfd):
        self.dragon.fly()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The creature flies!"
