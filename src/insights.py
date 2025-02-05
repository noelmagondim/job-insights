from src.jobs import read


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    jobs_list = read(path)
    data_type = set()
    for job in jobs_list:
        data_type.add(job["job_type"])
    return data_type


def filter_by_job_type(jobs, job_type):
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """

    list = []
    for job in jobs:
        if job["job_type"] == job_type:
            list.append(job)
    return list


def get_unique_industries(path):
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    jobs_list = read(path)
    data_type = set()
    for job in jobs_list:
        if job["industry"]:
            data_type.add(job["industry"])
    return data_type


def filter_by_industry(jobs, industry):
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    list = []
    for job in jobs:
        if job["industry"] == industry:
            list.append(job)
    return list


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    list = []
    for job in jobs_list:
        max_salary = job["max_salary"]
        if max_salary.isnumeric():
            list.append(int(max_salary))
    return max(list)


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs_list = read(path)
    list = []
    for job in jobs_list:
        min_salary = job["min_salary"]
        if min_salary.isnumeric():
            list.append(int(min_salary))
    return min(list)


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greater than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        max_salary = int(job["max_salary"])
        min_salary = int(job["min_salary"])
        int_salary = int(salary)
    except KeyError:
        raise ValueError
    except TypeError:
        raise ValueError
    if min_salary > max_salary:
        raise ValueError
    return min_salary <= int_salary <= max_salary


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    list = []

    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                list.append(job)
        except ValueError:
            pass
    return list
