from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    """
    Test the Brazilian Jobs file.
    """
    jobs = read_brazilian_file('tests/mocks/brazilian_jobs.csv')
    assert ('title' and 'salary' and 'type') in list(jobs[0].keys())
