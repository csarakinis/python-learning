import pytest
import kataexercises.scripts.exercise1 as j


def test_journey_true():
    journey = j.Journey(50, 2)
    journey.willyoumakeit()
    assert journey.outcome == True

def test_journey_false():
    journey = j.Journey(60, 2)
    journey.willyoumakeit()
    assert journey.outcome == False

    # assert journey.willyoumakeit == True