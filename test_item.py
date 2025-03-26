import pytest
import pygame
from item import Pellet, PowerPellet

@pytest.fixture
def pellet():
    return Pellet(10, 20)

@pytest.fixture
def power():
    return PowerPellet(30, 40)

def test_pellet_init(pellet):
    assert pellet.x == 10
    assert pellet.y == 20 
    assert pellet.radius == 2
    assert pellet.collected == False

def test_power_init(power):
    assert power.x == 30
    assert power.y == 40 
    assert power.radius == 8
    assert power.collected == False


