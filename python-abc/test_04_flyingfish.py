import pytest
from task_04_flyingfish import Fish, Bird, FlyingFish

class TestFishClass():
    fish = Fish()

    def test_fish_exists(self):
        assert isinstance(self.fish, Fish)

    def test_fish_has_swim(self, capfd):
        self.fish.swim()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The fish is swimming"

    def test_fish_has_habitat(self, capfd):
        self.fish.habitat()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The fish lives in water"


class TestBirdClass():
    bird = Bird()

    def test_bird_exists(self):
        assert isinstance(self.bird, Bird)

    def test_bird_has_fly(self, capfd):
        self.bird.fly()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The bird is flying"

    def test_bird_has_habitat(self, capfd):
        self.bird.habitat()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The bird lives in the sky"

class TestFlyingFish():
    flying_fish = FlyingFish()

    def test_flying_fish_exists(self):
        assert isinstance(self.flying_fish, FlyingFish)

    def test_flying_fish_inherits_bird_and_fish(self):
        assert issubclass(self.flying_fish.__class__, (Bird, Fish))

    def test_flying_fish_overrides_fly(self, capfd):
        self.flying_fish.fly()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The flying fish is soaring!"

    def test_flying_fish_overrides_swim(self, capfd):
        self.flying_fish.swim()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The flying fish is swimming!"

    def test_flying_fish_overrides_habitat(self, capfd):
        self.flying_fish.habitat()
        out, err = capfd.readouterr()
        assert out.split("\n")[-2] == "The flying fish lives both in water and the sky!"












