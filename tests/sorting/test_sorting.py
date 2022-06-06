from src.sorting import sort_by
from src.jobs import read


def test_sort_by_criteria():
    jobs = read('src/jobs.csv')
    
    sort_by(jobs, 'min_salary')
    assert jobs[0]['min_salary'] == '20000'

    sort_by(jobs, 'max_salary')
    assert jobs[0]['max_salary'] == '212901'

    sort_by(jobs, 'date_posted')
    assert jobs[0]['date_posted'] == '2020-05-08'
