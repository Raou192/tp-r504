import pytest
import fonctions as f
import math

def test_1():
	assert f.puissance(2,3) ==8
	assert f.puissance(2,2) ==4

def test_2():
	assert f.puissance(-1,2) ==1
	assert f.puissance(-1,3) ==-1

def test_all_x():
	assert f.puissance(0,3) ==0
	assert f.puissance(0,1) ==0
	assert f.puissance(0,0) ==1

	with pytest.raises(valueError):
		f.puissance(0,-1)
