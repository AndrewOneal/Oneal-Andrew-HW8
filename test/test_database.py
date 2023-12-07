import pytest
import sys
sys.path.append('src')
from database import DatabaseController

@pytest.fixture
def db():
    yield DatabaseController()

def test_init(db):
    pass

def test_addTable(db):
    pass

def test_addEntry(db):
    pass

def test_queryAllEntries(db):
    pass

def test_queryEntry(db):
    pass

def test_deleteAll(db):
    pass

