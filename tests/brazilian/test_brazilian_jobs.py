from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    """
    Test the Brazilian Jobs file.
    """
    jobs = read_brazilian_file('tests/mocks/brazilian_jobs.csv')
    assert ('titulo' and 'salario' and 'tipo') not in jobs[0]
    assert ('title' and 'salary' and 'type') in jobs[0]
