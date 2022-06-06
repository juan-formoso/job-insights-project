from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    """
    Test the Brazilian Jobs file.
    """
    jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert 'titulo' not in jobs[0]
    assert 'salario' not in jobs[0]
    assert 'tipo' not in jobs[0]
    assert 'title' in jobs[0]
    assert 'salary' in jobs[0]
    assert 'type' in jobs[0]
